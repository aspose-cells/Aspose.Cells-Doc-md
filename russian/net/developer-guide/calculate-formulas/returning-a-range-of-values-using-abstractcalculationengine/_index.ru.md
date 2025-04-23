---
title: Возвращение Диапазона Значений с Использованием AbstractCalculationEngine
description: В данной статье представлен абстрактный расчетный движок, возвращающий диапазон значений в Microsoft Excel с использованием библиотеки Aspose.Cells. Путем загрузки существующего файла Excel или создания нового файла Excel мы можем использовать методы, предоставленные Aspose.Cells, для получения диапазона значений и возврата результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, абстрактный расчетный движок, возвращающий серию значений
type: docs
weight: 55
url: /ru/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine), который используется для реализации определяемых пользователем или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В данной статье будет объяснено, как вернуть диапазон значений из [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

Следующий код демонстрирует использование класса [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) и возвращает диапазон значений через его метод.

Создайте класс с функцией *CalculateCustomFunction*. Этот класс реализует [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Теперь используйте вышеуказанную функцию в своей программе

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
