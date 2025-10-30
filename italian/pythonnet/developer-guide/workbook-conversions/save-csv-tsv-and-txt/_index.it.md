---
title: Converti Excel in CSV, TSV e Txt
linktitle: Salva come CSV, TSV e Txt
type: docs
weight: 40
url: /it/python-net/convert-excel-to-csv-tsv-and-txt/
description: Converti Excel in CSV, TSV e Txt utilizzando l API Aspose.Cells per Python via .NET.
keywords: Python Converti Excel in CSV, TSV e Txt, Converti Excel in CSV, TSV e Txt in Python via NET, Converti Workbook Excel in CSV, TSV e Txt.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET rende possibile la conversione di file excel, ods, json e di altri formati in CSV, TSV e TXT.

{{% /alert %}}

## **Salvataggio Workbook in formato testo o CSV**

A volte vuoi convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, etc.), sia Microsoft Excel che Aspose.Cells per Python via .NET di default salvano solo i contenuti del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un intero workbook in formato testo. Carica il workbook di origine che potrebbe essere un file di fogli di calcolo Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

È possibile modificare lo stesso esempio per salvare il file in formato CSV. Per impostazione predefinita, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) è la virgola, quindi non specificare un separatore se si salva in formato CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Salvataggio file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Argomenti avanzati**
- [Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV](/cells/it/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV](/cells/it/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="python-net" >}}
