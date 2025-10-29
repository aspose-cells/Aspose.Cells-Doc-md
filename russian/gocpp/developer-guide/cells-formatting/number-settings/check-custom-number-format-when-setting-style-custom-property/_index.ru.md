---
title: Проверить пользовательский числовой формат при установке свойства Style.Custom с помощью Golang через C++
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц, которая поддерживает проверку пользовательских числовых форматов при стилизации. В этой статье будет показано, как использовать библиотеку Aspose.Cells для проверки пользовательских числовых форматов, чтобы обеспечить правильность стиля.
keywords: Aspose.Cells, библиотеки C++, таблицы, стилизация, пользовательский числовой формат, проверка, валидация
type: docs
weight: 170
url: /ru/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если присвоить недопустимый пользовательский числовой формат свойству [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/), то Aspose.Cells не выбросит исключение. Но если вы хотите, чтобы Aspose.Cells проверял правильность присвоенного пользовательского числового формата, установите свойство [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) в значение **true**.

## **Проверить настраиваемый формат чисел при установке свойства Style.Custom**

Следующий пример кода присваивает недопустимый пользовательский числовой формат свойству [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/). Так как мы уже установили свойство [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) в **true**, происходит выброс исключения, например, неверный числовой формат. Ознакомьтесь с комментариями внутри кода для получения дополнительной информации.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
