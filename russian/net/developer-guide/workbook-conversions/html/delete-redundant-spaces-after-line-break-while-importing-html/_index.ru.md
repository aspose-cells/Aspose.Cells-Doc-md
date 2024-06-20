---
title: Удаление избыточных пробелов после переноса строки при импорте HTML
type: docs
weight: 20
url: /ru/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Пожалуйста, используйте свойство [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) и установите его в **true** для удаления всех избыточных пробелов после тега переноса строки. По умолчанию это свойство **false** и избыточные пробелы сохраняются в выходных файлах Excel.

{{% /alert %}}

## Эффект установки свойства HTMLLoadOptions.DeleteRedundantSpaces в значение false и true

На следующем скриншоте показан эффект установки этого свойства в **false** и **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Удаление избыточных пробелов после переноса строки при импорте HTML

### Пример программирования

Следующий пример кода демонстрирует использование свойства [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces). Пожалуйста, установите его **true** или **false**, чтобы получить вывод, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
