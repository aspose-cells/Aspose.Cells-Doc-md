---
title: Проверяйте, соответствует ли значение ячейки правилам проверки данных с помощью Golang через C++
linktitle: Проверка того, что значение ячейки удовлетворяет правилам валидации данных
type: docs
weight: 210
url: /ru/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Узнайте, как проверить, соответствует ли значение ячейки правилам проверки данных, с помощью API Aspose.Cells for C++.
keywords: Получить значение проверки ячейки, Получить значение проверки ячейки, Проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять правила проверки данных к ячейкам. Например, правило дескриминативной проверки определяет, что могут вводиться только числа между 10 и 20. Если пользователь вводит другое число, Excel показывает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы копируете и вставляете число, например 3, в ячейку, проверка не запускается и сообщение об ошибке не показывается.

Иногда необходимо программно проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке. В приведенном выше случае, например, ввод должен завершиться неудачей.

{{% /alert %}} 

## **Введение**
Aspose.Cells предоставляет метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/), который позволяет программно проверять значения ячеек. Если значение ячейки не соответствует правилу проверки данных, он возвращает **False**, иначе **True**.

Следующий пример кода показывает, как работает метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/). Сначала он вводит значение 3 в C1. Поскольку это не соответствует правилу проверки данных, метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) возвращает **False**. Затем он вводит значение 15 в C1. Поскольку это значение соответствует правилу проверки данных, метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) возвращает **True**. Аналогично для значения 30 он возвращает **False**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Вывод**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
