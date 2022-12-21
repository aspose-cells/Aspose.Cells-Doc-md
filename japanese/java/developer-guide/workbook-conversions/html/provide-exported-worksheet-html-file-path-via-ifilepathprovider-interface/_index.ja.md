---
title: IFilePathProvider インターフェイスを介して、エクスポートされたワークシートの HTML ファイル パスを提供します
type: docs
weight: 870
url: /ja/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **考えられる使用シナリオ**
複数のシートを含む Excel ファイルがあり、各シートを個別の HTML ファイルにエクスポートするとします。シートに他のシートへのリンクがある場合、それらのリンクはエクスポートされた HTML で壊れます。この問題に対処するために、Aspose.Cells が提供します。[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)壊れたリンクを修正するために実装できるインターフェース。
## **IFilePathProvider インターフェイスを介して、エクスポートされたワークシートの HTML ファイル パスを提供します**
をダウンロードしてください[サンプルエクセルファイル](5473417.zip)次のコードとそのエクスポートされた HTML ファイルで使用されます。これらのファイルはすべて*温度*ディレクトリ。あなたはそれを抽出する必要があります*子：*ドライブ。それからそれはなるでしょう*C:\Temp*ディレクトリ。次に、*Sheet1.html*ファイルをブラウザーで開き、その中の 2 つのリンクをクリックします。これらのリンクは、*C:\Temp\OtherSheets*ディレクトリ。

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

次のスクリーンショットは、*C:\Temp\Sheet1.html*そしてそのリンクは次のようになります

![todo:画像_代替_文章](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

次のスクリーンショットは、HTML ソースを示しています。リンクが現在参照していることがわかります。*C:\Temp\OtherSheets*ディレクトリ。これは、[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)インターフェース。

![todo:画像_代替_文章](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **サンプルコード**
ご注意ください*C:\Temp*ディレクトリは、説明のみを目的としています。選択した場所の任意のディレクトリを使用できます[サンプルエクセルファイル](5473414.xlsx)その中で、提供されたサンプル コードを実行します。次に作成します*その他のシート*ディレクトリ内のサブディレクトリを作成し、その中の 2 番目と 3 番目のワークシート HTML をエクスポートします。を変更してください*dirPath*提供されたコード内の変数で、実行前に選択したディレクトリを参照します。

{{% alert color="primary" %}} 

サンプルコードは、Aspose.Cells ライセンスを設定した場合のみ動作します。ライセンスを設定せずにコードを実行しようとすると、無限ループに陥ります。そのため、ライセンスが設定されていない場合は、メッセージを出力して実行を停止するチェックを追加しました。ライセンスを購入するか、Aspose.Purchase チームから 30 日間の一時ライセンスを要求できます。

{{% /alert %}} 

コード内のこれらの行にコメントすると、リンクが壊れます。*Sheet1.html*と*Sheet2.html*また*Sheet3.html*内部でリンクをクリックしても開きません*Sheet1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



以下は、提供されたコマンドで実行できる完全なサンプル コードです。[サンプルエクセルファイル](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
