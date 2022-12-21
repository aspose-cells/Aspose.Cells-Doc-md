---
title: 行または範囲のコピー中にチャートのデータ ソースを宛先ワークシートに変更する
type: docs
weight: 440
url: /ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **考えられる使用シナリオ**

グラフを含む行または範囲を新しいワークシートにコピーしても、グラフのデータ ソースは変更されません。たとえば、グラフのデータ ソースが =Sheet1!$A$1:$B$4 の場合、行または範囲を新しいワークシートにコピーした後、データ ソースは同じままになります (つまり、=Sheet1!$A$1:$B$4)。それはまだ古いワークシート、つまりSheet1を参照しています。これは、Microsoft Excel の動作でもあります。ただし、新しい宛先ワークシートを参照する場合は、[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)プロパティに設定し、**真実**を呼び出しながら[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法。宛先ワークシートが DestSheet の場合、グラフのデータ ソースは =Sheet1!$A$1:$B$4 から =DestSheet!$A$1:$B$4 に変更されます。

## **行または範囲のコピー中にチャートのデータ ソースを宛先ワークシートに変更する**

次のサンプル コードは、[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)プロパティを使用して、グラフを含む行または範囲を新しいワークシートにコピーします。コードは、[サンプルエクセルファイル](5113699.xlsx)を生成し、[出力エクセルファイル](5113697.xlsx).

![todo:画像_代替_文章](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
