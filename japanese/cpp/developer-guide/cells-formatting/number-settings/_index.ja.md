---
title: 数値設定とC++
linktitle: 数字の設定
description: Aspose.Cellsは、さまざまなセルの数値設定をサポートするC++ライブラリです。この記事では、Aspose.Cellsライブラリを使用してセルの数値設定を管理し、必要に応じてスプレッドシートの数値フォーマットを調整する方法を紹介します。
keywords: Aspose.Cells、C++ライブラリ、電子スプレッドシート、セルの数値設定、書式設定、管理、数字と日付の形式
type: docs
weight: 10
url: /ja/cpp/cells-number-settings/
---

## **数字と日付の表示形式を設定する方法**

Microsoft Excelの非常に強力な機能の1つは、ユーザーが数値値や日付の表示形式を設定できることです。数値データは10進数、通貨、パーセンテージ、分数、会計などを含むさまざまな値を表すために使用できることを知っています。すべてのこれらの数値値は、それが表す情報の種類に応じて異なる形式で表示されます。同様に、日付や時刻を表示するための多くの形式があります。
Aspose.Cellsはこの機能をサポートし、開発者が数値や日付の表示形式を設定できるようにします。

### **Microsoft Excelで表示形式を設定する方法**

Microsoft Excelで表示形式を設定するには：

1. 任意のセルを右クリックします。
1. **セルの書式設定** を選択します。ダイアログが表示され、さまざまな種類の値の表示形式を設定するのに使用されます。

ダイアログの左側には**一般**、**数値**、**通貨**、**会計**、**日付**、**時間**、**パーセンテージ**などの値のカテゴリが多数あります。Aspose.Cellsはこれらすべての表示形式をサポートしています。

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各項目は[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

Aspose.Cellsは、[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)および[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)メソッドを提供します。これらのメソッドはセルの書式設定を取得および設定するために使用されます。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)クラスは、数値や日付の表示形式に対応するためのいくつかの有用なプロパティを提供します。

### **組み込みの数値形式の使用方法**

Aspose.Cellsは、数値や日付の表示形式を構成するためのいくつかの組み込みの数値形式を提供しています。これらの組み込みの数値形式は、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトの[**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/)プロパティを使用して適用できます。すべての組み込みの数値形式には固有の数値が割り当てられています。開発者は[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトの[**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/)プロパティに任意の数値を割り当てて、表示形式を適用することができます。この方法は高速です。Aspose.Cellsでサポートされている組み込みの数値形式は以下のとおりです。

|**値**|**タイプ**|**フォーマット文字列**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **カスタム数値形式の使用方法**

表示形式を設定するために独自のカスタムフォーマット文字列を定義するには、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトの[**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)プロパティを使用します。この方法は事前に設定された形式を使用するよりも速くはありませんが、柔軟性があります。

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

[**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)プロパティを使用して数値形式を設定する場合、[**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/)プロパティを使用して設定された以前の形式は上書きされ、その逆も同様です。

{{% /alert %}}

## **高度なトピック**
- [Style.Customプロパティを設定する際のカスタム数値形式を確認する](/cells/ja/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [サポートされている数値形式のリスト](/cells/ja/cpp/list-of-supported-number-formats/)
- [カスタム日付形式パターン g および ge mm dd の表現](/cells/ja/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [ブックでのカスタム数値小数点およびグループの区切りの指定](/cells/ja/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNumカスタムパターンの書式設定の指定](/cells/ja/cpp/specifying-dbnum-custom-pattern-formatting/)
