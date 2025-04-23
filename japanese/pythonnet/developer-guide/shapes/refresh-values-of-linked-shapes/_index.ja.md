---
title: リンクされた形状の値をリフレッシュ
type: docs
weight: 3200
url: /ja/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

時には、Excelファイル内にリンクされたシェイプがあり、それが特定のセルにリンクされていることがあります。Microsoft Excelでは、リンクされたセルの値を変更するとリンクされたシェイプの値も変更されます。これはAspose.Cells for Python via .NETでも動作し、ワークブックをXLSまたはXLSX形式で保存する場合問題ありません。ただし、PDFやHTML形式で保存する場合は、[**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value)メソッドを呼び出してリンクされたシェイプの値を更新する必要があります。

{{% /alert %}}

## 例

以下のスクリーンショットは、下記のサンプルコードで使用されているソースExcelファイルを示しています。このファイルにはセルA1からE4までにリンクされた画像があります。Aspose.Cells for Python via .NETを使用してセルB4の値を変更し、その後[**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value)メソッドを呼び出して画像の値を更新し、PDF形式で保存します。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

以下のリンクから、元のExcelファイルと出力されたPDFをダウンロードできます。

### リンクされた図形の値を更新するためのC＃コード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
