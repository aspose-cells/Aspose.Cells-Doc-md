---
title: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 160
url: /it/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV**

Aspose.Cells fornisce la possibilità di mantenere i separatori di linea durante la conversione di fogli di calcolo in formato CSV. Per fare ciò, è possibile utilizzare la proprietà [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) della classe [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) è una proprietà booleana. Per mantenere i separatori per le righe vuote durante la conversione del file Excel in CSV, impostare la proprietà [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) su **true**.

Il seguente codice di esempio carica il [file Excel di origine](84378743.xlsx). Imposta la proprietà [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) su **true** e lo salva come [output.csv](84378744.csv). La schermata mostra il confronto tra il file Excel di origine, l'output predefinito generato durante la conversione del foglio di calcolo in CSV e l'output generato impostando [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) su **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
