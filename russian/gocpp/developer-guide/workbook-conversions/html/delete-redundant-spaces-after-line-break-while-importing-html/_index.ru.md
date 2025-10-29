---
title: Удалите лишние пробелы после разрывов строк при импорте HTML с помощью Golang через C++
linktitle: Удаление избыточных пробелов после переноса строки при импорте HTML
type: docs
weight: 20
url: /ru/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Узнайте, как удалять лишние пробелы после разрывов строк при импорте HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Пожалуйста, используйте свойство [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) и установите его в **true**, чтобы удалить все лишние пробелы после тега разрыва строки. По умолчанию это свойство равно **false**, и лишние пробелы сохраняются в выходных файлах Excel.

{{% /alert %}}

## Эффект установки свойства HTMLLoadOptions.DeleteRedundantSpaces в значение false и true

На следующем скриншоте показан эффект установки этого свойства в **false** и **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Удаление избыточных пробелов после переноса строки при импорте HTML

### Пример программирования

Следующий пример кода демонстрирует использование свойства [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/). Пожалуйста, установите его **true** или **false**, чтобы получить вывод, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
