---
title: Taglia le righe e le colonne vuote iniziali durante l'esportazione dei fogli di calcolo nel formato CSV
type: docs
weight: 100
url: /it/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Taglia le righe e le colonne vuote iniziali durante l'esportazione dei fogli di calcolo nel formato CSV utilizzando Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Possibili scenari di utilizzo**

A volte, il tuo file Excel o CSV ha colonne o righe iniziali vuote. Consideriamo ad esempio questa riga

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando si apre un file CSV in Microsoft Excel, Microsoft Excel elimina queste righe e colonne vuote iniziali.

 Per impostazione predefinita, Aspose.Cells for Python via .NET non scarta le colonne e le righe vuote iniziali durante il salvataggio, ma se desideri rimuoverle proprio come fa Microsoft Excel, allora Aspose.Cells for Python via .NET fornisce**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** proprietà. Per favore impostalo su**VERO**quindi tutte le righe e le colonne vuote iniziali verranno scartate al momento del salvataggio.

{{% alert color="primary" %}}

 Prima del rilascio di Aspose.Cells for Python via .NET 20.4, il valore predefinito di**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**era**falso**. Dalla versione 20.4, il valore predefinito di **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** È**VERO.**

{{% /alert %}}

##  **Taglia le righe e le colonne vuote iniziali durante l'esportazione dei fogli di calcolo nel formato CSV**

 Il codice di esempio seguente carica il file[file Excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote iniziali. Prima salva il file excel nel formato CSV senza alcuna modifica e poi imposta**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** proprietà a**VERO** e lo salva di nuovo. Lo screenshot mostra il[file Excel di origine](sampleTrimBlankColumns.xlsx), [output file CSV senza ritaglio](outputWithoutTrimBlankColumns.csv), e il[output CSV file con ritaglio](outputTrimBlankColumns.csv).

![cose da fare:immagine_alt_testo](result.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
