---
title: ハイパーリンクの種類の検出
type: docs
weight: 160
url: /ja/net/detect-hyperlink-type/
description: Aspose.Cells for .NET API を通じてハイパーリンク タイプを検出する方法を学習します。
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **ハイパーリンクの種類の検出**

Excel ファイルには、外部リンク、セル参照、ファイル パスなどのさまざまなタイプのハイパーリンクを含めることができます。Aspose.Cells は、ハイパーリンクのタイプを検出する機能をサポートしています。ハイパーリンクの種類は次のように表されます。[**ターゲットモードタイプ**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)列挙。の[**ターゲットモードタイプ**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Enumeration には次のメンバーがあります。

- 外部: 外部リンク
- FilePath: ファイル/フォルダーへのローカルおよびフルパス。
- 電子メール: 電子メール
- CellReference: セルまたは名前付き範囲へのリンク。

ハイパーリンクの種類を確認するには、[**ハイパーリンク**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink)クラスが提供するのは[**リンクタイプ**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)戻り値の型が次のプロパティ[**ターゲットモードタイプ**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)。次のコード スニペットは、[**リンクタイプ**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)これを使用してプロパティを[ソースエクセルファイル](94896195.xlsx).

### ソースコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

以下は、上記のコード スニペットによって生成された出力です。

### コンソール出力
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
