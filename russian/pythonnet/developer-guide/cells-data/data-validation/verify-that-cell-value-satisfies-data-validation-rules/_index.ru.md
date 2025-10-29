---
title: Проверка того, что значение ячейки удовлетворяет правилам валидации данных
type: docs
weight: 210
url: /ru/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Узнайте, как проверить, что значение ячейки удовлетворяет правилам валидации данных с помощью API Aspose.Cells для Python via .NET.
keywords: Библиотека Excel для Python, Получение значения валидации ячейки с помощью Python, Получение значений валидации ячейки с помощью Python, Проверка удовлетворения значения правилам проверки данных, примененных к ячейке.
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять правила валидации данных для ячеек. Например, валидация десятичных чисел указывает, что можно вводить только числа в диапазоне от 10 до 20. Если пользователь вводит другое число, Microsoft Excel показывает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы копируете и вставляете число, скажем, 3, в ячейку, Excel не выполняет проверку валидации и не показывает сообщение об ошибке.

Иногда необходимо программно проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке. В приведенном выше случае, например, ввод должен завершиться неудачей.

{{% /alert %}} 
## **Введение**
Aspose.Cells для Python via .NET предоставляет метод [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) для программной проверки значений ячеек. Если значение в ячейке не соответствует правилу валидации данных, он возвращает **False**, в противном случае **True**.

В следующем образце кода иллюстрируется работа метода [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#). Сначала он вводит значение 3 в C1. Поскольку это значение не удовлетворяет правилу валидации данных, метод [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) возвращает **False**. Затем вводится значение 15 в C1. Поскольку это значение удовлетворяет правилу валидации данных, метод [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) возвращает **True**. Аналогично для значения 30 он возвращает **False**.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Вывод**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
