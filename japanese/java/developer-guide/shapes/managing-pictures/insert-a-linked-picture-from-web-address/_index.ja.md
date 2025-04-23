---
title: Webアドレスからリンクされた画像の挿入
type: docs
weight: 50
url: /ja/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

時々、ワークシートにWeb（http://）から画像を挿入する必要があります。これを行うには、画像のURLとして指定し、表計算がMicrosoft Excelで開かれるたびに画像がダウンロードされます。 画像は実際にはExcel文書に物理的に埋め込まれていませんが、Webリソースを指し示しています。

{{% /alert %}}

## **Webアドレスからリンクされた画像の挿入**

### **Microsoft Excel の使用**

Microsoft Excel（たとえば2007）で：

1. **挿入**メニューをクリックし、**画像**を選択します。

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. 挿入画像ダイアログで画像のWebアドレスを指定します。 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

画像が挿入されます。

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Aspose.Cells for Javaを使用する**

Aspose.Cells for Javaは、[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture-int-int-int-int-java.lang.String-)を使用してリンクされた画像を追加することをサポートしています。

このメソッドは[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)オブジェクトを返します。

次の例は、ワークシートにWebアドレスからリンクされた画像を追加する方法を示しています。

コードを実行した後、生成されたExcelファイルには、最初のワークシートにリンクされた画像が含まれます。

**出力ファイル** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
{{< app/cells/assistant language="java" >}}
