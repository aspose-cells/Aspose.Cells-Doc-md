---
title: Проверьте пользовательский формат чисел при установке Style.Custom свойства
description: Aspose.Cells — это библиотека на Python для работы с файлами таблиц, которая поддерживает проверку пользовательских форматов чисел при стилизации. В этой статье показано, как использовать библиотеку Aspose.Cells для проверки пользовательских форматов чисел, чтобы убедиться в правильности стилизации.
keywords: Aspose.Cells, библиотеки Python, таблицы, стилизация, пользовательские форматы чисел, проверка, валидация
type: docs
weight: 170
url: /ru/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если вы назначаете недопустимый настраиваемый формат чисел для свойства [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom), то Aspose.Cells не будет генерировать исключение. Но если вы хотите, чтобы Aspose.Cells проверял, является ли назначенный настраиваемый формат чисел допустимым или нет, то установите свойство [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) в **true**.

## **Проверить настраиваемый формат чисел при установке свойства Style.Custom**

В следующем образце кода назначается недопустимый настраиваемый формат чисел для свойства [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Поскольку мы уже установили свойство [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) в **true**, поэтому возникает исключение, например, Недопустимый формат числа. Пожалуйста, прочтите комментарии внутри кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

