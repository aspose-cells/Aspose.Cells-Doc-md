---
title: GridWeb の LoadOptions
type: docs
weight: 90
url: /ja/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

ファイルをインポートする前に設定できるロードオプションがいくつかあります。

私たちは使うことができます[グリッドロードオプション](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(一般的なファイルの場合) および[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (csvファイルの場合)
 
{{% /alert %}} 
##  **他のエンコードでロードする**
csv ファイルの場合、実際にはテキストベースのファイルであり、xlsx 形式ファイルに記述されている特定のエンコーディングはありません。

したがって、ユーザーはファイルをロードする前に特定の文字エンコーディングを設定できます。

これは中国語でロードするサンプルコードです:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```