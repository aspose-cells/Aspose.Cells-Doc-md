---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/python-net/different-ways-to-open-files/
description: 本文介绍如何使用 Aspose.Cells for Python via .NET API 打开Excel文件。
keywords: 无需 Excel，即可在 Python 中打开 Excel 文件，你该如何操作。
---

{{% alert color="primary" %}}

使用 Aspose.Cells for Python via .NET，打开文件非常简单，例如，获取数据或使用设计模板来加快开发过程。

{{% /alert %}}

## **如何通过路径打开Excel文件**

开发者可以通过在 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的构造函数中指定本地计算机上的文件路径来打开 Microsoft Excel 文件。只需将路径作为字符串传入构造函数即可。Aspose.Cells for Python via .NET 会自动检测文件格式类型。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **如何通过流打开Excel文件**

通过流打开Excel文件也很简单。为此，请使用接收包含文件的*流*对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **如何只打开具有数据的文件**

要仅打开具有数据的文件，使用[**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions)和[**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter)类设置文件模板的相关属性和选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
