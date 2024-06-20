---
title: Tagliare le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 100
url: /it/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Possibili Scenari di Utilizzo**

A volte, il tuo file Excel o CSV contiene colonne o righe iniziali vuote. Ad esempio, considera questa riga

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV del genere in Microsoft Excel, allora Microsoft Excel scarta queste righe e colonne vuote iniziali.

Per impostazione predefinita, Aspose.Cells non scarta le colonne e le righe vuote iniziali durante il salvataggio, ma se desideri rimuoverle proprio come fa Microsoft Excel, allora Aspose.Cells fornisce la proprietà [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn). Impostala su **true** e allora tutte le righe e le colonne vuote iniziali saranno eliminate durante il salvataggio.

{{% alert color="primary" %}}

Prima del rilascio del Aspose.Cells for .NET 20.4, il valore predefinito di [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) era **false**. Dalla versione 20.4, il valore predefinito di [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) è **true.**

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV**

Il seguente codice di esempio carica il [file excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote iniziali. Prima salva il file excel in formato CSV senza alcuna modifica, e poi imposta la proprietà [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) su **true** e lo salva nuovamente. La schermata mostra il [file excel di origine](sampleTrimBlankColumns.xlsx), il [file CSV di output senza taglio](outputWithoutTrimBlankColumns.csv) e il [file CSV di output con taglio](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
