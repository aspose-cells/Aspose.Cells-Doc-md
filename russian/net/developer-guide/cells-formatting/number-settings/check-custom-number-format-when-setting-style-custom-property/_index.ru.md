---
title: Проверьте формат произвольного номера при настройке свойства Style.Custom
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает проверку пользовательских числовых форматов при стилизации. В этой статье показано, как использовать библиотеку Aspose.Cells для проверки пользовательских числовых форматов и правильности стиля.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /ru/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Возможные сценарии использования**

 Если вы присвоите неверный пользовательский формат номера[**Стиль.Пользовательский**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) свойство, то Aspose.Cells не выдаст никаких исключений. Но если вы хотите, чтобы Aspose.Cells проверял, действителен ли назначенный пользовательский формат номера, установите[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) свойство в *true**.

##  **Проверьте формат произвольного номера при настройке свойства Style.Custom.**

 В следующем примере кода присваивается недопустимый пользовательский формат номера.[**Стиль.Пользовательский**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) свойство. Поскольку мы уже установили[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) для свойства установлено значение *true**, поэтому выдается исключение, например, «Неверный формат числа». Пожалуйста, прочитайте комментарии внутри кода для получения дополнительной помощи.

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
