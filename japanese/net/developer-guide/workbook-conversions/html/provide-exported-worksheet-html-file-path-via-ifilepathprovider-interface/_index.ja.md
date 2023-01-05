---
title: IFilePathProvider インターフェイスを介して、エクスポートされたワークシートの html ファイル パスを提供します
type: docs
weight: 70
url: /ja/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **考えられる使用シナリオ**
複数のシートを含む Excel ファイルがあり、各シートを個別の HTML ファイルにエクスポートするとします。シートのいずれかに他のシートへのリンクがある場合、それらのリンクはエクスポートされた HTML で壊れます。この問題に対処するために、Aspose.Cells は[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)壊れたリンクを修正するために実装できるインターフェース。
## **エクスポートされたワークシート HTML ファイル パスを IFilePathProvider インターフェイス経由で提供します**
をダウンロードしてください[サンプルエクセルファイル](5115213.zip)次のコードとそのエクスポートされた HTML ファイルで使用されます。これらのファイルはすべて、Temp ディレクトリ内にあります。 C: ドライブに展開する必要があります。すると C:\Temp ディレクトリになります。次に、ブラウザで Sheet1.html ファイルを開き、その中の 2 つのリンクをクリックします。これらのリンクは、C:\Temp\OtherSheets ディレクトリ内にあるエクスポートされた 2 つの HTML ワークシートを参照しています。

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

次のスクリーンショットは、C:\Temp\Sheet1.html とそのリンクがどのように見えるかを示しています

![todo:画像_代替_文章](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

次のスクリーンショットは、HTML ソースを示しています。リンクが C:\Temp\OtherSheets ディレクトリを参照していることがわかります。これは、[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)インターフェース。

![todo:画像_代替_文章](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **サンプルコード**
 C:\Temp ディレクトリは説明のためだけのものであることに注意してください。選択した場所の任意のディレクトリを使用できます[サンプルエクセルファイル](5115211.xlsx)その中で、提供されたサンプル コードを実行します。次に、ディレクトリ内に OtherSheets サブディレクトリを作成し、その中に 2 番目と 3 番目のワークシート HTML をエクスポートします。提供されたコード内の dirPath 変数を変更し、実行前に選択したディレクトリを参照してください。

{{% alert color="primary" %}} 

サンプルコードは、Aspose.Cells ライセンスを設定した場合のみ動作します。ライセンスを設定せずにコードを実行しようとすると、無限ループに陥ります。そのため、ライセンスが設定されていない場合は、メッセージを出力して実行を停止するチェックを追加しました。ライセンスを購入するか、Aspose.Purchase チームから 30 日間の一時ライセンスを要求できます。

{{% /alert %}} 

コード内のこれらの行にコメントを付けると、Sheet1.html と Sheet2.html のリンクが破損するか、Sheet1.html 内でリンクがクリックされたときに Sheet3.html が開かないことを確認してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



以下は、提供されたコマンドで実行できる完全なサンプル コードです。[サンプルエクセルファイル](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
