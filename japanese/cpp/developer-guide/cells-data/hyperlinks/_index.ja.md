---
title: C++を使ってExcelまたはOpenOfficeにハイパーリンクを挿入
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/cpp/insert-hyperlinks-to-excel/
description: Aspose.Cellsライブラリを使って、MS Excelを使わずにExcelファイルにハイパーリンクを挿入する方法。
keywords: Excelにハイパーリンクを挿入する、またはハイパーリンクを追加または挿入する、URLにリンクを追加または挿入する、セルにリンクを追加または挿入する、外部ファイルにリンクを追加
---

{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。
Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}} 

## **ハイパーリンクの追加**
Aspose.Cellsは、APIまたはデザイナースプレッドシート（手動でハイパーリンクを作成し、それを他のスプレッドシートにインポートするためにAspose.Cellsを使用する）を使って、開発者がExcelファイルにハイパーリンクを追加できるようにします。

Aspose.Cellsは、Microsoft Excelファイルを表すクラス [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) を提供しています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) が含まれています。ワークシートは [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表され、さまざまなハイパーリンクを追加するためのメソッドを提供します。

## **URLへのリンクの追加**
[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスには [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) コレクションがあります。このコレクションの各アイテムは [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) を表します。URLにハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) コレクションの [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) メソッドを呼び出します。 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) メソッドは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されます。このような場合、セルが空の場合、URLアドレスもその空のセルの値として追加されます。セルが空でない場合は、ハイパーリンクが追加されても、セルの値はプレーンテキストのように見えます。それをハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 

## **同じファイル内のセルへのリンクの追加**
同じExcelファイル内のセルにハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) コレクションの [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) メソッドを呼び出します。この [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) メソッドは、内部および外部のハイパーリンクの両方に対応しています。オーバーロードされたメソッドの一つは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **外部ファイルへのリンクの追加**
外部Excelファイルにハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) コレクションの [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) メソッドを呼び出します。この [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) メソッドは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/cpp/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/cpp/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/cpp/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/cpp/get-hyperlinks-in-range/)
{{< app/cells/assistant language="cpp" >}}
