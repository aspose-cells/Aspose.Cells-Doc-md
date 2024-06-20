---
title: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 500
url: /ru/net/extract-text-from-the-gear-type-smartart-shape/
---

## **Возможные сценарии использования**

Aspose.Cells может извлекать текст из умной формы Gear Type Smart Art. Для этого сначала нужно преобразовать умную форму в групповую форму, используя метод [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart). Затем следует получить массив всех индивидуальных форм, составляющих групповую форму, с помощью метода [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes). Наконец, можно перебрать все индивидуальные формы по одной в цикле и извлечь их текст, используя свойство [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

В следующем примере кода загружается [образец файла Excel](67338483.xlsx), содержащий умную форму Gear Type Smart Art. Затем извлекается текст из ее индивидуальных форм, как обсуждалось выше. Пожалуйста, ознакомьтесь с выводом консоли в приведенном ниже примере кода в качестве примера.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
