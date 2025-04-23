---
title: Implementera 1904 datumsystem med C++
linktitle: Implementera 1904 Datumsystem
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stöder implementeringen av 1904 datumsystemet, vilket gör det möjligt för användare att beräkna och formatera baserat på 1904 års datumsystem. Denna artikel beskriver hur man implementerar 1904 datumsystemet med Aspose.Cells biblioteket.
keywords: Aspose.Cells, 1904 datumssystem, kalkylblad, beräkning, formatering
type: docs
weight: 7000
url: /sv/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel stöder två datumystem: 1900 datumsystem (standarddatumssystemet som implementeras i Excel för Windows) och 1904 datumsystem. 1904 datumsystem används normalt för att möjliggöra kompatibilitet med Macintosh Excel-filer och är standardsystemet om du använder Excel för Macintosh. Du kan ställa in 1904 datumsystemet för Excel-filer med Aspose.Cells.

{{% /alert %}}

För att implementera 1904 datumsystemet i Microsoft Excel (till exempel Microsoft Excel 2003):

1. Från menyn **Verktyg** väljer du **Alternativ** och väljer fliken **Beräkning**.
1. Välj alternativet **1904 datumssystem**.
1. Klicka på **OK**.

|**Välja 1904-datumssystem i Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Se följande kodexempel om hur du uppnår detta med Aspose.Cells API:erna.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
