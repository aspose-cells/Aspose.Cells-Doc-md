---
title: Удаление избыточных пробелов после переноса строки при импорте HTML
type: docs
weight: 20
url: /ru/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: Эта тема покажет вам, как удалить избыточные пробелы после переноса строки при импорте HTML с использованием Aspose.Cells для Python via NET.
keywords: Удалить избыточные пробелы после переноса строки при импорте HTML, Удалить избыточные пробелы для импорта html.
---

{{% alert color="primary" %}}

Пожалуйста, используйте свойство [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) и установите его в **true** для удаления всех избыточных пробелов после тега переноса строки. По умолчанию это свойство **false** и избыточные пробелы сохраняются в выходных файлах Excel.

{{% /alert %}}

## Эффект установки свойства HTMLLoadOptions.delete_redundant_spaces на false и true

На следующем скриншоте показан эффект установки этого свойства в **false** и **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Удаление избыточных пробелов после переноса строки при импорте HTML

### Пример программирования

Следующий пример кода демонстрирует использование свойства [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/). Пожалуйста, установите его **true** или **false**, чтобы получить вывод, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}
