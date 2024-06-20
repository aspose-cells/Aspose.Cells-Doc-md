---
title: GridWebのためのLoadOptions
type: docs
weight: 90
url: /ja/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: loadoption、loadoptions、setting、load、options、option
description: この記事ではGridWebでのロードオプションの使用方法について紹介します。
---

{{% alert color="primary" %}} 

ファイルをインポートする前に設定できるいくつかのロードオプションがあります。

[GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/)（一般的なファイル用）および[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/)（csvファイル用）を使用できます	

{{% /alert %}} 
## **他のエンコードでロードする**
csvファイルの場合、実際にはxlsx形式ファイルに記載されている特定のエンコードがありません。

したがって、ユーザーはファイルをロードする前に特定の文字エンコーディングを設定できます。

中国語でロードするサンプルコードが以下に示されています:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
