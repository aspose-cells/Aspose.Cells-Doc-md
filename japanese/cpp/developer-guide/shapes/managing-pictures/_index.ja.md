---
title: 画像の管理 with C++
linktitle: 画像の管理
type: docs
weight: 10
url: /ja/cpp/managing-pictures/
description: 画像を追加、配置、管理するためのAPI（Aspose.Cells for C++）を使用したスプレッドシートへの画像の挿入例。
---

Aspose.Cellsを使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の位置を実行時に制御することができます。これについては後のセクションで詳しく説明します。

この記事では、画像の追加方法と特定のセルの内容を示す画像の挿入方法について説明します。

## **画像の追加**

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:
- [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/)メソッドを[**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/)オブジェクトの[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)に呼び出すだけです。[**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/)メソッドは次のパラメータを取ります：

- **左上の行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **写真の位置合わせ**

Aspose.Cellsを使用して写真の位置合わせを制御する方法には2つの方法があります:

- 比例位置合わせ：行の高さと幅に比例した位置を定義します。
- 絶対位置指定：画像を挿入するページ上の正確な位置を定義します。例：セルの縁から左に40ピクセル、下に20ピクセル。

### **比例位置合わせ**

開発者は、[**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/)および[**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/)プロパティを使用して、画像の位置を行の高さおよび列の幅に比例させて調整できます。 `[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)`の[**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/)を渡すことで[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)オブジェクトを取得できます。この例では、F6セルに画像を配置しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **絶対位置づけ**

開発者は、[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)オブジェクトの[**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/)および[**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/)プロパティを使用して、絶対位置に写真を配置することもできます。この例では、セルF6に画像を配置し、左から60ピクセル、上から10ピクセルに配置します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **セル参照に基づいて画像を挿入**

Aspose.Cellsを使用すると、ワークシートのセルの内容を画像形状で表示できます。画像は、データを表示したいセルにリンクされています。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、自動的にグラフィックオブジェクトに変更が反映されます。

[**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/)メソッドを[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)オブジェクト（`[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)`の中にカプセル化）から呼び出すことで、ワークシートに画像を追加します。セル範囲は[**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/)属性を使って指定します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [セルのテキストと条件付きアイコンセットの追加](/cells/ja/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Webアドレスからリンクされた画像の挿入](/cells/ja/cpp/insert-a-linked-picture-from-web-address/)
- [セル参照に基づく画像の挿入](/cells/ja/cpp/insert-a-picture-based-on-cell-reference/)
- [Web画像のURLをExcelワークシートに読み込む](/cells/ja/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="cpp" >}}
