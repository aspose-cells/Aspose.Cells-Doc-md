---
title: Automatisk anpassning av rader för sammanslagna celler
type: docs
weight: 120
url: /sv/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel har en funktion som låter dig automatiskt justera höjden på en cell enligt dess innehåll. Funktionen kallas automatisk anpassning av rader. Microsoft Excel tillämpar inte automatisk anpassning på sammanslagna celler som standard. Ibland blir funktionen viktig för en användare som verkligen behöver implementera automatisk anpassning av rader även på sammanslagna celler.

{{% /alert %}}

## **Hur man använder AutoFitMergedCellsType för att autofita rader**
Aspose.Cells stödjer den här funktionen genom API:et [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/). Med detta API är det möjligt att auto-anpassa rader i ett kalkylblad inklusive sammanfogade celler. Här är en lista över alla möjliga typer av auto-anpassning av sammanfogade celler:

- Ingen
- Första raden
- Sista raden
- Varje rad

## **Autofit rader för sammanslagna celler**

Se följande kod, den skapar ett arbetsbokobjekt och lägger till flera kalkylblad. Använd olika metoder för autofit-operationer i varje kalkylblad. Skärmbilden visar resultaten efter körningen av exempelkoden.

<br>
<img src="result.png" width=80% />

## **C# Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
