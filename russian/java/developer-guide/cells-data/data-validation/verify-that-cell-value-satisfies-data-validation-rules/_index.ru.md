---
title: Проверка того, что значение ячейки удовлетворяет правилам валидации данных
type: docs
weight: 90
url: /ru/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям добавлять правила проверки данных в ячейки листа. Например, десятичная проверка может быть применена для ограничения чисел между 10 и 20. Если вводится какое-либо другое число за этот указанный диапазон, Microsoft Excel показывает сообщение об ошибке и просит пользователя ввести число из правильного диапазона. Если пользователь копирует и вставляет число, скажем 3, в ячейку, Excel не запускает проверку или показывает сообщение об ошибке.

{{% /alert %}}

## Проверьте, что значение ячейки удовлетворяет правилам проверки данных

Иногда необходимо динамически проверить, удовлетворяет ли заданное значение правилам проверки данных, примененным к ячейке. Для этой цели API Aspose.Cells предоставляет метод [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Если значение в ячейке не удовлетворяет правилу проверки данных, примененному к этой ячейке, он возвращает **False**, иначе **True**.

В следующем образце кода используется существующий в Excel файл, показанный на снимке экрана, метод [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Как видно на снимке экрана, ячейка **C1** имеет примененную **десятичную проверку** и примет только значения **от 10 до 20**. Когда значение ячейки находится между 10 и 20, метод [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) вернет **True**, в противном случае он вернет **False**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

Ниже показан образец кода, иллюстрирующий работу метода [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Сначала он вводит значение 3 в C1. Поскольку это не удовлетворяет правилам проверки данных, метод [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) возвращает **False**. Затем он вводит значение 15 в C1. Поскольку это значение удовлетворяет правилам проверки данных, метод [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) возвращает **True**. Точно так же он возвращает **False** для значения 30.

## Java-код для проверки, удовлетворяет ли значение ячейки правилам проверки данных

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Консольный вывод, сгенерированный образцовым кодом

Здесь показан вывод консоли, созданный при выполнении примерного кода с примерным файлом Excel, показанным выше.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
