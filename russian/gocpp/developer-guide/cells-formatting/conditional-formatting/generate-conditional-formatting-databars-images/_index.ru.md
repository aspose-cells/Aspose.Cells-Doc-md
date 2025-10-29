---
title: Создание изображений условных форматов DataBars с Golang через C++
linktitle: Генерация изображений полос данных условного форматирования
description: Aspose.Cells — это библиотека C++ для работы с электронными таблицами. Она поддерживает создание условных графиков данных и изображений, позволяя пользователям настраивать отображение таблицы в зависимости от значения ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для генерации условных графиков данных и изображений.
keywords: Aspose.Cells, Условное форматирование, Панели данных, Изображения, Таблицы
type: docs
weight: 40
url: /ru/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображения условного форматирования панелей данных. Вы можете использовать метод Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) для создания этих изображений. В этой статье показано, как создать изображение панели данных с помощью Aspose.Cells.

{{% /alert %}}

Следующий пример кода создает изображение DataBar для ячейки C1. Он сначала обращается к объекту условного форматирования ячейки, затем через этот объект — к [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) объекту и использует его метод [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) для генерации изображения ячейки. В конце он сохраняет изображение на диск.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
