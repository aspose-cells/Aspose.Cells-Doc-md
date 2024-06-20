---
title: Arbeitsblätter verwalten
type: docs
weight: 10
url: /de/python-java/manage-worksheets/
---

Das Verwalten von Arbeitsblättern mit Aspose.Cells für Python via Java ist sehr einfach. In diesem Artikel werden das Hinzufügen, der Zugriff und das Entfernen von Arbeitsblättern mithilfe der Aspose.Cells-API demonstriert.
## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**
Um eine neue Arbeitsmappe zu erstellen, erstellen Sie ein Objekt der Klasse [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). Die Klasse [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) repräsentiert eine Excel-Datei. Dann werden mithilfe der Methode [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) der [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) neue Arbeitsblätter zu der Excel-Datei hinzugefügt. Schließlich wird zur Speicherung der neu erstellten Excel-Datei die Methode [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) der Klasse [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) aufgerufen.

Der folgende Codeausschnitt demonstriert das Erstellen einer neuen Excel-Datei und das Hinzufügen eines Arbeitsblatts.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Arbeitsblätter zu einem Designer-Arbeitsblatt hinzufügen**
Das Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt ist genau dasselbe wie das Hinzufügen des Arbeitsblatts zu einer neuen Excel-Datei. Der einzige Unterschied besteht darin, dass anstelle einer neuen Excel-Datei eine vorhandene Datei durch die Klasse [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) geöffnet wird.

Der folgende Codeausschnitt zeigt das Hinzufügen eines Arbeitsblatts zu einem Designer-Arbeitsblatt.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Zugriff auf Arbeitsblätter mithilfe des Blattnamens**
Nach dem Laden einer Arbeitsmappe können Entwickler auf jedes Arbeitsblatt mithilfe seines Index oder Namens zugreifen. Der folgende Codeausschnitt zeigt den Zugriff auf ein Arbeitsblatt mithilfe seines Namens.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Arbeitsblätter entfernen**
Es kann vorkommen, dass einige Blätter aus der Arbeitsmappe entfernt werden müssen. Dafür bietet die API die Methode [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) an. Sie können den Blattindex oder den Blattnamen des zu entfernenden Blatts übergeben. Die folgenden Beispiele zeigen das Entfernen von Arbeitsblättern mithilfe des Blattindex und des Blattnamens.
### **Entfernen von Arbeitsblättern unter Verwendung des Blattindexes**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Arbeitsblätter anhand des Blattnamens entfernen**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
