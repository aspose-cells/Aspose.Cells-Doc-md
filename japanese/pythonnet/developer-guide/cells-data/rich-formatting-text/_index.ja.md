---
title: セルのリッチテキストの一部をアクセスして更新する
linktitle: リッチフォーマットテキスト
type: docs
weight: 40
url: /ja/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for Python via .NET API を使用して、セルのリッチテキストの部分をアクセスして更新する方法を学びます。
keywords: Python Excel ライブラリ、Python セルのリッチテキストへのアクセスと更新、Python セルのリッチテキストの取得、Python セルのリッチテキストの編集、Python セルのリッチテキストのアクセス、Python セルのリッチテキストの更新、Python セルのリッチテキストの変更。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET を使用すると、セルのリッチテキストの部分にアクセスして更新することができます。このために、[**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) と [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) のメソッドを使用できます。これらのメソッドは、フォント名、フォントカラー、太字などのフォントのさまざまなプロパティにアクセスして更新するために使用できる [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) オブジェクトの配列を返し、受け入れます。

{{% /alert %}}

## **セルのリッチテキストの部分にアクセスして更新**

次のコードは、[ソースエクセルファイル](5112369.xlsx) を使用して、[**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) と [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) の使用方法を示しています。ソースエクセルファイルには、セル A1 にリッチテキストが含まれています。3 つの部分に分かれ、それぞれ異なるフォントを使用しています。次のコードスニペットは、これらの部分にアクセスして最初の部分を新しいフォント名で更新します。最後に、ワークブックを[出力エクセルファイル](5112366.xlsx) として保存します。開くと、テキストの最初の部分のフォントが **"Arial"** に変更されていることがわかります。

### C# コードでセルのリッチテキストの部分にアクセスして更新する

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

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

