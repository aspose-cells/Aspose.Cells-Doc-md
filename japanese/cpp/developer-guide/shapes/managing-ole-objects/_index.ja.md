---
title: OLEオブジェクトの管理 with C++
linktitle: OLE オブジェクトを管理する
type: docs
weight: 50
url: /ja/cpp/managing-ole-objects/
description: Aspose.Cellsを使用してC++でワークシートにOLEオブジェクトを追加、抽出、操作する方法を学びます。
---

## **紹介**

OLE (Object Linking and Embedding) は、Microsoft の複合ドキュメントテクノロジーのフレームワークです。簡単に言うと、複合ドキュメントとは、テキスト、カレンダー、アニメーション、音声、動画、3D、定期的に更新されるニュース、コントロールなど、あらゆる種類の視覚的および情報オブジェクトを含む表示デスクトップのことです。各デスクトップオブジェクトは、ユーザーと相互作用し、他のデスクトップ上の他のオブジェクトとも通信できる独立したプログラムエンティティです。

OLE (Object Linking and Embedding) は、さまざまなプログラムでサポートされており、あるプログラムで作成したコンテンツを別のプログラムで利用できるようにするために使用されます。たとえば、Microsoft Word ドキュメントを Microsoft Excel に挿入することができます。挿入可能なコンテンツの種類を確認するには、**挿入** メニューで **オブジェクト** をクリックします。コンピュータにインストールされ、OLE オブジェクトをサポートするプログラムだけが **オブジェクトの種類** ボックスに表示されます。

### **ワークシートにOLEオブジェクトを挿入する**

Aspose.Cellsは、ワークシートへのOLEオブジェクトの追加、抽出、および操作をサポートします。そのため、コレクションリストに新しいOLEオブジェクトを追加するために使用される[**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/)クラスと、OLEオブジェクトを表す[**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/)クラスがあります。重要なメンバーは次の通りです：

- `[**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/)`プロパティは、イメージ（アイコン）のデータをバイト配列型で指定します。この画像は、ワークシート内のOLEオブジェクトを表示するために使われます。
- `[**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)`プロパティは、オブジェクトのデータをバイト配列の形式で指定します。このデータは、ダブルクリックによって関連付けられたプログラムで表示されます。

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **ワークブックからOLEオブジェクトを抽出**

以下の例では、ワークブックからOLEオブジェクトを抽出する方法を示します。この例では既存のXLSファイルから異なるOLEオブジェクトを取得し、OLEオブジェクトのファイル形式に基づいて異なるファイル（DOC、XLS、PPT、PDFなど）を保存します。

コードを実行した後、対応するOLEオブジェクト形式の異なるファイルを保存できます。

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
        case FileFormatType::Doc:
            fileName += u"doc";
            break;
        case FileFormatType::Xlsx:
            fileName += u"Xlsx";
            break;
        case FileFormatType::Ppt:
            fileName += u"Ppt";
            break;
        case FileFormatType::Pdf:
            fileName += u"Pdf";
            break;
        case FileFormatType::Unknown:
            fileName += u"Jpg";
            break;
        default:
            // Handle other formats if needed
            break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **埋め込まれたMOLファイルの抽出**

Aspose.Cellsは、分子データファイル（原子と結合の情報を含むmolファイル）のような珍しいタイプのオブジェクトの抽出もサポートしています。以下のコードスニペットは、埋め込まれたMOLファイルを抽出し、[サンプルExcelファイル](94896196.xlsx)を使用してディスクに保存する例です。

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ** 高度なトピック**
- [リンクされたオブジェクトの表示ラベルへのアクセスと変更](/cells/ja/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する](/cells/ja/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [ワークブックからOLEオブジェクトを抽出](/cells/ja/cpp/extract-ole-objects-from-workbook/)
- [埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する](/cells/ja/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Ole ObjectとしてWAVファイルを挿入する](/cells/ja/cpp/inserting-a-wav-file-as-an-ole-object/)
