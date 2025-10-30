---
title: Konvertera arbetsblad till bild med ImageOrPrint alternativ med C++
linktitle: Konvertera arbetsblad till bild
type: docs
weight: 90
url: /sv/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Lär dig hur du konverterar ett arbetsblad till en bildfil och använder olika bild och utskriftsalternativ med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och tillämpar olika bild- och utskriftsalternativ för bilden, såsom upplösning, TIFF-komprimering, bildformat och sidkvalitet.

{{% /alert %}}

## **Spara arbetsblad till bilder - Olika tillvägagångssätt**

Ibland kan du behöva presentera dina arbetsblad som en grafisk representation. Du kan behöva visa arbetsblybilder i dina applikationer eller webbsidor, infoga dem i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Kort sagt, du vill att ett arbetsblad ska renderas som en bild så att du kan använda det någon annanstans. Aspose.Cells stödjer konvertering av arbetsblad i Excel-filer till bilder. Dessutom stöder Aspose.Cells att ställa in olika alternativ som bildformat, upplösning (både vertikal och horisontell), bildkvalitet och andra bild- och utskriftsalternativ.

Du kan överväga Office Automation, men det har sina egna nackdelar. Det finns flera skäl och problem inblandade, såsom säkerhet, stabilitet, skalbarhet, hastighet, pris och funktioner. Kort sagt, det finns många skäl, där det främsta är att Microsoft själva starkt rekommenderar emot Office-automation från mjukvarulösningar.

Den här artikeln visar hur man skapar en konsolapplikation i Visual Studio, utför konvertering av ett arbetsblad till en bild med hjälp av olika bild- och utskriftsalternativ med några få och enkel rad kod med Aspose.Cells API.

Du måste inkludera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) namespace i ditt program/projekt. Det har flera värdefulla klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) och så vidare.

Klassen [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) representerar ett arbetsblad för att rendera bilder för arbetsbladet. Den har en överbelastad [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) metod som direkt kan konvertera ett arbetsblad till bildfil(er) specificerade med dina önskade attribut eller alternativ. Den kan returnera ett bitmap-objekt, och du kan spara en bildfil till disk/ström. Flera bildformat stöds, såsom BMP, PNG, GIF, JPEG, TIFF, EMF och liknande.

## **Användning av Aspose.Cells för att konvertera arbetsblad till bild med ImageOrPrint-alternativ**

### **Skapa en mallarbetsbok i Microsoft Excel**

Jag skapade ett nytt arbetsbok i MS Excel och lade till data i det första arbetsbladet. Nu kommer jag att konvertera arbetsbladet "Sheet1" i mallfilen till en bildfil "SheetImage.tiff" och tillämpa olika bildalternativ som horisontell och vertikal upplösning, TiffCompression och så vidare.

### **Ladda ner och installera Aspose.Cells**

Först måste du [ladda ner](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. Installera det på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och injicerar endast vattenstämplar i de producerade dokumenten.

### **Skapa ett projekt**

Starta Visual Studio och skapa en ny konsolapplikation. Det här exemplet visar en C++-konsolapplikation.

### **Lägg till referenser**

Det här projektet kommer att använda Aspose.Cells. Så, du måste lägga till en referens till Aspose.Cells-komponenten i ditt projekt. Till exempel, lägg till en referens till `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **Konvertera arbetsblad till en bildfil**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konverteringsalternativ**

Det är möjligt att spara specifika sidor som bilder. Följande kod konverterar de första och andra arbetsbladen i en arbetsbok till JPG-bilder.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Bildkonvertering med WorkbookRender**

Ett TIFF-bild kan innehålla mer än en frame. Du kan spara hela arbetsboken som en enskild TIFF-bild med flera frames eller sidor:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
