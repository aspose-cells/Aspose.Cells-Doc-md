---
title: Убедитесь, что значение Cell удовлетворяет правилам проверки данных.
type: docs
weight: 210
url: /ru/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Узнайте, как проверить, что значение Cell соответствует правилам проверки данных, с помощью Aspose.Cells for .NET API..
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять в ячейки правила проверки данных. Например, десятичная проверка указывает, что можно вводить только числа от 10 до 20. Если пользователь вводит другой номер. Microsoft Excel отображает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы скопируете и вставите в ячейку число, например 3, Excel не выполнит проверку и не отобразит сообщение об ошибке.

Иногда необходимо проверить, удовлетворяет ли значение правилам проверки данных, применяемым к ячейке программным способом. Например, в приведенном выше случае запись должна завершиться неудачно.

{{% /alert %}} 
##  **Введение**
 Aspose.Cells обеспечивает[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)метод для программной проверки значений ячеек. Если значение в ячейке не удовлетворяет правилу проверки данных, примененному к этой ячейке, возвращается *False**, в противном случае — *True**.

 Следующий пример кода иллюстрирует, как[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) метод работает. Сначала он вводит значение 3 в C1. Поскольку это не удовлетворяет правилу проверки данных,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) метод возвращает**ЛОЖЬ**. Затем он вводит значение 15 в C1. Поскольку это значение удовлетворяет правилу проверки данных, метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) возвращает **True**. Аналогично, он возвращает **False** за стоимость 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **Выход**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
