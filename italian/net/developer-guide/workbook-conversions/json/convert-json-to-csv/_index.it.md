---
title: Converti JSON in CSV
type: docs
weight: 210
url: /it/net/convert-json-to-csv/
---

## **Convertire JSON in CSV**

Aspose.Cells supporta la conversione di JSON semplice e annidato in CSV. A tale scopo, l'API fornisce [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) e [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) fornisce le opzioni per il layout JSON come [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle) (ignora il titolo se l'array è una proprietà di un oggetto) o [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable) (elabora l'array come una tabella). La classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) elabora il JSON utilizzando le opzioni di layout impostate con la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions).

Il seguente esempio di codice dimostra l'uso delle classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) e [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) per caricare il [file JSON di origine](104398869.json) e genera il [file CSV di output](104398870.csv).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
