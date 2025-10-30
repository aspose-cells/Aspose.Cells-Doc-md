---  
title: VBAコードに署名されているかどうかをC++で確認する  
linktitle: VBAコードが署名されているかどうかをチェック  
type: docs  
weight: 100  
url: /ja/cpp/check-if-vba-code-is-signed/  
description: Aspose.Cellsを使用してC++でExcelファイルのVBAコードが署名されているかどうかを確認する方法を学びます。  
---  

{{% alert color="primary" %}}  

Aspose.Cellsは、VBAコードプロジェクトが署名されているかどうかを確認できます。[**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) プロパティを使用して、VBAコードプロジェクトが署名されているかどうかを確認してください。  

{{% /alert %}}  

以下のコードは、[**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) プロパティを使用してVBAコードが署名されているかどうかを確認する方法を解説しています。任意のExcelファイルを使用してこのコードをテストできます。テスト用には[このExcelファイル](5115032.xlsm)を使用できます。  

## **C++でVBAコードに署名されているかどうかを確認する**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## コンソール出力  

上記のコードのコンソール出力は、提供された[サンプルExcelファイル](5115032.xlsm)を使用して以下のようになります。  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
