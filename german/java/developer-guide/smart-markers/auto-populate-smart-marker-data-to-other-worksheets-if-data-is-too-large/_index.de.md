---
title: Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn die Daten zu groß sind
type: docs
weight: 10
url: /de/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Mögliche Nutzungsszenarien**

Manchmal möchten Sie Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn sie zu groß sind. Angenommen, Ihre Datenquelle enthält 1500000 Datensätze. Dies sind zu viele Datensätze für ein einzelnes Arbeitsblatt, dann können Sie die restlichen Datensätze auf das nächste Arbeitsblatt verschieben.

## **Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn die Daten zu groß sind**

Der folgende Beispielcode hat eine Datenquelle mit 21 Datensätzen. Wir möchten nur 15 Datensätze in einem Arbeitsblatt anzeigen, dann werden die restlichen Datensätze automatisch auf das zweite Arbeitsblatt verschoben. Bitte beachten Sie, dass das zweite Arbeitsblatt auch das gleiche Smart-Marker-Tag haben sollte und Sie anrufen müssen[**WorkbookDesigner.process (sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) Methode für beide Blätter. Bitte überprüfen Sie die[Microsoft Access-Datenbankdatei](60489777.accdb) in diesem Code verwendet sowie die[Excel-Datei ausgeben](60489786.xlsx)generiert durch den Code für eine Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
