---  
title: Настройка полей комментария или формы внутри рабочего листа с помощью Golang через C++  
linktitle: Установить поля комментария или формы внутри таблицы  
type: docs  
weight: 1500  
url: /ru/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Узнайте, как устанавливать поля комментариев или форм внутри рабочего листа с помощью Aspose.Cells и Golang через C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells позволяет устанавливать поля любой фигуры или комментария, используя свойство [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/). Оно возвращает объект класса [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment), у которого есть различные свойства, например [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/) и др., которые можно использовать для установки верхних, левых, нижних и правых полей.  

## **Задать поля комментария или формы внутри рабочего листа**  

Пример кода ниже. Он загружает [пример файла Excel](61767851.xlsx), содержащего две фигуры. Код обращается к фигурам по очереди и устанавливает их верхние, левое, нижние и правые поля. Посмотрите [сгенерированный файл Excel](61767852.xlsx) и скриншот, показывающий эффект работы кода на выходном файле Excel.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Образец кода**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  
