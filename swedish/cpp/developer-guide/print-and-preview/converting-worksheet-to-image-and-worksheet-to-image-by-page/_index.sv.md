---
title: Konvertera arbetsblad till bild och arbetsblad till bild per sida med C++
linktitle: Konvertera kalkylblad till bild och Kalkylblad till bild per sida
type: docs
weight: 80
url: /sv/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Lär dig hur du konverterar ett arbetsblad till en bildfil och ett arbetsblad med flera sidor till en bildfil per sida med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklare en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och ett arbetsblad med flera sidor till en bildfil per sida.

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kanske behöver infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Kort sagt, du vill rendera kalkylbladet som en bild. Aspose.Cells stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells konvertering av en arbetsbok till flera bildfiler, en per sida.

Du kan använda Office Automation för att uppnå detta, men Office automation har sina nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt, det finns många skäl, men det huvudsakliga är att Microsoft själva starkt rekommenderar att motstå Office-automatisering.

{{% /alert %}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil**

Den här artikeln visar hur man skapar en konsolapplikation i Visual Studio, konverterar ett kalkylblad till en bild och konverterar ett kalkylblad till en bild för varje kalkylblad med några få och enkla rader kod med hjälp av Aspose.Cells API.

Du behöver inkludera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) namespace i ditt program/projekt. Den har flera värdefulla klasser, såsom [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) och så vidare. [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) klassen representerar ett arbetsblad för att rendera bilder av arbetsbladet och har en överlagrad [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) metod som kan konvertera ett arbetsblad till bildfiler direkt med alla inställningar eller alternativ. Den kan returnera ett `System.Drawing.Bitmap` objekt, och du kan spara en bildfil till disk/ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF och andra.

Den här artikeln förklarar hur man:

- Konvertera ett kalkylblad till en bild
- Konvertera varje sida i ett kalkylblad till en bild

Det här exemplet visar hur man använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbok till en bildfil.

### **Installationsprojekt**

1. Först, [ladda ner Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Installera det på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärkningsläget har ingen tidsbegränsning och injicerar endast vattenstämplar i producerade dokument. Starta nu Visual Studio och skapa ett nytt konsolprogram. Detta exempel använder ett C++ konsolprogram. Lägg till en referens till Aspose.Cells i det skapade projektet.

### **Konvertera kalkylblad till bildfil**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första kalkylbladet: **Testbook.xlsx** (1 kalkylblad). Nästa steg är att konvertera mallfilens kalkylblad Sheet1 till en bildfil som kallas SheetImage.jpg.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i **Testbook.xlsx** till en bildfil för att förklara hur enkel denna konvertering är.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Använda Aspose.Cells för att konvertera arbetsblad till bildfil per sida**

Detta exempel visar hur man använder Aspose.Cells för att konvertera ett arbetsblad från en mallarbok som har flera sidor till en bildfil per sida.

### **Konvertera kalkylblad till bild per sida**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första arbetsbladet: **Testbook2.xlsx** (1 arbetsblad).

Nu, konvertera mallfilens arbetsblad Sheet1 till bildfiler (en fil per sida). Eftersom jag redan skapat konsolapplikationen för att utföra kopieringsuppgiften, kommer jag att hoppa över de stegen för att skapa konsolapplikationen och gå direkt till arbetsbladskonverteringsstegen.

Följande är koden som används av komponenten för att slutföra uppgiften. Den konverterar Sheet1 i Testbook2.xlsx till bildfiler per sida.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
