---
title: Проверка того, что значение ячейки удовлетворяет правилам валидации данных
type: docs
weight: 210
url: /ru/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Узнайте, как проверить, удовлетворяет ли значение ячейки правилам валидации данных через API Aspose.Cells for .NET.
keywords: Получить значение проверки ячейки, Получить значение проверки ячейки, Проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять правила валидации данных для ячеек. Например, валидация десятичных чисел указывает, что можно вводить только числа в диапазоне от 10 до 20. Если пользователь вводит другое число, Microsoft Excel показывает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы копируете и вставляете число, скажем, 3, в ячейку, Excel не выполняет проверку валидации и не показывает сообщение об ошибке.

Иногда необходимо программно проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке. В приведенном выше случае, например, ввод должен завершиться неудачей.

{{% /alert %}} 
## **Введение**
Aspose.Cells предоставляет метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) для программной проверки значений ячеек. Если значение в ячейке не удовлетворяет правилу валидации данных, примененному к этой ячейке, он возвращает **False**, в противном случае **True**.

Следующий образец кода иллюстрирует работу метода [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue). Сначала он вводит значение 3 в C1. Поскольку это не удовлетворяет правилу валидации данных, метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) возвращает **False**. Затем он вводит значение 15 в C1. Поскольку это значение удовлетворяет правилу валидации данных, метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) возвращает **True**. Точно так же для значения 30 он возвращает **False**.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Вывод**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
