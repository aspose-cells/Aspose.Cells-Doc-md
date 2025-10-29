---
title: Конвертировать Excel в данные Python
type: docs
weight: 30
url: /ru/python-net/convert-excel-to-list/
description: Преобразовать Excel в список с использованием Aspose.Cells для Python via .NET API.
keywords: Преобразовать Excel в словарь с использованием библиотеки Python Excel, преобразовать книгу в словарь с использованием библиотеки Python Excel, преобразовать объект строки в список с использованием библиотеки Python Excel, как преобразовать объект ListObject в список, преобразовать объект столбца в список с использованием библиотеки Python Excel, преобразовать диапазон в список с использованием библиотеки Python Excel, преобразовать лист в список с использованием библиотеки Python Excel.
---

{{% alert color="primary" %}}

С помощью Aspose.Cells для Python via .NET API можно преобразовать данные Excel, такие как книги, листы, диапазоны, строки, столбцы и другие, в список Python.

{{% /alert %}}

## **Как преобразовать книгу Excel в словарь**
Вот пример кодового отрывка, демонстрирующего, как экспортировать данные Excel в словарь с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Обойти все листы и преобразовать книгу в словарь с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

Результат вывода:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Как преобразовать книгу Excel в список**
Вот пример кодового отрывка, демонстрирующего, как экспортировать данные Excel в список с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Обойти все листы и преобразовать книгу в список с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

Результат вывода:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Как преобразовать лист в список**
Вот пример кодового отрывка, демонстрирующего, как экспортировать данные листа в список с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Преобразовать данные листа в список с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

Результат вывода:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Как преобразовать ListObject Excel в список**
Вот пример фрагмента кода, демонстрирующий способ экспорта данных ListObject в список с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Создайте объект ListObject.
1. Преобразуйте данные ListObject в список с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

Результат вывода:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Как преобразовать строку Excel в список**
Вот пример фрагмента кода, демонстрирующий способ экспорта данных строки в список с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Получите объект строки по индексу строки.
1. Преобразуйте данные строки в список с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

Результат вывода:
```
['Detroit', 'Central', 3074]
```

## **Как преобразовать столбец Excel в список**
Вот пример фрагмента кода, демонстрирующий способ экспорта данных столбца в список с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Получите объект столбца по индексу столбца.
1. Преобразуйте данные столбца в список с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

Результат вывода:
```
['Store', 3055, 3036, 3074]
```

## **Как преобразовать диапазон Excel в список**
Вот пример кода для демонстрации того, как экспортировать данные диапазона в список с использованием Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Создайте диапазон.
1. Преобразуйте данные диапазона в список с использованием библиотеки Aspose.Cells для Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

Результат вывода:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
