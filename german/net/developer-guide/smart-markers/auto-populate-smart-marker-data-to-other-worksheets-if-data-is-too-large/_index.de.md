---
title: Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn die Daten zu groß sind
type: docs
weight: 50
url: /de/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Mögliche Nutzungsszenarien**
Manchmal möchten Sie Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn sie zu groß sind. Angenommen, Ihre Datenquelle enthält 1500000 Datensätze. Dies sind zu viele Datensätze für ein einzelnes Arbeitsblatt, dann können Sie die restlichen Datensätze auf das nächste Arbeitsblatt verschieben.
## **Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn die Daten zu groß sind**
 Der folgende Beispielcode hat eine Datenquelle mit 21 Datensätzen. Wir möchten nur 15 Datensätze in einem Arbeitsblatt anzeigen, dann werden die restlichen Datensätze automatisch auf das zweite Arbeitsblatt verschoben. Bitte beachten Sie, dass das zweite Arbeitsblatt auch das gleiche Smart-Marker-Tag haben sollte und Sie anrufen müssen[WorkbookDesigner.Process (sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) Methode für beide Blätter. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](60489775.xlsx) generiert durch den Code für eine Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
