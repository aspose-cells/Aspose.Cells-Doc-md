---
title: Webアドレスからリンク画像を挿入する方法をGo言語とC++を経由して学ぶ
linktitle: Webアドレスからリンクされた画像の挿入
type: docs
weight: 450
url: /ja/go-cpp/insert-a-linked-picture-from-web-address/
description: Aspose.Cells for C++を使用して、Webアドレスからリンクされた画像をワークシートに挿入する方法を学びます。
---

{{% alert color="primary" %}}

時々、ワークシートにWeb（http://）から画像を挿入する必要があります。これを行うには、画像のURLとして指定し、表計算がMicrosoft Excelで開かれるたびに画像がダウンロードされます。 画像は実際にはExcel文書に物理的に埋め込まれていませんが、Webリソースを指し示しています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（たとえば2007）で：

1. **挿入**メニューをクリックし、**画像**を選択します。
1. 挿入画像ダイアログで画像のWebアドレスを指定します。

## **Aspose.Cells for C++を使用した例**

Aspose.Cells for C++は、[**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/)メソッドを使用してリンクされた画像を追加することをサポートします。このメソッドは[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)オブジェクトを返します。

以下の例では、Webアドレスからリンクされた画像をワークシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
