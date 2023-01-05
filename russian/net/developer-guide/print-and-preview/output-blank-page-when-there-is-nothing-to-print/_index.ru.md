---
title: Вывод пустой страницы, когда нечего печатать
type: docs
weight: 90
url: /ru/net/output-blank-page-when-there-is-nothing-to-print/
---
## **Возможные сценарии использования**

 Если лист пуст, то Aspose.Cells ничего не напечатает при экспорте рабочего листа в изображение. Вы можете изменить это поведение, используя[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) имущество. Когда вы установите его**истинный**, он напечатает пустую страницу.

## **Вывод пустой страницы, когда нечего печатать**

Следующий пример кода создает пустую книгу с пустым листом и отображает пустой лист в изображение после установки параметра[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) собственность как**истинный**. Следовательно, он генерирует пустую страницу, поскольку печатать нечего, что вы можете видеть на изображении ниже.

![дело:изображение_альтернативный_текст](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
