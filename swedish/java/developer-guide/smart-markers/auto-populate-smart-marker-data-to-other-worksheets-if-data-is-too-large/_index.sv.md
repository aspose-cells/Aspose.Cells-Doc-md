---
title: Automatiskt fylla i Smart Marker data till andra kalkylblad om datan är för stor
type: docs
weight: 10
url: /sv/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Möjliga användningsscenario**

Ibland vill du automatiskt fylla i Smart Marker-data till andra kalkylblad om det är för stort. Antag att din datakälla har 1500000 poster. Dessa är för många poster för ett enskilt kalkylblad, då kan du flytta resten av posterna till nästa kalkylblad.

## **Automatiskt fylla i Smart Marker-data till andra kalkylblad om datan är för stor**

Följande provkod har en datakälla som har 21 poster. Vi vill visa endast 15 poster i ett kalkylblad, då flyttas resten av posterna automatiskt till det andra kalkylbladet. Observera, det andra kalkylbladet bör också ha samma Smart Marker-tag och du måste ringa [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean))-metoden för båda kalkylbladen. Vänligen kontrollera även [Microsoft Access-databasfilen](60489777.accdb) som används i denna kod samt den [output Excel-fil](60489786.xlsx) som genererats av koden för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
