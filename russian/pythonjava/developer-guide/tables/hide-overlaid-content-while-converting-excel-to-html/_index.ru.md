---
title: Скрыть перекрывающий контент при конвертации Excel в HTML
type: docs
weight: 40
url: /ru/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Скрыть перекрывающий контент при конвертации Excel в HTML**
При сохранении вашего файла Excel в HTML вы можете указать различные виды пересечений для строк ячеек. По умолчанию Aspose.Cells генерирует HTML в соответствии с Microsoft Excel, но когда вы изменяете HtmlCrossStringType на CROSS_HIDE_RIGHT, то скрывает все строки справа от ячейки, которые перекрываются или перекрывают строку ячейки.

В следующем образце кода загружается образец файла Excel и сохраняется в выходной HTML после установки HtmlCrossStringType как CROSS_HIDE_RIGHT

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
