---
title: DataView を GridWeb にインポートする
type: docs
weight: 60
url: /ja/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Microsoft .NET フレームワークのリリースにより、データを格納する新しい方法が導入されました。現在、オフライン モードでデータを保存する DataSet、DataTable、および DataView オブジェクト。これらのオブジェクトは、データ リポジトリとして非常に便利です。 Aspose.Cells.GridWeb を使用すると、DataTable または DataView オブジェクトからワークシートにデータをインポートできます。 Aspose.Cells.GridWeb は、DataView からのデータのインポートのみをサポートします。オブジェクトですが、DataTable オブジェクトは間接的に使用することもできます。この機能について詳しく説明しましょう。

{{% /alert %}} 
## **DataView からのデータのインポート**
GridWeb コントロールで GridWorsheetCollection の ImportDataView メソッドを使用して、DataView オブジェクトからデータをインポートします。データのインポート元の DataView オブジェクトを ImportDataView メソッドに渡します。インポート中に列ヘッダーとデータ スタイルを指定できます。

{{% alert color="primary" %}} 

データが DataView オブジェクトからインポートされると、インポートされたデータを保持するために新しいワークシートが作成されます。ワークシートには、DataTable と同じ名前が付けられます。

{{% /alert %}} 

**出力: DataView から新しいワークシートにインポートされたデータ** 

![todo:画像_代替_文章](import-dataview-to-gridweb_1.png)

列の幅は、列に含まれるすべてのデータが表示されるように調整されます。データが DataView からインポートされるとき、列幅は自動的に調整されません。ユーザーが自分で調整する必要があります。プログラムで列幅を調整するには、次を参照してください。[行と列のサイズ変更](/cells/ja/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataView メソッドのオーバーロード バージョンを使用すると、開発者は、インポートされたデータを保持するシートの名前と、DataView オブジェクトからインポートする特定の数の行と列を指定できます。

{{% /alert %}}
