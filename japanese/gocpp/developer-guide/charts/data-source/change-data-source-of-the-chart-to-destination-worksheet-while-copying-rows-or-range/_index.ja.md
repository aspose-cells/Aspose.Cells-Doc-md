---  
title: GolangからC++を使って、行や範囲をコピーしながらチャートのデータソースを宛先ワークシートに変更する  
description: Aspose.Cells for C++を使用して、行や範囲をコピーしながらチャートのデータソースを目的地のワークシートに変更する方法を学びます。ガイドでは、チャートのデータ範囲を更新し、それを目的地のワークシートにリンクさせる方法を示し、コピーされた行や範囲が正確に反映されることを保証します。  
keywords: Aspose.Cells for C++, チャート作成, データソース, 宛先ワークシート, 行, 範囲, コピー, 更新, データ範囲, リンク付け。  
type: docs  
weight: 440  
url: /ja/go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **可能な使用シナリオ**

新しいワークシートにチャートを含む行や範囲をコピーすると、チャートのデータソースは変更されません。例えば、チャートのデータソースが =Sheet1!$A$1:$B$4 の場合、行や範囲を新しいワークシートにコピーした後も、データソースは同じ =Sheet1!$A$1:$B$4 のままで、古いシート（Sheet1）を参照し続けます。これはMicrosoft Excelでも同じ挙動です。ただし、宛先ワークシートを参照させたい場合は、[**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) プロパティを使用し、[**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/) メソッドを呼び出す際に **true** に設定してください。例えば、宛先ワークシートが DestSheet の場合、チャートのデータソースは =Sheet1!$A$1:$B$4 から =DestSheet!$A$1:$B$4 に変わります。

## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**

次のサンプルコードは、チャートを含む行や範囲を新しいワークシートにコピーする際に、[**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/)プロパティの使用例を示しています。このコードは[サンプルExcelファイル](5113699.xlsx)を使用し、[出力Excelファイル](5113697.xlsx)を生成します。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}
