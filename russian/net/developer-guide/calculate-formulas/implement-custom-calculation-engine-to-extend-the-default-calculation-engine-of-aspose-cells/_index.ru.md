---
title: Реализация собственного расчетного механизма для расширения стандартного расчетного механизма Aspose.Cells
description: Эта статья описывает, как расширить стандартный расчетный механизм, реализуя собственный расчетный механизм с использованием библиотеки Aspose.Cells. Загружая существующий файл Excel или создавая новый, мы можем использовать методы, предоставленные Aspose.Cells, для реализации собственного расчетного механизма и получения результатов. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, Собственный расчетный механизм, расширение стандартного расчетного механизма
type: docs
weight: 80
url: /ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells имеет мощный расчетный механизм, который может рассчитывать практически все формулы Microsoft Excel. Тем не менее, он также позволяет вам расширять стандартный расчетный механизм для обеспечения вам большей мощности и гибкости.

Следующие свойства и классы используются при реализации этой функции.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

Приведенный ниже код реализует пользовательский расчетный движок. Он реализует интерфейс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine), который имеет метод [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем функцию **TODAY** и добавляем один день к системной дате. Таким образом, если текущая дата - 27/07/2023, то пользовательский движок будет рассчитывать TODAY() как 28/07/2023.

### **Пример программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше образца кода, значение (дата/время) ячейки A1 с пользовательским движком должно быть на один день позже, чем результат без пользовательского движка.

### **Связанная статья**

{{% alert color="primary" %}}

[Прямой расчет пользовательской функции без записи ее в рабочий лист](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
