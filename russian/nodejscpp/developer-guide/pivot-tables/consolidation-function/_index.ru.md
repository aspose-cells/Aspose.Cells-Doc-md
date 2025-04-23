---
title: Функция консолидации
type: docs
weight: 20
url: /ru/nodejs-cpp/consolidation-function/
description: Как применить функцию объединения (ConsolidationFunction) к полям данных сводной таблицы с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, библиотека Excel Node.js, функция объединения (ConsolidationFunction) к полям данных сводной таблицы с помощью библиотеки Excel Aspose.Cells for Node.js via C++.
---

## **Функция консолидации**

Aspose.Cells for Node.js via C++ может использоваться для применения функции объединения (ConsolidationFunction) к полям данных (или полям значений) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши по полю значений, выбрать опцию **Настройка поля значений...** и затем перейти на вкладку **Итоги по значениям**. Там вы можете выбрать любую функцию объединения по своему усмотрению, например сумму, подсчет, среднее, максимум, минимум, произведение, уникальный подсчет и т.д.

Aspose.Cells for Node.js via C++ предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/), поддерживающее следующие функции объединения.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Как применить функцию объединения (ConsolidationFunction) к полям данных сводной таблицы с помощью Aspose.Cells for Node.js via C++**

Следующий код применяет функцию объединения **Среднее** к первому полю данных (или значению) и функцию объединения **Уникальное количество** ко второму полю данных (или значению).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

Функция консолидации УНИКАЛЬНОЕ_КОЛИЧЕСТВО поддерживается только в Microsoft Excel 2013.

{{% /alert %}}
