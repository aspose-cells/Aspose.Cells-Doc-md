---
title: Kombinera flera arbetsböcker till en enkelt arbetsbok med C++
linktitle: Arbetsboksfusion
type: docs
weight: 66
url: /sv/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Lär dig att kombinera flera arbetsböcker till en arbetsbok med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland behöver du kombinera arbetsböcker med olika innehåll som bilder, diagram och data till en enda arbetsbok. Aspose.Cells stöder denna funktion. Den här artikeln visar hur man skapar en konsolapplikation i Visual Studio och kombinerar arbetsböcker med några enkla kodrader med Aspose.Cells.

{{% /alert %}}

## **Kombinera arbetsböcker med bilder och diagram**

Exempelkoden kombinerar två arbetsböcker till en enda arbetsbok med hjälp av Aspose.Cells. Koden laddar de ursprungliga arbetsböckerna, använder metoden [**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) för att kombinera dem och sparar utdataarbetsboken.

### **Källarbetsböcker**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Resultatarbetsböcker**

- [combined.xlsx](5473095.xlsx)

### **Skärmbilder**

Här är skärmbilder på käll- och resultatarbetsböcker.

{{% alert color="primary" %}}

Du kan använda vilka källarbetsböcker som helst. Dessa bilder är bara för illustration.

{{% /alert %}}

**Den första arbetsbokens arbetsblad - staplad** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Andra arbetsbladet i arbetsboken - linje** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Första arbetsbladet i bildarbetsboken - bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alla tre arbetsblad i den kombinerade arbetsboken - staplad, linje, bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Kombinera flera arbetsblad till ett enda arbetsblad](/cells/sv/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Sammanfoga filer](/cells/sv/cpp/merge-files/)
