---
title: C++でコントロールを管理する
linktitle: コントロールの管理
type: docs
weight: 150
url: /ja/cpp/managing-controls/
description: Aspose.Cellsを使用してC++でワークシートに線、長方形、弧、楕円、スピナー、スクロールバー、グループボックスなどのさまざまなコントロールを追加・管理する方法を学びます。
---

## **紹介**

開発者は、テキストボックス、チェックボックス、ラジオボタン、コンボボックス、ラベル、ボタン、線、長方形、弧、楕円、スピナー、スクロールバー、グループボックスなどのさまざまな描画オブジェクトを追加できます。Aspose.Cellsはすべての描画オブジェクトを含む `Aspose::Cells::Drawing` 名前空間を提供しています。ただし、まだサポートされていない描画オブジェクトや形がいくつかあります。これらの描画オブジェクトをMicrosoft Excelを使って設計者スプレッドシートで作成し、その後設計者スプレッドシートをAspose.Cellsにインポートしてください。Aspose.Cellsは、設計者スプレッドシートからこれらの描画オブジェクトを読み込み、生成されたファイルに書き込みができます。

## **ワークシートにテキストボックスコントロールを追加**

レポートで重要な情報を強調する一つの方法は、テキストボックスを使用することです。たとえば、企業名を強調するためにテキストを追加したり、最も売り上げの高い地理的地域を示すために使用したりします。Aspose.Cellsは、新しいテキストボックスをコレクションに追加するために使用される[**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/)クラスを提供しています。別の[**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/)クラスもあり、すべての種類の設定を定義するために使用されるテキストボックスを表しています。いくつか重要なメンバーがあります:

- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)プロパティは配置タイプを指定します。
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)プロパティはフォント属性を指定します。
- [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/)メソッドは、テキストボックスにハイパーリンクを追加します。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)プロパティは、テキストボックスの塗りつぶし形式を設定するために使用される[**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/)オブジェクトを返します。
- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)プロパティは、テキストボックスのラインのスタイルと太さを通常設定するために使用される[**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/)オブジェクトを返します。
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)プロパティは、テキストボックスの入力テキストを指定します。

次の例では、ブックの最初のワークシートに2つのテキストボックスを作成します。最初のテキストボックスはさまざまなフォーマット設定で整備されています。2番目はシンプルなものです。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // The path to the documents directory.
    U16String dataDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get the first worksheet in the book.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new textbox to the collection.
    int32_t textboxIndex = worksheet.GetTextBoxes().Add(2, 1, 160, 200);

    // Get the textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Fill the text.
    textbox0.SetText(u"ASPOSE______The .NET & JAVA Component Publisher!");

    // Set the placement.
    textbox0.SetPlacement(PlacementType::FreeFloating);

    // Set the font color.
    textbox0.GetFont().SetColor(Color::Blue());

    // Set the font to bold.
    textbox0.GetFont().SetIsBold(true);

    // Set the font size.
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic.
    textbox0.GetFont().SetIsItalic(true);

    // Add a hyperlink to the textbox.
    textbox0.AddHyperlink(u"http://www.aspose.com/");

    // Get the fill format of the textbox.
    FillFormat fillFormat = textbox0.GetFill();

    // Get the line format type of the textbox.
    LineFormat lineFormat = textbox0.GetLine();

    // Set the line weight.
    lineFormat.SetWeight(6.0);

    // Set the dash style to squaredot.
    lineFormat.SetDashStyle(MsoLineDashStyle::SquareDot);

    // Add another textbox.
    textboxIndex = worksheet.GetTextBoxes().Add(15, 4, 85, 120);

    // Get the second textbox.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Input some text to it.
    textbox1.SetText(u"This is another simple text box");

    // Set the placement type as the textbox will move and resize with cells.
    textbox1.SetPlacement(PlacementType::MoveAndSize);

    // Save the excel file.
    workbook.Save(dataDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **デザイナースプレッドシート内のテキストボックスコントロールの操作**

Aspose.Cellsでは、デザイナースプレッドシート内のテキストボックスにアクセスして操作することもできます。[**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)プロパティを使用して、シート内のテキストボックスのコレクションを取得します。

次の例では、上記の例で作成したMicrosoft Excelファイルを使用しています。2つのテキストボックスのテキストを取得し、2番目のテキストボックスのテキストを変更してファイルを保存します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // The path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"book1.xls");

    // Get the first worksheet in the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(0);

    // Obtain the text in the first textbox.
    U16String text0 = textbox0.GetText();

    // Get the second textbox object.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(1);

    // Obtain the text in the second textbox.
    U16String text1 = textbox1.GetText();

    // Change the text of the second textbox.
    textbox1.SetText(u"This is an alternative text");

    // Save the excel file.
    workbook.Save(srcDir + u"output.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにチェックボックスコントロールを追加する**

チェックボックスは、ユーザーが真偽またははい・いいえなどの2つのオプションから選択する方法を提供したい場合に便利です。Aspose.Cellsを使用すると、ワークシートでチェックボックスを使用できます。たとえば、特定の取得を考慮するかどうかを伴う財務予測ワークシートを作成した場合、そのワークシートの上部にチェックボックスを配置したいと思うかもしれません。その後、このチェックボックスの状態を他のセルにリンクすることができます。つまり、チェックボックスが選択されている場合、セルの値はTrueになり、選択されていない場合、セルの値はFalseになります。

### **Microsoft Excel の使用**

ワークシートにチェックボックスコントロールを配置するには、次の手順に従います。

1. フォームツールバーが表示されていることを確認します。
1. フォームツールバーの**チェックボックス**ツールをクリックします。
1. ワークシートエリアで、チェックボックスとチェックボックスの横に表示されるラベルを定義するためにクリックしてドラッグします。
1. チェックボックスが配置されたら、マウスカーソルをラベル領域に移動してラベルを変更します。
1. **セルリンク**フィールドで、このチェックボックスをリンクするセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

Aspose.Cellsには新しいチェックボックスをコレクションに追加するために使用される[**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/)クラスが提供されています。重要なメンバーを持つ他のクラス[**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/)もあります。

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)プロパティは、チェックボックスにリンクされるセルを指定します。
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)プロパティは、チェックボックスに関連付けられたテキスト文字列を指定します。これはチェックボックスのラベルです。
- [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/)プロパティは、チェックボックスが選択されているかどうかを指定します。

