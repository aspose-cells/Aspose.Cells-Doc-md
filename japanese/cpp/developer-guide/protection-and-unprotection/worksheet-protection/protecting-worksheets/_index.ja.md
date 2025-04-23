---
title: C++を使用したシートの保護
linktitle: ワークシートの保護
type: docs
weight: 10
url: /ja/cpp/protecting-worksheets/
description: Aspose.Cellsを使用して、Microsoft Excelファイルのシート、行、列、特定のセルを保護する方法を学びます。
---

{{% alert color="primary" %}}

シートが保護されている場合、ユーザーの操作は制限されます。例えば、データの入力や行・列の挿入・削除などができなくなります。

{{% /alert %}}

## **ワークシートを保護**

### **紹介**

Microsoft Excelの一般的な保護オプション:

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは機密データを非表示または保護しないため、ファイルの暗号化とは異なります。一般的に、ワークシートの保護はプレゼンテーション目的に適しています。ユーザーはワークシート内のデータ、コンテンツ、および書式設定を変更できなくなります。

### **ワークシートを保護する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスを許可する[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートに保護を適用するために使用される[**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)メソッドを提供します。[**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)メソッドは以下のパラメータを受け付けます:

- 保護タイプ、ワークシートに適用する保護の種類。保護タイプは[**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/)列挙型のヘルプを使用して適用されます。
- 新しいパスワード、ワークシートを保護するために使用する新しいパスワード。
- 古いパスワード、ワークシートがすでにパスワードで保護されている場合は、古いパスワードを渡します。ワークシートがすでに保護されていない場合は、nullを渡します。

[**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/)列挙型には、次の事前定義の保護タイプが含まれています:

|**保護タイプ**|**説明**|
| :- | :- |
|All|このワークシート上で何も変更できない|
|Contents|このワークシートにデータを入力できない|
|Objects|描画オブジェクトを変更できない|
|Scenarios|保存されたシナリオを変更できない|
|Structure|ユーザーは構造を変更できません|
|Windows|保護はウィンドウに適用されています|
|None|保護は適用されていません|

以下の例は、ワークシートにパスワードを設定して保護する方法を示しています。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

上記のコードを使用してワークシートを保護した後、ワークシートの保護を開いて確認することができます。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログが表示されます:

|**ユーザーがワークシートを変更できないと警告するダイアログ**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

ワークシートで作業するには、**ツール**メニューの**保護**から**ワークシートの保護を解除**を選択します。

ワークシートの保護を解除メニュー項目を選択すると、次のようなダイアログが開きます。パスワードを入力するように求められます。

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excelを使用してワークシート内の一部のセルを保護する**

ワークシート内の特定のセルをロックする必要がある場合があります。ワークシート内の特定のセルをロックするには、ワークシートの他のすべてのセルをロック解除する必要があります。ワークシートのすべてのセルは既にロックされています。MS Excelに任意のExcelファイルを開いて**書式 | セル...**をクリックして**セルの書式**ダイアログボックスを表示し、**保護**タブをクリックし、「ロック」のチェックボックスがデフォルトでチェックされていることを確認できます。

次のポイントは、MS Excelを使用していくつかのセルをロックする方法を説明しています。この方法は、Microsoft Office Excel 97、2000、2002、2003およびそれ以降のバージョンに適用されます。

1. **全選択**ボタン(行1の行番号の直上および列文字Aの左直上の灰色の四角形)をクリックしてワークシート全体を選択します。
1. **書式**メニューの**セル**をクリックし、**保護**タブをクリックし、**ロック**のチェックボックスをクリアします。
   これにより、ワークシートのすべてのセルがロック解除されます
   **セル**コマンドが利用できない場合、ワークシートの一部は既にロックされている可能性があります。 **ツール**メニューで、**保護**を指して、**ワークシートの保護を解除**をクリックします。
1. ロックしたいセルだけを選択し、ステップ2を繰り返しますが、この時に**ロック**のチェックボックスを選択します。
1. **ツール**メニューで**保護**を指して、**ワークシートの保護**をクリックし、**OK**をクリックします。
1. **ワークシートの保護**ダイアログボックスでは、ユーザーが変更できる要素を指定するオプションとパスワードを指定することができます。

### **Aspose Cellsを使用してワークシート内の一部のセルを保護する**

この方法では、Aspose.Cells APIのみを使用してタスクを実行します。

例: 次の例は、ワークシート内の一部のセルを保護する手順を示しています。まずワークシートのすべてのセルをロック解除し、それから3つのセル（A1、B1、C1）をロックします。最後にワークシートを保護します。 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトには、真偽値プロパティ[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)が含まれています。 [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)プロパティをtrueまたはfalseに設定し、*Column/Row.ApplyStyle()*メソッドを使用して希望の属性で行または列をロックまたはロック解除できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **ワークシート内の行を保護する**

Aspose.Cellsを使用すると、ワークシート内の任意の行を簡単にロックできます。ここでは、ワークシート内の特定の行に[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/)メソッドを[**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)クラスを使用して[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)を適用できます。このメソッドは、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトと[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)オブジェクトを引数に取り、適用される書式に関連するすべてのメンバーを持っています。

次の例は、ワークシート内の行を保護する手順を示しています。まず、ワークシートのすべてのセルをロック解除してから、第1行をロックします。最後にワークシートを保護します。 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトには、真偽値プロパティ[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)が含まれています。 [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)プロパティをtrueまたはfalseに設定することで、[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)オブジェクトを使用して行または列をロックまたはロック解除できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ワークシート内の列を保護する**

Aspose.Cellsを使用すると、ワークシート内の任意の列を簡単にロックできます。ここでは、ワークシート内の特定の列に[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/)メソッドを[**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/)クラスを使用して[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)を適用できます。このメソッドは、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトと[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)オブジェクトを引数に取り、適用される書式に関連するすべてのメンバーを持っています。

次の例は、ワークシート内の列を保護する手順を示しています。まず、ワークシートのすべてのセルをロック解除してから、第1列をロックします。最後にワークシートを保護します。 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトには、真偽値プロパティ[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)が含まれています。 [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)プロパティをtrueまたはfalseに設定することで、[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)オブジェクトを使用して行または列をロックまたはロック解除できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ユーザーに範囲の編集を許可する**

次の例は、保護されたワークシートで範囲の編集を許可する方法を示しています。

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
