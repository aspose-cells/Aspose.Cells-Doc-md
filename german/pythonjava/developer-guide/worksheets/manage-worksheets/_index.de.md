---
title: Arbeitsblätter verwalten
type: docs
weight: 10
url: /de/python-java/manage-worksheets/
---
Das Verwalten von Arbeitsblättern mit Aspose.Cells for Python via Java ist sehr einfach. In diesem Artikel demonstrieren wir das Hinzufügen, Zugreifen und Entfernen von Arbeitsblättern mithilfe von Aspose.Cells API.
## **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**
 Um eine neue Arbeitsmappe zu erstellen, erstellen Sie ein Objekt der[Arbeitsmappe](https://reference.aspose.com/cells/python/asposecells.api/Workbook) Klasse. Das[Arbeitsmappe](https://reference.aspose.com/cells/python/asposecells.api/Workbook) Klasse stellt eine Excel-Datei dar. Dann mit der[hinzufügen](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) Methode der[Arbeitsblattsammlung](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , werden der Excel-Datei neue Arbeitsblätter hinzugefügt. Um schließlich die neu erstellte Excel-Datei zu speichern, rufen Sie die[sparen](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) Methode der[Arbeitsmappe](https://reference.aspose.com/cells/python/asposecells.api/Workbook)Klasse.

Das folgende Code-Snippet veranschaulicht das Erstellen einer neuen Excel-Datei und das Hinzufügen eines Arbeitsblatts.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle**
Das Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt entspricht genau dem Hinzufügen des Arbeitsblatts zu einer neuen Excel-Datei. Der einzige Unterschied besteht darin, dass wir, anstatt eine neue Excel-Datei zu erstellen, eine vorhandene Datei öffnen[Arbeitsmappe](https://reference.aspose.com/cells/python/asposecells.api/Workbook)Klasse.

Das folgende Code-Snippet veranschaulicht das Hinzufügen eines Arbeitsblatts zu einem Designer-Arbeitsblatt.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Zugriff auf Arbeitsblätter mit Blattname**
Nach dem Laden einer Arbeitsmappe können Entwickler auf jedes Arbeitsblatt zugreifen, indem sie dessen Index oder Namen verwenden. Der folgende Codeausschnitt veranschaulicht den Zugriff auf ein Arbeitsblatt mithilfe seines Namens.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Arbeitsblätter entfernen**
Es kann vorkommen, dass sich einige Blätter treffen, um aus der Arbeitsmappe entfernt zu werden. Dafür sorgt die API[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) Methode. Sie können ihm den Blattindex oder den Blattnamen des zu entfernenden Blatts übergeben. Die folgenden Beispiele veranschaulichen das Entfernen von Arbeitsblättern mithilfe des Blattindex und des Blattnamens.
### **Arbeitsblätter mit Blattindex entfernen**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Entfernen von Arbeitsblättern unter Verwendung des Blattnamens**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
