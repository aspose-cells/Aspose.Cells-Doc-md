---
title: Converti JSON in CSV
type: docs
weight: 210
url: /it/python-net/convert-json-to-csv/
description: Scopri come convertire un file JSON in formato CSV con Aspose.Cells per l API Python via .NET.
keywords: Python Converti json in csv, Converti json in csv Python via NET, Esporta json in csv, Converti json in csv.
---

## **Convertire JSON in CSV**

Aspose.Cells per Python via .NET supporta la conversione di JSON semplici e annidati in CSV. A tale scopo, l'API fornisce le classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) e [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) fornisce le opzioni per il layout JSON come [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/) (ignora il titolo se l'array è una proprietà di un oggetto) o [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/) (elabora l'array come una tabella). La classe [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) elabora il JSON utilizzando le opzioni di layout impostate con la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions).

Il seguente esempio di codice dimostra l'uso delle classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) e [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) per caricare il [file JSON di origine](104398869.json) e genera il [file CSV di output](104398870.csv).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
