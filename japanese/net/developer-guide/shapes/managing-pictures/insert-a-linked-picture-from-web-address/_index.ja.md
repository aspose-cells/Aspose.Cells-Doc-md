---
title: Web アドレスからリンクされた画像を挿入する
type: docs
weight: 450
url: /ja/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Web (http://) からワークシートに画像を挿入する必要がある場合があります。これを行うには、画像の URL を指定すると、スプレッドシートが Microsoft Excel で開かれるたびに画像がダウンロードされます。画像は Excel ドキュメントに物理的に埋め込まれていませんが、Web リソースを指しています。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel (例: 2007):

1. クリック**入れる**メニューと選択**写真**.
1. [画像の挿入] ダイアログで、画像の Web アドレスを指定します。

## **Aspose.Cells for .NET を使用**

 Aspose.Cells for .NET は、[**ShapeCollection.AddLinkedPicture(int upperLeftRow、int upperLeftColumn、int heightPixels、int widthPixels、string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) .メソッドは[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。

次の例は、リンクされた画像を Web アドレスからワークシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
