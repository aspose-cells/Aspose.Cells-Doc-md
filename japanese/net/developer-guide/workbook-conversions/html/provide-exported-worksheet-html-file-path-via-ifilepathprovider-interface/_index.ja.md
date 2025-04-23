---
title: IFilePathProviderインターフェースを介してエクスポートされたワークシートのhtmlファイルパスを提供します。
type: docs
weight: 70
url: /ja/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能な使用シナリオ**
複数のシートを持つエクセルファイルがあるとし、各シートを個別のHTMLファイルにエクスポートしたいとします。いくつかのシートが他のシートへのリンクを持っている場合、そのリンクはエクスポートしたHTMLで壊れてしまいます。この問題に対処するために、Aspose.Cellsは[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)インターフェースを提供し、壊れたリンクを修正するために実装することができます。
## **IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する**
以下のコードで使用される[サンプルエクセルファイル](5115213.zip)およびそのエクスポートされたHTMLファイルをダウンロードしてください。これらのファイルはすべてTempディレクトリ内にあります。これをC:ドライブ上に解凍する必要があります。その後、C:\Tempディレクトリになります。その後、ブラウザでSheet1.htmlを開き、その中の2つのリンクをクリックしてください。これらのリンクは、C:\Temp\OtherSheetsディレクトリ内にある2つのエクスポートHTMLワークシートを参照しています。

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

次のスクリーンショットは、C:\Temp\Sheet1.htmlおよびそのリンクの外観を示しています。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

次のスクリーンショットはHTMLソースを示しています。リンクがC:\Temp\OtherSheetsディレクトリを参照していることがわかります。これは[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)インターフェースを使用して達成されました。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **サンプルコード**
C:\Tempディレクトリはイラストレーション目的のみです。任意のディレクトリを使用し、提供されたサンプルコードを実行することができます。それから、提供されたサンプルコード内のdirPath変数を変更し、実行前に自分の選択したディレクトリを参照してください。

{{% alert color="primary" %}} 

提供されたサンプルコードはAspose.Cellsライセンスを設定したときのみ動作します。ライセンスを設定せずにコードを実行しようとすると、無限ループに入ります。そのため、ライセンスが設定されていない場合にはメッセージを表示して実行を停止するチェックが追加されています。ライセンスを購入するか、Aspose.Purchaseチームから30日間の仮ライセンスをリクエストできます。

{{% /alert %}} 

このコード内のコメントアウトされた行を見ると、Sheet1.htmlのリンクが壊れ、Sheet2.htmlまたはSheet3.htmlがSheet1.html内のリンクがクリックされても開かなくなります。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



提供された[サンプルエクセルファイル](5115211.xlsx)で実行できる完全なサンプルコードはこちらです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
