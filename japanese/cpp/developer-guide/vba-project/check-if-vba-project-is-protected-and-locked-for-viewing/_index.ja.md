---
title: C++でVBAプロジェクトが保護されており、閲覧ロックされているかどうかを確認する
linktitle: VBA（Visual Basic for Applications）プロジェクトが保護されて表示ロックされているかどうかを確認
type: docs
weight: 30
url: /ja/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Excelファイル内のVBAプロジェクトが保護されているか、閲覧ロックされているかどうかをAspose.Cells for C++を使用して確認する方法を学びます。
---

## C++でVBAプロジェクトが保護されており閲覧可能かどうかを確認する方法

Aspose.Cellsを使用すると、ExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されているかつ、閲覧のためにロックされているかどうかを確認できます。そのためにAPIは[**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/)プロパティを提供します。閲覧用にロックされている場合、[**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/)プロパティは**true**を返します。

## **サンプルコード**

次のサンプルコードは、[サンプルExcelファイル](43352065.xlsm)をロードし、そのExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されており閲覧用にロックされているかどうかを確認します。参考のために、そのコンソール出力もご覧ください。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

上記のサンプルコードを提供された[サンプル Excelファイル](43352065.xlsm)で実行した際のConsoleの出力です。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
