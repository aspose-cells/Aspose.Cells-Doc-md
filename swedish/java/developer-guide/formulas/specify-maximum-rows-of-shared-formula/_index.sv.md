---
title: Ange maximala rader för delad formel
type: docs
weight: 40
url: /sv/java/specify-maximum-rows-of-shared-formula/
---

## **Möjliga användningsscenario**

Standardmaximala rader för delad formel är 64. Det kan vara vilket som helst antal, t.ex. det kan vara 1000. Prestandan för delad formel ändras därför med olika antal rader. Därför tillhandahåller Aspose.Cells [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) egenskapen som kan användas för att ange de maximala raderna för delad formel. Den delade formeln kommer att delas upp i flera delade formler om de totala raderna för den delade formeln är större än den som visas i följande skärmdump.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Ange maximala rader för delad formel**

Följande exempelkod förklarar användningen av [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) egenskapen. Den anger de maximala raderna för delade formler till 5 och lägger till den delade formeln i cell D1 för 100 rader och sparar till [utdata Excel-fil](61767869.xlsx). Om du extraherar innehållet i utdata Excel-filen och kontrollerar *sheet1.xml*, kommer du att se att den delade formeln delas upp efter varje 5 rader som markerats i den tidigare skärmdumpen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
