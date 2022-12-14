---
title: Убедитесь, что значение Cell удовлетворяет правилам проверки данных.
type: docs
weight: 210
url: /ru/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять в ячейки правила проверки данных. Например, десятичная проверка указывает, что можно вводить только числа от 10 до 20. Если пользователь вводит другой номер. Microsoft Excel показывает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы скопируете и вставите число, например 3, в ячейку, Excel не запустит проверку и не покажет сообщение об ошибке.

Иногда необходимо проверить, удовлетворяет ли значение правилам проверки данных, применяемым к ячейке программно. Например, в приведенном выше случае запись должна завершиться ошибкой.

{{% /alert %}} 
## **Введение**
 Aspose.Cells обеспечивает[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) метод для проверки значений ячеек программно. Если значение в ячейке не удовлетворяет правилу проверки данных, примененному к этой ячейке, возвращается**ЛОЖЬ** , еще**Истинный**.

 В следующем примере кода показано, как[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) метод работает. Сначала он вводит значение 3 в C1. Поскольку это не удовлетворяет правилу проверки данных,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) метод возвращает**ЛОЖЬ** . Затем он вводит значение 15 в C1. Поскольку это значение удовлетворяет правилу проверки данных,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) метод возвращает**Истинный** . Точно так же возвращается**ЛОЖЬ** на значение 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Выход**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
