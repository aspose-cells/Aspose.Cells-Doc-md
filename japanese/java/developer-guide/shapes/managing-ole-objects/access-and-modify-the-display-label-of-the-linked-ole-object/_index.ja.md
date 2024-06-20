---
title: リンクされたオブジェクトの表示ラベルへのアクセスと変更
type: docs
weight: 100
url: /ja/java/access-and-modify-the-display-label-of-the-linked-ole-object/
---

## **可能な使用シナリオ**

Microsoft Excelではスクリーンショットのようにリンクされたオブジェクトの表示ラベルを変更できます。Aspose.Cells APIを使用してリンクされたオブジェクトの表示ラベルにアクセスまたは変更することもできます。[**OleObject.Label**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#Label)プロパティを使用してください。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **リンクされたオブジェクトの表示ラベルへのアクセスと変更**

次のサンプルコードでは、リンクされたオブジェクトを含む[sample Excel file](64716833.xlsx)をロードします。このコードでは、Oleオブジェクトにアクセスし、そのラベルを「Sample APIs」から「Aspose APIs」に変更します。以下に示されているコンソール出力を参照してください。これはサンプルエクセルファイルに対するサンプルコードの影響を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-AccessAndModifyLabelOfOleObject.java" >}}

## **コンソール出力**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
