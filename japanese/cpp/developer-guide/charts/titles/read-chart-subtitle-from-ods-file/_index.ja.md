---
title: C++でODSファイルからチャートのサブタイトルを読み取る方法
linktitle: ODSファイルからチャートサブタイトルを読む
description: Aspose.Cells for C++を使用して、OpenDocumentスプレッドシート（ODS）ファイルからチャートのサブタイトルを読み取る方法を学びましょう。ガイドは、チャートのサブタイトルを抽出し、アクセスする方法を示します。
keywords: Aspose.Cells for C++、チャートサブタイトルの読み取り、OpenDocumentスプレッドシート、ODSファイル、チャート抽出、データ分析。
type: docs
weight: 160
url: /ja/cpp/read-chart-subtitle-from-ods-file/
---

## **ODSファイルからチャートサブタイトルを読む**

Aspose.Cellsは[**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/)プロパティを使用してODSファイル内のチャートサブタイトルを読み取る機能を提供します。以下のサンプルコードは[サンプルODSファイル](89620481.ods)を読み込み、[**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/)プロパティを使用してチャートサブタイトルを読み取り、それをコンソールウィンドウに出力します。参考のために以下のコードのコンソール出力をご覧ください。

## **サンプルコード**

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

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
