---
title: Modifiche all API pubblica in Aspose.Cells 8.8.0
type: docs
weight: 260
url: /it/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.7.2 alla 8.8.0 che potrebbero interessare ai sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Ottieni riferimenti di celle per la connessione esterna**
Aspose.Cells for .NET 8.8.0 ha esposto le seguenti nuove proprietà utili per recuperare i riferimenti di celle di destinazione e di output per le connessioni esterne memorizzate nel foglio di calcolo.

1. QueryTable.ConnectionId: Ottiene l'ID della connessione della tabella di query.
1. ExternalConnection.Id: Ottiene l'ID della connessione esterna.
1. ListObject.QueryTable: Ottiene la QueryTable collegata.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Trova tabelle di query e oggetti di elenco relativi alle connessioni dati esterne](/cells/it/net/trova-tabelle-di-query-e-oggetti-di-elenco-relativi-alle-connessioni-dati-esterne/)

{{% /alert %}} 
### **Aggiunta proprietà HTMLLoadOptions.KeepPrecision**
Aspose.Cells for .NET 8.8.0 ha aggiunto la proprietà HTMLLoadOptions.KeepPrecision per controllare la conversione dei valori numerici lunghi in notazione esponenziale durante l'importazione di file HTML. Per impostazione predefinita, qualsiasi valore più lungo di 15 cifre viene convertito in notazione esponenziale se i dati vengono importati da una stringa o un file HTML. Tuttavia, ora gli utenti possono controllare questo comportamento con l'aiuto della proprietà HTMLLoadOptions.KeepPrecision. Se la suddetta proprietà viene impostata su true, i valori saranno importati così come sono nella sorgente.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Evita la conversione di valori numerici grandi in notazione esponenziale](/cells/it/net/evita-la-notazione-esponenziale-dei-grandi-numeri-durante-limportazione-da/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Aggiunta proprietà HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Elimina spazi ridondanti da HTML](/cells/it/net/elimina-gli-spazi-redundanti-dopo-uninterruzione-di-riga-durante-limportazione/)

{{% /alert %}} 

Lo scenario di utilizzo semplice appare come segue.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Aggiunta proprietà Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 ha esposto la proprietà Style.QuotePrefix al fine di rilevare se un valore della cella inizia con un singolo simbolo di citazione.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Rilevare singola citazione all'inizio del valore della cella](/cells/it/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Lo scenario di utilizzo semplice appare come segue.

**C#**

{{< highlight csharp >}}

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
## **API deprecate**
### **Proprietà Obsoleta LoadOptions.ConvertNumericData**
Aspose.Cells 8.8.0 ha contrassegnato la proprietà LoadOptions.ConvertNumericData come obsoleta. Si prega di utilizzare la corrispondente proprietà delle classi HTMLLoadOptions o TxtLoadOptions.
