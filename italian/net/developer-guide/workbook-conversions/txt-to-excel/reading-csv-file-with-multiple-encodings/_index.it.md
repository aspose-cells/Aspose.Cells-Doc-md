---
title: Lettura del file CSV con codifiche multiple
type: docs
weight: 200
url: /it/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc.). Aspose.Cells consente di caricare tali file CSV e di convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

 Aspose.Cells fornisce il[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) proprietà, che è necessario impostare**VERO** per caricare correttamente il file CSV con più codifiche.

 Lo screenshot seguente mostra un file CSV di esempio che contiene due righe. La prima riga è dentro**ANSI** encoding e la seconda riga è in**Unicode** codifica

|**File di input**|
|:- |
|![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_1.png)|

 La seguente schermata mostra il file XLSX convertito dal precedente file CSV senza impostare il[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) proprietà a**VERO**. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna sistemazione fatta per codifiche multiple**|
|:- |
|![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_2.png)|

 La seguente schermata mostra il file XSLX convertito dal precedente file CSV dopo aver impostato l'estensione[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) proprietà a**VERO**. Come puoi vedere, il testo Unicode è ora convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
|:- |
|![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte correttamente il file CSV precedente nel formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## articoli Correlati

- [Apertura file CSV](/cells/it/net/opening-files-with-different-formats/#opening-csv-files)
