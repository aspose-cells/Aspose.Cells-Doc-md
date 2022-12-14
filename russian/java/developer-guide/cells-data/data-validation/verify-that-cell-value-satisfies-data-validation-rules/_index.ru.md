---
title: Убедитесь, что значение Cell удовлетворяет правилам проверки данных.
type: docs
weight: 90
url: /ru/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям добавлять правила проверки данных в ячейки рабочего листа. Например, десятичная проверка может применяться для ограничения чисел от 10 до 20. Если вводится любое другое число из указанного диапазона, Microsoft Excel показывает сообщение об ошибке и предлагает пользователю повторно ввести число из правильного диапазона. Если пользователь копирует число, например 3, в ячейку, Excel не запускает проверку и не отображает сообщение об ошибке.

{{% /alert %}}

## Убедитесь, что значение Cell удовлетворяет правилам проверки данных.

Иногда необходимо динамически проверять, удовлетворяет ли заданное значение правилам проверки данных, применяемым к ячейке. Для этой цели API Aspose.Cells предоставляют[**ячейка.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) метод. Если значение в ячейке не удовлетворяет правилу проверки данных, примененному к этой ячейке, возвращается**ЛОЖЬ** , еще**Истинный**.

Следующий пример файла Excel Microsoft используется с приведенным ниже образцом кода для проверки[**ячейка.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) метод. Как видно на снимке, клетки**С1** имеет**проверка десятичных данных** применяется и будет принимать только значения**между 10 и 20** . Всякий раз, когда значение ячейки находится между 10 и 20,[**ячейка.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) метод вернет**Истинный** , иначе вернется**ЛОЖЬ**.

![дело:изображение_альтернативный_текст](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 В следующем примере кода показано, как[**ячейка.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) метод работает. Сначала он вводит значение 3 в C1. Поскольку это не удовлетворяет правилу проверки данных,[**ячейка.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) метод возвращает**ЛОЖЬ** . Затем он вводит значение 15 в C1. Поскольку это значение удовлетворяет правилу проверки данных,[**ячейка.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) метод возвращает**Истинный** . Точно так же возвращается**ЛОЖЬ** на значение 30.

## Код Java для проверки соответствия значения Cell правилам проверки данных

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Консольный вывод, сгенерированный примером кода

Вот вывод консоли, сгенерированный при выполнении примера кода с примером файла Excel, показанным выше.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
