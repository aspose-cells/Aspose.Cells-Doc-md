---
title: Преобразование Excel в Pandas DataFrame
type: docs
weight: 30
url: /ru/python-net/convert-excel-to-pandas-dataframe/
description: Преобразовать Pandas в Excel с помощью Aspose.Cells для Python via .NET API.
keywords: Преобразование Excel в Pandas DataFrame в Python, Экспорт Excel в Pandas DataFrame в Python via NET, Преобразование xlsx в Pandas DataFrame в Python, Сохранение excel в Pandas DataFrame.
---

{{% alert color="primary" %}}

Используя Aspose.Cells для Python via .NET API, вы можете преобразовать Excel, TSV, CSV, Json и множество других форматов в pandas DataFrame.

{{% /alert %}}

## **Конвертация Excel в Pandas DataFrame с нуля**
Вот пример фрагмента кода, демонстрирующий, как экспортировать данные Excel в pandas DataFrame напрямую с использованием Aspose.Cells для Python via .NET:
1. Создать книгу и добавить некоторые значения.
1. Обойти данные в Excel и экспортировать данные в Pandas DataFrame с использованием Aspose.Cells для Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-directly.py" >}}

## **Преобразование существующего файла Excel в DataFrame pandas**
Вот пример кода, показывающий, как экспортировать данные из excel в DataFrame pandas, открыв существующий файл .xlsx с помощью Aspose.Cells для Python via .NET:
1. Откройте существующий [файл Excel](PandasTest.xlsx).
1. Преобразуйте данные каждой строки и столбца в DataFrame pandas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-by-openning-file.py" >}}

## **Преобразование Excel в Pandas DataFrame через данные json**
Вот пример фрагмента кода, демонстрирующий, как экспортировать данные Excel в pandas DataFrame через данные json с использованием Aspose.Cells для Python via .NET:
1. Создать книгу и добавить некоторые значения.
1. Экспортировать данные excel в JSON строку.
1. Использовать библиотеку pandas для чтения данных JSON.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-by-json.py" >}}

## **Преобразование Excel в DataFrame pandas через CSV файл**
Из-за особенностей формата файла CSV преобразование файла .xlsx в CSV и его последующая загрузка в DataFrame pandas — это естественный и простой процесс:
1. Преобразуйте существующий xlsx ([ProductDatatoCSV.xlsx](ProductDatatoCSV.xlsx)) в CSV файл.
1. Преобразуйте CSV файл в DataFrame pandas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-via-CSV.py" >}}
{{< app/cells/assistant language="python-net" >}}
