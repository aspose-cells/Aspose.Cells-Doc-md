---
title: Webアドレスからリンクされた画像の挿入
type: docs
weight: 450
url: /ja/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

時々、ワークシートにWeb（http://）から画像を挿入する必要があります。これを行うには、画像のURLとして指定し、表計算がMicrosoft Excelで開かれるたびに画像がダウンロードされます。 画像は実際にはExcel文書に物理的に埋め込まれていませんが、Webリソースを指し示しています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（たとえば2007）で：

1. **挿入**メニューをクリックし、**画像**を選択します。
1. 挿入画像ダイアログで画像のWebアドレスを指定します。

## **Aspose.Cells for .NETを使用する**

Aspose.Cells for .NETは、[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture)を使用してリンクされた画像を追加する機能をサポートします。このメソッドは[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトを返します。

次の例は、ワークシートにWebアドレスからリンクされた画像を追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
