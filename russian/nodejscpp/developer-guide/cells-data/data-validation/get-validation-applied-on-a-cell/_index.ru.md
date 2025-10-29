---
title: Получить примененную валидацию для ячейки
type: docs
weight: 200
url: /ru/nodejs-cpp/get-validation-applied-on-a-cell/
description: В этой статье показано, как применять проверку данных на ячейке с помощью Node.js через C++.
keywords: применить проверку ячейки в excel с помощью Node.js через C++, применить проверку к ячейке в excel с помощью Node.js через C++, применить проверку в excel с помощью Node.js через C++, проверка ячейки в excel с помощью Node.js через C++, Node.js через C++ применить проверку ячейки в excel, Node.js через C++ применить проверку на ячейке в excel, Node.js через C++ проверка ячейки в excel
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для Node.js, чтобы применить проверку к ячейке. Aspose.Cells предоставляет метод [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) для этой цели. Если проверка не применена к ячейке, он возвращает null.

Точно так же можно использовать метод [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-), чтобы получить примененную валидацию для ячейки, указав её индексы строки и столбца.

{{% /alert %}}

## Код Node.js для получения примененной проверки на ячейке

Следующий пример показывает, как получить проверку, примененную к ячейке.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## Связанные статьи

- [Валидация данных](/cells/ru/nodejs-cpp/data-validation/)
{{< app/cells/assistant language="nodejs-cpp" >}}
