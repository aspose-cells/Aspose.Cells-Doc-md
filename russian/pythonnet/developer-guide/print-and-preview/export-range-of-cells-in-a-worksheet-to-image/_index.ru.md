---
title: Экспорт диапазона ячеек листа в изображение
type: docs
weight: 60
url: /ru/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Возможные сценарии использования**

Вы можете создать изображение листа с помощью Aspose.Cells for Python via .NET. Однако иногда нужно экспортировать только диапазон ячеек из листа в изображение. В этой статье объясняется, как этого добиться.

## **Экспорт диапазона ячеек листа в изображение**

Для создания изображения диапазона установите область печати в нужный диапазон, затем установите все поля в 0. Также установите [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) в значение **true**. Ниже приведен скриншот [образца файла Excel](47153160.xlsx), используемого в коде. Вы можете попробовать код с любым файлом Excel.

## **Скриншот образца файла Excel и его экспортированного изображения**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Выполнение кода создает изображение только для диапазона D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
