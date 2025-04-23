---  
title: Überprüfen, ob VBA Code signiert ist mit C++  
linktitle: Überprüfen, ob VBA Code signiert ist  
type: docs  
weight: 100  
url: /de/cpp/check-if-vba-code-is-signed/  
description: Erfahren Sie, wie Sie überprüfen, ob der VBA Code in Excel Dateien mit Aspose.Cells und C++ signiert ist.  
---  

{{% alert color="primary" %}}  

Aspose.Cells ermöglicht es dem Benutzer, zu überprüfen, ob das VBA-Code-Projekt signiert ist oder nicht. Bitte verwenden Sie die [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/)-Eigenschaft, um zu überprüfen, ob das VBA-Code-Projekt signiert ist.  

{{% /alert %}}  

Der folgende Code erklärt, wie Sie überprüfen können, ob das VBA-Code-Projekt signiert ist oder nicht, mithilfe der [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/)-Eigenschaft. Sie können Ihre beliebigen Excel-Dateien verwenden, um diesen Code zu testen. Zum Testen können Sie [diese Excel-Datei verwenden, die im Code verwendet wird](5115032.xlsm).  

## **Überprüfen, ob VBA-Code signiert ist in C++**  

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

## Konsolenausgabe  

Unten ist die Konsolenausgabe des obigen Codes mithilfe der [Beispieldatei](5115032.xlsm), die über den Link bereitgestellt wird.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
