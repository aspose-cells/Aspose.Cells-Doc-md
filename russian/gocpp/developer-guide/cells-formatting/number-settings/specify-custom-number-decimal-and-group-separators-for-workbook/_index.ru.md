---
title: Задать пользовательские разделители десятичной части и группировки чисел для рабочей книги с помощью Golang через C++
linktitle: Задание пользовательских разделителей десятичных и групповых чисел
type: docs
weight: 110
url: /ru/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Изменить разделители десятичной части и группировки чисел в MS Excel и с помощью Golang через C++ с использованием API Aspose.Cells for C++.
keywords: указать пользовательский разделитель десятичной части для excel, указать пользовательский разделитель десятичной части для excel c++, указать пользовательский групповой разделитель excel, указать пользовательский групповой разделитель excel c++, указать пользовательский разделитель decimal и group для excel, указать пользовательский разделитель decimal и group для excel c++, изменить разделитель decimal и group в excel, изменить разделитель decimal в excel, изменить разделитель group в excel, изменить разделитель decimal в excel c++, изменить разделитель group в excel c++
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете указать пользовательские разделители десятичной точки и тысячи вместо использования системных разделителей из **Расширенных опций Excel**, как показано на скриншоте ниже.

Aspose.Cells предоставляет свойства [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) и [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) для установки пользовательских разделителей для форматирования/разбора чисел.

{{% /alert %}}

## **Указание пользовательских разделителей, используя Microsoft Excel**

На следующем скриншоте показаны **Расширенные параметры Excel** и выделена секция для указания **Пользовательских разделителей**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Указание пользовательских разделителей с использованием Aspose.Cells**

Приведенный ниже образец кода иллюстрирует, как указать пользовательские разделители с помощью API Aspose.Cells. Он указывает пользовательские разделители для десятичных и групповых чисел как точку и пробел соответственно.

### Код C++ для задания пользовательских разделителей чисел с десятичной точкой и группировкой

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
