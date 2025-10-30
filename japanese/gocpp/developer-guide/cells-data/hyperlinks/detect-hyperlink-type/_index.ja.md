---
title: Golangを使用してC++経由でハイパーリンクの種類を検出します
linktitle: ハイパーリンクタイプの検出
type: docs
weight: 160
url: /ja/go-cpp/detect-hyperlink-type/
description: Aspose.Cells for C++ APIを使ってハイパーリンクタイプを検出する方法を学びます。
keywords: ハイパーリンクのタイプの検出、ハイパーリンクのタイプを検出、ハイパーリンクのタイプを取得
---

## **ハイパーリンクのタイプの検出**

Excelファイルには、外部リンク、セル参照、ファイルパスなど、異なるタイプのハイパーリンクがあります。Aspose.Cellsはハイパーリンクのタイプを検出する機能をサポートしています。ハイパーリンクのタイプは[**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)列挙型によって表されます。[**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)列挙型には以下のメンバーがあります。

- External: 外部リンク
- FilePath: ファイル/フォルダへのローカルな完全なパス
- Email: Email
- CellReference: セルや名前付き範囲へのリンク

ハイパーリンクのタイプを確認するには、[**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/)クラスには[**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/)プロパティがあり、戻り値の型は[**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)です。次のコードスニペットは、この[**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/)プロパティの使用方法を示しています。

### ソースコード

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
上記のコードスニペットによって生成された出力は以下の通りです。

コンソール出力
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
