# Starts the LightCraft desktop app with the JSON-lines control channel
# that the OpenCode MCP server connects to (mcp --connect 127.0.0.1:7980).
# Idempotent: does nothing when the app is already listening.
param([int]$Port = 7980)

$ErrorActionPreference = 'Stop'
$appDir = Join-Path $env:LOCALAPPDATA 'Programs\ArtCraft\LightCraft'
$app = Join-Path $appDir 'lightcraft.exe'
$lib = Join-Path $env:USERPROFILE 'Pictures\LightCraft Library'

function Test-ControlPort {
    param([int]$P)
    $client = New-Object System.Net.Sockets.TcpClient
    try {
        $iar = $client.BeginConnect('127.0.0.1', $P, $null, $null)
        return $iar.AsyncWaitHandle.WaitOne(250, $false)
    } catch {
        return $false
    } finally {
        $client.Close()
    }
}

if (-not (Test-Path -LiteralPath $app)) {
    throw "LightCraft app not found: $app"
}
if (Test-ControlPort $Port) {
    Write-Output "LightCraft control channel already listening on 127.0.0.1:$Port"
    exit 0
}

$existing = Get-CimInstance Win32_Process -Filter "name = 'lightcraft.exe'" |
    Where-Object { $_.CommandLine -match '--control' } |
    Select-Object -First 1
if ($existing) {
    Write-Output "LightCraft app is running (pid $($existing.ProcessId)) but port $Port is not open yet"
    exit 0
}

$arguments = @('--library', ('"' + $lib + '"'), '--control', "$Port")
$proc = Start-Process -FilePath $app -ArgumentList $arguments -PassThru
for ($i = 0; $i -lt 80; $i++) {
    Start-Sleep -Milliseconds 500
    if (Test-ControlPort $Port) {
        Write-Output "LightCraft started (pid $($proc.Id)), control channel ready on 127.0.0.1:$Port"
        exit 0
    }
}
throw "LightCraft did not open the control port $Port within 40 seconds (pid $($proc.Id))"
