---
title: GridWeb 的 LoadOptions
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: 加载选项，设置，加载，选项
description: 本文介绍如何使用 GridWeb 中的加载选项。
---

{{% alert color="primary" %}} 

在导入文件之前，我们可以设置一些加载选项。

我们可以使用 [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/)（用于一般文件）和 [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/)（用于 CSV 文件）。	

{{% /alert %}} 
## **使用其他编码加载**
对于 CSV 文件，它实际上是基于文本的文件，没有在 xlsx 格式文件中描述的特定编码。

因此，用户可以在加载文件之前设置特定的字符编码。

这里有一个示例代码用于加载中文：

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
