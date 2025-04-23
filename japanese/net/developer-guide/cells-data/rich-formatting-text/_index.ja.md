---
title: セルのリッチテキストの一部をアクセスして更新する
linktitle: リッチフォーマットテキスト
type: docs
weight: 40
url: /ja/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for .NET APIを介してセルのリッチテキストの一部にアクセスおよび更新する方法を学びます。
keywords: セルのリッチテキストへのアクセスおよび更新、セルのリッチテキストの取得、セルのリッチテキストの編集、セルのリッチテキストへのアクセス、セルのリッチテキストの更新、セルのリッチテキストの変更
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、セルのリッチテキストの部分にアクセスして更新することができます。このために、[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)および[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッドを使用することができます。これらのメソッドは、フォント名、フォント色、太字などのフォントのさまざまなプロパティにアクセスおよび更新するために使用できる[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)オブジェクトの配列を返し、受け入れます。

{{% /alert %}}

## **セルのリッチテキストの部分にアクセスして更新**

以下のコードは、提供されたリンクからダウンロードできる[ソースのExcelファイル](5112369.xlsx)を使用して、[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)および[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッドの使用方法を示しています。ソースのExcelファイルには、セルA1にリッチテキストが含まれています。3つの部分があり、それぞれ異なるフォントを持っています。以下のコードスニペットは、これらの部分にアクセスして最初の部分のフォントを更新し、最終的にワークブックを[出力のExcelファイル](5112366.xlsx)として保存します。それを開くと、テキストの最初の部分のフォントが**"Arial"**に変更されていることがわかります。

### C# コードでセルのリッチテキストの部分にアクセスして更新する

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

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

{{< app/cells/assistant language="csharp" >}}
