---
title: セルのリッチテキストの一部をアクセスして更新する
linktitle: リッチフォーマットテキスト
type: docs
weight: 440
url: /ja/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用すると、セルのリッチテキストの一部にアクセスして更新することができます。そのために、Cell.getCharacters()およびCell.setCharacters()メソッドを使用できます。これらのメソッドは、フォント名、フォントカラー、太字などのフォントのさまざまなプロパティへのアクセスおよび更新に使用できるFontSettingオブジェクトの配列を返し、受け入れます。

{{% /alert %}} 
## **セルのリッチテキストの部分にアクセスして更新**
次のコードは、[提供されたリンク](5472937.xlsx)からダウンロードできるソースExcelファイルを使用して、Cell.getCharacters()およびCell.setCharacters()メソッドの使用方法を示しています。ソースExcelファイルにはセルA1にリッチテキストが含まれており、3つの部分があり、それぞれ異なるフォントである場合があります。これらの部分にアクセスして最初の部分を新しいフォント名で更新します。最終的に、[出力Excelファイル](5472930.xlsx)としてワークブックを保存します。開くと、テキストの最初の部分のフォントが**"Arial"**に変更されていることがわかります。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **コンソール出力**
上記サンプルコードの[提供されたリンク](5472937.xlsx)を使用したコンソール出力はこちらです。

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
{{< app/cells/assistant language="java" >}}
