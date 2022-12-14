---
title: Converti JSON in CSV
type: docs
weight: 210
url: /it/net/convert-json-to-csv/
---
## **Converti JSON in CSV**

Aspose.Cells supporta la conversione di JSON semplice e nidificato in CSV. Per questo, lo API fornisce**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** e**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** classi. Il**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**class fornisce le opzioni per il layout JSON come**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(ignora il titolo se l'array è una proprietà di un oggetto) o**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(elabora l'array come una tabella). Il**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**class elabora il JSON utilizzando le opzioni di layout impostate con il file**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**classe.

L'esempio di codice seguente illustra l'utilizzo di**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**e**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**classi per caricare il file[file JSON di origine](104398869.json) e genera il[file di output CSV](104398870.csv).

### **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
