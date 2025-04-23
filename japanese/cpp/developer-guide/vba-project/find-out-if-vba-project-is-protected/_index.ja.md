---  
title: C++を使用してVBAプロジェクトが保護されているかどうかを調べる  
linktitle: VBAプロジェクトが保護されているかどうかを調べる  
type: docs  
weight: 20  
url: /ja/cpp/find-out-if-vba-project-is-protected/  
description: Aspose.Cellsを使用してExcelファイルのVBAプロジェクトが保護されているかどうかを確認します。  
---  

## **C++でVBAプロジェクトが保護されているかどうかを確認する**

Aspose.Cellsを使用して[**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/)プロパティでExcelファイルのVBA（Visual Basic Applications）プロジェクトが保護されているかどうかを確認できます。

## **サンプルコード**

次のサンプルコードは、ブックを作成し、そのVBAプロジェクトが保護されているかどうかを確認します。そしてVBAプロジェクトを保護し、再び保護されているかどうかを確認します。コンソール出力も参照してください。保護前は[**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/)は**false**を返し、保護後は**true**を返します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

上記サンプルコードのコンソール出力の参考情報です。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
