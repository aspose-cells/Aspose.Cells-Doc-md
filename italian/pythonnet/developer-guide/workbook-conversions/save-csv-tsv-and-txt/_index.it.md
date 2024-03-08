---
title: Converti Excel in CSV,TSV e Txt
linktitle: Salva come CSV,TSV e Txt
type: docs
weight: 40
url: /it/python-net/convert-excel-to-csv-tsv-and-txt/
description: Converti Excel in CSV,TSV e Txt utilizzando Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET rende possibile convertire file Excel, ods, json e altri formati in CSV, TSV e TXT.

{{% /alert %}}

##  **Salvataggio della cartella di lavoro in formato testo o CSV**

volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), per impostazione predefinita sia Microsoft Excel che Aspose.Cells for Python via .NET salvano solo il contenuto del foglio di lavoro attivo.

Nell'esempio di codice seguente viene illustrato come salvare un'intera cartella di lavoro in formato testo. Carica la cartella di lavoro di origine che potrebbe essere qualsiasi file di foglio di calcolo Excel o OpenOffice Microsoft (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un numero qualsiasi di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli della cartella di lavoro nel formato TXT.

 Puoi modificare lo stesso esempio per salvare il file su CSV. Per impostazione predefinita,**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**è una virgola, quindi non specificare un separatore se si salva nel formato CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Salvataggio di file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **Argomenti avanzati**
- [Mantieni i separatori per le righe vuote durante l'esportazione dei fogli di calcolo nel formato CSV](/cells/it/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Taglia le righe e le colonne vuote iniziali durante l'esportazione dei fogli di calcolo nel formato CSV](/cells/it/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
