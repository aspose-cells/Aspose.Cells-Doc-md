---
title: Создание изображений DataBars условного форматирования
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц. Он поддерживает создание гистограмм и изображений условного форматирования, позволяя пользователям настраивать отображение электронной таблицы в зависимости от значений ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для создания гистограмм и изображений условного форматирования.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /ru/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Иногда вам необходимо создать изображения панелей данных условного форматирования. Вы можете использовать Aspose.Cells.[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) метод создания этих изображений. В этой статье показано, как создать изображение DataBar, используя Aspose.Cells.

{{% /alert %}}

 Следующий пример кода создает изображение DataBar ячейки C1. Сначала он обращается к объекту условия формата ячейки, а затем из этого объекта обращается к[**Панель данных**](https://reference.aspose.com/cells/net/aspose.cells/databar) объект и использует его[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)метод создания изображения клетки. Наконец, он сохраняет изображение на диске.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
