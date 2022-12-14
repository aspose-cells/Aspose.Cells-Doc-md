---
title: Mantieni i separatori per le righe vuote durante l'esportazione dei fogli di calcolo in formato CSV
type: docs
weight: 110
url: /it/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Mantieni i separatori per le righe vuote durante l'esportazione dei fogli di calcolo in formato CSV**

Aspose.Cells offre la possibilità di mantenere i separatori di riga durante la conversione dei fogli di calcolo in formato CSV. Per questo, puoi usare il**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**proprietà di**[TxtSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)**classe.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**è una proprietà booleana. Per mantenere i separatori per le righe vuote durante la conversione del file Excel in CSV, impostare il**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**proprietà a**VERO**.

Il codice di esempio seguente carica il file[file Excel di origine](KeepSeparatorsForBlankRow.xlsx). Tramonta**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**proprietà a**VERO** e lo salva come[KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). Lo screenshot mostra il confronto tra il file Excel di origine, l'output predefinito generato durante la conversione del foglio di calcolo in CSV e l'output generato impostando**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**a**VERO**.

![cose da fare:immagine_alt_testo](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
