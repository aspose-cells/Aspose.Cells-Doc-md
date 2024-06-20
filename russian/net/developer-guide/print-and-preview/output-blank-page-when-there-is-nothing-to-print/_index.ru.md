---
title: Вывод пустой страницы, когда нечего печатать
type: docs
weight: 90
url: /ru/net/output-blank-page-when-there-is-nothing-to-print/
---

## **Возможные сценарии использования**

Если лист пуст, то Aspose.Cells не выведет ничего при экспорте листа в изображение. Вы можете изменить это поведение, используя свойство [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint). Когда вы установите его в **true**, будут выведена пустая страница.

## **Вывод пустой страницы, когда нечего печатать**

Приведенный ниже образец кода создает пустую книгу с пустым листом и выводит пустой лист в изображение после установки свойства [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) в **true**. Следовательно, будет сгенерирована пустая страница, так как нет ничего для печати, что можно увидеть на изображении ниже.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
