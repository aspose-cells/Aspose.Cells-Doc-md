---
title: Экспорт диапазона Cells на листе в изображение
type: docs
weight: 60
url: /ru/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Возможные сценарии использования**

Вы можете создать изображение рабочего листа, используя Aspose.Cells. Однако иногда вам нужно экспортировать в изображение только диапазон ячеек рабочего листа. В этой статье объясняется, как этого добиться.

## **Экспорт диапазона Cells на листе в изображение**

 Чтобы сделать изображение диапазона, установите область печати на желаемый диапазон, а затем установите все поля на 0. Также установите[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) к**истинный** . Следующий код берет изображение диапазона D8:G16. Ниже приведен скриншот[образец файла Excel](47153160.xlsx) используется в коде. Вы можете попробовать код с любым файлом Excel.

## **Снимок экрана с образцом файла Excel и его экспортированным изображением**

**![todo:image_alt_text](экспорт-диапазона-ячеек-на-листе-в-изображение_1.png)**

При выполнении кода создается изображение только диапазона D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
