---
title: Повторное использование объектов стиля
description: В Aspose.Cells for .NET, создавая и используя повторно используемые объекты стиля, вы можете упростить управление стилями и повысить эффективность кода. Наше руководство поможет вам использовать преимущества многократно используемых объектов стиля и реализовать их в своем приложении.
keywords: Aspose.Cells for .NET, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /ru/net/reusing-style-objects/
---
{{% alert color="primary" %}}

Повторное использование объектов стиля может сэкономить память и ускорить работу программы.

{{% /alert %}}

Чтобы применить форматирование к большому диапазону ячеек на листе:

1. Создайте объект стиля.
1. Укажите атрибуты.
1. Примените стиль к ячейкам диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Поскольку[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) подход использует намного меньше памяти и является эффективным, старое свойство Cell.Style, которое потребляло много ненужной памяти, было удалено с выпуском Aspose.Cells 7.1.0.

{{% /alert %}}
