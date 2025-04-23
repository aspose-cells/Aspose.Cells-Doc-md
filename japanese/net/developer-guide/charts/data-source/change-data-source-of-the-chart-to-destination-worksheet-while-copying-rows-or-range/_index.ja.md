---
title: 行または範囲をコピーする際、チャートを新しいワークシートにコピーすると、チャートのデータソースは変更されません。
description: Aspose.Cells for .NETで行または範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更し、リンクさせる方法を学びます。コピーされた行または範囲がチャートで正確に反映されるよう、データ範囲を更新し、宛先ワークシートにリンクする方法を示すガイドです。
keywords: Aspose.Cells for .NET、チャート作成、データソース、宛先ワークシート、行、範囲、コピー、更新、データ範囲、リンク。
type: docs
weight: 440
url: /ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能な使用シナリオ**

チャートを含む行または範囲を新しいワークシートにコピーする場合、チャートのデータソースは変更されません。たとえば、チャートのデータソースが=Sheet1!$A$1:$B$4の場合、行または範囲を新しいワークシートにコピーした後も、データソースは=Sheet1!$A$1:$B$4のままです。これはMicrosoft Excelでも同様の動作です。ただし、新しい宛先ワークシートを参照するようにしたい場合は、[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)プロパティを使用して[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)メソッドを呼び出す際にそれを**true**に設定してください。たとえば、宛先ワークシートがDestSheetである場合、チャートのデータソースは=Sheet1!$A$1:$B$4から=DestSheet!$A$1:$B$4に変更されます。

## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**

次のサンプルコードは、チャートを含む行または範囲を新しいワークシートにコピーする際に[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) プロパティの使用方法を説明しています。コードは[サンプルExcelファイル](5113699.xlsx)を使用し、[出力Excelファイル](5113697.xlsx)を生成します。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
