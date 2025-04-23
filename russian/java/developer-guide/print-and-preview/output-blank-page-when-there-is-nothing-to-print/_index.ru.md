---
title: Вывод пустой страницы, когда нечего печатать
type: docs
weight: 80
url: /ru/java/output-blank-page-when-there-is-nothing-to-print/
---

## **Возможные сценарии использования**

Если лист пуст, то Aspose.Cells не будет ничего печатать при экспорте листа в изображение. Вы можете изменить это поведение, используя свойство [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint). Когда вы установите его в **true**, он будет печатать пустую страницу.

## **Вывод пустой страницы, когда нечего печатать**

Следующий образец кода создает пустую книгу, у которой пустой лист, и рендерит пустой лист в изображение после установки свойства [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) как **true**. В результате генерируется пустая страница, поскольку нет ничего, чтобы напечатать, что можно увидеть ниже.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
{{< app/cells/assistant language="java" >}}
