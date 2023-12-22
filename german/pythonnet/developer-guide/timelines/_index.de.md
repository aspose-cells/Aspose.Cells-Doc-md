---
title: Zeitleiste einfügen
linktitle: Zeitleisten
type: docs
weight: 170
url: /de/python-net/create-timeline/
description: Erfahren Sie, wie Sie eine Zeitleiste mit Aspose.Cells for Python via .NET erstellen.
---
##  **Mögliche Nutzungsszenarien**

Anstatt Filter anzupassen, um Datumsangaben anzuzeigen, können Sie eine PivotTable-Zeitleiste verwenden – eine dynamische Filteroption, mit der Sie einfach nach Datum/Uhrzeit filtern und mit einem Schieberegler den gewünschten Zeitraum vergrößern können. Microsoft In Excel können Sie eine Zeitleiste erstellen, indem Sie eine Pivot-Tabelle auswählen und dann auf *Einfügen > Zeitleiste* klicken. Aspose.Cells for Python via .NET ermöglicht Ihnen auch das Erstellen einer Zeitleiste mit dem[**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)Methode.

##  **Erstellen Sie eine Zeitleiste für eine Pivot-Tabelle**

 Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die[Beispiel-Excel-Datei](input.xlsx)das die Pivot-Tabelle enthält. Anschließend wird die Zeitleiste basierend auf dem ersten Basis-Pivot-Feld erstellt. Schließlich wird die Arbeitsmappe gespeichert[Ausgabe XLSX](output.xlsx) Format. Der folgende Screenshot zeigt die von Aspose.Cells for Python via .NET erstellte Zeitleiste in der Excel-Ausgabedatei.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

###  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

