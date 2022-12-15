---
title: Modifiche all'API pubblica in Aspose.Cells 8.1.0
type: docs
weight: 50
url: /it/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.0.2 alla 8.1.0, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta proprietà HtmlSaveOptions.ExportHiddenWorksheet**
La classe HtmlSaveOptions ha esposto la proprietà ExportHiddenWorksheet che può essere utilizzata per specificare se i fogli di lavoro nascosti vengono esportati in formato HTML. Il valore predefinito è vero. mentre se impostato su false, Aspose.Cells non esporterà i contenuti nascosti del foglio di lavoro.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Impedisci l'esportazione del foglio di lavoro nascosto](/cells/it/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Aggiunta proprietà Cell.StringValueWithoutFormat**
 La proprietà StringValueWithoutFormat è stata aggiunta alla classe Cell, per facilitare agli sviluppatori il recupero del valore della cella senza alcuna formattazione applicata.

Il frammento di codice fornito di seguito dimostra l'utilizzo del metodo Cell.getStringValueWithoutFormat rispetto a cell.getDisplayStringValue creando un foglio di calcolo da zero e applicando il formato numerico a una delle celle.

**Giava**

{{< highlight "csharp" >}}

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

Valore stringa formattato: 123.456
Valore stringa non formattato: 123456

{{% /alert %}}
## **Proprietà obsolete di byte, caratteri, caratteri con spazi, righe, paragrafi**
 Molte proprietà della classe BuiltInDocumentPropertyCollection sono state contrassegnate come obsolete a partire da Aspose.Cells for .NET 8.1.0. Queste proprietà includono byte, caratteri, caratteri con spazi, righe e paragrafi. La ragione è che le suddette proprietà non sono utili nella conservazione dei fogli di calcolo Excel perché Excel le omette. Dove queste proprietà sono state originariamente scritte per documenti Word e presentazioni PowerPoint.
