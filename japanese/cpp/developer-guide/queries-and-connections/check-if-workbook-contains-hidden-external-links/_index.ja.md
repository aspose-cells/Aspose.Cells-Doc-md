---
title: C++を使用してWorkbookに隠されたExternal Linksが含まれているかどうかを確認する
linktitle: ワークブックに非表示の外部リンクが含まれているかどうかを確認
type: docs
weight: 230
url: /ja/cpp/check-if-workbook-contains-hidden-external-links/
description: Aspose.Cells for C++を使用してExcelワークブックで隠された外部リンクを検出する方法を学びます。
---

## **可能な使用シナリオ**
時には、ワークブックにはMicrosoft Excelで閲覧できない隠された外部リンクが含まれている場合があります。 Aspose.Cellsは、見えるか見えないかに関係なく、すべての外部リンクを取得します。ただし、[ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) プロパティを確認して、その外部リンクが見えるかどうかを確認できます。

## **ワークブックに非表示の外部リンクが含まれる [ソースExcelファイル](5115413.xlsx) をロードする以下のサンプルコードでは、Microsoft Excelで表示されない非表示の外部リンクが含まれています。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) プロパティを出力した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティを出力します。以下のコンソール出力では、すべての外部リンクが非表示であることがわかります。**
以下のサンプルコードは、隠された外部リンクを含む[ソースExcelファイル](5115413.xlsx)を読み込みます。これらのリンクはMicrosoft Excelでは表示できませんが、ワークブック内には存在します。[ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/) プロパティを印刷した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) プロパティも出力されます。以下のコンソール出力では、すべての外部リンクが非表示であることが確認できます。

### **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **コンソール出力**
与えられた [サンプルExcelファイル](5115413.xlsx) で上記のサンプルコードを実行した場合の、コンソール出力は次のとおりです。

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
