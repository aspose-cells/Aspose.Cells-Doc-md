---
title: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами
type: docs
weight: 70
url: /ru/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Возможные сценарии использования**

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются в веб-браузерах. Когда вы конвертируете такой Excel файл в HTML с помощью Aspose.Cells, такие границы удаляются. Однако Aspose.Cells также поддерживает отображение таких границ с помощью свойства [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle). Пожалуйста, установите его значение **true**, и неподдерживаемые границы также будут экспортированы в файл HTML.

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**

Следующий образец кода загружает [образец Excel файла](64716806.xlsx), который содержит неподдерживаемые границы, как показано на следующем скриншоте. На скриншоте дополнительно показан эффект свойства [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) в [выходном HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
