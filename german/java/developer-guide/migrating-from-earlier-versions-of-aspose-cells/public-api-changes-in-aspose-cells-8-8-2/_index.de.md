---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.2
type: docs
weight: 290
url: /de/java/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.1 zu 8.8.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Verweise automatisch aktualisieren, während leere Zeilen und Spalten gelöscht werden**
 Aspose.Cells for Java 8.8.2 hat die überladenen Versionen der Methoden Cells.deleteBlankRows und Cells.deleteBlankColumns verfügbar gemacht. Die neuen Methoden können eine Instanz der DeleteOptions-Klasse akzeptieren und können verwendet werden, um die Situationen zu überwinden, die aufgrund von fehlerhaften Verweisen in Formeln, Diagrammreihendaten usw. auftreten können. Die DeleteOptions-Klasse hat derzeit nur ein Mitglied, eine Eigenschaft vom Typ Boolean mit dem Namen UpdateReference. Wenn die besagte Eigenschaft auf „true“ gesetzt ist und die Instanz der DeleteOptions-Klasse an die Methoden Cells.deleteBlankRows und Cells.deleteBlankColumns übergeben wird, passt API die Formelreferenzen (falls vorhanden) intern an, um die Änderungen aufzunehmen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Löschen leerer Zeilen und Spalten mit aktualisierten Referenzen](/cells/de/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

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
