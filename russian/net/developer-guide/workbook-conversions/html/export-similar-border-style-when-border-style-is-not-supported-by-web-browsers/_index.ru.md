---
title: Экспорт аналогичного стиля границы, если стиль границы не поддерживается веб-браузерами
type: docs
weight: 70
url: /ru/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Возможные сценарии использования**

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. Когда вы конвертируете такой файл Excel в HTML с помощью Aspose.Cells, такие границы удаляются. Однако Aspose.Cells также может поддерживать отображение таких границ с[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) имущество. Пожалуйста, установите его значение как**истинный**и неподдерживаемые границы также будут экспортированы в файл HTML.

## **Экспорт аналогичного стиля границы, если стиль границы не поддерживается веб-браузерами**

Следующий пример кода загружает[образец файла Excel](64716806.xlsx) который содержит некоторые неподдерживаемые границы, как показано на следующем снимке экрана. Скриншот дополнительно иллюстрирует эффект[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)имущество внутри[вывод HTML](64716804.zip).

![дело:изображение_альтернативный_текст](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
