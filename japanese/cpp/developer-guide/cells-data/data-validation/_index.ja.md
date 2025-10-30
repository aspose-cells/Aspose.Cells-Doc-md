---
title: C++によるデータ検証
linktitle: データ検証
type: docs
weight: 90
url: /ja/cpp/data-validation/
description: Aspose.Cells for C++ APIを使ったデータ検証の追加方法を学びます。
keywords: データ検証の追加、検証値の取得、整数の検証、リストの検証、日付の検証、時間の検証、文字列長の検証、既存の検証にセルエリアの追加、セルのドロップダウンが検証に含まれるかの確認、カスタム検証の追加  
---

{{% alert color="primary" %}}

Microsoft Excelはワークシートデータの自動フィルタリングや検証に優れた機能を提供します。Aspose.CellsはMicrosoft Excelのデータ検証とオートフィルタ機能を完全にサポートしています。本記事では、Microsoft Excelのこれらの機能の使用方法と、Aspose.Cellsでのコーディング方法について解説します。

{{% /alert %}}

## **データ検証の種類と実行**

データ検証は、ワークシートに入力されたデータに関するルールを設定する機能です。たとえば、「日付」と記載された列には日付のみが含まれるようにし、他の列には数字のみが含まれるようにすることができます。あるいは、「日付」と記載された列には特定の範囲内の日付のみが含まれるようにすることもできます。データ検証を使用すると、ワークシートのセルに入力される内容を制御することができます。

Microsoft Excel はさまざまな種類のデータ検証をサポートしています。それぞれの種類は、セルまたはセル範囲に入力されるデータの種類を制御するために使用されます。以下は、それぞれの種類を確認するためのコードスニペットの例です。

- 数値が整数で、つまり小数部を持たないこと。
- 小数点以下の桁に構造が正しいこと。コード例では、セルの範囲に2つの小数点以下があることを定義しています。
- 一覧からの値に制限されていること。一覧の検証では、セルやセル範囲に適用する別々の値の一覧が定義されます。
- 特定の範囲内の日付であること。
- 特定の範囲内の時間であること。
- 指定された文字長内のテキストであること。

### **Microsoft Excel でデータ検証**

Microsoft Excel を使用して検証を作成するには:

1. ワークシートで、検証を適用したいセルを選択します。
2. **データ** メニューから **検証** を選択します。 検証のダイアログが表示されます。
3. **設定** タブをクリックし、設定を入力します。

### **Aspose.Cells を使用したデータ検証**

データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データの入力を特定のタイプやサイズに制限したりすることができます。
Aspose.Cellsでは、各[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスには[**GetValidations()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getvalidations/)プロパティがあり、[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)オブジェクトのコレクションを表します。検証を設定するには、[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)クラスのいくつかのプロパティを以下のように設定します:

- Type：[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/)列挙型の定義された値のいずれかを使用して指定された検証タイプを表します。
- Operator – 検証で使用される演算子を表し、[**OperatorType**](https://reference.aspose.com/cells/cpp/aspose.cells/operatortype/) 列挙型で定義された事前定義の値のいずれかを使用して指定できます。
- Formula1：データ検証の最初の部分に関連付けられた値または式を表します。
- Formula2：データ検証の2番目の部分に関連付けられた値または式を表します。

{0} オブジェクトのプロパティが構成されたら、開発者は作成された検証を使用して、{@1} 構造を使用して検証を行う予定のセル範囲に関する情報を保存できます。

#### **データ検証の種類**

[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) 列挙型には、次のメンバーがあります:

|**メンバー名**|**説明**|
| :- | :- |
|AnyValue|任意の型の値を示します。
|WholeNumber|整数の検証タイプを示します。
|Decimal|10進数の検証タイプを示します。 |
|List|ドロップダウンリストの検証タイプを示します。 |
|Date|日付の検証タイプを示します。 |
|Time|時刻の検証タイプを示します。 |
|TextLength|テキストの長さの検証タイプを示します。 |
|Custom|カスタム検証タイプを示します。 |

##### **整数データの検証**

この種類の検証を使用すると、検証されたセルに指定された範囲内の整数のみを入力できます。以下のコード例では、WholeNumber検証タイプを実装する方法が示されています。例では、Microsoft Excelで作成したデータ検証と同じデータ検証をAspose.Cellsを使用して作成します。

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

    // Create a workbook object
    Workbook workbook;

    // Create a worksheet and get the first worksheet
    Worksheet ExcelWorkSheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Creating a Validation object
    Validation validation = validations.Get(validations.Add(ca));

    // Setting the validation type to whole number
    validation.SetType(ValidationType::WholeNumber);

    // Setting the operator for validation to Between
    validation.SetOperator(OperatorType::Between);

    // Setting the minimum value for the validation
    validation.SetFormula1(u"10");

    // Setting the maximum value for the validation
    validation.SetFormula2(u"1000");

    // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 1;
    area.StartColumn = 0;
    area.EndColumn = 1;

    // Adding the cell area to Validation
    validation.AddArea(area);

    // Save the workbook
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Validation applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **リストデータの検証**

この種類の検証では、ユーザーはドロップダウンリストから値を入力できます。リストにはデータを含む一連の行があります。この例では、リストのソースを保持するために2番目のワークシートが追加されます。ユーザーはリストからのみ値を選択できます。検証エリアは最初のワークシートのセル範囲 A1:A5 です。

ここで重要な点は、[**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/)プロパティを **true** に設定することです。

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

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Add a new worksheet and access it
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet2 = workbook.GetWorksheets().Get(i);

    // Create a range in the second worksheet
    Range range = worksheet2.GetCells().CreateRange(u"E1", u"E4");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"Blue");
    range.Get(1, 0).PutValue(u"Red");
    range.Get(2, 0).PutValue(u"Green");
    range.Get(3, 0).PutValue(u"Yellow");

    // Get the validations collection
    ValidationCollection validations = worksheet1.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Create a new validation to the validations list
    Validation validation = validations.Get(validations.Add(ca));

    // Set the validation type
    validation.SetType(ValidationType::List);

    // Set the operator
    validation.SetOperator(OperatorType::None);

    // Set the in cell drop down
    validation.SetInCellDropDown(true);

    // Set the formula1
    validation.SetFormula1(u"=MyRange");

    // Enable it to show error
    validation.SetShowError(true);

    // Set the alert type severity level
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the error title
    validation.SetErrorTitle(u"Error");

    // Set the error message
    validation.SetErrorMessage(u"Please select a color from the list");

    // Specify the validation area
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 4;
    area.StartColumn = 0;
    area.EndColumn = 0;

    // Add the validation area
    validation.AddArea(area);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **日付データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の日付値、または特定の条件を満たす日付値を入力できます。例では、ユーザーは1970年から1999年の間の日付を入力することに制限されます。ここでは、検証領域はB1セルです。

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

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into the A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Date b/w 1/1/1970 and 12/31/1999");

    // Set row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::Date);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"1/1/1970");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"12/31/1999");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Date Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Date");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Date Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **時間データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の時刻、または特定の条件を満たす時刻を入力できます。例では、ユーザーは午前09:00から11:30の間の時間のみを入力するように制限されます。ここでは、検証領域はB1セルです。

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

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Time b/w 09:00 and 11:30 'o Clock");

    // Set the row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    Validation validation = validations.Get(validations.Add(ca));

    // Set the data validation type
    validation.SetType(ValidationType::Time);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"09:00");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"11:30");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Information);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Time Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Time");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Time Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **テキスト長のデータ検証**

