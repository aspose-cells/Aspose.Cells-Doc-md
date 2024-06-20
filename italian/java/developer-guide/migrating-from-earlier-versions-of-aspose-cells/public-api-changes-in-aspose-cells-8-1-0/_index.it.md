---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.1.0
type: docs
weight: 50
url: /it/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Questo documento descrive i cambiamenti dell'API di Aspose.Cells dalla versione 8.0.2 alla 8.1.0, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta la proprietà HtmlSaveOptions.ExportHiddenWorksheet**
La classe HtmlSaveOptions ha esposto la proprietà ExportHiddenWorksheet che può essere utilizzata per specificare se i fogli di lavoro nascosti vengono esportati nel formato HTML. Il valore predefinito è true, mentre se impostato su false, Aspose.Cells non esporterà i contenuti dei fogli di lavoro nascosti.

{{% alert color="primary" %}} 

Si prega di verificare l'articolo dettagliato su [Impedire l'esportazione del foglio di lavoro nascosto](/cells/it/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Aggiunta la proprietà Cell.StringValueWithoutFormat**
La proprietà StringValueWithoutFormat è stata aggiunta alla classe Cell, al fine di facilitare agli sviluppatori il recupero del valore della cella senza alcuna formattazione applicata. 

Il frammento di codice fornito di seguito dimostra l'utilizzo del metodo Cell.getStringValueWithoutFormat rispetto al cell.getDisplayStringValue creando un foglio di calcolo da zero e applicando il formato numerico a una delle celle. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

L'output del codice precedente è il seguente

Valore Stringa Formattato: 123,456
Valore Stringa non Formattato: 123456

{{% /alert %}}
## **Proprietà Obsoletate Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs**
Molte proprietà della classe BuiltInDocumentPropertyCollection sono state contrassegnate come obsolete a partire dal Aspose.Cells for .NET 8.1.0. Queste proprietà includono Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Il motivo è che le suddette proprietà non sono utili nella preservazione dei fogli di calcolo di Excel perché Excel li omette. Queste proprietà erano originariamente scritte per documenti di Word e presentazioni di PowerPoint. 
