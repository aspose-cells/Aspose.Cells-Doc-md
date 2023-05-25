---
title: Вывод пустой страницы, когда нечего печатать
type: docs
weight: 80
url: /ru/java/output-blank-page-when-there-is-nothing-to-print/
---
##  **Возможные сценарии использования**

Если лист пуст, то Aspose.Cells ничего не напечатает при экспорте рабочего листа в изображение. Вы можете изменить это поведение, используя[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)свойство. Когда вы установите значение *true**, будет напечатана пустая страница.

##  **Вывод пустой страницы, когда нечего печатать**

Следующий пример кода создает пустую книгу с пустым листом и отображает пустой лист в изображение после установки параметра[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)свойство как *true**. Следовательно, он генерирует пустую страницу, поскольку печатать нечего, как вы можете видеть ниже.

![дело:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
