---
title: Aspose.Cells を使用して Microsoft Excel 経由で OLE オブジェクトを自動的に更新する
type: docs
weight: 270
url: /ja/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

Aspose.Cells は[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) Microsoft Excel で Excel ファイルを開いたときに OLE オブジェクトを更新するプロパティ。このプロパティにより、OLE オブジェクトは Microsoft Excel によって生成された正しい OLE イメージを表示します。

{{% /alert %}}

次のサンプル コードは、[サンプルエクセルファイル](5115231.xlsx)非現実的な OLE イメージを持っています。 OLE オブジェクトは実際には Microsoft の Word ドキュメントですが、サンプルの Excel ファイルには Microsoft の Word 画像ではなく動物の画像が表示されています。しかし、開いてみると[出力エクセルファイル](5115225.xlsx)、Microsoft が表示されます。Excel は正しい OLE イメージを表示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
