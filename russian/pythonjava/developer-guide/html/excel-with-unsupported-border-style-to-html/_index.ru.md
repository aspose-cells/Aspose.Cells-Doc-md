---
title: Excel с неподдерживаемым стилем границы в HTML
type: docs
weight: 80
url: /ru/python-java/excel-with-unsupported-border-style-to/
---
## **Excel с неподдерживаемым стилем границы в HTML**
Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. Когда такие файлы преобразуются в HTML с помощью Aspose.Cells, эти границы удаляются. Однако Aspose.Cells для Python через Java поддерживает отображение аналогичных границ с[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)имущество. Вы можете установить значение[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) собственность на**Истинный**экспортировать неподдерживаемые границы.

Следующий пример кода загружает[образец файла Excel](sampleExportSimilarBorderStyle.xlsx)который содержит некоторые неподдерживаемые границы, как показано на следующем снимке экрана. Скриншот дополнительно иллюстрирует эффект[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)имущество внутри[вывод HTML](outputExportSimilarBorderStyle.zip).

![дело:изображение_альтернативный_текст](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
