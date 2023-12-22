---
title: Cell のリッチ テキストの部分にアクセスして更新する
linktitle: リッチフォーマットのテキスト
type: docs
weight: 40
url: /ja/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Cell から Aspose.Cells for .NET API までのリッチ テキストの部分にアクセスして更新する方法を学習します。
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---
{{% alert color="primary" %}}

 Aspose.Cells を使用すると、セルのリッチ テキストの部分にアクセスして更新できます。この目的のために、次を使用できます[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)そして[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッド。これらのメソッドは、次の配列を返し、受け入れます。[**フォント設定**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)フォント名、フォントの色、太さなど、フォントのさまざまなプロパティにアクセスして更新するために使用できるオブジェクト。

{{% /alert %}}

##  **Cell のリッチ テキストの部分にアクセスして更新する**

次のコードは、の使用法を示しています。[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)そして[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)を使用した方法[ソースエクセルファイル](5112369.xlsx)提供されたリンクからダウンロードできます。ソース Excel ファイルのセル A1 にはリッチ テキストが含まれています。 3 つの部分に分かれており、各部分には異なるフォントが付いています。次のコード スニペットは、これらの部分にアクセスし、最初の部分を新しいフォント名で更新します。最後に、ワークブックを次のように保存します。[Excelファイルを出力する](5112366.xlsx)。これを開くと、テキストの最初の部分のフォントが *"Arial"** に変更されていることがわかります。

###  C# のリッチ テキストの部分にアクセスして更新するためのコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### サンプルコードによって生成されたコンソール出力

以下は、上記のサンプル コードを使用したコンソール出力です。[ソースエクセルファイル](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

