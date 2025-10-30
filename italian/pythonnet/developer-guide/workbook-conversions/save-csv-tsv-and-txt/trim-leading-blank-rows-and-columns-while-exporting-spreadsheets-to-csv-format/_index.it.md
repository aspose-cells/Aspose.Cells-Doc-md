---
title: Tagliare le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 100
url: /it/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Taglia le righe e le colonne vuote iniziali durante l esportazione dei fogli di calcolo nel formato CSV utilizzando Aspose.Cells for Python via .NET API.
keywords: Python taglia le righe e le colonne vuote iniziali durante l esportazione dei fogli di calcolo nel formato CSV, taglia le righe e le colonne vuote iniziali durante il salvataggio di excel nel formato CSV in Python via NET, Python taglia le righe e le colonne vuote iniziali durante l esportazione di excel nel formato CSV.
---

## **Possibili Scenari di Utilizzo**

A volte, il tuo file Excel o CSV contiene colonne o righe iniziali vuote. Ad esempio, considera questa riga

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV del genere in Microsoft Excel, allora Microsoft Excel scarta queste righe e colonne vuote iniziali.

Per impostazione predefinita, Aspose.Cells for Python via .NET non scarta le colonne e le righe vuote iniziali durante il salvataggio, ma se desideri rimuoverle proprio come fa Microsoft Excel, allora Aspose.Cells for Python via .NET fornisce la proprietà [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/). Si prega di impostarla su **true** e quindi tutte le righe e le colonne vuote iniziali verranno eliminate durante il salvataggio.

{{% alert color="primary" %}}

Prima del rilascio di Aspose.Cells for Python via .NET 20.4, il valore predefinito di [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) era **false**. Dal rilascio 20.4, il valore predefinito di [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) è **true**.

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV**

Il seguente codice di esempio carica il [file excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote iniziali. Prima salva il file excel in formato CSV senza alcuna modifica, e poi imposta la proprietà [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) su **true** e lo salva nuovamente. La schermata mostra il [file excel di origine](sampleTrimBlankColumns.xlsx), il [file CSV di output senza taglio](outputWithoutTrimBlankColumns.csv) e il [file CSV di output con taglio](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
