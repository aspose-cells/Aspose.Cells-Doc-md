---
title: Web アドレスからリンクされた画像を挿入する
type: docs
weight: 50
url: /ja/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Web (http://) からワークシートに画像を挿入する必要がある場合があります。これを行うには、画像の URL を指定すると、スプレッドシートが Microsoft Excel で開かれるたびに画像がダウンロードされます。画像は Excel ドキュメントに物理的に埋め込まれていませんが、Web リソースを指しています。

{{% /alert %}}

## **Web アドレスからリンクされた画像を挿入する**

### **Microsoft エクセルを使う**

Microsoft Excel (例: 2007):

1. クリック**入れる**メニューと選択**写真**.

![todo:画像_代替_文章](insert-a-linked-picture-from-web-address_1.png)

1. [画像の挿入] ダイアログで、画像の Web アドレスを指定します。

![todo:画像_代替_文章](insert-a-linked-picture-from-web-address_2.png)

画像が挿入されます。

![todo:画像_代替_文章](insert-a-linked-picture-from-web-address_3.png)

### **Aspose.Cells for Java を使用**

 Aspose.Cells for Java は、メソッドを使用したリンクされた画像の追加をサポートしています[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int 高さ, int 幅, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

メソッドは[**写真**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)物体。

次の例は、リンクされた画像を Web アドレスからワークシートに追加する方法を示しています。

コードを実行すると、生成された Excel ファイルの最初のワークシートにリンクされた画像が含まれます。

**出力ファイル** 

![todo:画像_代替_文章](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
