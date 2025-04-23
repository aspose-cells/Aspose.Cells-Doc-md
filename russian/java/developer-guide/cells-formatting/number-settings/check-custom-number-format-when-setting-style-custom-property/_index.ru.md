---
title: Проверьте пользовательский формат чисел при установке Style.Custom свойства
type: docs
weight: 160
url: /ru/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если вы назначите недопустимый пользовательский формат числа для свойства [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom), то Aspose.Cells не выдаст никакого исключения. Но если вы хотите, чтобы Aspose.Cells проверил, допустим ли назначенный пользовательский формат числа или нет, то установите свойство [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) на **true**.

## **Проверьте пользовательский формат числа при установке Style.Custom свойства**

Приведенный ниже образец кода назначает недопустимый пользовательский формат числа для свойства [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Поскольку мы уже установили свойство [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) на **true**, API выдаст исключение CellsException, например, *Invalid number format*.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
{{< app/cells/assistant language="java" >}}
