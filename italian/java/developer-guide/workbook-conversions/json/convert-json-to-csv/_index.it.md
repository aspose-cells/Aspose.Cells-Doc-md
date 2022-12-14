---
title: Converti JSON in CSV
type: docs
weight: 160
url: /it/java/convert-json-to-csv/
---
Aspose.Cells supporta la conversione di JSON semplice e nidificato in CSV. Per questo, lo API fornisce[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)e[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classi. Il[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)class fornisce le opzioni per il layout JSON come[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignora il titolo se l'array è una proprietà di un oggetto) o[**ArrayComeTabella**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(elabora l'array come una tabella). Il[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)class elabora il JSON utilizzando le opzioni di layout impostate con il file[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)classe.

L'esempio di codice seguente illustra l'utilizzo di[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)e[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classi per caricare il file[file JSON di origine](SampleJson.json)e genera il[file di output CSV](SampleJson_out.csv).

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
