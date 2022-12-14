---
title: Ange maximalt antal rader med delad formel
type: docs
weight: 40
url: /sv/net/specify-maximum-rows-of-shared-formula/
---
## **Möjliga användningsscenarier**

De maximala standardraderna i den delade formeln är 64. Det kan vara vilket antal som helst, t.ex. 1000. Prestandan för delade formeln ändras med ett annat antal rader. Därför tillhandahåller Aspose.Cells[**Arbetsbok.Inställningar.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)egenskap som kan användas för att ange det maximala antalet rader i den delade formeln. Den delade formeln delas upp i flera delade formler om det totala antalet rader i den delade formeln är större än det som visas i följande skärmdump.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Ange maximalt antal rader med delad formel**

Följande exempelkod förklarar användningen av[**Arbetsbok.Inställningar.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)fast egendom. Den ställer in det maximala antalet rader i den delade formeln till 5 och lägger till den delade formeln i cell D1 för 100 rader och sparar till[utdata Excel-fil](61767856.xlsx). Om du extraherar innehållet i utdata Excel-fil och kontrollerar*ark1.xml*, kommer du att se de delade formeln delas efter var 5:e rad som markerats i skärmdumpen ovan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
