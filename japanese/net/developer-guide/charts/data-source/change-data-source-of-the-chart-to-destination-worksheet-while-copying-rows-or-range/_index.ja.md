---
title: 行または範囲のコピー中にグラフのデータ ソースを宛先ワークシートに変更する
description: Aspose.Cells for .NET の行または範囲をコピーするときに、グラフのデータ ソースを宛先ワークシートに変更する方法を学びます。ガイドでは、グラフのデータ範囲を更新して宛先ワークシートにリンクする方法を説明します。範囲がチャートに正確に反映されます。
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **考えられる使用シナリオ**

グラフを含む行または範囲を新しいワークシートにコピーしても、グラフのデータ ソースは変更されません。たとえば、グラフのデータ ソースが =Sheet1!$A$1:$B$4 の場合、行または範囲を新しいワークシートにコピーした後、データ ソースは同じ =Sheet1!$A$1:$B$4 のままになります。まだ古いワークシート、つまり Sheet1 を参照しています。これは Microsoft Excel でも同様の動作です。ただし、新しい宛先ワークシートを参照したい場合は、[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)プロパティを設定して、**真実**電話をかけながら[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法。ここで、宛先ワークシートが DestSheet の場合、グラフのデータ ソースは =Sheet1!$A$1:$B$4 から =DestSheet!$A$1:$B$4 に変更されます。

##  **行または範囲のコピー中にグラフのデータ ソースを宛先ワークシートに変更する**

次のサンプルコードは、[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)プロパティを使用して、グラフを含む行または範囲を新しいワークシートにコピーします。コードでは、[サンプルエクセルファイル](5113699.xlsx)そして、[Excelファイルを出力する](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
