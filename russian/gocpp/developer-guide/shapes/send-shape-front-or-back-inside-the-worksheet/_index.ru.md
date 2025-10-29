---
title: Отправить фигуру на передний или задний план внутри листа с помощью Golang через C++
linktitle: Отправить форму вперед или назад внутри листа
type: docs
weight: 3400
url: /ru/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Узнайте, как изменять z порядок фигур в листе с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда в одном месте находится несколько фигур, их видимость определяется их положением по z-порядку. Aspose.Cells предоставляет метод [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/), который изменяет z-область фигуры. Если вы хотите отправить фигуру на задний план, используйте отрицательное число, например -1, -2, -3 и т.д. Если хотите поднять фигуру на передний план, используйте положительное число, например 1, 2, 3 и т.д.

## **Отправить форму вперед или назад внутри листа**

Следующий пример кода демонстрирует использование метода [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/). Пожалуйста, посмотрите [приведенный пример файла Excel](50528330.xlsx), использованный в коде, и [сгенерированный выходной файл Excel](50528331.xlsx). Скриншот показывает эффект работы кода на примере файла Excel при запуске.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
