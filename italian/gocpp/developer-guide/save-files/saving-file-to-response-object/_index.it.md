---
title: Salva il file nel oggetto Response con Golang tramite C++
linktitle: Salvataggio File in un Oggetto di Risposta
type: docs
weight: 50
url: /it/go-cpp/saving-file-to-response-object/
description: Impara come salvare i file dinamicamente e inviarli direttamente al browser di un cliente usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile manipolare i file. Questo articolo spiega i vari modi in cui i file possono essere salvati in un oggetto di risposta.

{{% /alert %}}

## **Salvataggio del file nell'oggetto di risposta**

È anche possibile generare un file dinamicamente e inviarlo direttamente a un browser del client. Per farlo, utilizza una versione sovraccaricata speciale del metodo [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) che accetta i seguenti parametri:

- Oggetto **HttpResponse**.
- Nome file.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), il tipo di content-disposition del file di output.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), il tipo di formato del file.

L'enumerazione [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) determina se il file inviato al browser fornisce l'opzione di aprire direttamente nel browser o in un'applicazione associata a .xls/.xlsx o un'altra estensione.

L'enumerazione contiene i seguenti tipi di salvataggio predefiniti:

|**Tipo**|**Descrizione**|
| :- | :- |
|Allegato|Invia il foglio di calcolo al browser e apre un'applicazione come allegato associato a .xls/.xlsx o altre estensioni|
|Inline|Invia il documento al browser e presenta un'opzione per salvare il foglio di calcolo sul disco o aprirlo all'interno del browser|

### **File XLS**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **File XLSX**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **File PDF**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Nota**

A causa dell'oggetto "System.Web.HttpResponse" che non è incluso in .NET5 e .Netstandard,
Quindi questa funzione non esiste nella versione Aspose.Cells .NET5 e .Netstandard, è possibile fare riferimento al codice seguente per salvare il file nello stream, quindi manipolare lo stream.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
