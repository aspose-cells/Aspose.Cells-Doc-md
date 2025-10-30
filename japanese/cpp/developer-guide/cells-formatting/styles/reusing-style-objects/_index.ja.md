---
title: C++を使ったスタイルオブジェクトの再利用
linktitle: スタイルオブジェクトの再利用
description: Aspose.Cells for C++では、再利用可能なスタイルオブジェクトを作成して使用することで、スタイル管理を簡素化し、コード効率を向上させられます。ガイドは再利用可能なスタイルオブジェクトの利点を活用し、アプリケーションに実装する方法を示します。
keywords: Aspose.Cells for C++、スタイルオブジェクト再利用、スタイル管理、コード効率、再利用可能なスタイル、アプリケーション開発、APIリファレンス、サンプルコード、ダウンロード、サポート。
type: docs
weight: 3000
url: /ja/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

スタイルオブジェクトを再利用することでメモリを節約し、プログラムを高速化できます。

{{% /alert %}}

ワークシート内の大きな範囲のセルにフォーマットを適用するには:

1. スタイルオブジェクトを作成します。
1. 属性を指定します。
1. 範囲のセルにスタイルを適用します。

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

古い Cell.Style プロパティは不要なメモリを多く消費していたため、[**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) アプローチを使用するとメモリを大幅に削減でき、効率的です。これにより、Aspose.Cells 7.1.0 のリリースに伴い、古い Cell.Style プロパティが削除されました。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
