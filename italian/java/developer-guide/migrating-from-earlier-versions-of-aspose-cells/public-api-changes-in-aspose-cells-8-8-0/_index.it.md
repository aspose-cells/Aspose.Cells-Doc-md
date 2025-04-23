---
title: Modifiche all API pubblica in Aspose.Cells 8.8.0
type: docs
weight: 270
url: /it/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.7.2 alla 8.8.0 che potrebbero interessare ai sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Ottieni riferimenti di celle per la connessione esterna**
Aspose.Cells for Java 8.8.0 ha esposto le seguenti nuove proprietà che sono utili per recuperare i riferimenti alla cella di destinazione e di output per le connessioni esterne memorizzate nel foglio di calcolo. 

1. QueryTable.ConnectionId: Ottiene l'ID della connessione della tabella di query.
1. ExternalConnection.Id: Ottiene l'ID della connessione esterna.
1. ListObject.QueryTable: Ottiene la QueryTable collegata.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Trova Tabelle Query e Oggetti Lista relativi alle Connessioni Dati Esterne](/cells/it/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Aggiunta proprietà HTMLLoadOptions.KeepPrecision**
Aspose.Cells for Java 8.8.0 ha aggiunto la proprietà HTMLLoadOptions.KeepPrecision al fine di controllare la conversione di valori numerici lunghi in notazione esponenziale durante l'importazione di file HTML. Per impostazione predefinita, ogni valore più lungo di 15 cifre viene convertito in notazione esponenziale se i dati vengono importati da una stringa o file HTML. Tuttavia, ora gli utenti possono controllare questo comportamento con l'aiuto della proprietà HTMLLoadOptions.KeepPrecision. Se la suddetta proprietà è impostata su true, i valori verranno importati così come sono nella fonte.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Evitare la Conversione di Valori Numerici Lunghi in Notazione Esponenziale ](/cells/it/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Aggiunta proprietà HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Eliminare Spazi Redundanti da HTML](/cells/it/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Lo scenario di utilizzo semplice appare come segue. 

**Java**

{{< highlight csharp >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Aggiunta proprietà Style.QuotePrefix**
Aspose.Cells for Java 8.8.0 ha esposto la proprietà Style.QuotePrefix al fine di rilevare se un valore della cella inizia con il simbolo di un singolo apice. 

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Rilevare il Singolo Apice all'Inizio del Valore della Cella](/cells/it/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Lo scenario di utilizzo semplice appare come segue. 

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **API deprecate**
### **Proprietà Obsoleta LoadOptions.ConvertNumericData**
Aspose.Cells 8.8.0 ha contrassegnato la proprietà LoadOptions.ConvertNumericData come obsoleta. Si prega di utilizzare la corrispondente proprietà delle classi HTMLLoadOptions o TxtLoadOptions.
{{< app/cells/assistant language="java" >}}
