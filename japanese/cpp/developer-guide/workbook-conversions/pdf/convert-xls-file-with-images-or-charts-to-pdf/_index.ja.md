---
title: C++を使用して画像やチャートを含むXLSファイルをPDFに変換
linktitle: 画像やグラフが含まれる XLS ファイルを PDF ドキュメントに変換する
type: docs
weight: 50
url: /ja/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Aspose.CellsとC++を使用して、画像やチャートを含むXLSファイルをPDFドキュメントに変換します。
---

{{% alert color="primary" %}} 

Aspose.Cellsは、画像やチャートを含むXLSファイルをPDFドキュメントに変換することをサポートしています。Aspose.Cells for C++は、スプレッドシートのPDFへの変換を独立して行うことができます。Aspose.PDF for C++は変換には必要ありません。このプロセスはメモリ内で行われ、テンポラリーや中間XMLファイルに依存しません。これにより、大きなExcelファイル、例えば画像、チャート、その他の描画オブジェクトを含むものも迅速かつ効率的に変換できます。

{{% /alert %}} 
## **サンプルコード**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDFへレンダリングする直前に[Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/)メソッドを呼び出すのが最良です。これにより、数式依存の値が再計算され、正しい値がPDFに描画されます。

{{% /alert %}}
