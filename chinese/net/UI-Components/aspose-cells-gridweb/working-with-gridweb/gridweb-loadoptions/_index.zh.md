---
title: GridWeb 的加载选项
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

在导入文件之前，我们可以设置一些加载选项。

我们可以用[网格加载选项](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)（对于一般文件）和[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) （对于 csv 文件）
 
{{% /alert %}} 
##  **加载其他编码**
对于csv文件，其实是一个文本文件，没有xlsx格式文件中描述的具体编码。

因此，用户可以在加载文件之前设置特定的字符编码。

这是一个用中文加载的示例代码：

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```