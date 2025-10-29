---
title: Реализовать собственный движок вычислений для расширения стандартного движка Aspose.Cells с Golang через C++
linktitle: Реализуйте пользовательский движок расчетов
description: В этой статье рассказывается, как расширить стандартный движок вычислений, реализовав собственный движок с помощью Aspose.Cells и Golang через C++. Загружая существующий файл Excel или создавая новый, можно использовать предоставляемые Aspose.Cells методы для реализации собственного движка и получения результатов. В конце сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, пользовательский движок расчетов, расширяет стандартный движок, C++
type: docs
weight: 80
url: /ru/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells имеет мощный расчетный механизм, который может рассчитывать практически все формулы Microsoft Excel. Тем не менее, он также позволяет вам расширять стандартный расчетный механизм для обеспечения вам большей мощности и гибкости.

Следующие свойства и классы используются при реализации этой функции.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

Приведенный ниже код реализует пользовательский расчетный движок. Он реализует интерфейс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/), который имеет метод [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем функцию **TODAY** и добавляем один день к системной дате. Таким образом, если текущая дата - 27/07/2023, то пользовательский движок будет рассчитывать TODAY() как 28/07/2023.

### **Пример программирования**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше образца кода, значение (дата/время) ячейки A1 с пользовательским движком должно быть на один день позже, чем результат без пользовательского движка.

### **Связанная статья**

{{% alert color="primary" %}}

[Прямое вычисление пользовательской функции без её записи в лист](/cells/ru/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
