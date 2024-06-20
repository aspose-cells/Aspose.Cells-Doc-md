---
title: Возврат диапазона значений с помощью ICustomFunction
description: В этой статье описывается, как использовать библиотеку Aspose.Cells для возврата диапазона значений с помощью ICustomFunction в Microsoft Excel. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, чтобы получить диапазон значений и вернуть результат. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, ICustomFunction, возвращает серию значений
type: docs
weight: 50
url: /ru/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) устарел с выходом Aspose.Cells for Java 20.8. Используйте класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine). Использование класса [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) описано в следующей статье.

[Возврат диапазона значений с помощью AbstractCalculationEngine](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells предоставляет интерфейс [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В основном, когда вы реализуете метод интерфейса [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), вам необходимо возвращать значение одной ячейки. Но иногда вам нужно вернуть диапазон значений. В этой статье будет объяснено, как вернуть диапазон значений из [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

Следующий код реализует [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) и возвращает диапазон значений через его метод.

Создайте класс с функцией *CalculateCustomFunction*. Этот класс реализует [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Теперь используйте вышеуказанную функцию в своей программе

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
