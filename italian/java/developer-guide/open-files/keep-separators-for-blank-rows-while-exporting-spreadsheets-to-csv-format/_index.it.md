---
title: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 110
url: /it/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV**

Aspose.Cells fornisce la possibilità di mantenere i separatori di linea durante la conversione di fogli di calcolo in formato CSV. Per fare ciò, è possibile utilizzare la proprietà [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) della classe [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) è una proprietà booleana. Per mantenere i separatori per le righe vuote durante la conversione del file Excel in CSV, impostare la proprietà [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) su **true**.

Il seguente codice di esempio carica il [file Excel di origine](KeepSeparatorsForBlankRow.xlsx). Imposta la proprietà [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) a **true** e lo salva come [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). La schermata mostra il confronto tra il file Excel di origine, l'output predefinito generato durante la conversione del foglio elettronico in CSV e l'output generato impostando [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) a **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