次の例では、ワークシートにチェックボックスを追加する方法を示しています。

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a new Workbook instance
    Workbook excelbook = Workbook();

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add a checkbox to the first worksheet in the workbook
    int32_t index = worksheet.GetCheckBoxes().Add(5, 5, 100, 120);

    // Get the checkbox object
    Drawing::CheckBox checkbox = worksheet.GetCheckBoxes().Get(index);

    // Set its text string
    checkbox.SetText(u"Click it!");

    // Get cells collection and set B1 cell value
    Cells cells = worksheet.GetCells();
    Cell cellB1 = cells.Get(u"B1");
    cellB1.PutValue(u"LnkCell");

    // Set B1 cell as a linked cell for the checkbox
    checkbox.SetLinkedCell(u"B1");

    // Check the checkbox by default
    checkbox.SetValue(true);

    // Save the excel file
    excelbook.Save(u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにラジオボタンコントロールを追加する**

ラジオボタン、またはオプションボタンは、円形のボックスからなるコントロールです。ユーザーはラウンドボックスを選択することで決定を行います。ラジオボタンは通常、他のラジオボタンに伴って表示され、グループとして振る舞います。ユーザーは1つのボタンのみを選択することで、どのボタンが有効か決定します。ユーザーが1つのボタンをクリックすると、それは選択されます。グループ内の1つのボタンが選択されると、同じグループのボタンは空になります。

### **Microsoft Excel の使用**

ワークシートにラジオボタンコントロールを配置するには、次の手順に従います。

1. **フォーム** ツールバーが表示されていることを確認します。
1. **オプションボタン**ツールをクリックします。
1. ワークシートで、オプションボタンとオプションボタンの横に表示されるラベルを定義するためにクリックしてドラッグします。
1. ワークシートにラジオボタンを配置したら、マウスカーソルをラベル領域に移動してラベルを変更します。
1. **セルリンク**フィールドで、このラジオボタンがリンクされるセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)クラスは[**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/)というメソッドを提供し、これを使ってワークシートにラジオボタンコントロールを追加します。メソッドは[**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/)オブジェクトを返します。[**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/)クラスはオプションボタンを表します。重要なメンバーは次のとおりです：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)プロパティは、ラジオボタンにリンクされるセルを指定します。
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)プロパティは、ラジオボタンに関連付けられたテキスト文字列を指定します。これはラジオボタンのラベルです。
- [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/)プロパティは、ラジオボタンが選択されているかどうかを指定します。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)プロパティは、ラジオボタンの塗りつぶし形式を指定します。
- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)プロパティは、オプションボタンの線の形式スタイルを指定します。

