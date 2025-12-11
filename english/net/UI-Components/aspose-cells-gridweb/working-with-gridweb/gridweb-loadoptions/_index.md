---
title: LoadOptions for GridWeb
type: docs
weight: 90
url: /net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,load,options,option
description: This article introduces how to work with load options in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

There are some load options we can set before importing the file.

We can use [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (for general files) and [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (for CSV files).	
 
{{% /alert %}} 

## **Load with Other Encoding**

For a CSV file, it is actually a text‑based file without the specific encoding described in the XLSX format.

Therefore, users can set a specific character encoding before loading the file.

Here is a sample code to load a Chinese CSV file:

```csharp
GridTxtLoadOptions topt = new GridTxtLoadOptions();
topt.Encoding = Encoding.GetEncoding("GB2312");
GridWeb1.LoadOptions = topt;
string filePath = Server.MapPath("~/workbook/chinesefile.csv");
GridWeb1.ImportExcelFile(filePath);
```
