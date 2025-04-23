---
title: Установить поля комментария или формы внутри таблицы
type: docs
weight: 90
url: /ru/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет устанавливать поля любой формы или комментария, используя свойство [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment). Это свойство возвращает объект класса [**ShapeTextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) с различными свойствами, например [**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt), [**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt), [**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt), [**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt), и т. д., которые можно использовать для установки верхних, левых, нижних и правых полей.

## **Задать поля комментария или формы внутри рабочего листа**

Пожалуйста, посмотрите следующий примерный код. Он загружает [примерный файл Excel](61767867.xlsx), содержащий две фигуры. Код обращается к формам по очереди и устанавливает их верхние, левые, нижние и правые поля. Пожалуйста, посмотрите [выходной файл Excel](61767866.xlsx), сгенерированный кодом, и скриншот, показывающий эффект кода на выходной файл Excel.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
