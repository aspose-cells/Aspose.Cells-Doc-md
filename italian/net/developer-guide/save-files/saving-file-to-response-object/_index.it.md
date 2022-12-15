---
title: Salvataggio del file nell'oggetto risposta
type: docs
weight: 50
url: /it/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells consente di manipolare i file. Questo articolo spiega i vari modi in cui i file possono essere salvati in un oggetto risposta.

{{% /alert %}}

## **Salvataggio del file nell'oggetto risposta**

 È anche possibile generare dinamicamente un file e inviarlo direttamente a un browser client. Per fare ciò, utilizzare una versione speciale di overload del file**[Salva](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**metodo che accetta i seguenti parametri:

-  ASP.NET**[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**oggetto.
- Nome del file.
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, il tipo di disposizione del contenuto del file di output.
- **[Opzioni di salvataggio](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, il tipo di formato file

 Il**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**l'enumerazione determina se il file inviato al browser offre la possibilità di aprirsi da solo direttamente nel browser o in un'applicazione associata a .xls/.xlsx o un'altra estensione.

L'enumerazione contiene i seguenti tipi di salvataggio predefiniti:

|**Tipo**|**Descrizione**|
|:- |:- |
|Attaccamento|Invia il foglio di calcolo al browser e si apre in un'applicazione come allegato associato a .xls/.xlsx o altre estensioni|
|In linea|Invia il documento al browser e presenta un'opzione per salvare il foglio di calcolo su disco o aprirlo all'interno del browser|

### **File XLS**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **File XLSX**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **File PDF**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Nota**

causa dell'oggetto "System.Web.HttpResponse" non contenuto in .NET5 e .Netstandard,
Quindi questa funzione non esiste nella versione Aspose.Cells .NET5 e .Netstandard, puoi fare riferimento al seguente codice per salvare il file nello stream, quindi eseguire l'operazione sullo stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

