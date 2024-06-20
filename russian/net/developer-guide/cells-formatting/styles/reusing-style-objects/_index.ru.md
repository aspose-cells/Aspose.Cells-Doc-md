---
title: Повторное использование объектов стиля
description: В Aspose.Cells for .NET, создавая и используя повторно используемые объекты стилей, вы можете упростить управление стилями и улучшить эффективность кода. Наш руководство поможет вам использовать преимущества повторно используемых объектов стилей и реализовать их в вашем приложении.
keywords: Aspose.Cells for .NET, повторное использование объектов стиля, управление стилями, эффективность кода, повторно используемые стили, разработка приложений, справочник API, пример кода, загрузка, поддержка.
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
1. Примените стиль к ячейкам в диапазоне.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

Поскольку подход [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) использует гораздо меньше памяти и является эффективным, старое свойство Cell.Style, которое потребляло много ненужной памяти, было удалено с выпуском Aspose.Cells 7.1.0.

{{% /alert %}}
