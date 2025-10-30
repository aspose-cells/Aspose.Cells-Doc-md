---
title: 既存のスタイルをC++で変更する
description: Aspose.Cellsは、スプレッドシートファイルの操作に使用できるC++ライブラリであり、既存のセルスタイルを変更できます。この記事では、Aspose.Cellsライブラリを使用して既存のセルスタイルを変更し、セルの外観を必要に応じて調整する方法を紹介します。
keywords: 既存のスタイルを変更し、アプリケーションの外観と使いやすさをカスタマイズする、ガイド、チュートリアル、ヘルプドキュメント、開発ドキュメント、APIリファレンス、サンプルコード、ダウンロード、サポート。
type: docs
weight: 90
url: /ja/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

セルに同じフォーマットオプションを適用するには、新しいフォーマットスタイルオブジェクトを作成します。フォーマットスタイルオブジェクトは、フォント、フォントサイズ、インデント、数値、罫線、パターンなどのフォーマット特性を組み合わせたものであり、名前が付けられ、セットとして保存されます。適用されると、そのスタイルのすべてのフォーマットが適用されます。

既存のスタイルを使用して、ブックと共に保存し、同じ属性で情報を書式設定することもできます。

セルが明示的にフォーマットされていない場合、**通常**スタイル(ワークブックのデフォルトスタイル)が適用されます。Microsoft Excelでは、通常スタイルに加えてComma、Currency、Percentなどのスタイルがいくつか事前に定義されています。

Aspose.Cellsを使用すると、これらのスタイルのいずれか、または独自の属性で定義したスタイルを修正することができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel 97-2003でスタイルを更新するには:

1. **書式**メニューで **スタイル** をクリックします。
1. **スタイル名** リストから変更したいスタイルを選択します。
1. **変更** をクリックします。
1. 「セルの書式設定」ダイアログのタブを使用して、望むスタイルオプションを選択します。
1. **OK** をクリックします。
1. **スタイルに含まれるもの** で、希望するスタイルの機能を指定します。
1. **OK** をクリックしてスタイルを保存し、選択した範囲に適用します。

## **Aspose.Cellsの使用**

次の例は[**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/)メソッドの使用方法を示しています。

### **スタイルの作成と変更**

この例は、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトを作成し、それをセル範囲に適用し、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトを変更します。変更は自動的にセルとスタイルが適用された範囲に反映されます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **既存のスタイルの変更**

この例では、範囲にすでに適用されているPercentという名前のスタイルが含まれる単純なテンプレートExcelファイルを使用します。具体的な手順は以下の通りです:

1. スタイルを取得します。
1. スタイルオブジェクトを作成します。
1. スタイルフォーマットを変更します。

変更は自動的に適用された範囲に適用されます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
