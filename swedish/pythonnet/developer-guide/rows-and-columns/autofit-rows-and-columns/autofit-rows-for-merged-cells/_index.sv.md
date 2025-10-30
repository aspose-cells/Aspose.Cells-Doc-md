---
title: Automatisk anpassning av rader för sammanslagna celler
type: docs
weight: 120
url: /sv/python-net/autofit-rows-for-merged-cells/
description: Denna artikel visar hur man autofitar rader för sammanslagna celler genom Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Hur man använder AutoFitMergedCellsType för att automatiskt anpassa rader, Autofit rader för sammanslagna celler i Python.
---

{{% alert color="primary" %}}

Microsoft Excel har en funktion som låter dig automatiskt justera höjden på en cell enligt dess innehåll. Funktionen kallas automatisk anpassning av rader. Microsoft Excel tillämpar inte automatisk anpassning på sammanslagna celler som standard. Ibland blir funktionen viktig för en användare som verkligen behöver implementera automatisk anpassning av rader även på sammanslagna celler.

{{% /alert %}}

## **Hur man använder AutoFitMergedCellsType för att autofita rader**
Aspose.Cells för Python via .NET stöder denna funktion genom [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) API:et. Med detta API är det möjligt att automatiskt anpassa rader i ett kalkylblad inklusive sammanslagna celler. Här är en lista över alla möjliga typer av autofit för sammanslagna celler:

- NONE
- FÖRSTA_RADEN
- SISTA_RADEN
- VARJE_RAD

## **Autofit rader för sammanslagna celler**

Se följande kod, den skapar ett arbetsbokobjekt och lägger till flera kalkylblad. Använd olika metoder för autofit-operationer i varje kalkylblad. Skärmbilden visar resultaten efter körningen av exempelkoden.

<br>
<img src="result.png" width=80% />

## **C# Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
