---
title: 画像の管理
type: docs
weight: 10
url: /ja/java/managing-pictures/
---

Aspose.Cellsを使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の位置を実行時に制御することができます。これについては後のセクションで詳しく説明します。

この記事では、画像の追加方法と特定のセルの内容を示す画像の挿入方法について説明します。

## **画像の追加**

スプレッドシートに画像を追加するのは非常に簡単です。わずかなコード行しか必要ありません。

単に[**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection)オブジェクトでカプセル化された[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)コレクションの[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-)メソッドを呼び出します。[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-)メソッドは以下のパラメータを取ります:

- **左上の行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **画像の位置づけ**

Aspose.Cellsを使用して画像を以下のように位置付けることができます:

- [絶対位置づけ](/cells/ja/java/managing-pictures/#absolute-positioning)。

### **絶対位置づけ**

開発者は[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX)オブジェクトの[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY)メソッドと[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)メソッドを使用して画像を絶対位置づけすることができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **高度なトピック**
- [Webアドレスからリンクされた画像の挿入](/cells/ja/java/insert-a-linked-picture-from-web-address/)
- [セル参照に基づいて画像を挿入](/cells/ja/java/insert-a-picture-based-on-cell-reference/)
- [URLからWeb画像をExcelワークシートに挿入](/cells/ja/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="java" >}}
