---
title: Konvertera Excel till PDF med C++
linktitle: Konvertera Excel till PDF
type: docs
weight: 220
url: /sv/cpp/convert-excel-to-pdf/
description: Lär dig hur man konverterar Excel arbetsböcker till PDF format med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel-arbetsböcker till PDF. I detta exempel kommer vi att se hela konverteringen av ett Excel-ark till PDF.

{{% /alert %}}

## **Konvertering av Excelarbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, myndigheter och individer. Det är ett standarddokumentformat, och programvaruutvecklare ombeds ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{% alert color="primary" %}}

Aspose.Cells for C++ skriver direkt information om API och versionsnummer i utdata. Till exempel, när man renderar ett dokument till PDF, fyller Aspose.Cells for C++ i fältet **PDF Producer** med ett värde, t.ex. 'Aspose.Cells v23.2'.

Observera att du kan ändra denna information i utdata genom att använda egenskapen [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **Direkt konvertering**

Aspose.Cells for C++ stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara enkelt en Excel-fil till PDF med [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassens [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metod. [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metoden ger enum-medlemmen [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/), som konverterar de inbyggda Excel-filerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassen genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Utför något arbete (insätt data, tillämpa formatering, sätt in formler, infoga bilder eller andra ritobjekt, och så vidare) på kalkbladet med Aspose.Cells API:er.
1. När kalkbladskoden är klar, anropa [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassens [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metod för att spara kalkbladet.

Filformatet bör vara PDF, så välj *Pdf* (ett fördefinierat värde) från [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)-uppräkningen för att generera det slutgiltiga PDF-dokumentet.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"output.pdf";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the document in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Document saved successfully in PDF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Avancerad konvertering**

Du kan också välja att använda [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-klassen för att ställa in olika attribut för konverteringen. Att ställa in olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-klassen ger dig kontroll över utskrifts-, teckensnitts-, säkerhets- och komprimeringsinställningar för utdata PDF.

Den viktigaste egenskapen är [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), som gör att du kan ställa in PDF-standardens efterlevnandenivå. För närvarande kan du spara till PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u-format. Observera att med PDF/A-formatet är utdatafilen större än en vanlig PDF-fil.

#### **Spara arbetsboken som PDF/A-kompatibla filer**

Kodsnutten nedan demonstrerar hur man använder [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-klassen för att spara Excel-filer till PDF/A-kompatibla PDF-format.

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

    // Instantiate new workbook
    Workbook workbook;

    // Insert a value into the A1 cell in the first worksheet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(U16String(u"Testing PDF/A"));

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set the compliance type
    pdfSaveOptions.SetCompliance(PdfCompliance::PdfA1b);

    // Save the file
    workbook.Save(outDir + u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file created successfully with PDF/A-1b compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Observera att [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/)-egenskapen tillkom med utgåvan av Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Ange PDF-skapandetid**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-klassen kan du hämta eller ange tiden för PDF-skapandet. Följande kod visar användningen av [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcreatedtime/)-egenskapen för att sätta skapandetiden för PDF-filen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"Book1.xlsx";

    // Load excel file containing charts
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions options;
	options.SetCreatedTime(Date{ 2025,01,01 });

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(srcDir + u"output.pdf", options);

    std::cout << "Workbook saved to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Ange alternativet för att kopiera innehållet för tillgänglighet**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-klassen kan du hämta eller ange PDF [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/)-alternativet för att kontrollera innehållsåtkomst i den konverterade PDF-filen.

```cpp
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
    U16String inputPath = srcDir + u"BookWithSomeData.xlsx";

    // Load excel file containing some data
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOpt;

    // Create an instance of PdfSecurityOptions
    PdfSecurityOptions securityOptions;

    // Set AccessibilityExtractContent to false
    securityOptions.SetAccessibilityExtractContent(false);

    // Set the security option in the PdfSaveOptions
    pdfSaveOpt.SetSecurityOptions(securityOptions);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(outDir + u"outFile.pdf", pdfSaveOpt);

    std::cout << "Workbook saved to PDF format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Exportera anpassade egenskaper till PDF**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-klassen kan du exportera anpassade egenskaper i källarbetsboken till PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/)-uppräkningen tillhandahålls för att specificera hur egenskaper exporteras. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Arkiv och sedan Egenskaper, som visas på bilden nedan. Mallfilen "sourceWithCustProps.xlsx" kan laddas ner [här](sourceWithCustProps.xlsx) för testning, och utdata PDF-filen "outSourceWithCustProps" är tillgänglig [här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load excel file containing custom properties
    U16String inputFilePath(u"sourceWithCustProps.xlsx");
    Workbook workbook(inputFilePath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set CustomPropertiesExport property to PdfCustomPropertiesExport::Standard
    pdfSaveOptions.SetCustomPropertiesExport(PdfCustomPropertiesExport::Standard);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    U16String outputFilePath(u"outSourceWithCustProps.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Konverteringsattribut**

Vi arbetar för att förbättra konverteringsfunktionerna vid varje ny version. Aspose.Cells' konvertning av Excel till PDF har fortfarande ett par begränsningar. MapChart stöds inte vid konvertering till PDF-format. Dessutom är några ritobjekt inte väl stödda.

Följande tabel listar alla funktioner som fullt ut eller delvis stöds vid export till PDF med Aspose.Cells. Denna tabell är inte slutgiltig och täcker inte alla kalkbladsattribut, men identifierar de funktioner som inte stöds eller endast delvis stöds vid konvertering till PDF.

| **Dokumentelement** | **Attribut** | **Stöds** | **Noteringar** |
| :- | :- | :- | :- |
| Justering |  | Ja |  |
| Bakgrundsinställningar |  | Ja |  |
| Ram | Färg | Ja |  |
| Ram | Linjestil | Ja |  |
| Ram | Linjebredd | Ja |  |
| Cell Data |  | Ja |  |
| Kommentarer |  | Ja |  |
| Villkorlig formatering |  | Ja |  |
| Dokumentegenskaper |  | Ja |  |
| Ritobjekt |  | Delvis | Skuggor och 3D-effekter för ritobjekt stöds inte väl; WordArt och SmartArt stöds delvis. |
| Teckensnitt | Storlek | Ja |  |
| Teckensnitt | Färg | Ja |  |
| Teckensnitt | Stil | Ja |  |
| Teckensnitt | Understrykning | Ja |  |
| Teckensnitt | Effekter | Ja |  |
| Bilder |  | Ja |  |
| Hyperlänk |  | Ja |  |
| Diagram |  | Delvis | MapChart stöds inte. |
| Sammanfogade celler |  | Ja |  |
| Sidbrytning |  | Ja |  |
| Sidlayout | Sidhuvud/Fot | Ja |  |
| Sidlayout | Marginal | Ja |  |
| Sidlayout | Sidorientering | Ja |  |
| Sidlayout | Sidstorlek | Ja |  |
| Sidlayout | Utskriftsområde | Ja |  |
| Sidlayout | Utskriftstitlar | Ja |  |
| Sidlayout | Skalning | Ja |  |
| Radhöjd/Kolumnbredd |  | Ja |  |
| RTL (Höger till Vänster) Språk |  | Ja |  |

{{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) precis innan du renderar kalkylbladet till PDF-format. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena visas i PDF-filen.

{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till bokmärken i PDF med namngivna destinationer](/cells/sv/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Ändra typsnitt på bara specifika Unicode-tecken vid sparande till PDF](/cells/sv/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Konvertera XLSX-fil till PDF-format](/cells/sv/cpp/convert-xlsx-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format kompatibelt med PDFA-1a](/cells/sv/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla arbetsbokskolumner på en enda PDF-sida](/cells/sv/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Hämta DrawObject och gräns vid rendering till PDF med hjälp av DrawObjectEventHandler-klassen](/cells/sv/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Hämta varningar för teckensnittsbyte vid konvertering av Excel-fil](/cells/sv/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorera fel vid rendering av Excel till PDF](/cells/sv/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF-konvertering](/cells/sv/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer vid sparande till PDF](/cells/sv/cpp/print-comments-while-saving-to-pdf/)
- [Rendera Office-tillägg vid konvertering av Excel till PDF](/cells/sv/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendera en PDF-sida per Excel-ark - Konvertering från Excel till PDF](/cells/sv/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendera Unicode-supplementära tecken i utgående PDF med Aspose.Cells](/cells/sv/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resamplings tillagda bilder - Konvertering från Excel till PDF](/cells/sv/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje arbetsblad i en separat PDF-fil](/cells/sv/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel som PDF med standard- eller minsta storlek](/cells/sv/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Spara angivna arbetsblad som PDF](/cells/sv/cpp/save-specified-worksheets-to-pdf/)
- [Säkra PDF-dokument](/cells/sv/cpp/secure-pdf-documents/)
- [Ange hur textsträngar ska korsas i utgående PDF och bild](/cells/sv/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
