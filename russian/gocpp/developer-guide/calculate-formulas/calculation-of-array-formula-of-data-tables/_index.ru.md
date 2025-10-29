---
title: Вычисление массивных формул таблиц данных с помощью Golang через C++
linktitle: Вычисление массивной формулы таблиц данных
description: Как использовать библиотеку Aspose.Cells для вычисления массивных формул таблицы данных в Microsoft Excel с помощью Golang через C++. Загружая существующий файл Excel или создавая новый, мы можем использовать предоставляемый Aspose.Cells метод для вычисления массивной формулы таблицы данных и получения результата. В конце сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, таблицы данных, массивные формулы, вычисления, C++
type: docs
weight: 70
url: /ru/go-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Вы можете создать таблицу данных в Microsoft Excel, используя Данные > Анализ по сценариям > Таблица данных.... Теперь Aspose.Cells позволяет вычислять массивные формулы таблицы данных. Пожалуйста, используйте [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) так, как обычно, чтобы вычислить любой тип формул.

{{% /alert %}}

В следующем образце кода мы использовали [исходный файл Excel](5115535.xlsx). Если вы измените значение ячейки B1 на 100, значения Таблицы данных, заполненные желтым цветом, станут равными 120, как показано на следующих изображениях. Образец кода генерирует [выходной PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Вот образец кода, используемый для генерации [выходного PDF](5115538.pdf) из [исходного файла Excel](5115535.xlsx). Пожалуйста, прочитайте комментарии для получения дополнительной информации.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfArrayFormulaOfDataTables.go" >}}
