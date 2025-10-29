---
title: Установить поля комментария или формы внутри таблицы
type: docs
weight: 1500
url: /ru/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Возможные сценарии использования**

Aspose.Cells for Python via .NET позволяет устанавливать поля любого объекта или комментария, используя свойство [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment). Это свойство возвращает объект класса [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment), который имеет разные свойства, например [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt), [**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt), [**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt), [**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt) и т.д., которые можно использовать для установки верхнего, левого, нижнего и правого полей.

## **Задать поля комментария или формы внутри рабочего листа**

Пожалуйста, ознакомьтесь со следующим образцом кода. Он загружает [образец Excel файла](61767851.xlsx), содержащий две формы. Код получает доступ к формам поочередно и устанавливает их верхние, левые, нижние и правые поля. Пожалуйста, ознакомьтесь с [файлом вывода Excel](61767852.xlsx), сгенерированным кодом, и снимком экрана, показывающим эффект кода на файл вывода Excel.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
