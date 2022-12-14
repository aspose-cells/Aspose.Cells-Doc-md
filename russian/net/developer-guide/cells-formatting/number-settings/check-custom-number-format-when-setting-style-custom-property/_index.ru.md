---
title: Проверьте пользовательский числовой формат при настройке свойства Style.Custom
type: docs
weight: 170
url: /ru/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Возможные сценарии использования**

 Если вы назначите недопустимый пользовательский формат номера для[**Стиль.Пользовательский**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)свойство, то Aspose.Cells не вызовет никаких исключений. Но если вы хотите, чтобы Aspose.Cells проверял, является ли назначенный пользовательский формат номера действительным или нет, установите[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) собственность на**истинный**.

## **Проверьте пользовательский числовой формат при настройке свойства Style.Custom.**

 Следующий пример кода назначает недопустимый формат пользовательского номера для[**Стиль.Пользовательский**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) имущество. Так как мы уже установили[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) собственность на**истинный**, поэтому выдает исключение, например, неверный числовой формат. Пожалуйста, прочитайте комментарии внутри кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
