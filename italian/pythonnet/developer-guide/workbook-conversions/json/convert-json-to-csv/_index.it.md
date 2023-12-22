---
title: Convertire JSON in CSV
type: docs
weight: 210
url: /it/python-net/convert-json-to-csv/
description: Scopri come convertire json in file CSV con Aspose.Cells for Python via .NET API.
keywords: Python Convert json to csv, Convert json to csv Pyton via NET, Export json to csv, Convert json to csv
---
##  **Convertire JSON in CSV**

Aspose.Cells for Python via .NET supporta la conversione di JSON semplice e nidificato in CSV. Per questo, API fornisce**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)** E**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classi. IL**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**La classe fornisce le opzioni per il layout JSON come**[ignore_array_title](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)**(ignora il titolo se l'array è una proprietà di un oggetto) o ** [array_as_table](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)**(elabora l'array come una tabella). Il **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**elabora JSON utilizzando le opzioni di layout impostate con**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**classe.

Nell'esempio di codice seguente viene illustrato l'utilizzo di**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**E**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classi per caricare il file[file sorgente JSON](104398869.json) e genera il[file di output CSV](104398870.csv).

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
