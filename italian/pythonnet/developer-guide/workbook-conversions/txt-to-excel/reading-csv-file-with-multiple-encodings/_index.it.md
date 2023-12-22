---
title: Lettura del file CSV con codifiche multiple
type: docs
weight: 200
url: /it/python-net/reading-csv-file-with-multiple-encodings/
description: Lettura del file CSV con codifiche multiple utilizzando Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

A volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc.). Aspose.Cells ti consente di caricare tali file CSV e di convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

 Aspose.Cells fornisce il[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) proprietà, che è necessario impostare su**VERO** per caricare correttamente il file CSV con più codifiche.

 La schermata seguente mostra un file di esempio CSV che contiene due righe. La prima riga è dentro**ANSI** codifica e la seconda riga è inserita**Unicode** codifica

|**File di input**|
| :- |
|![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_1.png)|

La schermata seguente mostra il file XLSX convertito dal file CSV precedente senza impostare il valore[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)proprietà su *true**. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna sistemazione per la codifica multipla**|
| :- |
|![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_2.png)|

 La seguente schermata mostra il file XSLX convertito dal file CSV sopra dopo aver impostato il file[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)proprietà su *true**. Come puoi vedere, il testo Unicode è ora convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
| :- |
|![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte correttamente il file CSV sopra nel formato XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
