---
title: Генерация изображений полос данных условного форматирования
type: docs
weight: 170
url: /ru/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображения условного форматирования панелей данных. Вы можете использовать метод Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) для создания этих изображений. В этой статье показано, как создать изображение панели данных с помощью Aspose.Cells.

{{% /alert %}}

## **Пример**

Приведенный ниже образец кода генерирует изображение DataBar ячейки C1. Сначала он получает объект условия форматирования ячейки и затем из этого объекта получает объект DataBar и использует его метод [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) для генерации изображения ячейки. Наконец, он сохраняет изображение на диск.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
