---
title: Внедрите пользовательский механизм вычислений, чтобы расширить механизм вычислений по умолчанию Aspose.Cells.
description: В этой статье описывается, как расширить механизм вычислений по умолчанию, реализовав собственный механизм вычислений с помощью библиотеки Aspose.Cells. Загрузив существующий файл Excel или создав новый, мы можем использовать методы, предоставленные Aspose.Cells, для реализации пользовательского механизма вычислений и получения результатов. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Внедрение пользовательского механизма вычислений**

Aspose.Cells имеет мощный вычислительный механизм, позволяющий рассчитывать почти все формулы Microsoft Excel. Несмотря на это, он также позволяет вам расширить механизм вычислений по умолчанию, что обеспечивает большую мощность и гибкость.

При реализации этой функции используются следующие свойства и классы.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Следующий код реализует пользовательский механизм вычислений. Он реализует интерфейс**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** который имеет**[Рассчитать (данные CalculationData)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** метод. Этот метод вызывается для всех ваших формул. Внутри этого метода мы фиксируем**TODAY** функцию и добавьте один день к системной дате. Таким образом, если текущая дата — 27.07.2023, то пользовательский механизм рассчитает TODAY() как 28.07.2023.

###  **Пример программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше примера кода: значение (дата и время) A1 с пользовательским механизмом должно быть на один день позже, чем результат без специального механизма.

###  **Связанная статья**

{{% alert color="primary" %}}

[Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
