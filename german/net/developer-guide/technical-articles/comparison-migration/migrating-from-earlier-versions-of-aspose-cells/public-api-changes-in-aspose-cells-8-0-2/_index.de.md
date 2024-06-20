---
title: Öffentliche API Änderungen in Aspose.Cells 8.0.2
type: docs
weight: 30
url: /de/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells-API von Version 8.0.1 auf 8.0.2, die für Modul-/Anwendungs-Entwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **TextDirection-Eigenschaft zur Shape-Klasse hinzugefügt**
Die Shape-Klasse hat die TextDirection-Eigenschaft freigelegt, die verwendet werden kann, um die Richtung des Textflusses für das Shape-Objekt zu erhalten oder festzulegen. Die TextDirection-Eigenschaft kann auch verwendet werden, um die gewünschte Textrichtung für die Kommentare in einer Tabellenkalkulation festzulegen, wie unten dargestellt.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Ändern der Textrichtung des Kommentars](/cells/de/net/textrichtung-des-kommentars-ändern/)

{{% /alert %}}
## **ConvertFormulasData-Eigenschaft zur HTMLLoadOptions-Klasse hinzugefügt**
Die ConvertFormulasData-Eigenschaft wurde der HTMLLoadOptions-Klasse hinzugefügt, um den Entwicklern das Laden von Excel-Formeln aus HTML-Dateien zu erleichtern. Die boolesche ConvertFormulasData-Eigenschaft gibt an, ob der String in eine Formel umgewandelt werden soll, wenn der Zeichenwert mit dem Zeichen '=' beginnt.

**C#**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

Der Standardwert der ConvertFormulasData-Eigenschaft ist false.

{{% /alert %}}
## **ImageOptions-Eigenschaft zur HtmlSaveOptions-Klasse hinzugefügt**
Die ImageOptions-Eigenschaft wurde der HtmlSaveOptions-Klasse hinzugefügt. Durch Freilegung der ImageOptions-Eigenschaft können die Entwickler die Einstellungen für die in HTML eingebetteten Bilder beim Exportieren von Tabellenkalkulationen festlegen.
## **Veraltete HtmlSaveOptions.ExportChartImageFormat-Eigenschaft**
HtmlSaveOptions.ExportChartImageFormat wurde ab Aspose.Cells for .NET 8.0.2 als veraltet markiert. Es wird empfohlen, HtmlSaveOptions.ImageOptions stattdessen für die Einstellungen des Bildformats beim Export von Arbeitsmappen in das HTML-Format zu verwenden.
