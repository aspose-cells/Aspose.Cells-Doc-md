---
title: Cell のリッチ テキストの一部にアクセスして更新する
linktitle: リッチ フォーマット テキスト
type: docs
weight: 40
url: /ja/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

Aspose.Cells では、セルのリッチ テキストの一部にアクセスして更新できます。この目的のために、使用できます[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)と[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッド。これらのメソッドは、次の配列を返し、受け入れます。[**フォント設定**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)フォント名、フォントの色、太さなど、フォントのさまざまなプロパティにアクセスして更新するために使用できるオブジェクト。

{{% /alert %}}

## **Cell のリッチ テキストの一部にアクセスして更新する**

次のコードは、[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)と[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)を使用した方法[ソースエクセルファイル](5112369.xlsx)提供されたリンクからダウンロードできます。ソースの Excel ファイルには、セル A1 にリッチ テキストがあります。 3 つの部分があり、各部分には異なるフォントがあります。次のコード スニペットは、これらの部分にアクセスし、最初の部分を新しいフォント名で更新します。最後に、ワークブックを次のように保存します。[出力エクセルファイル](5112366.xlsx).開くと、テキストの最初の部分のフォントが に変更されていることがわかります。**「アリエル」**.

### Cell のリッチ テキストの一部にアクセスして更新するための C# コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### サンプル コードによって生成されたコンソール出力

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

