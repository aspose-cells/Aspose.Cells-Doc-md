---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.2
type: docs
weight: 280
url: /de/net/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.1 zu 8.8.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Verweise automatisch aktualisieren, während leere Zeilen und Spalten gelöscht werden**
Aspose.Cells for .NET 8.8.2 hat die überladenen Versionen der Methoden Cells.DeleteBlankRows und Cells.DeleteBlankColumns verfügbar gemacht. Die neuen Methoden können eine Instanz der DeleteOptions-Klasse akzeptieren und können verwendet werden, um die Situationen zu überwinden, die aufgrund von fehlerhaften Verweisen in Formeln, Diagrammreihendaten usw. auftreten können. Die DeleteOptions-Klasse hat derzeit nur ein Mitglied, eine Eigenschaft vom Typ Boolean mit dem Namen UpdateReference. Wenn die besagte Eigenschaft auf „true“ gesetzt ist und die Instanz der Klasse „DeleteOptions“ an die Methoden „Cells.DeleteBlankRows“ und „Cells.DeleteBlankColumns“ übergeben wird, passt API die Formelreferenzen (falls vorhanden) intern an, um die Änderungen aufzunehmen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Löschen leerer Zeilen und Spalten mit aktualisierten Referenzen](/cells/de/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
