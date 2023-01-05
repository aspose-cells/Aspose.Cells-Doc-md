---
title: Pubblico API Modifiche Aspose.Cells 8.8.0
type: docs
weight: 270
url: /it/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.7.2 alla 8.8.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Ottieni Cell Riferimenti per connessione esterna**
 Aspose.Cells for Java 8.8.0 ha esposto le seguenti nuove proprietà che sono utili per recuperare i riferimenti delle celle di destinazione e di output per le connessioni esterne memorizzate nel foglio di calcolo.

1. QueryTable.ConnectionId: ottiene l'ID connessione della tabella delle query.
1. ExternalConnection.Id: ottiene l'ID della connessione esterna.
1. ListObject.QueryTable: ottiene la QueryTable collegata.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne](/cells/it/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Aggiunta proprietà HTMLLoadOptions.KeepPrecision**
Aspose.Cells for Java 8.8.0 ha aggiunto la proprietà HTMLLoadOptions.KeepPrecision per controllare la conversione di valori numerici lunghi in notazione esponenziale durante l'importazione di file HTML. Per impostazione predefinita, qualsiasi valore più lungo di 15 cifre viene convertito in notazione esponenziale se i dati vengono importati dalla stringa o dal file HTML. Tuttavia, ora gli utenti possono controllare questo comportamento con l'aiuto della proprietà HTMLLoadOptions.KeepPrecision. Se la suddetta proprietà è impostata su true, i valori verranno importati così come sono nell'origine.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[ Evitare la conversione di grandi valori numerici in notazione esponenziale](/cells/it/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

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
Aspose.Cells for Java 8.8.0 ha esposto la proprietà HTMLLoadOptions.DeleteRedundantSpaces per mantenere o eliminare gli spazi extra dopo il tag di interruzione di riga (<br>Tag) durante l'importazione dei dati dalla stringa o dal file HTML. La proprietà HTMLLoadOptions.DeleteRedundantSpaces ha il valore predefinito false, il che significa che tutti gli spazi extra verranno conservati e importati nell'oggetto Workbook, tuttavia, se impostata su true, API eliminerà tutti gli spazi ridondanti che seguono il tag di interruzione di riga.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Elimina gli spazi ridondanti da HTML](/cells/it/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 Lo scenario di utilizzo semplice è il seguente.

**Java**

{{< highlight "csharp" >}}

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

byte[]byteArray = html.getBytes();

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
 Aspose.Cells for Java 8.8.0 ha esposto la proprietà Style.QuotePrefix per rilevare se un valore di cella inizia con un simbolo di virgoletta singola.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Rileva la quotazione singola all'inizio del valore Cell](/cells/it/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 Lo scenario di utilizzo semplice è il seguente.

**Java**

{{< highlight "csharp" >}}

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
## **API obsolete**
### **Proprietà LoadOptions.ConvertNumericData obsoleta**
Aspose.Cells 8.8.0 ha contrassegnato la proprietà LoadOptions.ConvertNumericData come obsoleta. Utilizzare la proprietà corrispondente dalle classi HTMLLoadOptions o TxtLoadOptions.
