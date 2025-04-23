---
title: ハイパーリンクタイプの検出
type: docs
weight: 160
url: /ja/nodejs-cpp/detect-hyperlink-type/
description: ## Aspose.Cells for Node.js via C++ APIを使ったハイパーリンクの種類の検出方法を学びます。
keywords: C++経由のNode.jsでハイパーリンクの種類を検出、C++経由のNode.jsでハイパーリンクのタイプを検出、C++経由でNode.jsのハイパーリンクのタイプを取得
---

## **ハイパーリンクのタイプの検出**

Excelファイルには外部リンク、セル参照、ファイルパスなどさまざまな種類のハイパーリンクが存在します。Aspose.Cells for Node.js via C++はハイパーリンクの種類を検出する機能をサポートしています。ハイパーリンクの種類は[**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype)列挙体で表され、[**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype)列挙体には次のメンバーがあります。

- 外部：外部リンク
- ファイルパス：ファイル/フォルダへのローカルおよび完全パス。
- Eメール：メールアドレス
- セル参照：セルまたは名前付き範囲へのリンク

ハイパーリンクの種類を確認するには、[**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink)クラスは[**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--)メソッドを提供しており、戻り値の型は[**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype)です。以下のコードスニペットは、[このExcelファイル](94896195.xlsx)を使って[**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--)メソッドの使用例を示しています。

### ソースコード

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


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