次の例では、ワークシートにラジオボタンを追加する方法を示しています。例では、3つの年齢グループを表すラジオボタンが追加されています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook excelbook;

    // Get the first worksheet
    Worksheet sheet = excelbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Insert a value in C2
    Cell cellC2 = cells.Get(u"C2");
    cellC2.PutValue(u"Age Groups");

    // Set the font text bold.
    Style style = cellC2.GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style back
    cellC2.SetStyle(style);

    // Add radio buttons to the first sheet.
    ShapeCollection shapes = sheet.GetShapes();

    // Create first radio button
    RadioButton radio1= shapes.AddRadioButton(3, 0, 2, 0, 30, 110);


    // Set its text string.
    radio1.SetText(u"20-29");
    // Set A1 cell as a linked cell for the radio button.
    radio1.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio1.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line1 = radio1.GetLine();
    line1.SetWeight(4);
    // Set the dash style of the radio button.
    line1.SetDashStyle(MsoLineDashStyle::Solid);

    // Create second radio button
    RadioButton radio2 = shapes.AddRadioButton(6, 0, 2, 0, 30, 110);
    // Set its text string.
    radio2.SetText(u"30-39");
    // Set A1 cell as a linked cell for the radio button.
    radio2.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio2.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line2 = radio2.GetLine();
    line2.SetWeight(4);
    // Set the dash style of the radio button.
    line2.SetDashStyle(MsoLineDashStyle::Solid);

    // Create third radio button
    RadioButton radio3=shapes.AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string.
    radio3.SetText(u"40-49");
    // Set A1 cell as a linked cell for the radio button.
    radio3.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio3.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line3 = radio3.GetLine();
    line3.SetWeight(4);
    // Set the dash style of the radio button.
    line3.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file.
    excelbook.Save(srcDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにコンボボックスコントロールを追加する**

データの入力を容易にするか、定義した項目にエントリを制限するためには、ワークシートの他のセルからコンパイルされる有効なエントリのコンボボックス、またはドロップダウンリストを作成できます。セルのドロップダウンリストを作成すると、そのセルの隣に矢印が表示されます。そのセルに情報を入力するには、矢印をクリックし、その後、欲しいエントリをクリックします。

### **Microsoft Excel の使用**

ワークシートにコンボボックスコントロールを配置するには、次の手順に従います：

1. **フォーム** ツールバーが表示されていることを確認します。
1. **コンボボックス** ツールをクリックします。
1. ワークシートエリアで、コンボボックスを保持する四角形を定義するためにクリックしてドラッグします。
1. コンボボックスがワークシートに配置されたら、コントロールを右クリックして **コントロールの書式設定** をクリックし、入力範囲を指定します。
1. **セルリンク** フィールドで、このコンボボックスをリンクするセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

クラス [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) は [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/) という名前のメソッドを提供し、これはワークシートにコンボボックスコントロールを追加するために使用されます。このメソッドは [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) オブジェクトを返します。[**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) クラスはコンボボックスを表します。いくつかの重要なメンバを持っています：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) プロパティはコンボボックスにリンクされたセルを指定します。
- [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) プロパティはコンボボックスを埋めるために使用されるワークシートのセル範囲を指定します。
- [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) プロパティはドロップダウン部分に表示されるリスト行の数を指定します。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) プロパティはコンボボックスが 3D シェーディングを持っているかどうかを示します。

