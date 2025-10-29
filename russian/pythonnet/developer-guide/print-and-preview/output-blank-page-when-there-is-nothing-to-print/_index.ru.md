---
title: Вывод пустой страницы, когда нечего печатать
type: docs
weight: 90
url: /ru/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **Возможные сценарии использования**

Если лист пустой, тогда Aspose.Cells for Python via .NET не будет ничего печатать при экспорте листа в изображение. Вы можете изменить это поведение используя свойство [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print). Когда вы установите его в **true**, будет напечатана пустая страница.

## **Вывод пустой страницы, когда нечего печатать**

Приведенный ниже образец кода создает пустую книгу с пустым листом и выводит пустой лист в изображение после установки свойства [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) в **true**. Следовательно, будет сгенерирована пустая страница, так как нет ничего для печати, что можно увидеть на изображении ниже.

![todo:image_alt_text](1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
