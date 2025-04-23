---
title: Отправить форму вперед или назад внутри листа
type: docs
weight: 3400
url: /ru/net/send-shape-front-or-back-inside-the-worksheet/
---

## **Возможные сценарии использования**

Когда в одном и том же месте находится несколько Фигур, их видимость определяется их позициями по z-порядку. Aspose.Cells предоставляет метод [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback), который изменяет позицию Фигуры в z-порядке. Если вы хотите отправить Фигуру назад, вы будете использовать отрицательное число, например -1, -2, -3 и т. д., а если вы хотите отправить Фигуру вперед, вы будете использовать положительное число, например 1, 2, 3 и т. д.

## **Отправить форму вперед или назад внутри листа**

Следующий образец кода объясняет использование метода [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback). Пожалуйста, обратитесь к [образцу файла Excel](50528330.xlsx), использованному в коде, и [выходному файлу Excel](50528331.xlsx), сгенерированному им. Скриншот показывает эффект кода на образце файла Excel при выполнении.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