次の例は、ワークシートにコンボボックスを追加する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook.
    Workbook workbook;

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection.
    Cells cells = sheet.GetCells();

    // Input a value.
    Cell cellB3 = cells.Get(u"B3");
    cellB3.PutValue(u"Employee:");

    // Set it bold.
    Style style = cellB3.GetStyle();
    style.SetIsBorderApplied(true);
    cellB3.SetStyle(style);

    // Input some values that denote the input range for the combo box.
    cells.Get(u"A2").PutValue(u"Emp001");
    cells.Get(u"A3").PutValue(u"Emp002");
    cells.Get(u"A4").PutValue(u"Emp003");
    cells.Get(u"A5").PutValue(u"Emp004");
    cells.Get(u"A6").PutValue(u"Emp005");
    cells.Get(u"A7").PutValue(u"Emp006");

    // Add a new combo box.
    ComboBox comboBox = sheet.GetShapes().AddComboBox(2, 0, 2, 0, 22, 100);

    // Cleanup Aspose resources
    Aspose::Cells::Cleanup();

    return 0;
}
```

## **ワークシートにラベルコントロールを追加する**

ラベルはスプレッドシートの内容に関するユーザーへの情報提供手段です。Aspose.Cells を使用すると、ワークシートにラベルを追加および操作することができます。クラス [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) は、ワークシートにラベルコントロールを追加するために使用する [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/) という名前のメソッドを提供します。このメソッドは [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) オブジェクトを返します。[**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) クラスはワークシート内のラベルを表します。いくつかの重要なメンバを持っています：

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) メソッドはラベルのキャプション文字列を指定します。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) メソッドは、ラベルがワークシート内のセルにどのようにアタッチされるかを指定します。

次の例は、ワークシートにラベルを追加する方法を示しています。

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

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new label to the worksheet
    Label label = sheet.GetShapes().AddLabel(2, 0, 2, 0, 60, 120);

    // Set the caption of the label
    label.SetText(u"This is a Label");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Label added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにリストボックスコントロールを追加する**

リストボックスコントロールは、単一または複数のアイテム選択を可能にするリストコントロールを作成します。

### **Microsoft Excel の使用**

ワークシートにリストボックスコントロールを配置するには：

1. **フォーム** ツールバーが表示されていることを確認します。
1. **リストボックス** ツールをクリックします。
1. ワークシートエリアで、リストボックスを保持する四角形を定義するためにクリックしてドラッグします。
1. リストボックスがワークシートに配置されたら、コントロールを右クリックして **コントロールの書式設定** をクリックし、入力範囲を指定します。
1. **セルリンク** フィールドで、このリストボックスをリンクするセルのアドレスを指定し、選択タイプ（単一、複数、拡張）属性を設定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

クラス [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) は、ワークシートにリストボックスコントロールを追加するために使用される [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/) という名前のメソッドを提供します。このメソッドは [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) オブジェクトを返します。[**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) クラスはリストボックスを表します。いくつかの重要なメンバを持っています：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) メソッドはリストボックスにリンクされたセルを指定します。
- [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) メソッドはリストボックスを埋めるために使用されるワークシートのセル範囲を指定します。
- [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) メソッドはリストボックスの選択モードを指定します。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) メソッドはリストボックスに3Dシェーディングがあるかどうかを示します。

次の例は、ワークシートにリストボックスを追加する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection
    Cells cells = sheet.GetCells();

    // Input a value
    cells.Get(U16String(u"B3")).PutValue(U16String(u"Choose Dept:"));

    // Set it bold
    Style style = cells.Get(U16String(u"B3")).GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    cells.Get(U16String(u"B3")).SetStyle(style);

    // Input some values that denote the input range for the list box
    cells.Get(U16String(u"A2")).PutValue(U16String(u"Sales"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"Finance"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"MIS"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"R&D"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Marketing"));
    cells.Get(U16String(u"A7")).PutValue(U16String(u"HRA"));

    // Add a new list box
    ListBox listBox = sheet.GetShapes().AddListBox(2, 0, 3, 0, 122, 100);

    // Set the placement type
    listBox.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell
    listBox.SetLinkedCell(U16String(u"A1"));

    // Set the input range
    listBox.SetInputRange(U16String(u"A2:A7"));

    // Set the selection type
    listBox.SetSelectionType(SelectionType::Single);

    // Set the list box with 3-D shading
    listBox.SetShadow(true);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **ボタンコントロールをワークシートに追加する**

ボタンは何かアクションを行うために便利です。時には、ボタンにVBAマクロを割り当てたり、Webページを開くためのハイパーリンクを割り当てることも有用です。

### **Microsoft Excel の使用**

ボタンコントロールをワークシートに配置するには:

1. **フォーム** ツールバーが表示されていることを確認します。
1. **ボタン** ツールをクリックします。
1. ワークシート領域でクリックしてドラッグして、ボタンを配置する矩形を定義します。
1. リストボックスがワークシートに配置されたら、コントロールを右クリックして **フォーマットコントロール** を選択し、VBAマクロを指定し、フォント、配置、サイズ、余白などに関連する属性を設定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

 [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) クラスは、ボタンコントロールをワークシートに追加するための [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/) という名前のメソッドを提供します。このメソッドは [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) オブジェクトを返します。クラス [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) はボタンを表します。いくつかの重要なメンバーがあります:

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) プロパティはボタンのキャプションを指定します。
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) プロパティはボタンコントロールのラベルのフォント属性を指定します。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) プロパティはボタンがワークシートのセルにアタッチされる方法を指定します。
- [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) プロパティはボタンコントロールにハイパーリンクを追加します。ボタンをクリックすると関連するURLに移動します。

次の例は、ワークシートにボタンを追加する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new button to the worksheet
    Drawing::Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);

    // Set the caption of the button
    button.SetText(u"Aspose");

    // Set the Placement Type, the way the Button is attached to the cells
    button.SetPlacement(PlacementType::FreeFloating);

    // Set the font name
    Font font = button.GetFont();
    font.SetName(u"Tahoma");

    // Set the caption string bold
    font.SetIsBold(true);

    // Set the color to blue
    font.SetColor(Color::Blue());

    // Set the hyperlink for the button
    button.AddHyperlink(u"http://www.aspose.com/");

    // Save the file
    workbook.Save(srcDir + u"book1.out.xls");

    std::cout << "Button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにラインコントロールを追加する**

### **Microsoft Excel の使用**

1. **描画** ツールバーで **オートシェイプ** をクリックし、**ライン** を指して、希望のラインスタイルを選択します。
1. ドラッグしてラインを描きます。
1. 次のいずれかを行います。
   1. ラインを開始点から15度の角度で制限するには、ドラッグしながら **SHIFT** キーを押します。
   1. 最初の端点から異なる方向にラインを長くするには、ドラッグしながら **CTRL** キーを押します。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)クラスは[**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/)というメソッドを提供し、これを使ってワークシートに線形状を追加します。メソッドは[**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/)オブジェクトを返します。[**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/)クラスは線を表します。重要なメンバーは次のとおりです：

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) メソッドはラインのフォーマットを指定します。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) メソッドはラインがワークシートのセルにアタッチされる方法を指定します。

次の例は、ワークシートにラインを追加する方法を示しています。異なるスタイルで3つのラインが作成されます。

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

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new line to the worksheet
    LineShape line1 = worksheet.GetShapes().AddLine(5, 0, 1, 0, 0, 250);

    // Set the line dash style
    line1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line1.SetPlacement(PlacementType::FreeFloating);

    // Add another line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line dash style
    line2.GetLine().SetDashStyle(MsoLineDashStyle::DashLongDash);

    // Set the weight of the line
    line2.GetLine().SetWeight(4);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Add the third line to the worksheet
    LineShape line3 = worksheet.GetShapes().AddLine(13, 0, 1, 0, 0, 250);

    // Set the line dash style
    line3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line3.SetPlacement(PlacementType::FreeFloating);

    // Make the gridlines invisible in the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Lines added successfully to the worksheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ラインに矢印を追加する**

Aspose.Cellsでは、矢印付きの直線を描画することもできます。直線に矢印を追加したり、直線のフォーマットを行ったりすることができます。例えば、直線の色を変更したり、直線の太さやスタイルを指定したりすることができます。

次の例は、ラインに矢印を追加する方法を示しています。

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

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line color
    line2.GetLine().SetFillType(FillType::Solid);
    line2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the weight of the line
    line2.GetLine().SetWeight(3);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Set the line arrows
    line2.GetLine().SetEndArrowheadWidth(MsoArrowheadWidth::Medium);
    line2.GetLine().SetEndArrowheadStyle(MsoArrowheadStyle::Arrow);
    line2.GetLine().SetEndArrowheadLength(MsoArrowheadLength::Medium);
    line2.GetLine().SetBeginArrowheadStyle(MsoArrowheadStyle::ArrowDiamond);
    line2.GetLine().SetBeginArrowheadLength(MsoArrowheadLength::Medium);

    // Make the gridlines invisible in the first worksheet
    workbook.GetWorksheets().Get(0).SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **ワークシートに長方形コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに長方形の図形を描画できます。長方形や正方形などを作成できます。また、コントロールの塗りつぶしの色や境界線の色を書式設定することができます。たとえば、長方形の色を変更したり、シェーディングの色を設定したり、必要に応じて長方形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **描画**ツールバーで、**長方形**をクリックします。
1. 長方形を描画するには、ドラッグします。
1. 次のいずれかを行います。
   1. 長方形を開始点から正方形に描画するには、ドラッグしながらSHIFTキーを押し続けます。
   1. 長方形を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)には、ワークシートに長方形を追加するための[**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/)という名前のメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/)は長方形を表します。いくつか重要なメンバーがあります。

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)プロパティは長方形の線の書式属性を指定します。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)プロパティは[**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)を指定し、長方形がワークシートのセルにアタッチされる方法を示します。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)プロパティは長方形の塗りつぶしの書式スタイルを指定します。

次の例は、ワークシートに長方形を追加する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a rectangle control to the first worksheet
    RectangleShape rectangle = excelbook.GetWorksheets().Get(0).GetShapes().AddRectangle(3, 0, 2, 0, 70, 130);

    // Set the placement of the rectangle
    rectangle.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    rectangle.GetLine().SetWeight(4);

    // Set the dash style of the rectangle
    rectangle.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the Excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Rectangle shape added and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートに円弧コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに円弧の図形を描画できます。シンプルな円弧や塗りつぶした円弧を作成できます。また、コントロールの塗りつぶしの色や境界線の色を書式設定することができます。たとえば、円弧の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて図形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **図形の自動スタイル**で、**円弧**をクリックします。
1. 円弧を描画するには、ドラッグします。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)には、ワークシートに円弧形状を追加するための[**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/)という名前のメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/)は円弧を表します。いくつか重要なメンバーがあります。

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)プロパティは円弧形状の線の書式属性を指定します。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)プロパティは[**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)を指定し、円弧がワークシートのセルにアタッチされる方法を示します。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)プロパティは形状の塗りつぶし形式スタイルを指定します。
- [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/)プロパティは右下の行インデックスを指定します。
- [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/)プロパティは右下の列インデックスを指定します。

次の例は、ワークシートに円弧形状を追加する方法を示しています。この例では、塗りつぶしの円弧形状とシンプルな円弧形状の2つを作成します。

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
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add an arc shape
    ArcShape arc1 = worksheet.GetShapes().AddArc(2, 0, 2, 0, 130, 130);

    // Set the fill shape color
    arc1.GetFill().SetFillType(FillType::Solid);
    arc1.GetFill().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc1.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another arc shape
    ArcShape arc2 = worksheet.GetShapes().AddArc(9, 0, 2, 0, 130, 130);

    // Set the line color
    arc2.GetLine().SetFillType(FillType::Solid);
    arc2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc2.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    U16String outputPath = outDir + u"book1.out.xls";
    excelbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートに楕円コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに楕円の図形を描画できます。単純な楕円や塗りつぶした楕円形状を作成し、コントロールの塗りつぶしの色や境界線の色を書式設定できます。たとえば、楕円の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて図形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

- *図形*ツールバーで、*楕円*をクリックします。
- 楕円を描画するには、ドラッグします。
- 以下のいずれか、または両方を行います。
- 楕円を開始点から円として描画するには、ドラッグしながらSHIFTキーを押し続けます。
- 楕円を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)は、ワークシートに楕円形を追加するために使用される[**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/)は楕円形を表し、いくつかの重要なメンバーがあります。

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)プロパティは楕円形の線形式属性を指定します。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)プロパティはワークシート内のセルに楕円形を接続する方法を指定します。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)プロパティは形状の塗りつぶし形式スタイルを指定します。
- [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/)プロパティは右下の行インデックスを指定します。
- [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/)プロパティは右下の列インデックスを指定します。

次の例は、ワークシートに楕円形を追加する方法を示しています。この例では、塗りつぶしの楕円形と単純な円形の2つの楕円形を作成します。

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
    Workbook excelbook;

    // Add an oval shape
    Oval oval1 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(2, 0, 2, 0, 130, 160);

    // Set the placement of the oval
    oval1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval1.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another oval (circle) shape
    Oval oval2 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(9, 0, 2, 15, 130, 130);

    // Set the placement of the oval
    oval2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval2.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにスピンボックスコントロールを追加**

スピンボックスは、ボタン（スピンボタンと呼ばれる）に取り付けられたテキストボックスで、テキストボックスの値を逐次的に変更するためにクリックする上向き矢印と下向き矢印で構成されます。スピンボックスを使用することで、財務モデルの入力がモデルの出力にどのように影響するかを確認できます。スピンボタンを特定の入力セルに取り付けることができます。スピンボタンの上向き矢印または下向き矢印をクリックすると、対象の入力セル内の整数値が増減します。*Aspose.Cells*を使用すると、ワークシートにスピンボックスを作成できます。

### **Microsoft Excel の使用**

ワークシートにスピンボックスコントロールを配置するには:

- *フォーム*ツールバーが表示されていることを確認します。
- *スピンボックス*ツールをクリックします。
- ワークシート領域で、スピンボックスを保持する矩形を定義するためにクリックしてドラッグします。
- スピンボックスをワークシートに配置したら、コントロールを右クリックして *フォーマットコントロール* をクリックし、最大値、最小値、増分値を指定します。
- *セルリンク* フィールドに、このスピンボックスをリンクするセルのアドレスを指定します。
- *OK* をクリックします。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)は、ワークシートにスピンボックスコントロールを追加するために使用される[**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/)はスピンボックスを表し、いくつかの重要なメンバーがあります。

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)プロパティは、スピンボックスにリンクされたセルを指定します。
- [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/)プロパティは、スピンボックス範囲の最大値を指定します。
- [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/)プロパティは、スピンボックス範囲の最小値を指定します。
- [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/)プロパティは、スピンボックスが1行スクロールされる値の量を指定します。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/)プロパティは、スピンボックスに3Dシェーディングがあるかどうかを示します。
- [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/)プロパティは、スピンボックスの現在の値を指定します。

次の例は、ワークシートにスピンボックスを追加する方法を示しています。

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
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Select Value:");

    // Set the font color of the cell
    Style styleA1 = cells.Get(u"A1").GetStyle();
    styleA1.GetFont().SetColor(Color::Red());

    // Set the font text bold
    styleA1.GetFont().SetIsBold(true);

    // Input value into A2 cell
    cells.Get(u"A2").PutValue(0);

    // Set the shading color to black with solid background
    Style styleA2 = cells.Get(u"A2").GetStyle();
    styleA2.SetForegroundColor(Color::Black());
    styleA2.SetPattern(BackgroundType::Solid);

    // Set the font color of the cell
    styleA2.GetFont().SetColor(Color::White());

    // Set the font text bold
    styleA2.GetFont().SetIsBold(true);

    // Add a spinner control
    Spinner spinner = worksheet.GetShapes().AddSpinner(1, 0, 1, 0, 20, 18);

    // Set the placement type of the spinner
    spinner.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    spinner.SetLinkedCell(u"A2");

    // Set the maximum value
    spinner.SetMax(10);

    // Set the minimum value
    spinner.SetMin(0);

    // Set the incremental change for the control
    spinner.SetIncrementalChange(2);

    // Set it 3-D shading
    spinner.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートにスクロールバーコントロールを追加する**

スクロールバーコントロールは、ワークシート上のデータを選択するのを支援するために使用され、スピンボックスコントロールと同様の方法でワークシートに追加できます。ワークシートにコントロールを追加し、セルにリンクすることで、コントロールの現在の位置の数値を返すことができます。

### **Microsoft Excel の使用**

- Excel 2003およびそれ以前のバージョンでは、*フォーム*ツールバーの *スクロールバー* ボタンをクリックし、高さでセルB2:B6をカバーし、列の1/4程度の幅でスクロールバーを作成します。
- Excel 2007では、*開発*タブをクリックし、*挿入*をクリックし、フォームコントロールセクションで*スクロールバー*をクリックします。
- スクロールバーを右クリックし、*フォーマットコントロール*をクリックします。
- 次の情報を入力し、*OK*をクリックします。
  - *現在の値*ボックスに1と入力します。
  - *最小値*ボックスに1と入力します。この値は、スクロールバーの上部をリスト内の最初のアイテムに制限します。
  - *最大値*ボックスに20と入力します。この数はリスト内のエントリの最大数を指定します。
  - *増分変更*ボックスに1と入力します。この値は、スクロールバーが現在の値を増分変更する数を制御します。
  - *ページ変更*ボックスに5と入力します。このエントリは、スクロールバー内のスクロールボックスのいずれかの側をクリックした場合に、現在の値が増分変更される量を制御します。
  - リストで選択されたアイテムに応じてセルG1に数値を入力する場合、*セルリンク*ボックスにG1と入力します。
- スクロールバーが選択されていないことを確認するために、どこかのセルをクリックします。

スクロールバーの上または下のコントロールをクリックすると、セルG1はスクロールバーの現在の値に増分変更を足したり引いたりした数値に更新されます。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)クラスは、ワークシートにスクロールバーコントロールを追加するために使用される[**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/)オブジェクトを返します。[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/)クラスはスクロールバーを表します。いくつかの重要なメンバーがあります:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)プロパティは、スクロールバーにリンクされたセルを指定します。
- [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/)プロパティは、スクロールバー範囲の最大値を指定します。
- [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/)プロパティは、スクロールバー範囲の最小値を指定します。
- [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/)プロパティは、スクロールバーが1行スクロールされたときの値の量を指定します。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/)プロパティは、スクロールバーに3Dの影があるかどうかを示します。
- [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/)プロパティは、スクロールバーの現在の値を指定します。
- [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/)プロパティは、スクロールバー内のスクロールボックスのいずれかの側をクリックした場合に、現在の値が増分変更される量を指定します。

以下の例は、ワークシートにスクロールバーを追加する方法を示しています。

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
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Invisible the gridlines of the worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a value into A1 cell
    cells.Get(u"A1").PutValue(1);

    // Set the font color of the cell
    cells.Get(u"A1").GetStyle().GetFont().SetColor(Color::Maroon());

    // Set the font text bold
    cells.Get(u"A1").GetStyle().GetFont().SetIsBold(true);

    // Set the number format
    cells.Get(u"A1").GetStyle().SetNumber(1);

    // Add a scrollbar control
    ScrollBar scrollbar = worksheet.GetShapes().AddScrollBar(0, 0, 1, 0, 125, 20);

    // Set the placement type of the scrollbar
    scrollbar.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    scrollbar.SetLinkedCell(u"A1");

    // Set the maximum value
    scrollbar.SetMax(20);

    // Set the minimum value
    scrollbar.SetMin(1);

    // Set the incr. change for the control
    scrollbar.SetIncrementalChange(1);

    // Set the page change attribute
    scrollbar.SetPageChange(5);

    // Set it 3-D shading
    scrollbar.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Scrollbar added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートでグループコントロールにグループボックスコントロールを追加する**

特定のグループに所属するラジオボタンやその他のコントロールを実装する必要がある場合は、グループボックスまたは長方形コントロールを含めることによって実装できます。これらの2つのオブジェクトのいずれかがグループのデリミタとして機能します。これらの形を追加した後は、2つ以上のラジオボタンやその他のグループオブジェクトを追加できます。

### **Microsoft Excel の使用**

ワークシートにグループボックスコントロールを配置し、その中にコントロールを配置するには:

- フォームを開始するには、メインメニューで*表示*をクリックし、*ツールバー*と*フォーム*をクリックします。
- *フォーム*ツールバーで、*グループボックス*をクリックし、ワークシート上に長方形を描きます。
- ボックスのキャプション文字列を入力します。
- *フォーム*ツールバーで、*オプションボタン*をクリックし、*グループボックス*内のキャプション文字列の真下をクリックします。
- 再度*フォーム*ツールバーで、*オプションボタン*をクリックし、前のラジオボタンの下に*グループボックス*内をクリックします。
- もう一度*フォーム*ツールバーで、*オプションボタン*をクリックし、前のラジオボタンの下に*グループボックス*内をクリックします。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)クラスは、ワークシートにグループボックスを追加し、コントロールをグループ化するための[**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/)オブジェクトを返します。また、[**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/)クラスの[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)メソッドは、形をグループ化し、[**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)配列をパラメータとして取り、[**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/)オブジェクトを返します。[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/)クラスはグループボックスを表します。いくつかの重要なメンバーがあります:

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)プロパティは、グループボックスのキャプション文字列を指定します。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/)プロパティは、グループボックスに3Dの影があるかどうかを示します。

以下の例は、ワークシートにグループボックスを追加し、コントロールをグループ化する方法を示しています。

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
    Workbook excelbook;

    // Add a group box to the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    GroupBox box = worksheet.GetShapes().AddGroupBox(1, 0, 1, 0, 300, 250);

    // Set the caption of the group box
    box.SetText(u"Age Groups");
    box.SetPlacement(PlacementType::FreeFloating);

    // Make it 2-D box
    box.SetShadow(false);

    // Add a radio button
    RadioButton radio1 = worksheet.GetShapes().AddRadioButton(3, 0, 2, 0, 30, 110);

    // Set its text string
    radio1.SetText(u"20-29");

    // Set A1 cell as a linked cell for the radio button
    radio1.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio1.SetShadow(true);

    // Set the weight of the radio button
    radio1.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio2 = worksheet.GetShapes().AddRadioButton(6, 0, 2, 0, 30, 110);

    // Set its text string
    radio2.SetText(u"30-39");

    // Set A1 cell as a linked cell for the radio button
    radio2.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio2.SetShadow(true);

    // Set the weight of the radio button
    radio2.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio3 = worksheet.GetShapes().AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string
    radio3.SetText(u"40-49");

    // Set A1 cell as a linked cell for the radio button
    radio3.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio3.SetShadow(true);

    // Set the weight of the radio button
    radio3.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Get the shapes
    Vector<Shape> shapeobjects{ box, radio1, radio2, radio3 };

    // Group the shapes
    GroupShape group = worksheet.GetShapes().Group(shapeobjects);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [Aspose.Cells を使用して ActiveX コントロールを追加する](/cells/ja/cpp/add-activex-controls-using-aspose-cells/)
- [ActiveXコントロールを削除](/cells/ja/cpp/remove-activex-control/)
- [ActiveX ComboBoxコントロールを更新](/cells/ja/cpp/update-activex-combobox-control/)
{{< app/cells/assistant language="cpp" >}}
