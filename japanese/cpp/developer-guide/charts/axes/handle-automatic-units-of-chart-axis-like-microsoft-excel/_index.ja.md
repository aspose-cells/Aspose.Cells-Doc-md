---
title: Microsoft Excelのようにチャート軸の自動単位を管理する方法（C++）
linktitle: チャート軸の自動単位を管理する方法
description: Aspose.Cells for C++でチャート軸の自動単位を管理し、Microsoft Excelと同様に調整およびカスタマイズする方法を学びます。ガイドは、科学的表記の表示やスケール調整を含む設定例を示します。
keywords: Aspose.Cells for C++、チャート軸、自動単位、Microsoft Excel、設定、カスタマイズ、科学記数法、スケーリング。
type: docs
weight: 120
url: /ja/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **可能な使用シナリオ**
Aspose.Cellsの初期バージョンは、画像またはPDFとしてチャートをレンダリングする際にチャート軸の自動単位を適切に処理することができませんでした。現在、Aspose.Cellsはチャート軸の自動単位を処理するようになりました。コードの変更はありません。チャートを画像またはPDFに変換するだけで、Microsoft Excelがそれをレンダリングするようにチャート軸がレンダリングされます。

## **Microsoft Excelのようにチャートの軸の自動単位を処理する**
次のサンプルコードは、[サンプルExcelファイル](61767755.xlsx)をロードし、[出力PDFチャート](61767752.pdf)を生成します。スクリーンショットは、赤い四角でチャート軸の自動単位を示し、また、サンプルExcelファイルのチャートと出力PDFチャートを比較しています。両方が完全に同じです。

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **サンプルコード**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
