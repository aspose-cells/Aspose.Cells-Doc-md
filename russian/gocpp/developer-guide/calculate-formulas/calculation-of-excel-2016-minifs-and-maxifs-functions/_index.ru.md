---
title: Вычисление функций MINIFS и MAXIFS Excel 2016 с Golang через C++
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для вычисления функций MINIFS и MAXIFS в Microsoft Excel 2016 с помощью C++.
keywords: Aspose.Cells, Excel, 2016, функция MINIFS, функция MAXIFS, вычисление
type: docs
weight: 300
url: /ru/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Возможные сценарии использования**
Microsoft Excel 2016 поддерживает функции MINIFS и MAXIFS. Эти функции не поддерживаются в Excel 2013 или более ранних версиях. Aspose.Cells также поддерживает вычисление этих функций. Следующий скриншот иллюстрирует использование этих функций. Пожалуйста, прочитайте комментарии внутри скриншота, чтобы понять, как работают эти функции.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Расчет функций MINIFS и MAXIFS Excel 2016**
Следующий пример загружает [образец файла Excel](5115149.xlsx) и вызывает метод [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/), чтобы выполнить вычисление формул через Aspose.Cells, а затем сохраняет результаты в [выводной PDF](5115154.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}
