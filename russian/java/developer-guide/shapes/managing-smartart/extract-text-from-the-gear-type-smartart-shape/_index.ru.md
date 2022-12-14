---
title: Извлечение текста из формы SmartArt типа шестеренки
type: docs
weight: 130
url: /ru/java/extract-text-from-the-gear-type-smartart-shape/
---
## **Возможные сценарии использования**

Aspose.Cells может извлекать текст из формы Smart Art Shape Gear Type. Для этого сначала нужно преобразовать фигуру Smart Art Shape в фигуру группы с помощью[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) метод. Затем вы должны получить массив всех индивидуальных фигур, образующих групповую фигуру, используя[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) метод. Наконец, вы можете повторять все отдельные фигуры одну за другой в цикле и извлекать их текст, используя[**Форма.Текст**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)имущество.

## **Извлечение текста из формы SmartArt типа шестеренки**

Следующий пример кода загружает[образец файла Excel](67338510.xlsx)который содержит Gear Type Smart Art Shape. Затем он извлекает текст из отдельных фигур, как обсуждалось выше. См. консольный вывод кода, приведенного ниже, для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
