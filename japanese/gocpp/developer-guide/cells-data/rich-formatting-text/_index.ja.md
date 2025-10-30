---
title: GolangをC++経由で使用してセルのリッチテキストの一部にアクセスおよび更新
linktitle: リッチフォーマットテキスト
type: docs
weight: 40
url: /ja/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for C++ APIを使ったセルのリッチテキスト部分のアクセスと更新の方法を学習します。
keywords: セルのリッチテキストへのアクセスおよび更新、セルのリッチテキストの取得、セルのリッチテキストの編集、セルのリッチテキストへのアクセス、セルのリッチテキストの更新、セルのリッチテキストの変更
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、セルのリッチテキストの部分にアクセスして更新することができます。このために、[**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/)および[**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)メソッドを使用することができます。これらのメソッドは、フォント名、フォント色、太字などのフォントのさまざまなプロパティにアクセスおよび更新するために使用できる[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)オブジェクトの配列を返し、受け入れます。

{{% /alert %}}

## **セルのリッチテキストの部分にアクセスして更新**

以下のコードは、[ソースExcelファイル](5112369.xlsx)を使用した[**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/)および[**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)メソッドの使用例を示しています。ソースExcelファイルのセルA1には3つの部分に分かれたリッチテキストがあり、それぞれ異なるフォントが設定されています。このコードはこれらの部分にアクセスし、最初の部分のフォントを**"Arial"**に更新します。修正したブックは[出力Excelファイル](5112366.xlsx)として保存されます。

### リッチテキスト部分にアクセスし更新するC++コード

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### サンプルコードによって生成されたコンソール出力

こちらは[ソースExcelファイル](5112369.xlsx)を使用したときのコンソール出力例です:

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
