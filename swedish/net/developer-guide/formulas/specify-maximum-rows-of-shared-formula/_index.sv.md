---
title: Ange maximala rader för delad formel
type: docs
weight: 40
url: /sv/net/specify-maximum-rows-of-shared-formula/
---

## **Möjliga användningsscenario**

Standard maximalt antal rader för den delade formeln är 64. Det kan vara vilket nummer som helst t.ex. det kan vara 1000. Prestandan för den delade formeln ändras med olika antal rader. Därför tillhandahåller Aspose.Cells egenskapen [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) som kan användas för att ange det maximala antalet rader för den delade formeln. Den delade formeln kommer att delas in i flera delade formler om det totala antalet rader för den delade formeln är större än det som visas i följande skärmbild.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Ange maximala rader för delad formel**

Följande kodexempel förklarar användningen av [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) egenskapen. Den sätter det maximala antalet rader för den delade formeln till 5 och lägger till den delade formeln i cellen D1 för 100 rader och sparar till [utmatnings-excelfil](61767856.xlsx). Om du extraherar innehållet i utmatnings-excelfilen och kontrollerar *sheet1.xml*, kommer du att se att den delade formeln delas upp efter varje 5 rader som markerat i den tidigare skärmbilden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
