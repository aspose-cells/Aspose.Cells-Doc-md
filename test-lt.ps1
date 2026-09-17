$text = "test"
$response = Invoke-RestMethod -Method Post -Uri 'https://api.languagetool.org/v2/check' -Body @{ text = $text; language = 'en-US' }
Write-Host "Matches: $($response.matches.Count)"