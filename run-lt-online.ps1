# PowerShell script to spell‑check markdown files using LanguageTool public API (limited to first 10 files for quick run)

$docRoot = Join-Path $PSScriptRoot "english\\net\\developer-guide\\pivot-tables"
$reportPath = Join-Path $PSScriptRoot "english_net_pivot_tables_spell_suggestions_report.md"

# Initialize markdown report
"# English \\ net Documentation – Spell & Grammar Review" | Set-Content $reportPath
"" | Add-Content $reportPath
"| File | Line | Issue | Error | Suggestion |" | Add-Content $reportPath
"|------|------|-------|---------|" | Add-Content $reportPath

function Get-LineNumberFromOffset([string]$text, [int]$offset) {
    if ($offset -le 0) { return 1 }
    $prefix = $text.Substring(0, $offset)
    ($prefix -split "`n").Count
}

# Get up to 10 markdown files
$mdFiles = Get-ChildItem -Path $docRoot -Recurse -Filter "*.md" -File | Select-Object -First 10

foreach ($file in $mdFiles) {
    $content = Get-Content -Raw -LiteralPath $file.FullName
    $maxChunk = 18000
    if ($content.Length -gt $maxChunk) {
        $lines = $content -split "`n"
        $chunks = @()
        $current = ""
        foreach ($ln in $lines) {
            if (($current.Length + $ln.Length + 1) -gt $maxChunk) {
                $chunks += $current
                $current = ""
            }
            $current += $ln + "`n"
        }
        if ($current) { $chunks += $current }
    } else {
        $chunks = @($content)
    }

    $offsetBase = 0
    foreach ($chunk in $chunks) {
        $response = Invoke-RestMethod -Method Post -Uri 'https://api.languagetool.org/v2/check' -Body @{ text = $chunk; language = 'en-US' }
        foreach ($match in $response.matches) {
            if ($match.context) { $errorText = $match.context.text } else { $errorText = "" }
            $suggestion = if ($match.replacements -and $match.replacements.Count -gt 0) { $match.replacements[0] } else { "" }
            $lineNum = Get-LineNumberFromOffset $chunk $match.offset
            $lineNum += $offsetBase
            "| $($file.FullName.Substring($PSScriptRoot.Length+1)) | $lineNum | $($match.rule.category.id) | $errorText | $suggestion |" | Add-Content $reportPath

        }
        $offsetBase += ($chunk -split "`n").Count
    }
}

Write-Host "Report generated at $reportPath"