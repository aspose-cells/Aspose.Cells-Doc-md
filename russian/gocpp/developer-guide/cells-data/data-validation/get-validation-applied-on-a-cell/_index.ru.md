---
title: Получить проверку, примененную к ячейке, с помощью Golang через C++
linktitle: Получить примененную валидацию для ячейки
type: docs
weight: 200
url: /ru/go-cpp/get-validation-applied-on-a-cell/
description: Эта статья показывает, как применять проверку данных на ячейке с помощью Golang через C++.
keywords: применить проверку ячейки в Excel с помощью C++, применить проверку к ячейке в Excel с помощью C++, установить проверку в Excel с помощью C++, проверка ячейки в Excel с помощью C++, C++ применение проверки ячейки в Excel, C++ установка проверки для ячейки в Excel, C++ проверка ячейки в Excel, C++ проверка ячейки в Excel
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells, чтобы получить проверку, примененную к ячейке. Aspose.Cells предоставляет метод [**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/) для этой цели. Если на ячейке не применена проверка, он возвращает null.

Точно так же можно использовать метод [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/), чтобы получить примененную валидацию для ячейки, указав её индексы строки и столбца.

{{% /alert %}}

## C++ код для получения примененной проверки к ячейке

Следующий пример показывает, как получить проверку, примененную к ячейке.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## Связанные статьи

- [Валидация данных](/cells/ru/cpp/data-validation/)
