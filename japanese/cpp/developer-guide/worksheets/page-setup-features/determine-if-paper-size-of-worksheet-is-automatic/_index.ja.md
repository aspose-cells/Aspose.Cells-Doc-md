---
title: C++でワークシートの用紙サイズが自動かどうかを判断する
linktitle: ワークシートの用紙サイズが自動かどうかを判定する
type: docs
weight: 90
url: /ja/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: この文章は、C++のAPIまたはサンプルコードを使用して、ワークシートの用紙サイズが自動かどうかをプログラム的に判断する方法を説明します。
keywords: C++でワークシートの用紙サイズが自動かどうかを判断する
---

## **可能な使用シナリオ**

ほとんどの場合、ワークシートの用紙サイズは自動設定です。自動の場合、多くは*レター*に設定されています。ユーザーが設定した場合は自動ではありません。`Worksheet`クラスの[**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/)プロパティを使って紙のサイズが自動かどうかを調べることができます。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプルコードは、次の2つのExcelファイルをロードし

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

そして最初のワークシートの用紙サイズが自動かどうかを確認します。Microsoft Excelでは、ページ設定ウインドウを通じて用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

上記のサンプルコードを指定されたサンプルExcelファイルで実行したときのコンソール出力は次の通りです。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
