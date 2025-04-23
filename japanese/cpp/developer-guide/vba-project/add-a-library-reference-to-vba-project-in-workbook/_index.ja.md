---
title: C++でワークブックのVBAプロジェクトにライブラリ参照を追加する
linktitle: ワークブックのVBAプロジェクトにライブラリの参照を追加
type: docs
weight: 80
url: /ja/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Aspose.Cells for C++を使用して、ワークブックのVBAプロジェクトにライブラリ参照を追加または登録する方法を学びます。
---

{{% alert color="primary" %}}

時折、コードを通じてVBAプロジェクトにライブラリ参照を追加または登録する必要があります。Aspose.Cellsの[**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/)メソッドを使用して行うことができます。

{{% /alert %}}

## **Microsoft ExcelのVBAプロジェクトにライブラリ参照を追加する**

Microsoft Excelでは、**ツール > 参照設定...**をクリックしてVBAプロジェクトにライブラリ参照を追加できます。

## **Aspose.Cellsを使用してワークブックのVBAプロジェクトにライブラリ参照を追加する**

次のサンプルコードは、ブックのVBAプロジェクトに2つのライブラリ参照を追加または登録します。

```c++
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

    // Path of output excel file
    U16String outputPath = outDir + u"Output_out.xlsm";

    // Create a new workbook
    Workbook workbook;

    // Get the VBA project from the workbook
    VbaProject vbaProj = workbook.GetVbaProject();

    // Add registered references to the VBA project
    vbaProj.GetReferences().AddRegisteredReference(u"stdole", u"*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
    vbaProj.GetReferences().AddRegisteredReference(u"Office", u"*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "VBA project references added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
