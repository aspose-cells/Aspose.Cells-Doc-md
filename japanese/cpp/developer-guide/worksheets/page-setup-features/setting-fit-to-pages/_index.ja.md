---
title: C++でExcelをフィットページの幅と高さで印刷する方法
linktitle: Excelを縮小ページ幅と高さに印刷するにはどうすればよいですか
type: docs
weight: 200
url: /ja/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: この記事では、C++のAspose.Cellsライブラリを使用して、FitToPagesWideとFitToPagesTallを設定する方法についてコード例を示します。
keywords: C++でFitToPagesWideとFitToPagesTallを設定する方法、FitToPagesWideとFitToPagesTallをC++で追加する方法、ExcelでFitToPagesWideとFitToPagesTallを設定・クリアする方法、Excelをフィットページの幅と高さで印刷する方法、ワークシートを1ページに印刷する方法、すべての列を1ページに印刷する方法。
---

## **紹介**

 FitToPagesWideとFitToPagesTallの設定は、Microsoft Excelなどのスプレッドシートアプリケーションで、印刷時にスプレッドシートの縮尺を制御するために使用されます。これらの設定は、印刷結果が指定したページ数内に収まるように、横方向と縦方向の両方でスケーリングを行います。各設定の詳細は以下の通りです：

1. FitToPagesWide：この設定は、印刷出力が何ページの横幅に収まるべきかを指定します。たとえば、FitToPagesWideを1に設定すると、内容は1ページ幅に収まるように縮尺されます。
1. FitToPagesTall：この設定は、印刷出力が何ページの高さに収まるべきかを指定します。たとえば、FitToPagesTallを1に設定すると、内容は1ページの高さに収まるように縮尺されます。

## **FitToPagesWide と FitToPagesTall を使用する理由**
FitToPagesWideとFitToPagesTallを設定する理由は次の通りです：
1. 印刷レイアウトの制御：横と縦のページ数を指定することで、印刷された文書が見やすく整理された状態になるように保証できます。列や行がページ間で不自然に切れることも避けられます。
1. 一貫性：複数のシートやレポートを印刷する場合、これらの設定を使用すると一貫したフォーマットを維持でき、印刷されたドキュメントの比較や分析が容易になります。
1. プロフェッショナルなプレゼンテーション：内容を適切に縮尺してページ数に合わせることで、より洗練されたプレゼンテーションに仕上げることができます。

## **Excelでファイルを横長・縦長のフィットページとして印刷する方法**

Microsoft ExcelでFitToPagesWideとFitToPagesTallを設定するには、以下の手順に従います：

1. Excelワークブックを開き、印刷したいシートに移動します。
1. リボンのページレイアウトタブに移動します。
1. ページセットアップグループ内の、右下の小さな矢印をクリックしてページ設定ダイアログボックスを開きます。
1. ページ設定ダイアログの「ページ」タブに切り替えます。
1. スケーリングの下にある「次のページに合わせる」を選択し、必要なページ幅と高さを指定します：最初のボックスにページ幅を入力します（Fit to xページの幅）、2番目のボックスにページの高さを入力します（Fit to yページの高さ）。
<br>
<img src="2.png" width=60% />

1. 設定を適用するにはOKをクリックします。

## **Aspose.Cells を使用して Excel を横長・縦長フィットページとして印刷する方法**

指定されたワークシートでFitToPagesWideとFitToPagesTallを設定するには：最初に[サンプルファイル](input.xlsx)を読み込み、その後、目的のワークシートの[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)オブジェクトの[**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/)と[**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/)のプロパティを変更します。以下はC++の例です：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

出力結果：
<br>
<img src="1.png" width=60% />

## **Aspose.Cellsを使用したワークシートを1ページとして印刷する方法**

ワークシートを1ページとして印刷するには：最初に[サンプルファイル](sample.xlsx)を読み込み、その後、[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/)プロパティを設定します。以下はC++の例です：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

出力結果：
<br>
<img src="3.png" width=60% />

## **Aspose.Cellsを使用してワークシートのすべての列を1ページに印刷する方法**

ワークシートのすべての列を1ページに印刷するには：最初に[サンプルファイル](sample.xlsx)を読み込み、その後、[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/)プロパティを設定します。以下はC++の例です：

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

出力結果：
<br>
<img src="4.png" width=60% />
