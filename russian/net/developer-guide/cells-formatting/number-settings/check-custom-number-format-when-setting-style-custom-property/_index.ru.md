---
title: Проверьте пользовательский формат чисел при установке Style.Custom свойства
description: Aspose.Cells  это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает проверку пользоватских форматов чисел при стилизации. В этой статье будет показано, как использовать библиотеку Aspose.Cells для проверки пользоватских форматов чисел, чтобы убедиться, что стилизация правильна.
keywords: Aspose.Cells, .NET библиотеки, электронные таблицы, стилизация, настраиваемое форматирование чисел, проверка, валидация
type: docs
weight: 170
url: /ru/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если вы назначаете недопустимый настраиваемый формат чисел для свойства [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom), то Aspose.Cells не будет генерировать исключение. Но если вы хотите, чтобы Aspose.Cells проверял, является ли назначенный настраиваемый формат чисел допустимым или нет, то установите свойство [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) в **true**.

## **Проверить настраиваемый формат чисел при установке свойства Style.Custom**

В следующем образце кода назначается недопустимый настраиваемый формат чисел для свойства [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). Поскольку мы уже установили свойство [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) в **true**, поэтому возникает исключение, например, Недопустимый формат числа. Пожалуйста, прочтите комментарии внутри кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
{{< app/cells/assistant language="csharp" >}}
