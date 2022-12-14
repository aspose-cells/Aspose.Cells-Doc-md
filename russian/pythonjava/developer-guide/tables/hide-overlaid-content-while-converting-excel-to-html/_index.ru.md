---
title: Скрыть наложенный контент при преобразовании Excel в HTML
type: docs
weight: 40
url: /ru/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Скрыть наложенный контент при преобразовании Excel в HTML**
Когда вы сохраняете файл Excel в формате HTML, вы можете указать различные перекрестные типы для строк ячеек. По умолчанию Aspose.Cells генерирует HTML в соответствии с Microsoft Excel, но при изменении[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)к[ПЕРЕСЕКАТЬ_СПРЯТАТЬ_ПРАВИЛЬНО](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)затем он скрывает все строки с правой стороны ячейки, которые перекрываются или перекрываются со строкой ячейки.

Следующий пример кода загружает[образец файла Excel](sampleHidingOverlaidContentWithCrossHideRight.xlsx)и сохраняет его в[вывод HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)после установки[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)в качестве[ПЕРЕСЕКАТЬ_СПРЯТАТЬ_ПРАВИЛЬНО](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). Скриншот объясняет, как[ПЕРЕСЕКАТЬ_СПРЯТАТЬ_ПРАВИЛЬНО](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)влияет на вывод HTML из вывода по умолчанию.

![дело:изображение_альтернативный_текст](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
