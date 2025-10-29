---
title: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами
type: docs
weight: 70
url: /ru/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Возможные сценарии использования**

Microsoft Excel поддерживает некоторые типы пунктирных границ, не поддерживаемых веб-браузерами. При преобразовании такого файла Excel в HTML с помощью Aspose.Cells для Python via .NET такие границы удаляются. Однако Aspose.Cells для Python via .NET также может отображать такие границы с помощью свойства [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style). Установите его значение в **true**, и неподдерживаемые границы также будут экспортированы в HTML.

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**

Следующий образец кода загружает [образец Excel файла](64716806.xlsx), который содержит неподдерживаемые границы, как показано на следующем скриншоте. На скриншоте дополнительно показан эффект свойства [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) в [выходном HTML](64716804.zip).

![todo:image_alt_text](1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
