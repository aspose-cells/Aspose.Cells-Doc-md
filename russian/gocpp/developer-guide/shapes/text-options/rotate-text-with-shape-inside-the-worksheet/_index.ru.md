---
title: Поворот текста с формой внутри рабочего листа с помощью Golang через C++
linktitle: Повернуть текст
type: docs
weight: 1300
url: /ru/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Узнайте, как управлять вращением текста в формах на листах Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете добавлять текст внутри любой формы, используя Microsoft Excel. Если добавлять фигуру с помощью очень старой версии Microsoft Excel 2003, текст не будет вращаться вместе с формой. Однако при использовании новых версий Excel, таких как 2007, 2010, 2013 или 2016, текст будет вращаться вместе с формой. Вы можете управлять этим с помощью свойства [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/). Значение по умолчанию этого свойства — **true**, что означает, что текст будет вращаться с формой. Если установить значение **false**, текст не будет вращаться вместе с формой.

## **Повернуть текст с фигурой внутри таблицы**

Следующий пример загружает [образец файла Excel](64716896.xlsx), который содержит треугольную фигуру, и вращение текста со всей фигурой. Если открыть пример файла в Microsoft Excel и повернуть треугольную фигуру, текст также повернётся с ней. Затем код устанавливает свойство [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) в значение **false** и сохраняет как [выходной файл Excel](64716897.xlsx). При открытии этого файла в Excel и вращении треугольной фигуры текст уже не будет вращаться. Ниже приведен скриншот, демонстрирующий эффект работы кода на примере файла.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
