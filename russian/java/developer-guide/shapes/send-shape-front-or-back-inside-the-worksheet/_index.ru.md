---
title: Отправить форму вперед или назад внутри листа
type: docs
weight: 600
url: /ru/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Возможные сценарии использования**

Когда в одном и том же месте присутствует несколько форм, то то, как они будут видны, зависит от их позиций в порядке z. Aspose.Cells предоставляет метод [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)), который изменяет позицию порядка z формы. Если вы хотите отправить форму назад, вы будете использовать отрицательное число, например, -1, -2, -3 и т. д., и если вы хотите отправить форму вперед, вы будете использовать положительное число, например, 1, 2, 3 и т. д.

## **Отправить форму вперед или назад внутри листа**

Нижеприведенный образец кода объясняет использование метода [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)). Пожалуйста, посмотрите [образец файла Excel](50528362.xlsx), используемый в коде, и [выходной файл Excel](50528361.xlsx), сгенерированный им. На скриншоте показан эффект кода на образцовом файле Excel при выполнении.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
