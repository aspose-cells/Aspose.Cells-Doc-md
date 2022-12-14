---
title: Укажите пользовательские десятичные числа и разделители групп для книги
type: docs
weight: 100
url: /ru/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: В этой статье показано, как изменить десятичное число и разделитель групп в MS Excel и с помощью кода Java с помощью файла Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 В Microsoft Excel вы можете указать пользовательские десятичные разделители и разделители тысяч вместо использования системных разделителей из**Расширенные параметры Excel** как показано на скриншоте ниже.

 Aspose.Cells обеспечивает[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) а также[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) свойства, чтобы установить пользовательские разделители для форматирования/анализа чисел.

{{% /alert %}}

## **Указание пользовательских разделителей с помощью Microsoft Excel**

1.  Открытым**Опции** в**Файл** вкладка
1. Открой**Передовой** вкладка
1.  Измените настройки в**Параметры редактирования** раздел.

 На следующем снимке экрана показано**Расширенные параметры Excel** и выделяет раздел для указания**Пользовательские разделители**.

![дело:изображение_альтернативный_текст](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Указание пользовательских разделителей с помощью Aspose.Cells**

 В следующем примере кода показано, как указать настраиваемые разделители с помощью Aspose.Cells API. Он указывает настраиваемые десятичные числа и разделители групп в виде точки и пробела соответственно. Итак, число**123,456.789** будет отображаться как**123 456.789** как показано на снимке экрана, на котором показан выходной PDF-файл, сгенерированный кодом.

![дело:изображение_альтернативный_текст](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
