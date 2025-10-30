---
title: Gestire la cartella di lavoro con Golang tramite C++
linktitle: Workbook
type: docs
weight: 60
url: /it/go-cpp/managing-workbooks-and-worksheets/
description: Impara come Gestire un Workbook tramite le API Aspose.Cells for C++.
keywords: Come Gestire un Workbook in C++, Gestisci Workbook e fogli di lavoro usando C++, Opera su workbook e fogli di lavoro in C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ fornisce un'API potente e flessibile per gestire workbook e fogli di lavoro. Questa sezione spiega come creare, aprire e manipolare workbooks e fogli di lavoro programmaticamente.

{{% /alert %}}

## **Creazione di un nuovo foglio di lavoro**
Per creare un nuovo workbook:

1. Creare un'istanza della classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).
2. Aggiungere fogli di lavoro alla cartella di lavoro usando la classe [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Salvare la cartella di lavoro usando il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **Apertura di un Workbook Esistente**
Per aprire un workbook esistente:

1. Creare un'istanza della classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) e passare il percorso del file al costruttore.
2. Accedere ai fogli di lavoro usando la classe [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Modifica il workbook secondo necessità.
4. Salvare la cartella di lavoro usando il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **Gestione dei Fogli di Lavoro**
Aspose.Cells for C++ offre un'ampia gamma di metodi per gestire i fogli di lavoro, inclusa l’aggiunta, la rimozione e la rinomina dei fogli.

### **Aggiunta di un Foglio di Lavoro**
Per aggiungere un nuovo foglio di lavoro:

1. Accedere alla classe [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) dalla cartella di lavoro.
2. Usare il metodo [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/) per aggiungere un nuovo foglio di lavoro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **Rimozione di un foglio di lavoro**
Per rimuovere un foglio di lavoro:

1. Accedere alla classe [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) dalla cartella di lavoro.
2. Usare il metodo [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/) per rimuovere un foglio di lavoro per indice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **Rinomina un foglio di lavoro**
Per rinominare un foglio di lavoro:

1. Accedere alla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) dalla cartella di lavoro.
2. Usare il metodo [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/) per rinominare il foglio di lavoro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **Conclusioni**
Aspose.Cells for C++ fornisce un insieme completo di strumenti per la gestione di workbook e fogli di lavoro. Che tu abbia bisogno di creare un nuovo workbook, aprirne uno esistente o manipolare i fogli di lavoro, Aspose.Cells rende semplice lavorare con i file Excel programmaticamente.
