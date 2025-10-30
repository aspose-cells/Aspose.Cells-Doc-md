---
title: リンクされた形状の値をリフレッシュ
type: docs
weight: 3200
url: /ja/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

時々、Excelファイルにはセルにリンクされた形状がある場合があります。Microsoft Excelでは、リンクされたセルの値を変更すると、リンクされた形状の値も変更されます。Aspose.Cellsでも、XLSまたはXLSX形式でワークブックを保存する場合には、この動作が適切に機能します。ただし、ワークブックをPDFやHTML形式で保存する場合には、リンクされた形状の値をリフレッシュするために[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue())メソッドを呼び出さなければなりません。

{{% /alert %}}

## 例

次のスクリーンショットは、サンプルコードで使用される元のExcelファイルを示しています。A1からE4までのセルにリンクされた画像が含まれています。Aspose.CellsでセルB4の値を変更し、[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue())メソッドを呼び出して画像の値をリフレッシュし、PDF形式で保存します。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

リンクから[ソースExcelファイル](sampleRefreshValueOfLinkedShapes.xlsx)と[出力PDF](95584292.pdf)をダウンロードできます。

### リンクされた図形の値を更新するためのC＃コード

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
