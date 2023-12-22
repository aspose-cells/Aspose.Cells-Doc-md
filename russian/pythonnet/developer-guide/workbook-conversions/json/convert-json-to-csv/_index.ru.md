---
title: Преобразовать JSON в CSV
type: docs
weight: 210
url: /ru/python-net/convert-json-to-csv/
description: Узнайте, как преобразовать файл JSON в CSV с помощью Aspose.Cells for Python via .NET API.
keywords: Python Convert json to csv, Convert json to csv Pyton via NET, Export json to csv, Convert json to csv
---
##  **Преобразовать JSON в CSV**

Aspose.Cells for Python via .NET поддерживает преобразование как простых, так и вложенных чисел JSON в CSV. Для этого API предоставляет**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)** и**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** занятия.**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**класс предоставляет параметры для макета JSON, например**[ignore_array_title](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)** (игнорирует заголовок, если массив является свойством объекта) или ** [array_as_table](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)**(обрабатывает массив как таблицу). **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**класс обрабатывает JSON, используя параметры макета, установленные с помощью**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**сорт.

В следующем примере кода показано использование**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**и**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** классы для загрузки[исходный файл JSON](104398869.json) и генерирует[выходной файл CSV](104398870.csv).

###  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
