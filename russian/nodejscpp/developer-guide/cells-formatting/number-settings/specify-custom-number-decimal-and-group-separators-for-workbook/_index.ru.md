---
title: Укажите пользовательский разделитель десятичной и разрядной группы для книги
linktitle: Укажите пользовательский разделитель десятичной и разрядной группы для книги
type: docs
weight: 110
url: /ru/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Измените десятичные и групповые разделители чисел в Excel с помощью Aspose.Cells for Node.js via C++. 
keywords: укажите пользовательский десятичный разделитель в Excel node.js через C++, укажите пользовательский групповой разделитель в Excel node.js через C++, измените десятичный и групповой разделители в Excel через C++
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете указать пользовательские разделители десятичной точки и тысячи вместо использования системных разделителей из **Расширенных опций Excel**, как показано на скриншоте ниже.

Aspose.Cells предоставляет методы [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) и [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) для установки пользовательских разделителей для форматирования/парсинга чисел.

{{% /alert %}}

## **Указание пользовательских разделителей, используя Microsoft Excel**

На следующем скриншоте показаны **Расширенные параметры Excel** и выделена секция для указания **Пользовательских разделителей**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Указание пользовательских разделителей с помощью Aspose.Cells for Node.js via C++**

Приведенный ниже образец кода иллюстрирует, как указать пользовательские разделители с помощью API Aspose.Cells. Он указывает пользовательские разделители для десятичных и групповых чисел как точку и пробел соответственно.

### код Node.js для указания пользовательских десятичных и групповых разделителей чисел

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


