---
title: ページ設定と印刷オプション（C++）
linktitle: ページ設定および印刷オプション
type: docs
weight: 60
url: /ja/cpp/page-setup-and-printing-options/
description: Aspose.Cellsを使用してページ設定と印刷設定を構成し、印刷プロセスを制御します（C++）。
---

{{% alert color="primary" %}}

開発者は、印刷プロセスを制御するためにページ設定と印刷設定を構成する必要があります。Aspose.Cellsではページ設定と印刷設定を制御するためのさまざまなオプションがサポートされています。

この記事は、Visual Studioでコンソールアプリケーションを作成し、少ないコードでページ設定と印刷オプションをワークシートに適用する方法を示しています。

{{% /alert %}}

## **ページ設定および印刷設定の操作**

この例では、Microsoft Excelでワークブックを作成し、Aspose.Cellsを使用してページ設定と印刷オプションを設定しました。

### **Aspose.Cellsを使用してページ設定オプションを設定する**

まず、Microsoft Excelで簡単なワークシートを作成します。次に、ページ設定オプションを適用します。コードを実行すると、以下のスクリーンショットのようにページ設定オプションが変更されます。

|**出力ファイル。**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Microsoft Excelのワークシートにいくつかのデータを作成します。
   1. Microsoft Excelで新しいブックを開きます。
   1. いくつかのデータを追加します。
1. ページ設定オプションを設定します。
   ファイルにページ設定オプションを適用します。以下は、新しいオプションが適用される前のデフォルトオプションのスクリーンショットです。

|**デフォルトのページ設定オプション。**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [ダウンロード](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++。
   1. 開発コンピュータにインストールします。
      すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。
1. プロジェクトを作成します。
   1. Visual Studioを開始します。
   1. 新しいコンソールアプリケーションを作成します。
      この例はC++のコンソールアプリケーションを示します。
1. 参照を追加します。
   1. この例ではAspose.Cellsを使用するため、プロジェクトにそのコンポーネントへの参照を追加します。例：
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. APIを呼び出すアプリケーションを記述します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **印刷オプションの設定**

ページ設定設定には、ワークシートページの印刷方法を制御するいくつかの印刷オプション（シートオプションとも呼ばれる）も提供されます。これにより、ユーザーは次のような操作ができます。

- ワークシートの特定の印刷エリアを選択します。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

次の例では、上記の例（PageSetup.xls）で作成されたファイルに印刷オプションを適用します。以下のスクリーンショットは、新しいオプションが適用される前のデフォルトの印刷オプションを示しています。

|**入力ドキュメント**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
コードを実行すると、印刷オプションが変更されます。

|**出力ファイル**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
