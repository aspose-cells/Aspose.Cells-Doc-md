---
title: C++を使ってExcelワークブックのVBAプロジェクトにパスワード保護をかける
linktitle: ExcelワークブックのVBAプロジェクトにパスワードを設定する
type: docs
weight: 10
url: /ja/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Aspose.Cellsを使ったExcelワークブックのVBAプロジェクトにパスワードをかける方法を学びます。
---

## **C++でExcelワークブックのVBAプロジェクトにパスワードを設定**

Aspose.Cellsの[**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/)メソッドを使用して、ワークブックのVBA（Visual Basic for Applications）プロジェクトにパスワード保護を設定できます。

## **サンプルコード**

以下のサンプルコードは、[サンプルExcelファイル](43352067.xlsm)を読み込み、そのVBAプロジェクトにアクセスして、パスワードで保護します。最後に、[出力Excelファイル](43352068.xlsm)として保存します。

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"samplePasswordProtectVBAProject.xlsm";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outputPasswordProtectVBAProject.xlsm";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Lock the VBA project for viewing with password
    vbaProject.Protect(true, u"11");

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "VBA project password protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
