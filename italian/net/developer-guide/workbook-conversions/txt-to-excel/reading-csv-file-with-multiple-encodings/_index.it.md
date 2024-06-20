---
title: Lettura di file CSV con codifiche multiple
type: docs
weight: 200
url: /it/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

A volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc). Aspose.Cells ti permette di caricare tali file CSV e convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded), che è necessario impostare su **true** per caricare correttamente il tuo file CSV con più codifiche.

La seguente schermata mostra un esempio di file CSV che contiene due righe. La prima riga è in codifica **ANSI** e la seconda riga è in codifica **Unicode**

|**File di input**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La seguente schermata mostra il file XLSX convertito dal file CSV precedente senza impostare la proprietà [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) su **true**. Come si può vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna modifica per la codifica multipla**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La seguente schermata mostra il file XSLX convertito dal file CSV precedente dopo aver impostato la proprietà [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) su **true**. Come si può vedere, il testo Unicode è ora convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte il precedente file CSV nel formato XLSX correttamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Articoli correlati

- [Apertura dei file CSV](/cells/it/net/opening-files-with-different-formats/#opening-csv-files)
