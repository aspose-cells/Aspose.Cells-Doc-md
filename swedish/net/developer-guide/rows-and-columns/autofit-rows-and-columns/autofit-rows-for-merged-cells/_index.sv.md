---
title: AutoFit-rader för sammanslagna Cells
type: docs
weight: 120
url: /sv/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel tillhandahåller en funktion som låter dig anpassa storleken på en cell automatiskt efter dess innehåll. Funktionen kallas auto-fit rader. Microsoft Excel ställer inte in automatisk anpassning på sammanslagna celler. Ibland blir funktionen viktig för en användare som verkligen behöver implementera auto-fit rader på sammanslagna celler också.

{{% /alert %}}

##  **Hur man använder AutoFitMergedCellsType för automatisk anpassning av rader**
 Aspose.Cells stöder den här funktionen genom[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API. Med denna API är det möjligt att automatiskt anpassa rader i ett kalkylblad inklusive sammanslagna celler. Här är en lista över alla möjliga typer av automatiskt anpassade sammanslagna celler:

- Ingen
- Första linjen
- Sista raden
- Varje linje

##  **Autofit rader för sammanslagna Cells**

Se följande kod, den skapar ett arbetsboksobjekt och lägg till flera kalkylblad. Använd olika metoder för autoanpassningsoperationer i varje kalkylblad. Skärmdumpen visar resultaten efter exekveringen av exempelkoden.

<br>
<img src="result.png" width=80% />

##  **C# Provkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
