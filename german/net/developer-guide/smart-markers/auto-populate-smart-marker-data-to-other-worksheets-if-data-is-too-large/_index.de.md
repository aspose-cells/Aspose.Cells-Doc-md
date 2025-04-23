---
title: Automatisch Smart Marker Daten in andere Arbeitsblätter eintragen, wenn Daten zu groß sind
type: docs
weight: 50
url: /de/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie Smart Marker-Daten automatisch in andere Arbeitsblätter übertragen, wenn sie zu groß sind. Angenommen, Ihre Datenquelle enthält 1500000 Datensätze. Dies sind zu viele Datensätze für ein einzelnes Arbeitsblatt. Sie können dann den Rest der Datensätze in das nächste Arbeitsblatt verschieben. 
## **Automatische Befüllung von Smart Marker-Daten in andere Arbeitsblätter, wenn die Daten zu groß sind**
Der folgende Beispielcode verfügt über eine Datenquelle mit 21 Datensätzen. Wir möchten nur 15 Datensätze in einem Arbeitsblatt anzeigen, dann werden die restlichen Datensätze automatisch in das zweite Arbeitsblatt verschoben. Bitte beachten Sie, dass das zweite Arbeitsblatt auch denselben Smart-Marker-Tag haben sollte, und Sie müssen die Methode [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) für beide Blätter aufrufen. Bitte beachten Sie die [Ausgabedatei Excel](60489775.xlsx), die vom Code generiert wurde, als Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
