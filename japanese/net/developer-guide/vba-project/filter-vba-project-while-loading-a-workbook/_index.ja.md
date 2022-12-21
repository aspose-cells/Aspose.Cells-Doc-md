---
title: ワークブックの読み込み中に VBA プロジェクトをフィルター処理する
type: docs
weight: 140
url: /ja/net/filter-vba-project-while-loading-a-workbook/
---
## **C# で Excel ワークブックをロード中に VBA プロジェクトをフィルター処理する**

一部の .xlsm/.xslb ファイルには、大量のマクロ (または非常に長いマクロ) が含まれています。 Aspose.Cells は、そのようなワークブックを開くときに、この (メタ) データを無条件に読み込みます。ただし、これを制御する必要がある場合があります[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)多数のワークブックのシート名のみを抽出する必要がある場合は、そのような不要なコンテンツをスキップします。このフィルターは、新しいオプションを導入することによって提供されます。[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **サンプルコード**

次のサンプル コードは、VBA のみがフィルター処理されるようにブックを読み込みます。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
