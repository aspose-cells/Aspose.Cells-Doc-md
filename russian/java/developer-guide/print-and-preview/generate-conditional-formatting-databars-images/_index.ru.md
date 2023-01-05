---
title: Создание условного форматирования изображений DataBars
type: docs
weight: 170
url: /ru/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Иногда вам нужно создать изображения панелей данных условного форматирования. Вы можете использовать Aspose.Cells[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)для создания этих изображений. В этой статье показано, как создать изображение DataBar с помощью Aspose.Cells.

{{% /alert %}}

## **Пример**

 Следующий пример кода создает изображение DataBar для ячейки C1. Сначала он обращается к объекту условия формата ячейки, а затем из этого объекта обращается к объекту DataBar и использует его[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) метод для создания изображения ячейки. Наконец, он сохраняет изображение на диск.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
