---
title: Excel с неподдерживаемым стилем границы в HTML
type: docs
weight: 80
url: /ru/python-java/excel-with-unsupported-border-style-to/
---

## **Excel с неподдерживаемым стилем границы в HTML**
Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. При конвертации таких файлов в HTML с помощью Aspose.Cells эти границы удаляются. Однако Aspose.Cells для Python via Java поддерживает отображение аналогичных границ с помощью свойства ExportSimilarBorderStyle в HtmlSaveOptions. Можно установить значение свойства ExportSimilarBorderStyle в True для экспорта неподдерживаемых границ.

В следующем образце кода загружается образец файла Excel, который содержит некоторые неподдерживаемые границы, как показано на следующем снимке экрана. Снимок экрана также иллюстрирует эффект свойства ExportSimilarBorderStyle в HtmlSaveOptions в выходном HTML.

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
