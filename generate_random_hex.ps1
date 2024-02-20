$randomBytes = [byte[]]::new(16)
$randomGenerator = [System.Security.Cryptography.RNGCryptoServiceProvider]::new()
$randomGenerator.GetBytes($randomBytes)
$randomHexString = [System.BitConverter]::ToString($randomBytes) -replace '-'
$randomHexString.ToLower()