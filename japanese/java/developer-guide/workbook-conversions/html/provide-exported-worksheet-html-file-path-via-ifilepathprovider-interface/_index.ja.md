---
title: IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する
type: docs
weight: 870
url: /ja/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能な使用シナリオ**
例えば、複数のシートを持つエクセルファイルがあり、それぞれのシートを個別のHTMLファイルにエクスポートしたいとします。もし、いくつかのシートに他のシートへのリンクがある場合、そのリンクはエクスポートされたHTMLでは壊れた状態になります。この問題に対処するために、Aspose.Cellsは[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider) インターフェースを提供しており、これを実装して壊れたリンクを修正できます。
## **IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する**
以下のコードで使用された[サンプルエクセルファイル](5473417.zip)とそのエクスポートされたHTMLファイルをダウンロードしてください。これらのファイルはすべて*Temp*ディレクトリ内にあります。それらを*C:*ドライブに解凍すれば*C:\Temp*ディレクトリになります。その後、ブラウザで*Sheet1.html*ファイルを開き、それに含まれるリンクをクリックしてください。これらのリンクは*Sheet1.html*内にあるこれらの2つのエクスポートされたHTMLワークシートを参照しています。これらのワークシートは*C:\Temp\OtherSheets*ディレクトリ内にあります。

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下のスクリーンショットは*C:\Temp\Sheet1.html*とそのリンクの外観を示しています

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下のスクリーンショットはHTMLソースを示しています。リンクが*C:\Temp\OtherSheets*ディレクトリを参照するように修正されたことがわかります。これは[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider) インターフェースを使用して達成されました。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **サンプルコード**
注意：*C:\Temp*ディレクトリはイメージです。実行する前に、好きなディレクトリを使用し、[サンプルエクセルファイル](5473414.xlsx)をそのディレクトリに配置し、提供されたサンプルコード内の*dirPath*変数を変更し、実行してください。それにより、指定したディレクトリ内に*OtherSheets*サブディレクトリが作成され、その中に2番目と3番目のワークシートのHTMLがエクスポートされます。

{{% alert color="primary" %}} 

提供されたサンプルコードはAspose.Cellsライセンスを設定したときのみ動作します。ライセンスを設定せずにコードを実行しようとすると、無限ループに入ります。そのため、ライセンスが設定されていない場合にはメッセージを表示して実行を停止するチェックが追加されています。ライセンスを購入するか、Aspose.Purchaseチームから30日間の仮ライセンスをリクエストできます。

{{% /alert %}} 

これらの行のコメントアウトを解除すると、*Sheet1.html*のリンクが壊れ、*Sheet2.html*または*Sheet3.html*を*Sheet1.html*内のリンクをクリックしても開くことができなくなります



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



提供された[サンプルエクセルファイル](5473414.xlsx)を使用して、以下の完全なサンプルコードを実行できます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
