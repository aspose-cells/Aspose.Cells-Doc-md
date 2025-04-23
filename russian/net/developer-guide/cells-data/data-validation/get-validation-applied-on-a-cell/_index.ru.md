---
title: Получить примененную валидацию для ячейки
type: docs
weight: 200
url: /ru/net/get-validation-applied-on-a-cell/
description: В этой статье показано, как применить проверку к ячейке с помощью C#
keywords: применить проверку ячейки в Excel с помощью c#, применить проверку на ячейку в Excel с помощью c#, применить проверки в Excel с помощью c#, проверка ячейки в Excel с помощью c#, c# применить проверку ячейки в Excel, c# применить проверку на ячейку в Excel, c# проверка ячейки в Excel, c# проверка ячейки
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells, чтобы получить проверку, примененную к ячейке. Aspose.Cells предоставляет метод [**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) для этой цели. Если на ячейке не применена проверка, он возвращает null.

Точно так же можно использовать метод [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell), чтобы получить примененную валидацию для ячейки, указав её индексы строки и столбца.

{{% /alert %}}

## Код на C# для получения примененной проверки на ячейку

Приведенный ниже образец кода показывает, как получить примененную валидацию для ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## Связанные статьи

- [Валидация данных](/cells/ru/net/data-validation/)
{{< app/cells/assistant language="csharp" >}}
