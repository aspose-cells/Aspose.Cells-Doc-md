---
title: Webアドレスからリンクされた画像の挿入
type: docs
weight: 450
url: /ja/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

時々、ワークシートにWeb（http://）から画像を挿入する必要があります。これを行うには、画像のURLとして指定し、表計算がMicrosoft Excelで開かれるたびに画像がダウンロードされます。 画像は実際にはExcel文書に物理的に埋め込まれていませんが、Webリソースを指し示しています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（たとえば2007）で：

1. **挿入**メニューをクリックし、**画像**を選択します。
1. 挿入画像ダイアログで画像のWebアドレスを指定します。

## **Aspose.Cells for Python via .NETを使用して**

Aspose.Cells for Python via .NETは、[**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture)を使用してリンクされた画像を追加できます。このメソッドは[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)オブジェクトを返します。

次の例は、ワークシートにWebアドレスからリンクされた画像を追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
