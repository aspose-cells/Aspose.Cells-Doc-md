---  
title: 行や範囲をコピーしながら、チャートのデータソースをコピー先のワークシートに変更します。  
description: Aspose.Cells for C++を使用して、行や範囲をコピーしながらチャートのデータソースを目的地のワークシートに変更する方法を学びます。ガイドでは、チャートのデータ範囲を更新し、それを目的地のワークシートにリンクさせる方法を示し、コピーされた行や範囲が正確に反映されることを保証します。  
keywords: Aspose.Cells for C++, チャート作成, データソース, 宛先ワークシート, 行, 範囲, コピー, 更新, データ範囲, リンク付け。  
type: docs  
weight: 440  
url: /ja/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **可能な使用シナリオ**

新しいワークシートにチャートを含む行や範囲をコピーすると、チャートのデータソースは変更されません。例えば、チャートのデータソースが =Sheet1!$A$1:$B$4 の場合、行や範囲を新しいワークシートにコピーした後も、データソースは同じ =Sheet1!$A$1:$B$4 のままで、古いシート（Sheet1）を参照し続けます。これはMicrosoft Excelでも同じ挙動です。ただし、宛先ワークシートを参照させたい場合は、[**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) プロパティを使用し、[**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/) メソッドを呼び出す際に **true** に設定してください。例えば、宛先ワークシートが DestSheet の場合、チャートのデータソースは =Sheet1!$A$1:$B$4 から =DestSheet!$A$1:$B$4 に変わります。

## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**

次のサンプルコードは、チャートを含む行や範囲を新しいワークシートにコピーする際に、[**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/)プロパティの使用例を示しています。このコードは[サンプルExcelファイル](5113699.xlsx)を使用し、[出力Excelファイル](5113697.xlsx)を生成します。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
