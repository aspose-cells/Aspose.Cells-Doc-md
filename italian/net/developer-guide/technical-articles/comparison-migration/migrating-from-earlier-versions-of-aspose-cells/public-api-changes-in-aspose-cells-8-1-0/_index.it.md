---
title: Pubblico API Modifiche Aspose.Cells 8.1.0
type: docs
weight: 40
url: /it/net/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche al Aspose.Cells API dalla versione 8.0.2 alla 8.1.0, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta proprietà HtmlSaveOptions.ExportHiddenWorksheet**
La classe HtmlSaveOptions ha esposto la proprietà ExportHiddenWorksheet che può essere utilizzata per specificare se i fogli di lavoro nascosti vengono esportati in formato HTML. Il valore predefinito è vero. mentre se impostato su false, Aspose.Cells non esporterà i contenuti nascosti del foglio di lavoro.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Impedisci l'esportazione del foglio di lavoro nascosto](/cells/it/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Aggiunta proprietà Cell.StringValueWithoutFormat**
La proprietà StringValueWithoutFormat è stata aggiunta alla classe Cell, per facilitare agli sviluppatori il recupero del valore della cella senza alcuna formattazione applicata.

Il frammento di codice fornito di seguito illustra l'utilizzo della proprietà Cell.StringValueWithoutFormat rispetto a cell.DisplayStringValue creando un foglio di calcolo da zero e applicando il formato numerico a una delle celle.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

L'output del codice precedente è il seguente

123,456

123456

{{% /alert %}}
## **Proprietà obsolete di byte, caratteri, caratteri con spazi, righe, paragrafi**
Molte proprietà della classe BuiltInDocumentPropertyCollection sono state contrassegnate come obsolete a partire da Aspose.Cells for .NET 8.1.0. Queste proprietà includono byte, caratteri, caratteri con spazi, righe e paragrafi. La ragione è che le suddette proprietà non sono utili nella conservazione dei fogli di calcolo Excel perché Excel le omette. Dove queste proprietà sono state originariamente scritte per documenti Word e presentazioni PowerPoint.
