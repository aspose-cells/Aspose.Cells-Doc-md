---
title: Golangを使用したC++でリンクされたOleオブジェクトの表示ラベルにアクセスおよび変更する
linktitle: リンクされたオブジェクトの表示ラベルへのアクセスと変更
type: docs
weight: 100
url: /ja/go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Aspose.Cells for C++を使用してExcelファイルのリンクされたOleオブジェクトの表示ラベルにアクセスおよび変更する方法を学ぶ。
---

## **可能な使用シナリオ**

Microsoft Excelでは、次のスクリーンショットのようにOleオブジェクトの表示ラベルを変更できます。Aspose.Cells APIの [**GetLabel()**](https://reference.aspose.com/cells/go-cpp/oleobject/getlabel/) と [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) メソッドを使用してOleオブジェクトの表示ラベルにアクセスまたは変更することも可能です。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **リンクされたオブジェクトの表示ラベルへのアクセスと変更**

次のサンプルコードを参照してください。Ole Objectを含む[sample Excel file](64716810.xlsx)を読み込みます。コードはOle Objectにアクセスし、そのラベルをサンプルAPIからAspose APIに変更します。下記のコンソール出力を参照してください。これはサンプルコードのサンプルExcelファイルへの効果を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessAndModifyTheDisplayLabelOfTheLinkedOleObject.go" >}}
## **コンソール出力**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
