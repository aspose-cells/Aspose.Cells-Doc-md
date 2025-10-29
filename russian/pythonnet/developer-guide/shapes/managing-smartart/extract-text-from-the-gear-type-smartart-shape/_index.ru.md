---
title: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 500
url: /ru/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **Возможные сценарии использования**

Aspose.Cells может извлекать текст из умной формы Gear Type Smart Art. Для этого сначала нужно преобразовать умную форму в групповую форму, используя метод [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art). Затем следует получить массив всех индивидуальных форм, составляющих групповую форму, с помощью метода [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes). Наконец, можно перебрать все индивидуальные формы по одной в цикле и извлечь их текст, используя свойство [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

В следующем примере кода загружается [образец файла Excel](67338483.xlsx), содержащий умную форму Gear Type Smart Art. Затем извлекается текст из ее индивидуальных форм, как обсуждалось выше. Пожалуйста, ознакомьтесь с выводом консоли в приведенном ниже примере кода в качестве примера.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
