---
title: セルのリッチテキストの一部をアクセスして更新する
linktitle: リッチフォーマットテキスト
type: docs
weight: 40
url: /ja/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: セルのリッチテキストの部分にアクセスし更新する方法をAspose.Cells for Node.js via C++ APIを使って学びます。
keywords: セルのリッチテキストへのアクセスおよび更新、セルのリッチテキストの取得、セルのリッチテキストの編集、セルのリッチテキストへのアクセス、セルのリッチテキストの更新、セルのリッチテキストの変更
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++を使えば、セルのリッチテキストの部分にアクセスし更新できます。このために [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) と [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) メソッドを使用します。これらのメソッドは、フォント名、フォントカラー、太字などのフォントのさまざまなプロパティにアクセスし更新できる [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) オブジェクトの配列を返し、受け入れます。

{{% /alert %}}

## **セルのリッチテキストの部分にアクセスして更新**

以下のコードは、提供されたリンクからダウンロードできる[元のExcelファイル](5112369.xlsx)を使用した[**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) と [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) のメソッドの使用例を示しています。元のエクセルファイルのセルA1にはリッチテキストがあります。これは3つの部分に分かれていて、それぞれ異なるフォントを持っています。以下のコードスニペットはこれらの部分にアクセスし、最初の部分のフォント名を新しいものに更新します。最後に、ワークブックを[出力Excelファイル](5112366.xlsx)として保存します。開くと最初の部分のフォントが「 Arial」に変更されているのがわかります。

### Nodejsを使ったセルのリッチテキスト部分のアクセスと更新のコード

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

### サンプルコードによって生成されたコンソール出力

以下は、[ソースエクセルファイル](5112369.xlsx) を使用して上記サンプルコードのコンソール出力です。

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