このタイプの検証を使用すると、ユーザーは検証されたセルに指定された長さのテキスト値を入力できます。例では、ユーザーは5文字を超えない文字列値を入力することが制限されています。検証エリアはB1セルです。

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

    // Create a new workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter a string not more than 5 chars");

    // Set row height and column width for the cell
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::TextLength);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::LessOrEqual);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"5");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Warning);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Text Length Error");

    // Set the data validation error message
    validation.SetErrorMessage(u" Enter a Valid String");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"TextLength Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **データ検証ルール**

データ検証が実装されている場合、セルに異なる値を割り当てて検証を確認できます。 [**Cell.GetValidationValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) は検証結果を取得するために使用できます。次の例では、異なる値を使用してこの機能をデモンストレーションしています。テスト用のサンプルファイルは、次のリンクからダウンロードできます。

[sampleDataValidationRules.xlsx](77496339.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **セルの検証がドロップダウンであるかどうかをチェック**

検証がドロップダウンかどうかを確認する

[sampleValidation.xlsx](79527947.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleValidation.xlsx";

    // Create workbook
    Workbook book(inputFilePath);

    // Get worksheet
    Worksheet sheet = book.GetWorksheets().Get(u"Sheet1");

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Check validation for cell A2
    Cell a2 = cells.Get(u"A2");
    Validation va2 = a2.GetValidation();
    if (va2.GetInCellDropDown())
    {
        std::cout << "A2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "A2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell B2
    Cell b2 = cells.Get(u"B2");
    Validation vb2 = b2.GetValidation();
    if (vb2.GetInCellDropDown())
    {
        std::cout << "B2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "B2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell C2
    Cell c2 = cells.Get(u"C2");
    Validation vc2 = c2.GetValidation();
    if (vc2.GetInCellDropDown())
    {
        std::cout << "C2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "C2 is NOT a dropdown" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **既存の検証にCellAreaを追加**

既存の検証に [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) を追加する場合があります。[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) を使用して [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) を追加する場合、Aspose.Cells は新しいエリアがすでに存在するかどうかをチェックします。ファイルに検証が多数ある場合は、これにパフォーマンスの影響があります。これを克服するために、APIは [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) メソッドを提供します。 *checkIntersection* パラメーターは、指定されたエリアと既存の検証エリアとの交差をチェックするかどうかを示します。これを **false** に設定すると、他のエリアをチェックしないようになります。 *checkEdge* パラメーターは、適用エリアをチェックするかどうかを示します。新しいエリアが左上のエリアになる場合、内部設定が再構築されます。新しいエリアが左上のエリアでないことを確信している場合、このパラメーターを **false** に設定できます。

新しい[**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/)を既存の[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)に追加する[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/)メソッドの使用を示すコードスニペット。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ValidationsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    Validation validation = worksheet.GetValidations().Get(0);

    // Create cell area
    CellArea cellArea = CellArea::CreateCellArea(u"D5", u"E7");

    // Adding the cell area to Validation
    validation.AddArea(cellArea, false, false);

    // Save the output workbook
    workbook.Save(outDir + u"ValidationsSample_out.xlsx");

    std::cout << "Validation added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

ソースエクセルファイルと出力エクセルファイルが添付されています。

[ソースファイル](96928093.xlsx)

[出力ファイル](96928220.xlsx)

## **高度なトピック**
- [ODS ファイルでのセル検証を取得](/cells/ja/cpp/get-cell-validation-in-ods-files/)
- [セルに適用された検証を取得する](/cells/ja/cpp/get-validation-applied-on-a-cell/)
- [セルの値がデータ検証ルールを満たすかどうかを確認する](/cells/ja/cpp/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="cpp" >}}
