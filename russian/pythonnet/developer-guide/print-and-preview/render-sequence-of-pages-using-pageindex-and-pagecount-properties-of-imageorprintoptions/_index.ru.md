---
title: Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions
type: docs
weight: 110
url: /ru/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Возможные сценарии использования**

Вы можете отображать последовательность страниц вашего файла Excel в виде изображений с помощью Aspose.Cells for Python via .NET с помощью свойств [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) и [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Эти свойства полезны, когда страниц много, например тысячи, и нужно отображать только некоторые из них. Это сэкономит время обработки и памяти во время рендеринга.

## **Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions**

В следующем образцовом коде загружается [образец Excel-файла](55541781.xlsx) и воспроизводятся только страницы 4, 5, 6 и 7 с использованием [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) и [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count) свойств. Вот воспроизведенные страницы, созданные кодом.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
