---
title: 行または範囲をコピーする際、チャートを新しいワークシートにコピーすると、チャートのデータソースは変更されません。
description: Aspose.Cells for Python via .NET で行や範囲をコピーしながらチャートのデータソースを別のワークシートに変更する方法を学びましょう。 チャートのデータ範囲を更新し、それを宛先のワークシートにリンクさせる方法を説明し、コピーした行や範囲が正確に反映されるようにします。
keywords: Aspose.Cells for Python via .NET、グラフ作成、データソース、宛先のワークシート、行、範囲、コピー、更新、データ範囲、リンク。
type: docs
weight: 440
url: /ja/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能な使用シナリオ**

チャートを含む行または範囲を新しいワークシートにコピーする場合、チャートのデータソースは変更されません。たとえば、チャートのデータソースが=Sheet1!$A$1:$B$4の場合、行または範囲を新しいワークシートにコピーした後も、データソースは=Sheet1!$A$1:$B$4のままです。これはMicrosoft Excelでも同様の動作です。ただし、新しい宛先ワークシートを参照するようにしたい場合は、[**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet)プロパティを使用して[**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows)メソッドを呼び出す際にそれを**true**に設定してください。たとえば、宛先ワークシートがDestSheetである場合、チャートのデータソースは=Sheet1!$A$1:$B$4から=DestSheet!$A$1:$B$4に変更されます。

## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**

次のサンプルコードは、チャートを含む行または範囲を新しいワークシートにコピーする際に[**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) プロパティの使用方法を説明しています。コードは[サンプルExcelファイル](5113699.xlsx)を使用し、[出力Excelファイル](5113697.xlsx)を生成します。

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
