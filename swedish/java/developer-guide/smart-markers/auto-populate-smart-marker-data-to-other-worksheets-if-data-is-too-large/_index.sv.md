---
title: Fyll i smartmarkördata automatiskt till andra kalkylblad om data är för stor
type: docs
weight: 10
url: /sv/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Möjliga användningsscenarier**

Ibland vill du automatiskt fylla i smart markördata till andra kalkylblad om den är för stor. Anta att din datakälla har 1500000 poster. Det här är för många poster för ett enda kalkylblad, då kan du flytta resten av posterna till nästa kalkylblad.

## **Fyll i smartmarkördata automatiskt till andra kalkylblad om data är för stor**

Följande exempelkod har en datakälla som har 21 poster. Vi vill bara visa 15 poster i ett kalkylblad, sedan flyttas resten av posterna automatiskt till det andra kalkylbladet. Observera att det andra kalkylbladet också ska ha samma smarta markörtagg och du måste ringa[**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) metod för båda arken. Vänligen kontrollera[Microsoft Access Database-fil](60489777.accdb) används i denna kod såväl som i[utdata Excel-fil](60489786.xlsx)genereras av koden för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
