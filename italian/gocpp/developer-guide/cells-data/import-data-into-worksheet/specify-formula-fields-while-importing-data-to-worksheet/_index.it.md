---
title: Specificare i campi formula durante l importazione dei dati nel foglio di lavoro con Golang tramite C++
linktitle: Specificare i campi della formula durante l importazione dei dati nel foglio di lavoro
type: docs
weight: 300
url: /it/go-cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Impara come specificare i campi formula durante l importazione dei dati nel foglio di lavoro attraverso l API Aspose.Cells for C++.
keywords: Specificare campi di formula durante l importazione dei dati nel foglio di lavoro, Imposta campi di formula durante l aggiunta di dati al foglio di lavoro
---

## **Possibili Scenari di Utilizzo**

È possibile specificare i campi di formula quando si importano dati nel foglio di lavoro utilizzando [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/go-cpp/importtableoptions/getisformulas/). Questa proprietà accetta un array booleano in cui il valore **true** significa che il campo è un campo di formula. Ad esempio, se il terzo campo è un campo di formula, allora il terzo valore nell'array sarà **true**.

## **Specifica i campi di formula durante l'importazione dei dati nel foglio di lavoro.**

Si prega di consultare il seguente codice di esempio che spiega come specificare il campo della formula durante l'importazione dei dati in un foglio di lavoro. Si prega di consultare il [file Excel di output](61767838.xlsx) generato dal codice e lo screenshot che mostra l'effetto del codice sul file Excel di output.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyFormulaFieldsWhileImportingDataToWorksheet.go" >}}
