---
title: Konvertera XLSX fil till PDF format med C++
linktitle: Konvertera XLSX fil till PDF format
type: docs
weight: 30
url: /sv/cpp/convert-xlsx-file-to-pdf-format/
description: Lär dig hur du konverterar Excel filer till PDF format med Aspose.Cells for C++ med hög precision och noggrannhet.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av programvara, hårdvara och operativsystem som används för att skapa dessa dokument. En PDF-fil kan innehålla vilken kombination av text, grafik och bilder som helst på ett enhetsoberoende och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar mindre plats än originalfilen.

Ibland måste du konvertera en Microsoft Excel-fil till PDF. För detta krävs en snabb, säker, noggrann och tillförlitlig lösning som låter dig distribuera PDF-dokument världen över. Det finns många konverteringsverktyg som kan göra detta, men du måste se till att utformningen av det ursprungliga Excel-dokumentet bevaras i det genererade PDF-dokumentet. Bilder, diagram, former, datamärkningar, teckensnitt, attribut, färger, sidinställningar, textinriktning, kanter, diagram osv. ska tydligt återges. [Aspose.Cells](https://products.aspose.com/cells/cpp/) säkerställer högkvalitativ konvertering.

Detta dokument är utformat för att ge en omfattande förståelse för hur ett Microsoft Excel-dokument (innehållande bilder, diagram, formatering etc.) kan konverteras till PDF. Därför visar det hur man skapar en enkel konsolapplikation i C++ som konverterar en Excel-fil till PDF med Aspose.Cells API. Konversionen utförs med hög precision och noggrannhet.

{{% /alert %}}

## **Konvertera Excel till PDF**

Detta exempel använder en Excel-fil (SampleInput.xlsx) som mall. Arbetsboken innehåller arbetsblad med diagram och bilder. Varje arbetsblad innehåller olika typer av format med typsnitt, attribut, färger, skuggningseffekter och kantlinjer. Det finns ett kolumndiagram på det första arbetsbladet och en bild på det sista.

### **Den förkonfigurerade Excelfilen**

Mallfilen har tre arbetsblad, inklusive diagram och bilder som media. Det första arbetsbladet har diagram, och det sista arbetsbladet har en bild, som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|

### **Konverteringsprocess**

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att kalla på [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metoden precis innan kalkylbladet renderas till PDF. Detta säkerställer att formelberoende värden omberäknas och att de korrekta värdena visas i PDF-filen.

{{% /alert %}}

### **Resultat**

När ovanstående kod har körts skapas en PDF-fil i mappen Files i din programkatalog.
Följande skärmbilder visar PDF-sidorna. Observera att sidhuvuden och sidfötter också behålls i den utmatade PDF-filen.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|
