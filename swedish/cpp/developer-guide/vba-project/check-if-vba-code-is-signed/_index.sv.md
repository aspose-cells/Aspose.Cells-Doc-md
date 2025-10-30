---  
title: Kontrollera om VBA koden är signerad med C++  
linktitle: Kontrollera om VBA koden är signerad  
type: docs  
weight: 100  
url: /sv/cpp/check-if-vba-code-is-signed/  
description: Lär dig hur du kontrollerar om VBA koden i Excel filer är signerad med Aspose.Cells och C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells gör det möjligt för användaren att kontrollera om VBA-projektet är signerat eller inte. Använd [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/)-egenskapen för att kontrollera detta.  

{{% /alert %}}  

Följande kod förklarar hur man kontrollerar om VBA-koden är signerad eller inte med hjälp av [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/)-egenskapen. Du kan använda vilken som helst av dina Excel-filer för att testa denna kod. Som test kan du använda [denna Excel-fil som används i koden](5115032.xlsm).  

## ** Kontrollera om VBA-koden är signerad i C++**  

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

## Konsoloutput  

Nedan är konsoloutputen av ovanstående kod med [exempel excelfil](5115032.xlsm) tillhandahållen via länken.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
