---
title: Converti JSON in CSV con Golang tramite C++
linktitle: Converti JSON in CSV
type: docs
weight: 210
url: /it/go-cpp/convert-json-to-csv/
description: Impara come convertire JSON in CSV usando Aspose.Cells for C++ con esempi di JSON semplice e annidato.
---

## **Convertire JSON in CSV**

Aspose.Cells supporta la conversione di JSON semplice e annidato in CSV. Per questo, l'API fornisce le classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) e [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) offre le opzioni per il layout JSON come [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (ignora il titolo se l'array è una proprietà di un oggetto) o [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (elabora l'array come una tabella). La classe [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) elabora il JSON usando le opzioni di layout impostate con la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/).

 Il seguente esempio di codice dimostra l'uso delle classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) e [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) per caricare il [file JSON sorgente](104398869.json) e genera il [file CSV di output](104398870.csv).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
