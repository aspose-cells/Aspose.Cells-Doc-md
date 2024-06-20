---
title: ハイパーリンクタイプの検出
type: docs
weight: 160
url: /ja/python-net/detect-hyperlink-type/
description: Aspose.Cells for Python via .NET APIを使用してハイパーリンクのタイプを検出する方法について学びます。
keywords: Python Excel ライブラリ、Python ハイパーリンクタイプの検出、Python ハイパーリンクのタイプの検出、Python ハイパーリンクの種類の取得。
---

## **ハイパーリンクタイプの検出**

Excel ファイルには、外部、セル参照、ファイルパスなど、異なる種類のハイパーリンクが含まれている場合があります。Aspose.Cells for Python via .NET は、ハイパーリンクの種類を検出する機能をサポートしています。ハイパーリンクの種類は [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) 列挙型によって表されます。[**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) 列挙型には、次のメンバーがあります。

- EXTERNAL: 外部リンク
- FILE_PATH: ファイル/フォルダへのローカルおよび完全なパス。
- EMAIL: 電子メール
- CELL_REFERENCE: セルや名前付き範囲へのリンク。

ハイパーリンクのタイプを確認するには、[**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink)クラスには[**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/)プロパティがあり、戻り値の型は[**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype)です。次のコードスニペットは、この[**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/)プロパティの使用方法を示しています。

### ソースコード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

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
