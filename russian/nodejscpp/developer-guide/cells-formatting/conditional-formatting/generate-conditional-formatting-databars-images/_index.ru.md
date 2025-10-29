---
title: Генерация изображений полос данных условного форматирования
linktitle: Генерация изображений полос данных условного форматирования
description: Aspose.Cells — это библиотека Node.js для работы с таблицами. Она поддерживает создание условных индикаторов данных и изображений, позволяя пользователям настраивать отображение таблицы в зависимости от значений ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для генерации условных индикаторов данных и изображений.
keywords: Aspose.Cells, Условное форматирование, Индикаторы данных, Изображения, Таблицы, Node.js через C++
type: docs
weight: 40
url: /ru/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображения условного форматирования панелей данных. Вы можете использовать метод Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) для создания этих изображений. В этой статье показано, как создать изображение панели данных с помощью Aspose.Cells.

{{% /alert %}}

Следующий пример кода создает изображение DataBar для ячейки C1. Он сначала обращается к объекту условного форматирования ячейки, затем через этот объект — к [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) объекту и использует его метод [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) для генерации изображения ячейки. В конце он сохраняет изображение на диск.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
