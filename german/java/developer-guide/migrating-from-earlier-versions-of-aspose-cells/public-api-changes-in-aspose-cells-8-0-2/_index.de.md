---
title: Öffentlich API Änderungen in Aspose.Cells 8.0.2
type: docs
weight: 40
url: /de/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.0.1 zu 8.0.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **TextDirection-Eigenschaft zur Shape-Klasse hinzugefügt**
Die Shape-Klasse verfügt über eine verfügbar gemachte TextDirection-Eigenschaft, mit der die Richtung des Textflusses für das Shape-Objekt abgerufen oder festgelegt werden kann. Die TextDirection-Eigenschaft kann auch verwendet werden, um die gewünschte Textrichtung für die Kommentare in einer Tabelle festzulegen, wie unten gezeigt.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **ConvertFormulasData-Eigenschaft zur HTMLLoadOptions-Klasse hinzugefügt**
Die ConvertFormulasData-Eigenschaft wurde der HTMLLoadOptions-Klasse hinzugefügt, um Entwicklern das Laden von Excel-Formeln aus HTML-Dateien zu erleichtern. Die boolesche Eigenschaft ConvertFormulasData gibt an, ob die Zeichenfolge in eine Formel konvertiert werden soll oder nicht, wenn der Zeichenfolgenwert mit dem Zeichen „=“ beginnt.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

Der Standardwert der ConvertFormulasData-Eigenschaft ist false.

{{% /alert %}}
## **ImageOptions-Eigenschaft zur HtmlSaveOptions-Klasse hinzugefügt**
 Die ImageOptions-Eigenschaft wurde der HtmlSaveOptions-Klasse hinzugefügt. Das Verfügbarmachen der ImageOptions-Eigenschaft hat es den Entwicklern ermöglicht, die Einstellungen für die in HTML eingebetteten Bilder beim Exportieren von Tabellenkalkulationen festzulegen.
## **Veraltete HtmlSaveOptions.ExportChartImageFormat-Eigenschaft**
HtmlSaveOptions.ExportChartImageFormat wurde ab Aspose.Cells for .NET 8.0.2 als veraltet markiert. Es wird empfohlen, stattdessen HtmlSaveOptions.ImageOptions für Bildformateinstellungen zu verwenden, während Tabellenkalkulationen in das Format HTML exportiert werden.
