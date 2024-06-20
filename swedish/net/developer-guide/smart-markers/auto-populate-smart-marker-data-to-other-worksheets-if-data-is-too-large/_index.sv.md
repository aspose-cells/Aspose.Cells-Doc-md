---
title: Automatiskt fylla i Smart Marker data till andra kalkylblad om datan är för stor
type: docs
weight: 50
url: /sv/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Möjliga användningsscenario**
Ibland vill du automatiskt fylla i smartmarker-data till andra kalkylblad om den är för stor. Antag att din datakälla har 1500000 poster. Dessa är för många poster för ett enda kalkylblad, då kan du flytta resten av posterna till nästa kalkylblad. 
## **Autofyll Smart Marker-data till andra kalkylblad om datan är för stor**
Följande exempelkod har en datakälla som har 21 poster. Vi vill visa endast 15 poster i ett kalkylblad, då kommer resten av posterna automatiskt att flyttas till det andra kalkylbladet. Observera, det andra kalkylbladet ska också ha samma smartmärkestag och du måste ringa [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) metoden för båda ark. Se den [utmatade Excelfilen](60489775.xlsx) som genererats av koden som referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
