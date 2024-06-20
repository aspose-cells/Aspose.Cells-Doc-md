---
title: Генерация изображений полос данных условного форматирования
description: Aspose.Cells  это .NET библиотека для работы с файлами электронных таблиц. Она поддерживает генерацию условно отформатированных панелей данных и изображений, что позволяет пользователям настраивать отображение электронных таблиц в зависимости от значений ячеек. В этой статье будет рассмотрено, как использовать библиотеку Aspose.Cells для генерации условно отформатированных панелей данных и изображений.
keywords: Aspose.Cells, Условное форматирование, Панели данных, Изображения, Таблицы
type: docs
weight: 40
url: /ru/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображения условного форматирования панелей данных. Вы можете использовать метод Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) для создания этих изображений. В этой статье показано, как создать изображение панели данных с помощью Aspose.Cells.

{{% /alert %}}

В следующем образце кода генерируется изображение панели данных ячейки C1. Сначала он получает объект условного форматирования ячейки, и затем из этого объекта извлекает объект [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) и использует его метод [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) для создания изображения ячейки. Наконец, он сохраняет изображение на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
