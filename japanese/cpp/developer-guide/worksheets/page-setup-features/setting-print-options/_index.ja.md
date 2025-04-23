---
title: C++で印刷オプションを設定する
linktitle: 印刷オプションの設定
type: docs
weight: 40
url: /ja/cpp/setting-print-options/
description: この記事は、C++ APIとライブラリを使用してExcelワークシートのページ設定機能の印刷オプションをプログラム的に設定する方法を示しています。印刷範囲、印刷タイトル、ページ順序を設定できます。
keywords: エクセルの印刷範囲設定（C++）、印刷タイトル設定（C++）、ページ順序設定（C++）
---

{{% alert color="primary" %}}

Microsoft Excel のページ設定設定には、ワークシートページが印刷される方法を制御するいくつかの印刷オプション (またはシートオプションとも呼ばれる) が含まれています。

{{% /alert %}}

## **印刷オプションの設定**

これらの印刷オプションにより、ユーザーは次のような操作を行うことができます:

- ワークシート上の特定の印刷範囲を選択する。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

Aspose.CellsはMicrosoft Excelが提供するすべての印刷オプションをサポートしており、開発者は[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)クラスが提供するプロパティを使用してこれらのオプションをワークシートに簡単に設定できます。これらのプロパティの使用方法については、以下で詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、印刷エリアにはデータを含むワークシートのすべての領域が組み込まれます。開発者はワークシートの特定の印刷エリアを設定することができます。

特定の印刷エリアを選択するには、[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) クラスの [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) プロパティを使用します。このプロパティに、印刷エリアを定義するセル範囲を割り当てます。

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **印刷タイトルを設定する**

Aspose.Cells を使用すると、印刷されるワークシートのすべてのページで行および列見出しを繰り返し指定することが可能です。これを行うには、[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) クラスの [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) および [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) プロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **その他の印刷オプションの設定**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) クラスには、以下の一般的な印刷オプションを設定するためのいくつかの他のプロパティも提供されています:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): グリッド線を印刷するかどうかを定義するブール型プロパティ。
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): 行および列見出しを印刷するかどうかを定義するブール型のプロパティ。
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): ブラックアンドホワイトモードでワークシートを印刷するかどうかを定義するブールプロパティ。
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): ワークシート上に印刷コメントを表示するか、ワークシートの最後に表示するかを定義する。
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): グラフィックスなしでシートを印刷するかどうかを定義するブール型プロパティ。
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): セルのエラーを表示された通り、空白、ダッシュ、またはN/Aとして印刷するかどうかを定義します。

[**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/)および[**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/)プロパティを設定するために、Aspose.Cellsは[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)および[**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/)という2つの列挙型も提供しており、それぞれ[**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/)と[**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/)のプロパティに事前定義された値を割り当てることができます。

[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) 列挙型の事前に定義された値は、以下にその説明とともにリストされています。

|**コメント印刷タイプ**|**説明**|
| :- | :- |
|PrintInPlace|: ワークシート上に表示されているコメントを印刷することを指定。
|PrintNoComments|: コメントを印刷しないことを指定。
|PrintSheetEnd|: ワークシートの最後にコメントを印刷することを指定。

[**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) 列挙型の事前に定義された値は、以下にその説明とともにリストされています。

|**エラー印刷タイプ**|**説明**|
| :- | :- |
|PrintErrorsBlank|: エラーを印刷しないことを指定。
|PrintErrorsDash|: エラーを "--" として印刷することを指定。
|PrintErrorsDisplayed|: 表示されているエラーを印刷することを指定。
|PrintErrorsNA|: エラーを "#N/A" として印刷することを指定。

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ページ順の設定**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) クラスは、ワークシートを印刷するための複数のページの順序を設定するために使用される [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) プロパティを提供します。ページを順に印刷するためには、次の2つの可能性があります。

- **Down then over:** 右側のページを印刷する前に、すべてのページを下に印刷します。
- **Over then down:** 下側のページを印刷する前に、左から右のページを印刷します。

Aspose.Cellsは、[**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) という列挙型を提供し、すべての事前に定義された順序タイプが含まれています。

列挙型 [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) の事前に定義された値は、以下にその説明とともにリストされています。

|**印刷順序タイプ**|**説明**|
| :- | :- |
|DownThenOver|: 下に印刷してから右に印刷するよう指定。
|OverThenDown|: 左から右に印刷してから下に印刷するよう指定。

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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
