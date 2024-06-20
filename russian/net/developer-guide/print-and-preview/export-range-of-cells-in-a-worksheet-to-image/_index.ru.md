---
title: Экспорт диапазона ячеек листа в изображение
type: docs
weight: 60
url: /ru/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Возможные сценарии использования**

Вы можете создать изображение листа с помощью Aspose.Cells. Однако иногда вам может потребоваться экспортировать только диапазон ячеек листа в изображение. В этой статье объясняется, как это сделать.

## **Экспорт диапазона ячеек листа в изображение**

Для создания изображения диапазона установите область печати в нужный диапазон, затем установите все поля в 0. Также установите [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) в значение **true**. Ниже приведен скриншот [образца файла Excel](47153160.xlsx), используемого в коде. Вы можете попробовать код с любым файлом Excel.

## **Скриншот образца файла Excel и его экспортированного изображения**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Выполнение кода создает изображение только для диапазона D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
