---
title: Создание условного форматирования изображений DataBars
type: docs
weight: 40
url: /ru/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Иногда вам нужно создать изображения панелей данных условного форматирования. Вы можете использовать Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) способ создания этих изображений. В этой статье показано, как создать изображение DataBar с помощью Aspose.Cells.

{{% /alert %}}

Следующий пример кода создает изображение DataBar для ячейки C1. Сначала он обращается к объекту условия формата ячейки, а затем из этого объекта обращается к[**Панель данных**](https://reference.aspose.com/cells/net/aspose.cells/databar) объект и использует его[**Изображать()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)способ создания изображения клетки. Наконец, он сохраняет изображение на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
