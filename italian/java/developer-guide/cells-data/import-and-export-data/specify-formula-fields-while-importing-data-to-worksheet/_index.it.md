---
title: Specificare i campi della formula durante l importazione dei dati nel foglio di lavoro
type: docs
weight: 220
url: /it/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **Possibili Scenari di Utilizzo**

Puoi specificare campi di formula quando importi dati nel tuo foglio di lavoro usando il metodo [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas). Questo metodo prende un array booleano dove il valore **true** significa che il campo è un campo di formula. Ad esempio, se il terzo campo è un campo di formula, allora il terzo valore nell'array sarà **true**.

## **Specifica i campi di formula durante l'importazione dei dati nel foglio di lavoro.**

Per favore, vedi il seguente codice di esempio che spiega come specificare il campo di formula durante l'importazione dei dati in un foglio di lavoro. Si prega di vedere il [file Excel di output](61767850.xlsx) generato dal codice e la schermata che mostra l'effetto del codice sul file Excel di output.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
