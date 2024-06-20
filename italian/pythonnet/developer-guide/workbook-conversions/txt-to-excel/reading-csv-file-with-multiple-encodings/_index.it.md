---
title: Lettura di file CSV con codifiche multiple
type: docs
weight: 200
url: /it/python-net/reading-csv-file-with-multiple-encodings/
description: Lettura del file CSV con più codifiche utilizzando Aspose.Cells per Python via .NET API.
keywords: Lettura del file CSV con più codifiche in Python, Convertire il file CSV con più codifiche in Excel in Python via NET, Convertire il file CSV con più codifiche in xlsx in Python, Caricare il file CSV con più codifiche in un file Excel.
---

{{% alert color="primary" %}}

A volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc). Aspose.Cells ti permette di caricare tali file CSV e convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/), che è necessario impostare su **true** per caricare correttamente il tuo file CSV con più codifiche.

La seguente schermata mostra un esempio di file CSV che contiene due righe. La prima riga è in codifica **ANSI** e la seconda riga è in codifica **Unicode**

|**File di input**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La seguente schermata mostra il file XLSX convertito dal file CSV precedente senza impostare la proprietà [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) su **true**. Come si può vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna modifica per la codifica multipla**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La seguente schermata mostra il file XSLX convertito dal file CSV precedente dopo aver impostato la proprietà [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) su **true**. Come si può vedere, il testo Unicode è ora convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte il precedente file CSV nel formato XLSX correttamente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
