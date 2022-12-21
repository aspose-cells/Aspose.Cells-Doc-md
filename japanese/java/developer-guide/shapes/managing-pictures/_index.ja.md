---
title: 画像の管理
type: docs
weight: 10
url: /ja/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の配置は実行時に制御できます。これについては、以降のセクションで詳しく説明します。

Aspose.Cells for Java は、BMP、JPEG、PNG、GIF の画像形式のみをサポートします。

例で使用されるインデックスは 0 から始まります。

{{% /alert %}}

## **写真を追加する**

スプレッドシートに画像を追加するのはとても簡単です。数行のコードしか必要ありません。

単純に[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) の方法[**ピクチャー**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection)コレクション ([**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)物体）。の[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)メソッドは、次のパラメーターを取ります。

- **左上行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **写真の配置**

画像は、次のように Aspose.Cells を使用して配置できます。

- [絶対位置](/cells/ja/java/managing-pictures/#absolute-positioning).

### **絶対位置**

開発者は、[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX)と[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY)のメソッド[**写真**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)物体。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **先行トピック**
- [Web アドレスからリンクされた画像を挿入する](/cells/ja/java/insert-a-linked-picture-from-web-address/)
- [Cell 参照に基づいて画像を挿入する](/cells/ja/java/insert-a-picture-based-on-cell-reference/)
- [URL から Web 画像を Excel ワークシートに挿入する](/cells/ja/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
