---
title: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 130
url: /ru/java/extract-text-from-the-gear-type-smartart-shape/
---

## **Возможные сценарии использования**

Aspose.Cells может извлекать текст из фигуры Smart Art Shape. Для этого сначала необходимо преобразовать Smart Art Shape в Group Shape, используя метод [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--). Затем вы должны получить массив всех Individual Shapes, составляющих Group Shape, с помощью метода [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--). Наконец, вы можете перебирать все Individual Shapes по очереди в цикле и извлекать их текст с использованием свойства [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

Приведенный ниже образец кода загружает содержащий форму Smart Art типа Gear образец Excel-файл. Затем извлекает текст из его индивидуальных форм, как обсуждалось выше. Пожалуйста, обратитесь к выводу консоли приведенного ниже кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
