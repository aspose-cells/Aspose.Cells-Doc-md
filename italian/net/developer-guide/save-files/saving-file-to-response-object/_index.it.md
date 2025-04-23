---
title: Salvataggio File in un Oggetto di Risposta
type: docs
weight: 50
url: /it/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile manipolare i file. Questo articolo spiega i vari modi in cui i file possono essere salvati in un oggetto di risposta.

{{% /alert %}}

## **Salvataggio del file nell'oggetto di risposta**

È anche possibile generare un file dinamicamente e inviarlo direttamente a un browser del client. Per farlo, utilizza una versione sovraccaricata speciale del metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) che accetta i seguenti parametri:

- Oggetto ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8).
- Nome file.
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition), il tipo di content-disposition del file di output.
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions), il tipo di formato file.

L'enumerazione [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) determina se il file inviato al browser fornisce l'opzione di aprire direttamente nel browser o in un'applicazione associata a .xls/.xlsx o un'altra estensione.

L'enumerazione contiene i seguenti tipi di salvataggio predefiniti:

|**Tipo**|**Descrizione**|
| :- | :- |
|Allegato|Invia il foglio di calcolo al browser e apre un'applicazione come allegato associato a .xls/.xlsx o altre estensioni|
|Inline|Invia il documento al browser e presenta un'opzione per salvare il foglio di calcolo sul disco o aprirlo all'interno del browser|

### **File XLS**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **File XLSX**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **File PDF**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Nota**

A causa dell'oggetto "System.Web.HttpResponse" che non è incluso in .NET5 e .Netstandard,
Quindi questa funzione non esiste nella versione Aspose.Cells .NET5 e .Netstandard, è possibile fare riferimento al codice seguente per salvare il file nello stream, quindi manipolare lo stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
