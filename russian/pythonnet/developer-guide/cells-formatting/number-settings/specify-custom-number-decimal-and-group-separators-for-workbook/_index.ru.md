---
title: Укажите пользовательский разделитель десятичной и разрядной группы для книги
type: docs
weight: 110
url: /ru/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Изменение разделителя десятичных и группового разделителя чисел в MS Excel и с помощью кода C# с помощью API Aspose.Cells для Python via .NET.
keywords: указать пользовательский десятичный разделитель excel, указать пользовательский десятичный разделитель excel c#, указать пользовательский групповой разделитель excel, указать пользовательский групповой разделитель excel c#, указать пользовательский десятичный и групповой разделитель excel, указать пользовательский десятичный и групповой разделитель excel c#, изменить десятичный и групповой разделитель excel c#, изменить десятичный и групповой разделитель excel, изменить десятичный разделитель excel, изменить десятичный разделитель excel c#, изменить групповой разделитель excel, изменить групповой разделитель excel c#
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете указать пользовательские разделители десятичной точки и тысячи вместо использования системных разделителей из **Расширенных опций Excel**, как показано на скриншоте ниже.

Aspose.Cells для Python via .NET предоставляет свойства [**WorkbookSettings.number_decimal_separator**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/number_decimal_separator/) и [**WorkbookSettings.number_group_separator**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/number_group_separator/) для установки пользовательских разделителей при форматировании/парсинге чисел.

{{% /alert %}}

## **Указание пользовательских разделителей, используя Microsoft Excel**

На следующем скриншоте показаны **Расширенные параметры Excel** и выделена секция для указания **Пользовательских разделителей**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Задание пользовательских разделителей с помощью Aspose.Cells для Python via .NET**

Следующий пример кода показывает, как указать пользовательские разделители с помощью API Aspose.Cells для Python via .NET. Он задает пользовательские разделители десятичных и групповых чисел как точку и пробел соответственно.

### Образец кода на C#, указывающий пользовательские разделители для десятичных и групповых чисел

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomDecimalAndGroupSeparator.py" >}}

