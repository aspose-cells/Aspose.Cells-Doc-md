---
title: Установить поля комментария или формы внутри таблицы
type: docs
weight: 1500
url: /ru/net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет установить поля любой формы или комментария с использованием свойства [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/fontsettingcollection/properties/textalignment). Это свойство возвращает объект класса [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment), который имеет различные свойства, например [**TopMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/topmarginpt), [**LeftMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/leftmarginpt), [**BottomMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/bottommarginpt), [**RightMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rightmarginpt), и т. д., которые могут быть использованы для установки верхнего, левого, нижнего и правого полей.

## **Задать поля комментария или формы внутри рабочего листа**

Пожалуйста, ознакомьтесь со следующим образцом кода. Он загружает [образец Excel файла](61767851.xlsx), содержащий две формы. Код получает доступ к формам поочередно и устанавливает их верхние, левые, нижние и правые поля. Пожалуйста, ознакомьтесь с [файлом вывода Excel](61767852.xlsx), сгенерированным кодом, и снимком экрана, показывающим эффект кода на файл вывода Excel.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
