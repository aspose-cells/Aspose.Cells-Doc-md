---
title: C++でExcelテーマと色彩を利用する
linktitle: Excelのテーマと色
type: docs
weight: 100
url: /ja/cpp/excel-themes-and-colors/
description: Aspose.Cells for C++ APIを用いたExcelのカラースキームの使用例
keywords: C++でカラースキームを作成および適用、プログラム的にカスタムカラースキームを作成、カスタムカラースキームを適用する方法、C++でExcelのカラースキームを使用する方法
---

## **Excelでのカラースキームの適用と作成方法**
ドキュメントテーマを使用すると、Excelドキュメントの色、フォント、グラフィックの書式効果を簡単に調整し、迅速に更新できます。 
テーマは名前付きスタイル、グラフィカル効果、ブックの他のオブジェクトを使用して統一された外観を提供します。たとえば、OfficeテーマとApexテーマでは、Accent1スタイルは異なる外観になります。よくあるのは、ドキュメントテーマを適用してから、必要に応じて修正することです。

### **Excelでのカラースキームの適用方法**
1. Excelを開き、「ページレイアウト」タブに移動します。
1. 「テーマ」セクションの「カラー」ボタンをクリックします。
<br>
<img src="color.png" width=70% />
1. 要件に合ったカラーパレットを選択するか、スキームにマウスを重ねてライブプレビューを表示します。

### **Excelでのカスタムカラースキームの作成方法**
ドキュメントに新鮮で独自の外観を与えるために独自のカラーセットを作成するか、組織のブランド規準に準拠します。

1. Excelを開き、「ページレイアウト」タブに移動します。
1. 「テーマ」セクションの「カラー」ボタンをクリックします。
1. 「カスタムカラーのカスタマイズ...」ボタンをクリックします。
<br>
<img src="color2.png" width=70% />

1. 「新しいテーマの色の作成」ダイアログボックスで、各要素の色を選択できます。
<br>
<img src="color3.png" width=70% />
1. 必要な色をすべて選択した後、「名前」フィールドにカスタムカラースキームの名前を入力します。

1. 「保存」ボタンをクリックしてカスタムカラースキームを保存します。カスタムカラースキームは今後の使用のために「カラー」ドロップダウンメニューで利用可能になります。

## **Aspose.Cellsでのカラースキームの作成と適用方法**
Aspose.Cellsにはテーマと色をカスタマイズする機能が提供されています。

### **Aspose.Cellsでのカスタムカラーテーマの作成方法**
ファイルでテーマカラーが使用されている場合、各セルを個々に変更する必要はありません。テーマの色を修正するだけで済みます。

使用例では、希望の色でカスタムテーマを適用する方法が示されています。Microsoft Excel 2007 で手動で作成されたサンプルテンプレートファイルを使用します。

使用例では、テンプレートXLSXファイルを読み込み、さまざまなテーマカラータイプの色を定義し、カスタムカラーを適用してExcelファイルを保存します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aspose.Cells でテーマカラーを適用する方法**

使用例では、セルの前景色とフォント色を、ブックのデフォルトテーマの色タイプに基づいて適用します。また、Excelファイルをディスクに保存します。

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

    // Create workbook
    Workbook workbook;

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aspose.Cells でテーマカラーを取得および設定する方法**
 テーマカラーを実装するいくつかのメソッドとプロパティが以下に示されています。

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/)：前景色を設定するために使用されます。
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/)：背景色を設定するために使用されます。
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/)：フォントの色を設定するために使用されます。
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/)：テーマカラーを取得するために使用されます。
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/)：テーマカラーを設定するために使用されます。

使用例では、テーマカラーを取得および設定する方法が示されています。

使用例では、テンプレートXLSXファイルを使用して、さまざまなテーマカラータイプの色を取得し、色を変更し、Microsoft Excelファイルを保存します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [Excelファイルからテーマデータを抽出](/cells/ja/cpp/extract-theme-data-from-excel-file/)
