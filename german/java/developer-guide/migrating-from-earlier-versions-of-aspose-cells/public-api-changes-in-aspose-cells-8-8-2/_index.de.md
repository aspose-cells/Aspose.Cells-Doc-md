---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.2
type: docs
weight: 290
url: /de/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen der Aspose.Cells-API von Version 8.8.1 auf 8.8.2, die für Modul-/Anwendungsentwickler interessant sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen etc., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Automatisches Aktualisieren von Verweisen beim Löschen von leeren Zeilen und Spalten**
Aspose.Cells for Java 8.8.2 hat die überlasteten Versionen der Methoden Cells.deleteBlankRows & Cells.deleteBlankColumns freigelegt. Die neuen Methoden können eine Instanz der Klasse DeleteOptions akzeptieren und können verwendet werden, um den Situationen entgegenzuwirken, die aufgrund von defekten Verweisen in Formeln, Diagrammseriendaten und so weiter entstehen könnten. Die Klasse DeleteOptions hat derzeit nur ein Element, eine Eigenschaft vom Typ Boolean mit dem Namen UpdateReference. Wenn besagte Eigenschaft auf true gesetzt ist und die Instanz der Klasse DeleteOptions an die Methoden Cells.deleteBlankRows & Cells.deleteBlankColumns übergeben wird, wird die API intern die Formelverweise (falls vorhanden) anpassen, um die Änderungen zu berücksichtigen. 

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [Löschen von leeren Zeilen & Spalten mit aktualisierten Verweisen](/cells/de/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
