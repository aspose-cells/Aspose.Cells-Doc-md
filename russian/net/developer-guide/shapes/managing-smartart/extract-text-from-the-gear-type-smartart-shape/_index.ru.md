---
title: Извлечение текста из формы SmartArt типа шестеренки
type: docs
weight: 500
url: /ru/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Возможные сценарии использования**

 Aspose.Cells может извлекать текст из формы Smart Art Shape Gear Type. Для этого сначала нужно преобразовать фигуру Smart Art Shape в фигуру группы с помощью[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) метод. Затем вы должны получить массив всех индивидуальных фигур, образующих групповую фигуру, используя[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) метод. Наконец, вы можете повторять все отдельные фигуры одну за другой в цикле и извлекать их текст, используя[**Форма.Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)имущество.

## **Извлечение текста из формы SmartArt типа шестеренки**

 Следующий пример кода загружает[образец файла Excel](67338483.xlsx) который содержит Gear Type Smart Art Shape. Затем он извлекает текст из отдельных фигур, как обсуждалось выше. См. консольный вывод кода, приведенного ниже, для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
