---
title: Converti JSON in CSV
type: docs
weight: 160
url: /it/java/convert-json-to-csv/
---

Aspose.Cells supporta la conversione di JSON semplici e nidificati in CSV. A tale scopo, l'API fornisce le classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) e [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) fornisce le opzioni per la struttura JSON come [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (ignora il titolo se l'array è una proprietà di un oggetto) o [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (elabora l'array come una tabella). La classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) elabora il JSON utilizzando le opzioni di layout impostate con la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions).

Il seguente esempio di codice dimostra l'uso delle classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) e [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) per caricare il [file JSON di origine](SampleJson.json) e generare l [file CSV di output](SampleJson_out.csv).

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
{{< app/cells/assistant language="java" >}}
