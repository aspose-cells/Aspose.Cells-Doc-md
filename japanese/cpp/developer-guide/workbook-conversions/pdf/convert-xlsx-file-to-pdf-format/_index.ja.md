---
title: C++でXLSXファイルをPDF形式に変換する方法を学ぶ。
linktitle: XLSX ファイルを PDF フォーマットに変換する
type: docs
weight: 30
url: /ja/cpp/convert-xlsx-file-to-pdf-format/
description: Aspose.Cells for C++を使用してExcelファイルを高精度・高忠実度でPDFに変換する方法を学ぶ。
---

{{% alert color="primary" %}}

PDF（ポータブルドキュメントフォーマット）は、作成に使用されたソフトウェア、ハードウェア、オペレーティングシステムとは関係なくドキュメントを表します。PDFファイルは、テキスト、グラフィックス、画像の任意の組み合わせをデバイス非依存かつ解像度非依存の方式で含むことができます。PDFファイルは圧縮されていることが多く、元のファイルより容量が小さくなります。

Microsoft ExcelファイルをPDFに変換する必要がある場合、迅速で安全、正確で信頼性の高いソリューションが必要です。これにより、世界中にPDFドキュメントを配布できます。このタスクを実行できる多くの変換ツールがありますが、元のExcelドキュメントのレイアウトが出力されるPDFに正確に保持されていることを確認する必要があります。画像、チャート、シェイプ、データの書式設定、フォント、属性、色、ページ設定、テキストの向き、境界線、チャートなどが正確に再現される必要があります。 [Aspose.Cells](https://products.aspose.com/cells/cpp/)は高忠実度の変換を保証します。

このドキュメントは、画像、チャート、書式設定などを含むMicrosoft ExcelドキュメントのPDFへの変換方法について包括的に理解できるように設計されています。そのために、C++でExcelファイルをPDFに変換するシンプルなコンソールアプリケーションの作成方法を示しています。高精度、高忠実度の変換を行います。

{{% /alert %}}

## **ExcelをPDFに変換する**

この例では、テンプレートとしてExcelファイル（SampleInput.xlsx）を使用しています。ワークブックにはチャートと画像が含まれたシートがあります。各シートにはフォント、属性、色、シェーディング効果、境界線を使用したさまざまな書式があります。最初のシートには縦列チャート、最後には画像があります。

### **テンプレートの Excel ファイル**

テンプレートファイルには、チャートと画像を含む3つのシートがあります。最初のシートはチャートを持ち、最後のシートには画像があります。スクリーンショットは以下の通りです。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|

### **変換プロセス**

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、[Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)メソッドをPDFにレンダリングする直前に呼び出すのが最良です。これにより、数式に依存した値が再計算され、正しい値がPDFに描画されます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーションディレクトリのFilesフォルダにPDFファイルが作成されます。
以下のスクリーンショットは、PDFページを示しています。ヘッダーとフッターも出力されたPDFファイルに保持されていることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|
{{< app/cells/assistant language="cpp" >}}
