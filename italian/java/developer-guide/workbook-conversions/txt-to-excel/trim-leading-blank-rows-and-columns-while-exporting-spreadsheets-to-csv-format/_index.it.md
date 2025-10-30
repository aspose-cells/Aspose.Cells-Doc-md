---
title: Tagliare le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 50
url: /it/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Possibili Scenari di Utilizzo**

A volte, il tuo file Excel o CSV contiene colonne o righe iniziali vuote. Ad esempio, considera questa riga

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV del genere in Microsoft Excel, allora Microsoft Excel scarta queste righe e colonne vuote iniziali.

Per impostazione predefinita, Aspose.Cells non scarta le colonne e le righe vuote iniziali durante il salvataggio, ma se desideri rimuoverle proprio come fa Microsoft Excel, allora Aspose.Cells fornisce la proprietà [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn). Impostala su **true** e allora tutte le righe e le colonne vuote iniziali saranno eliminate durante il salvataggio.

{{% alert color="primary" %}}

Prima del rilascio di Aspose.Cells for Java 20.4, il valore predefinito di [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) era **falso**. Dalla versione 20.4, il valore predefinito di [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) è **vero.**

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV**

Il seguente codice di esempio carica il file excel di origine che ha due colonne vuote iniziali. Prima salva il file excel in formato CSV senza alcuna modifica e poi imposta la proprietà [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) su **true** e lo salva nuovamente. La schermata mostra il [file excel di origine](sampleTrimBlankColumns.xlsx), [file CSV di output senza ritaglio](outputWithoutTrimBlankColumns.csv), e il [file CSV di output con ritaglio](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
