---
title: C++でチャートのワークシートを取得する
linktitle: チャートのワークシートを取得
description: Aspose.Cells for C++を使用して Excel のチャートに関連付けられたワークシートを取得する方法を学びます。ガイドでは、ワークシートにアクセスし、操作を行ってチャートの基礎データを操作する方法を示します。
keywords: Aspose.Cells for C++、Excelチャート、ワークシート、データ操作、基礎データ、操作
type: docs
weight: 1000
url: /ja/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

時には、チャートのリファレンスからワークシートにアクセスしたい場合があります。Aspose.Cellsは、[**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/)メソッドを提供しており、これによりチャートを含むワークシートのリファレンスを返します。

{{% /alert %}}

以下の例では、[**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/)メソッドの使用方法を示します。まずワークシートの名前を出力し、その後最初のチャートにアクセスします。次に、[**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/)メソッドを使用して再びワークシートの名前を出力します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

以下はサンプルコードのコンソール出力です。同じワークシート名が2回印刷されることがわかります。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
