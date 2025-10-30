---
title: C++でWebアドレスからリンクされた画像を挿入する
linktitle: Webアドレスからリンクされた画像の挿入
type: docs
weight: 450
url: /ja/cpp/insert-a-linked-picture-from-web-address/
description: Aspose.Cells for C++を使用して、Webアドレスからリンクされた画像をワークシートに挿入する方法を学びます。
---

{{% alert color="primary" %}}

時々、ワークシートにWeb（http://）から画像を挿入する必要があります。これを行うには、画像のURLとして指定し、表計算がMicrosoft Excelで開かれるたびに画像がダウンロードされます。 画像は実際にはExcel文書に物理的に埋め込まれていませんが、Webリソースを指し示しています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（たとえば2007）で：

1. **挿入**メニューをクリックし、**画像**を選択します。
1. 挿入画像ダイアログで画像のWebアドレスを指定します。

## **Aspose.Cells for C++を使用した例**

Aspose.Cells for C++は、[**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/)メソッドを使用してリンクされた画像を追加することをサポートします。このメソッドは[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)オブジェクトを返します。

以下の例では、Webアドレスからリンクされた画像をワークシートに追加する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
