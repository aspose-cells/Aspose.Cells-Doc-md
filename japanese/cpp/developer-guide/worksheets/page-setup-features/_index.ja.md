---
title: ページ設定の機能（C++）
linktitle: ページ設定機能
type: docs
weight: 60
url: /ja/cpp/page-setup-features/
description: Aspose.Cellsを使ってExcelファイルのページ設定機能をC++で設定する方法について学びます。
---

## **ページ設定機能**

Aspose.Cellsは、Excelファイルのページ設定オプションを設定するための包括的な機能セットを提供します。これらの機能により、余白、向き、紙サイズなど、ページレイアウトのさまざまな側面を制御できます。

### **ページ余白を設定**

`PageSetup`クラスを使用して、ワークシートのページ余白を設定できます。以下の例では、上部、下部、左側、右側の余白の設定方法を示します。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **ページの向きを設定**

`PageSetup`クラスを使用して、ページの向きを縦または横に設定できます。次の例は、ページの向きを横向きに設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **用紙サイズを設定**

`PageSetup`クラスを使用して、印刷用紙サイズを設定できます。次の例は、用紙サイズをA4に設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **印刷範囲を設定**

`PageSetup`クラスを使用して、印刷するセルの範囲を定義できます。次の例は、印刷範囲を設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **ページの区切りを設定**

`ページの区切り`を挿入して、ページの終了位置や新しいページの開始位置を制御できます。次の例は、横方向のページ区切りを挿入する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **ヘッダーとフッターを設定**

`PageSetup`クラスを使用して、ワークシートのヘッダーとフッターをカスタマイズできます。次の例は、カスタムヘッダーとフッターを設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **印刷タイトルを設定**

`PageSetup`クラスを使用して、各ページの上部または左側に繰り返す行または列を指定できます。次の例は、印刷タイトルの設定方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **印刷品質を設定**

`PageSetup`クラスを使用して、ワークシートの印刷品質を設定できます。次の例は、印刷品質を設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **印刷順序を設定**

`PageSetup`クラスを使用して、ワークシートの印刷順を設定できます。次の例は、「上から、次に下」の順序に設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **印刷グリッド線を設定**

`PageSetup`クラスを使用して、グリッド線を印刷するかどうかを制御できます。次の例は、グリッド線の印刷を有効にする方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **見出しの印刷を設定**

`PageSetup`クラスを使用して、行と列の見出しを印刷するかどうかを制御できます。次の例は、見出しの印刷を有効にする方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **白黒印刷を設定**

`PageSetup`クラスを使用して、ワークシートを白黒で印刷するかどうかを制御できます。次の例は、白黒印刷を有効にする方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **下書き印刷を設定**

`PageSetup`クラスを使用して、ワークシートの下書き品質での印刷を制御できます。次の例は、下書き品質の印刷を有効にする方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **コメントの印刷を設定**

`PageSetup`クラスを使用して、コメントを印刷するかどうかを制御できます。次の例は、コメントの印刷を有効にする方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **エラーの印刷を設定**

`PageSetup`クラスを使用して、エラーの印刷方法を制御できます。次の例は、エラーの印刷オプションを設定する方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **印刷範囲をページ数に合わせて調整**

`PageSetup`クラスを使用して、印刷範囲が特定のページ数に収まるようにスケーリングできるかどうかを制御できます。次の例は、印刷範囲を横1ページ、縦1ページに収める設定方法を示しています：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **印刷スケール設定**

`PageSetup`クラスを使用してワークシートの印刷スケールを設定できます。以下の例では印刷スケールを50％に設定する方法を示します：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **印刷の中央を横方向と縦方向に設定**

`PageSetup`クラスを使用して、ワークシートが印刷ページの中央に水平および垂直に配置されているかどうかを制御できます。以下の例では、ワークシートを横方向と縦方向に中央に配置する方法を示します：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **最初のページ番号設定**

`PageSetup`クラスを使用して、印刷の最初のページ番号を設定できます。以下の例では、最初のページ番号を設定する方法を示します：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **ページ番号の設定**

`PageSetup`クラスを使用して、ページ番号を印刷するかどうかを制御できます。以下の例では、ページ番号の印刷を有効にする方法を示します：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **ページ順序の設定**

`PageSetup`クラスを使用して、ページの印刷順序を設定できます。以下の例では、「下から、次に横」の順でページを設定する方法を示します：

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
