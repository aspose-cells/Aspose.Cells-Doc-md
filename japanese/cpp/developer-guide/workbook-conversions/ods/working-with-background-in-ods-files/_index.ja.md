---
title: C++を使用してODSファイルの背景を操作する
linktitle: ODSファイルでの背景の処理
type: docs
weight: 150
url: /ja/cpp/working-with-background-in-ods-files/
description: Aspose.Cellsを使用して、ODSファイルの色付きおよびグラフィック背景を管理する方法を学びます。
---

## **ODSファイルでの背景**

ODSファイルにシートに背景を追加することができます。背景は塗りつぶしの背景やグラフィック背景のいずれかです。この背景はファイルが開かれている場合は見えませんが、PDFとして印刷されると、PDFに背景が表示されます。背景は印刷プレビューダイアログにも表示されます。

Aspose.Cellsは、ODSファイルで背景情報を読み込み、背景を追加する機能を提供します。

## **ODSファイルの背景を読み込む**

Aspose.Cellsは、ODSファイルの背景を管理するために[**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/)クラスを提供します。以下のコード例は、[**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/)クラスを使用してソースODS([source ODS](90112030.ods))ファイルを読み込み、背景情報を取得する方法を示しています。コードによって生成されるコンソール出力を参考にしてください。

### **サンプルコード**

```c++
#include <iostream>
#include <fstream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"GraphicBackground.ods");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    std::cout << "Background Type: " << static_cast<int>(background.GetType()) << std::endl;
    std::cout << "Background Position: " << static_cast<int>(background.GetGraphicPositionType()) << std::endl;

    Vector<uint8_t> graphicData = background.GetGraphicData();
    std::string filePath = (outDir + u"background.jpg").ToUtf8();
    std::ofstream fout(filePath, std::ios::binary);
    fout.write(reinterpret_cast<const char*>(graphicData.GetData()), graphicData.GetLength());
    fout.close();

    std::cout << "Background image saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **コンソール出力**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **ODSファイルに色付きの背景を追加する**

Aspose.Cellsは、ODSファイルの背景を管理するために[**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/)クラスを提供します。次のコード例は、[**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/)プロパティを使用してODSファイルに色の背景を追加する方法を示しています。コードで生成された[出力ODS](90112031.ods)ファイルを参照してください。

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell values
    worksheet.GetCells().Get(0, 0).SetValue(1);
    worksheet.GetCells().Get(1, 0).SetValue(2);
    worksheet.GetCells().Get(2, 0).SetValue(3);
    worksheet.GetCells().Get(3, 0).SetValue(4);
    worksheet.GetCells().Get(4, 0).SetValue(5);
    worksheet.GetCells().Get(5, 0).SetValue(6);
    worksheet.GetCells().Get(0, 1).SetValue(7);
    worksheet.GetCells().Get(1, 1).SetValue(8);
    worksheet.GetCells().Get(2, 1).SetValue(9);
    worksheet.GetCells().Get(3, 1).SetValue(10);
    worksheet.GetCells().Get(4, 1).SetValue(11);
    worksheet.GetCells().Get(5, 1).SetValue(12);

    // Access the ODS page background
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    // Set background color and type
    background.SetColor(Color::Azure());
    background.SetType(OdsPageBackgroundType::Color);

    // Save the workbook
    workbook.Save(outDir + u"ColoredBackground.ods", SaveFormat::Ods);

    std::cout << "Workbook saved successfully with colored background!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ODSファイルにグラフィックの背景を追加する**

Aspose.Cellsは、ODSファイルの背景を管理するために[**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/)クラスを提供します。次のコード例は、[**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/getgraphicdata/)プロパティを使用してグラフィック背景をODSファイルに追加する方法を示しています。コードで生成された[出力ODS](90112030.ods)ファイルを参照してください。

### **サンプルコード**

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}


int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set values in cells
    worksheet.GetCells().Get(0, 0).SetValue(1);
    worksheet.GetCells().Get(1, 0).SetValue(2);
    worksheet.GetCells().Get(2, 0).SetValue(3);
    worksheet.GetCells().Get(3, 0).SetValue(4);
    worksheet.GetCells().Get(4, 0).SetValue(5);
    worksheet.GetCells().Get(5, 0).SetValue(6);
    worksheet.GetCells().Get(0, 1).SetValue(7);
    worksheet.GetCells().Get(1, 1).SetValue(8);
    worksheet.GetCells().Get(2, 1).SetValue(9);
    worksheet.GetCells().Get(3, 1).SetValue(10);
    worksheet.GetCells().Get(4, 1).SetValue(11);
    worksheet.GetCells().Get(5, 1).SetValue(12);

    // Get the ODS page background
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    // Set background type to graphic
    background.SetType(OdsPageBackgroundType::Graphic);

    // Read the background image file
    Vector<uint8_t> graphicData = GetDataFromFile(U16String(srcDir + u"background.jpg"));

    // Set graphic data and type
    background.SetGraphicData(graphicData);
    background.SetGraphicType(OdsPageBackgroundGraphicType::Area);

    // Save the workbook
    workbook.Save(outDir + u"GraphicBackground.ods", SaveFormat::Ods);

    std::cout << "Graphic background applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
