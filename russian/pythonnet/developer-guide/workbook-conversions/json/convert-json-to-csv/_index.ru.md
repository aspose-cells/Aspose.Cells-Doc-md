---
title: Конвертировать JSON в CSV
type: docs
weight: 210
url: /ru/python-net/convert-json-to-csv/
description: Узнайте, как преобразовать json в файл csv с помощью Aspose.Cells for Python via .NET API.
keywords: Python Преобразование json в файл csv, Преобразование json в файл csv Pyton via NET, Экспорт json в csv, Преобразование json в файл csv
---

## **Преобразовать JSON в CSV**

Aspose.Cells для Python via .NET поддерживает преобразование как простого, так и вложенного JSON в CSV. Для этого API предоставляет классы [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) и [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) предоставляет параметры для макета JSON, такие как [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/) (игнорирует заголовок, если массив является свойством объекта) или [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/) (обрабатывает массив как таблицу). Класс [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) обрабатывает JSON с параметрами макета, установленными с использованием класса [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions).

Приведенный ниже образец кода демонстрирует использование классов [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) и [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) для загрузки [исходного файла JSON](104398869.json) и генерации [выходного файла CSV](104398870.csv).

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
