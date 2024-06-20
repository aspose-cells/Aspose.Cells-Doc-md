---
title: ハイパーリンクタイプの検出
type: docs
weight: 160
url: /ja/net/detect-hyperlink-type/
description: Aspose.Cells for .NET APIを介してハイパーリンクのタイプを検出する方法を学ぶ
keywords: ハイパーリンクのタイプの検出、ハイパーリンクのタイプを検出、ハイパーリンクのタイプを取得
---

## **ハイパーリンクタイプの検出**

Excelファイルには、外部リンク、セル参照、ファイルパスなど、異なるタイプのハイパーリンクがあります。Aspose.Cellsはハイパーリンクのタイプを検出する機能をサポートしています。ハイパーリンクのタイプは[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)列挙型によって表されます。[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)列挙型には以下のメンバーがあります。

- External: 外部リンク
- FilePath: ファイル/フォルダへのローカルな完全なパス
- Email: Email
- CellReference: セルや名前付き範囲へのリンク

ハイパーリンクのタイプを確認するには、[**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink)クラスには[**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)プロパティがあり、戻り値の型は[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)です。次のコードスニペットは、この[**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)プロパティの使用方法を示しています。

### ソースコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

上記のコードスニペットによって生成された出力は以下の通りです。

コンソール出力
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
