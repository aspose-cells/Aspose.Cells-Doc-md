---
title: マージンの設定（C++）
linktitle: マージンの設定
type: docs
weight: 20
url: /ja/cpp/setting-margins/
description: C++を使って、ページ余白、中央配置、ヘッダーとフッターの余白をプログラム的に設定する方法を学びます（Aspose.Cells for C++）。
keywords: Excelワークシートの余白を中央に設定（C++）、ヘッダーとフッターの余白を設定（C++）
---

{{% alert color="primary" %}}

Aspose.CellsはMicrosoft Excelのページ設定オプションを完全にサポートしています。開発者は印刷プロセスを制御するためにワークシートのページ設定設定を構成する必要があります。このトピックでは、Aspose.Cellsを使用してページ余白を設定する方法について説明します。

{{% /alert %}}

## **マージンの設定**

Aspose.Cellsは、Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイル内の各ワークシートへアクセス可能な [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートのページセットアップオプションを設定するために使用される [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)プロパティを提供します。[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)属性は[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)クラスのオブジェクトであり、印刷されたワークシートのページレイアウト設定を可能にします。[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)クラスはさまざまなページ設定オプションを設定するためのプロパティとメソッドを提供します。

### **ページ余白**

ページ余白（左、右、上、下）を[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)クラスのメンバーを使って設定します。一部のメソッド例は以下の通りです。

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ページの中央に配置**

ページを横方向および縦方向に中央揃えに配置することは可能です。そのための便利なメンバーとして[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)クラスの[**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/)と[**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/)があります。

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ヘッダーとフッタのマージン**

ヘッダーとフッターの余白を設定するには、[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)クラスのメンバーである[**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/)と[**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/)を使います。

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
