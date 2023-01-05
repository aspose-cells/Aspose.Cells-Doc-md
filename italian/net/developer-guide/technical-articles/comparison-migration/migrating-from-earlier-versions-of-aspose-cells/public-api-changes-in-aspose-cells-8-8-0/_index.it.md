---
title: Pubblico API Modifiche Aspose.Cells 8.8.0
type: docs
weight: 260
url: /it/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.7.2 alla 8.8.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Ottieni Cell Riferimenti per connessione esterna**
Aspose.Cells for .NET 8.8.0 ha esposto le seguenti nuove proprietà che sono utili per recuperare i riferimenti delle celle di destinazione e di output per le connessioni esterne memorizzate nel foglio di calcolo.

1. QueryTable.ConnectionId: ottiene l'ID connessione della tabella delle query.
1. ExternalConnection.Id: ottiene l'ID della connessione esterna.
1. ListObject.QueryTable: ottiene la QueryTable collegata.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne](/cells/it/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Aggiunta proprietà HTMLLoadOptions.KeepPrecision**
Aspose.Cells for .NET 8.8.0 ha aggiunto la proprietà HTMLLoadOptions.KeepPrecision per controllare la conversione di valori numerici lunghi in notazione esponenziale durante l'importazione di file HTML. Per impostazione predefinita, qualsiasi valore più lungo di 15 cifre viene convertito in notazione esponenziale se i dati vengono importati dalla stringa o dal file HTML. Tuttavia, ora gli utenti possono controllare questo comportamento con l'aiuto della proprietà HTMLLoadOptions.KeepPrecision. Se la suddetta proprietà è impostata su true, i valori verranno importati così come sono nell'origine.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[ Evitare la conversione di grandi valori numerici in notazione esponenziale](/cells/it/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Aggiunta proprietà HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 ha esposto la proprietà HTMLLoadOptions.DeleteRedundantSpaces per mantenere o eliminare gli spazi extra dopo il tag di interruzione di riga (<br>Tag) durante l'importazione dei dati dalla stringa o dal file HTML. La proprietà HTMLLoadOptions.DeleteRedundantSpaces ha il valore predefinito false, il che significa che tutti gli spazi extra verranno conservati e importati nell'oggetto Workbook, tuttavia, se impostata su true, API eliminerà tutti gli spazi ridondanti che seguono il tag di interruzione di riga.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Elimina gli spazi ridondanti da HTML](/cells/it/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Lo scenario di utilizzo semplice è il seguente.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Aggiunta proprietà Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 ha esposto la proprietà Style.QuotePrefix per rilevare se un valore di cella inizia con un simbolo di virgoletta singola.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Rileva la quotazione singola all'inizio del valore Cell](/cells/it/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Lo scenario di utilizzo semplice è il seguente.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **API obsolete**
### **Proprietà LoadOptions.ConvertNumericData obsoleta**
Aspose.Cells 8.8.0 ha contrassegnato la proprietà LoadOptions.ConvertNumericData come obsoleta. Utilizzare la proprietà corrispondente dalle classi HTMLLoadOptions o TxtLoadOptions.
