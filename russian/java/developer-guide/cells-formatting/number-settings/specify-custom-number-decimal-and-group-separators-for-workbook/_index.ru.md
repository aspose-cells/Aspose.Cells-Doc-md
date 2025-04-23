---
title: Укажите пользовательский разделитель десятичной и разрядной группы для книги
type: docs
weight: 100
url: /ru/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Эта статья показывает, как изменить разделитель десятичной точки и группы в MS Excel и с помощью кода на Java, используя API Aspose.Cells for Java.
keywords: указать пользовательский десятичный разделитель excel, указать пользовательский десятичный разделитель excel java, указать пользовательский разделитель группы excel, указать пользовательский разделитель группы excel java, указать пользовательский десятичный и разделитель группы excel, указать пользовательский десятичный и разделитель группы excel java, изменить десятичный и разделитель группы excel java, изменить десятичный и разделитель группы excel, изменить десятичный разделитель excel, изменить десятичный разделитель excel java, изменить разделитель группы excel, изменить разделитель группы excel java
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете указать пользовательские разделители десятичной точки и тысячи вместо использования системных разделителей из **Расширенных опций Excel**, как показано на скриншоте ниже.

Aspose.Cells предоставляет свойства [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) и [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) для установки пользовательских разделителей для форматирования/парсинга чисел.

{{% /alert %}}

## **Указание пользовательских разделителей, используя Microsoft Excel**

1. Откройте **Параметры** на вкладке **Файл**.
1. Откройте вкладку **Расширенные**.
1. Измените настройки в разделе **Настройки редактирования**.

На следующем скриншоте показаны **Расширенные параметры Excel** и выделена секция для указания **Пользовательских разделителей**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Указание пользовательских разделителей с использованием Aspose.Cells**

Приведенный ниже образец кода иллюстрирует, как указать пользовательские разделители с использованием API Aspose.Cells. Он указывает пользовательские десятичный и групповой разделители как точку и пробел соответственно. Таким образом, число **123,456.789** будет отображаться как **123 456.789**, как показано на скриншоте, который показывает созданный кодом PDF.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
{{< app/cells/assistant language="java" >}}
