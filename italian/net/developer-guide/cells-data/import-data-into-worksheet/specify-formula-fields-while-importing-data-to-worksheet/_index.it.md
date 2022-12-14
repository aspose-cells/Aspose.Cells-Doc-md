---
title: Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro
type: docs
weight: 300
url: /it/net/specify-formula-fields-while-importing-data-to-worksheet/
---
## **Possibili scenari di utilizzo**

È possibile specificare i campi formula quando si importano dati nel foglio di lavoro utilizzando il file[**ImportTableOptions.IsFormulas**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/isformulas) . Questa proprietà prende l'array booleano dove il valore**VERO**indica che il campo è un campo formula. Ad esempio, se il terzo campo è un campo formula, lo sarà anche il terzo valore nell'array**VERO**.

## **Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro**

 Vedere il seguente codice di esempio che spiega come specificare il campo formula durante l'importazione dei dati in un foglio di lavoro. Si prega di consultare il[file Excel di output](61767838.xlsx)generato dal codice e lo screenshot che mostra l'effetto del codice sul file Excel di output.

![cose da fare:immagine_alt_testo](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.cs" >}}
