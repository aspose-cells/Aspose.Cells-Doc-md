---
title: Поднимите фигуры на передний или задний план в рабочем листе
type: docs
weight: 3400
url: /ru/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Возможные сценарии использования**

Когда в одном и том же месте находится несколько Фигур, их видимость определяется их позициями по z-порядку. Aspose.Cells предоставляет метод [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)), который изменяет позицию Фигуры в z-порядке. Если вы хотите отправить Фигуру назад, вы будете использовать отрицательное число, например -1, -2, -3 и т. д., а если вы хотите отправить Фигуру вперед, вы будете использовать положительное число, например 1, 2, 3 и т. д.

## **Переместите фигуру вперёд или назад внутри рабочего листа**

Следующий пример кода объясняет использование метода [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)). Пожалуйста, ознакомьтесь с [примером файла Excel](sampleToFrontOrBack.xlsx), используемым в коде, и [выходным файлом Excel](50528331.xlsx), созданным им. Скриншот показывает результат выполнения кода на примере файла Excel.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
