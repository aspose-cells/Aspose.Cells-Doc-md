---
title: GridWebにDataViewをインポート
type: docs
weight: 60
url: /ja/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb、インポート
description: この記事では、GridWeb内のデータをインポートする方法について紹介しています。
---

{{% alert color="primary" %}} 

Microsoft .NET Frameworkのリリースに伴い、データの新しい格納方法が導入されました。 DataSet、DataTable、DataViewオブジェクトは、オフラインモードでデータを格納するようになりました。 これらのオブジェクトは、データのリポジトリとして非常に便利です。 Aspose.Cells.GridWebを使用すると、DataTableまたはDataViewオブジェクトからワークシートにデータをインポートできます。 Aspose.Cells.GridWebはDataViewオブジェクトからのデータのインポートのみをサポートしますが、DataTableオブジェクトも間接的に使用できます。 この機能について詳しく説明します。

{{% /alert %}} 
## **DataViewからのデータのインポート**
GridWebコントロールのGridWorsheetCollectionのImportDataViewメソッドを使用してDataViewオブジェクトからデータをインポートします。 ImportDataViewメソッドに、データをインポートしたいDataViewオブジェクトを渡します。 インポート時に列ヘッダーとデータスタイルを指定することが可能です。

{{% alert color="primary" %}} 

DataViewオブジェクトからデータをインポートすると、インポートされたデータを保持する新しいワークシートが作成されます。 ワークシートの名前はDataTableと同じです。

{{% /alert %}} 

**出力：DataViewから新しいワークシートにインポートされたデータ** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

列の幅は、それらが含むすべてのデータを表示するように調整されます。 DataViewからデータをインポートすると、列の幅は自動的に調整されません。 ユーザーは自分で調整する必要があります。 列の幅をプログラムで調整するには、[行と列のサイズ変更](/cells/ja/net/aspose-cells-gridweb/resize-rows-and-columns/)を参照してください。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataViewメソッドのオーバーロードバージョンを使用すると、インポートされたデータを保持するシートの名前とDataViewオブジェクトからインポートする行数と列数を指定することができます。

{{% /alert %}}
