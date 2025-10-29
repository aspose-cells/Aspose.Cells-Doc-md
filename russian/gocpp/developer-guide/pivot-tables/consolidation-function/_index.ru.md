---
title: Функция объединения с Golang через C++
linktitle: Функция консолидации
type: docs
weight: 20
url: /ru/go-cpp/consolidation-function/
description: Узнайте, как применить функцию объединения к полям данных сводной таблицы с использованием Aspose.Cells с Golang через C++.
---

## **Функция консолидации**

Aspose.Cells можно использовать для применения функции объединения к полям данных (или значениям) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши на поле значения, затем выбрать опцию **Настройки поля значения...**, а затем выбрать вкладку **Сводные значения по**. Оттуда вы можете выбрать любую функцию объединения по своему выбору, такую как Сумма, Количество, Среднее, Максимум, Минимум, Произведение, Уникальное количество и т. д.

Aspose.Cells предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/) для поддержки следующих функций консолидации.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Применение функции консолидации к данным полей сводной таблицы**

Следующий код применяет функцию объединения **Среднее** к первому полю данных (или значению) и функцию объединения **Уникальное количество** ко второму полю данных (или значению).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

Функция консолидации Уникальное количество поддерживается только Microsoft Excel 2013.

{{% /alert %}}
