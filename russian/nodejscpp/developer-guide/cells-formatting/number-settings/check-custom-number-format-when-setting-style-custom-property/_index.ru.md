---
title: Проверьте пользовательский формат чисел при установке Style.Custom свойства
linktitle: Проверьте пользовательский формат чисел при установке Style.Custom свойства
description: Aspose.Cells — это библиотека для Node.js для работы с файлами таблиц, которая поддерживает проверку пользовательских форматов чисел при стилизации. В этой статье вы узнаете, как использовать библиотеку Aspose.Cells для проверки пользовательских форматов чисел и обеспечения правильности стилизации.
keywords: Aspose.Cells, библиотеки Node.js, таблицы, стилизация, проверка пользовательских форматов чисел, валидация
type: docs
weight: 170
url: /ru/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если вы назначите недопустимый пользовательский формат числа методу [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-), то Aspose.Cells for Node.js via C++ не выбросит исключение. Но если вы хотите, чтобы Aspose.Cells проверил правильность назначенного пользовательского формата числа, установите метод [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) в значение **true**.

## **Проверка пользовательского формата числа при установке метода Style.setCustom(string)**

Следующий пример кода назначает недопустимый пользовательский формат числа методу [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-). Так как мы уже установили метод [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) в **true**, возникает исключение, например, неверный формат числа. Ознакомьтесь с комментариями внутри кода для получения дальнейшей помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

