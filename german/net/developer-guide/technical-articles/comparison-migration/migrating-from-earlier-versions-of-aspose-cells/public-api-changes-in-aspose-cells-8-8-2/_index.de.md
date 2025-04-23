---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.2
type: docs
weight: 280
url: /de/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen der Aspose.Cells-API von Version 8.8.1 auf 8.8.2, die für Modul-/Anwendungsentwickler interessant sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen etc., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Referenzen automatisch aktualisieren beim Löschen von leeren Zeilen und Spalten**
Aspose.Cells for .NET 8.8.2 hat die überladenen Versionen der Cells.DeleteBlankRows und Cells.DeleteBlankColumns Methoden freigelegt. Die neuen Methoden können eine Instanz der DeleteOptions-Klasse akzeptieren und können dazu verwendet werden, die Situationen zu bewältigen, die durch kaputte Referenzen in Formeln, Diagrammdatenreihen usw. entstehen könnten. Die DeleteOptions-Klasse hat derzeit nur ein Element, eine Eigenschaft des Typs Boolean mit dem Namen UpdateReference. Wenn die genannte Eigenschaft auf true gesetzt ist und die Instanz der DeleteOptions-Klasse an die Cells.DeleteBlankRows & Cells.DeleteBlankColumns Methoden übergeben wird, wird die API intern die Formelverweise (falls vorhanden) an die Änderungen anpassen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den detaillierten Artikel über [Löschen leerer Zeilen und Spalten mit aktualisierten Verweisen](/cells/de/net/aktualisieren-von-verweisen-in-anderen-arbeitsblättern-beim-löschen-leerer-spalten-und-zeilen-in-einem-arbeitsblatt/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
