---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.1.0
type: docs
weight: 40
url: /it/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Questo documento descrive i cambiamenti dell'API di Aspose.Cells dalla versione 8.0.2 alla 8.1.0, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta la proprietà HtmlSaveOptions.ExportHiddenWorksheet**
La classe HtmlSaveOptions ha esposto la proprietà ExportHiddenWorksheet che può essere utilizzata per specificare se i fogli di lavoro nascosti vengono esportati nel formato HTML. Il valore predefinito è true, mentre se impostato su false, Aspose.Cells non esporterà i contenuti dei fogli di lavoro nascosti.

{{% alert color="primary" %}} 

Si prega di consultare l'articolo dettagliato su [Prevenire l'esportazione dei contenuti nascosti della tabella](/cells/it/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Aggiunta la proprietà Cell.StringValueWithoutFormat**
La proprietà StringValueWithoutFormat è stata aggiunta alla classe Cell, al fine di facilitare agli sviluppatori il recupero del valore della cella senza alcuna formattazione applicata.

Di seguito il codice fornito mostra l'utilizzo della proprietà Cell.StringValueWithoutFormat rispetto a cell.DisplayStringValue creando un foglio di calcolo da zero e applicando il formato numerico a una delle celle.

**C#**

{{< highlight csharp >}}

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
## **Proprietà Obsoletate Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs**
Molte proprietà della classe BuiltInDocumentPropertyCollection sono state contrassegnate come obsolete a partire dal Aspose.Cells for .NET 8.1.0. Queste proprietà includono Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Il motivo è che le suddette proprietà non sono utili nella preservazione dei fogli di calcolo di Excel perché Excel li omette. Queste proprietà erano originariamente scritte per documenti di Word e presentazioni di PowerPoint.
{{< app/cells/assistant language="csharp" >}}
