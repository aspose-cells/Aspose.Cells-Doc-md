---
title: Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する
type: docs
weight: 270
url: /ja/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ExcelファイルがMicrosoft Excelで開かれるときにOLEオブジェクトを再表示するための[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload)プロパティを提供します。このプロパティにより、OLEオブジェクトは、Microsoft Excelによって生成された正しいOLEイメージを表示します。

{{% /alert %}}

次のサンプルコードでは、実際のOLEイメージでないOLEオブジェクトを含む[サンプルExcelファイル](5115231.xlsx)を読み込みます。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルExcelファイルではMicrosoft Wordイメージの代わりに動物のイメージが表示されます。しかし、[出力Excelファイル](5115225.xlsx)を開くと、Microsoft Excelが正しいOLEイメージを表示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
