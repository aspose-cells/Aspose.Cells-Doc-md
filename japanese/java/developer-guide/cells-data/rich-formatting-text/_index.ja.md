---
title: Cell のリッチ テキストの一部にアクセスして更新する
linktitle: リッチ フォーマット テキスト
type: docs
weight: 440
url: /ja/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells では、セルのリッチ テキストの一部にアクセスして更新できます。この目的のために、Cell.getCharacters() および Cell.setCharacters() メソッドを使用できます。これらのメソッドは、フォント名、フォントの色、太さなどのフォントのさまざまなプロパティにアクセスして更新するために使用できる FontSetting オブジェクトの配列を返し、受け入れます。

{{% /alert %}} 
## **Cell のリッチ テキストの一部にアクセスして更新する**
次のコードは、[ソースエクセルファイル](5472937.xlsx)提供されたリンクからダウンロードできます。ソースの Excel ファイルには、セル A1 にリッチ テキストがあります。 3 つの部分があり、各部分は異なるフォントです。これらの部分にアクセスし、最初の部分を新しいフォント名で更新します。最後に、ワークブックを次のように保存します[出力エクセルファイル](5472930.xlsx).開くと、テキストの最初の部分のフォントが に変更されていることがわかります。**「アリエル」**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **コンソール出力**
以下は、上記のサンプル コードを使用したコンソール出力です。[ソースエクセルファイル](5472937.xlsx).

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
