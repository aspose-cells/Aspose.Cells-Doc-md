---
title: Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro
type: docs
weight: 220
url: /it/java/specify-formula-fields-while-importing-data-to-worksheet/
---
## **Possibili scenari di utilizzo**

 È possibile specificare i campi formula quando si importano dati nel foglio di lavoro utilizzando il file[**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas) metodo. Questo metodo prende l'array booleano dove il valore**VERO**indica che il campo è un campo formula. Ad esempio, se il terzo campo è un campo formula, lo sarà anche il terzo valore nell'array**VERO**.

## **Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro**

 Vedere il seguente codice di esempio che spiega come specificare il campo formula durante l'importazione dei dati in un foglio di lavoro. Si prega di consultare il[file Excel di output](61767850.xlsx) generato dal codice e lo screenshot che mostra l'effetto del codice sul file Excel di output.

![cose da fare:immagine_alt_testo](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
