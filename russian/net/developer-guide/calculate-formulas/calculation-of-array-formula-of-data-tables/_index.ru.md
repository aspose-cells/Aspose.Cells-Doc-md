---
title: Вычисление массивной формулы таблиц данных
description: Как использовать библиотеку Aspose.Cells для вычисления массивных формул для таблицы данных в Microsoft Excel. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать метод, предоставленный Aspose.Cells, для вычисления массивной формулы в таблице данных и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, таблицы данных, массивные формулы, вычисления
type: docs
weight: 70
url: /ru/net/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Вы можете создать таблицу данных в Microsoft Excel, используя Данные > Анализ по сценариям > Таблица данных.... Теперь Aspose.Cells позволяет вычислять массивные формулы таблицы данных. Пожалуйста, используйте [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) так, как обычно, чтобы вычислить любой тип формул.

{{% /alert %}}

В следующем образце кода мы использовали [исходный файл Excel](5115535.xlsx). Если вы измените значение ячейки B1 на 100, значения Таблицы данных, заполненные желтым цветом, станут равными 120, как показано на следующих изображениях. Образец кода генерирует [выходной PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Вот образец кода, используемый для генерации [выходного PDF](5115538.pdf) из [исходного файла Excel](5115535.xlsx). Пожалуйста, прочитайте комментарии для получения дополнительной информации.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
