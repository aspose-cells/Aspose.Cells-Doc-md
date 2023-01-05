---
title: Pubblico API Modifiche Aspose.Cells 8.0.2
type: docs
weight: 40
url: /it/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche al Aspose.Cells API dalla versione 8.0.1 alla 8.0.2, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta proprietà TextDirection alla classe Shape**
La classe Shape ha esposto la proprietà TextDirection che può essere utilizzata per ottenere o impostare la direzione del flusso di testo per l'oggetto Shape. La proprietà TextDirection può essere utilizzata anche per impostare la direzione del testo desiderata per i commenti in un foglio di calcolo, come illustrato di seguito.

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
## **Aggiunta la proprietà ConvertFormulasData alla classe HTMLLoadOptions**
La proprietà ConvertFormulasData è stata aggiunta alla classe HTMLLoadOptions, per facilitare agli sviluppatori il caricamento delle formule Excel dai file HTML. La proprietà booleana ConvertFormulasData indica se convertire o meno la stringa in una formula quando il valore della stringa inizia con il carattere '='.

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

Il valore predefinito della proprietà ConvertFormulasData è false.

{{% /alert %}}
## **Proprietà ImageOptions aggiunta alla classe HtmlSaveOptions**
 La proprietà ImageOptions è stata aggiunta alla classe HtmlSaveOptions. L'esposizione della proprietà ImageOptions ha consentito agli sviluppatori di impostare le preferenze per le immagini incorporate nel HTML durante l'esportazione dei fogli di calcolo.
## **Proprietà HtmlSaveOptions.ExportChartImageFormat obsoleta**
HtmlSaveOptions.ExportChartImageFormat è stato contrassegnato come obsoleto a partire da Aspose.Cells for .NET 8.0.2. Si consiglia invece di utilizzare HtmlSaveOptions.ImageOptions per le impostazioni del formato immagine durante l'esportazione di fogli di calcolo nel formato HTML.
