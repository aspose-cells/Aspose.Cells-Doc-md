---
title: GridWeb的LoadOptions
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: loadoption、loadoptions、setting、load、options、option
description: 本文介绍了如何在GridWeb中使用加载选项
---

{{% alert color="primary" %}} 

我们可以在导入文件之前设置一些加载选项

我们可以使用[GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/)（用于一般文件）和[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/)（用于csv文件）	

{{% /alert %}} 
## **使用其他编码加载**
对于csv文件，实际上是一个基于文本的文件，在xlsx格式文件中没有特定的编码描述

因此，用户可以在加载文件之前设置特定的字符编码

这里是一个加载中文样本代码

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
