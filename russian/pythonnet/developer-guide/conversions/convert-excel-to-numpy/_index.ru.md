---
title: Преобразование Excel в NumPy
type: docs
weight: 30
url: /ru/python-net/convert-excel-to-numpy/
description: Преобразование Excel в NumPy с использованием Aspose.Cells для Python via .NET API.
keywords: Преобразование Excel в массив NumPy на Python, Экспортирование книги в массив NumPy на Python via NET, Преобразование строки в массив NumPy на Python, Преобразование таблицы в массив NumPy на Python, Экспортирование ListObject в массив NumPy на Python via NET, Преобразование диапазона в массив NumPy на Python, Столбец в массив NumPy с использованием Python.
---

## **Введение в NumPy**
NumPy (Numerical Python) - это открытое расширение числовых вычислений Python. Этот инструмент может использоваться для хранения и обработки больших матриц, что намного эффективнее, чем вложенная структура списков Python (которая также может использоваться для представления матриц). Он поддерживает большое количество многомерных массивов и операций с матрицами, а также предоставляет большое количество библиотек математических функций для операций с массивами. 

Основные функции NumPy:
1. Ndarray - это многомерный массив, представляющий собой быструю, гибкую и экономящую место структуру данных.
1. Линейная алгебра, включая умножение матриц, транспонирование, обращение и т.д.
1. Преобразование Фурье, выполнение быстрого преобразования Фурье для массива.
1. Быстрые операции с массивами с плавающей запятой.
1. Интеграция кода на языке C в Python для увеличения скорости его выполнения.

С помощью Aspose.Cells для Python via .NET API вы можете конвертировать Excel, TSV, CSV, Json и множество других форматов в Numpy ndarray.

## **Как конвертировать книгу Excel в NumPy ndarray**
Вот пример кода, демонстрирующий, как экспортировать данные Excel в массив NumPy, используя Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Обработайте данные Excel и экспортируйте данные в массив NumPy, используя Aspose.Cells для Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

Результат вывода:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Как конвертировать рабочий лист в NumPy ndarray**
Вот пример кода, демонстрирующий, как экспортировать данные рабочего листа в Numpy ndarray, используя Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Конвертируйте данные рабочего листа в Numpy ndarray, используя Aspose.Cells для Python Excel библиотеки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

Результат вывода:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Как конвертировать диапазон Excel в NumPy ndarray**
Вот пример кода, демонстрирующий, как экспортировать данные диапазона в массив NumPy, используя Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Создайте диапазон.
1. Конвертируйте данные диапазона в Numpy ndarray, используя Aspose.Cells для Python Excel библиотеки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

Результат вывода:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Как конвертировать ListObject Excel в NumPy ndarray**
Вот пример фрагмента кода, демонстрирующий, как экспортировать данные ListObject в массив NumPy, используя Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Создайте объект ListObject.
1. Преобразуйте данные ListObject в массив NumPy с использованием библиотеки Excel для Python Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

Результат вывода:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Как преобразовать строку Excel в массив NumPy**
Вот пример фрагмента кода, демонстрирующий, как экспортировать данные строки в массив NumPy, используя Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Получите объект строки по индексу строки.
1. Преобразуйте данные строки в массив NumPy с использованием библиотеки Excel для Python Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

Результат вывода:
```
['Detroit' 'Central' '3074']
```

## **Как преобразовать столбец Excel в массив NumPy**
Вот пример фрагмента кода, демонстрирующий, как экспортировать данные столбца в массив NumPy, используя Aspose.Cells для Python via .NET:
1. Загрузите [образец файла](sample_data.xlsx).
1. Получите первый лист.
1. Получите объект столбца по индексу столбца.
1. Преобразуйте данные столбца в массив NumPy с использованием библиотеки Excel для Python Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

Результат вывода:
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
