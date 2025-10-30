---
title: C++でワークブックからOLEオブジェクトを抽出する
linktitle: ワークブックからOLEオブジェクトを抽出
type: docs
weight: 110
url: /ja/cpp/extract-ole-objects-from-workbook/
description: Aspose.Cellsを使ってワークブックからOLEオブジェクトを抽出する方法を学びます。
---

{{% alert color="primary" %}}

時には、ワークブックからOLEオブジェクトを抽出する必要があります。Aspose.CellsはこれらのOLEオブジェクトの抽出と保存をサポートしています。

このガイドでは、Visual Studioでコンソールアプリケーションを作成し、少ないコード行数でワークブックからさまざまなOLEオブジェクトを抽出する方法を示します。

{{% /alert %}}

## **ワークブックからOLEオブジェクトを抽出**

### **テンプレートワークブックの作成**

1. Microsoft Excelでワークブックを作成します。
1. 最初のシートにOLEオブジェクトとしてMicrosoft Wordドキュメント、Excelワークブック、およびPDFドキュメントを追加します。

|**OLEオブジェクトを含むテンプレートドキュメント（OleFile.xls）**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

次に、OLEオブジェクトを抽出し、それぞれのファイルタイプでハードディスクに保存します。

### **Aspose.Cellsをダウンロードしてインストールする**

1. [Aspose.Cells for C++をダウンロード](https://downloads.aspose.com/cells/cpp)。
1. 開発コンピュータにインストールします。

すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。

### **プロジェクトを作成する**

**Visual Studio**を起動し、新しいコンソールアプリケーションを作成します。この例はC++のコンソールアプリケーションです。

1. 参照を追加
   1. プロジェクトにAspose.Cellsコンポーネントを参照として追加します。例えば、...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dllに参照を追加します。

### **OLE オブジェクトの抽出**

以下のコードは、OLEオブジェクト（DOC、XLS、PDFファイル）を検索し抽出し、ディスクに保存します。

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
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
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
