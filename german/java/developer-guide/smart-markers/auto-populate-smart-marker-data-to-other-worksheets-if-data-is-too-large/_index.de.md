---
title: Automatisch Smart Marker Daten in andere Arbeitsblätter eintragen, wenn Daten zu groß sind
type: docs
weight: 10
url: /de/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie Smart-Marker-Daten automatisch in andere Arbeitsblätter eintragen, wenn sie zu groß sind. Angenommen, Ihre Datenquelle enthält 1500000 Datensätze. Das sind zu viele Datensätze für ein einziges Arbeitsblatt, dann können Sie den Rest der Datensätze in das nächste Arbeitsblatt verschieben.

## **Automatisches Ausfüllen von Smart Marker-Daten in anderen Arbeitsblättern, wenn die Daten zu groß sind**

Der folgende Beispielcode hat eine Datenquelle, die 21 Datensätze enthält. Wir möchten nur 15 Datensätze in einem Arbeitsblatt anzeigen, dann werden die restlichen Datensätze automatisch in das zweite Arbeitsblatt verschoben. Beachten Sie, dass das zweite Arbeitsblatt auch dasselbe Smart-Marker-Tag haben sollte und Sie müssen die Methode [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean)) für beide Blätter aufrufen. Bitte prüfen Sie auch die [Microsoft Access-Datenbankdatei](60489777.accdb), die in diesem Code verwendet wird, sowie die [Ausgabe-Excel-Datei](60489786.xlsx), die der Code als Referenz generiert.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
