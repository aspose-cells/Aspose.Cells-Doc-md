---
title: Проверьте пользовательский числовой формат при настройке свойства Style.Custom
type: docs
weight: 160
url: /ru/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Возможные сценарии использования**

 Если вы назначите недопустимый пользовательский формат номера для[**Стиль.Пользовательский**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)свойство, то Aspose.Cells не будет вызывать никаких исключений. Но если вы хотите, чтобы Aspose.Cells проверял, действителен ли назначенный формат пользовательского номера, установите[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) собственность на**истинный**.

## **Проверьте пользовательский числовой формат при настройке свойства Style.Custom.**

 Следующий пример кода назначает недопустимый формат пользовательского номера для[**Стиль.Пользовательский**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) имущество. Поскольку мы уже установили[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) собственность на**истинный** , поэтому API вызовет исключение CellsException, например*Неверный числовой формат*.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
