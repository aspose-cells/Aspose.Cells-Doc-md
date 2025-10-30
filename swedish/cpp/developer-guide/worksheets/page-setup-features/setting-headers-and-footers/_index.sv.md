---
title: Inställningar av sidhuvuden och sidfötter med C++
linktitle:  Inställa sidhuvuden och sidfötter 
type: docs
weight: 30
url: /sv/cpp/setting-headers-and-footers/
description: Denna artikel förklarar hur man programmatiskt infogar en bild i sidhuvuden och sidfötter i Excel ark genom att ställa in sidhuvud och sidfot med skriptkommandon med hjälp av C++ API eller bibliotek.
keywords: infoga bild i excel sidhuvud sidfot c++, ställ in excel sidhuvud sidfot skriptkommandon c++
---

{{% alert color="primary" %}}

Sidhuvuden och sidfötter är textrader som visas under övre marginalen eller ovanför den nedre marginalen. Det är möjligt att lägga till sidhuvuden och sidfötter i kalkylbladen också. Sidhuvuden och sidfötter kan användas för att visa användbar information som sidnummer, författarnamn, ämnesnamn eller datum och tid. Sidhuvuden och sidfötter hanteras med sidlayoutinställningarna.

{{% /alert %}}

## **Ställa in sidhuvuden och sidfötter**

Aspose.Cells möjliggör att lägga till sidhuvuden och sidfötter till kalkylblad vid körning, men vi rekommenderar att sidhuvuden och sidfötter ställs in manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett GUI-verktyg för att ställa in sidhuvuden och sidfötter för att spara ansträngning och utvecklingstid. Aspose.Cells kan importera filen och spara inställningarna.

För att lägga till sidhuvuden och sidfötter vid körning tillhandahåller Aspose.Cells speciella API-anrop och skriptkommandon för att formatera sidhuvuden och sidfötter.

### **Skriptkommandon**

Skriptkommandon är speciella kommandon som tillåter dig att ställa in sidhuvud- och sidfotformatering.

|**Skriptkommandon**|**Beskrivning**|
| :- | :- |
|&P|Det nuvarande sidnumret|
|&G|En bild|
|&N|Det totala antalet sidor|
|&D|Aktuellt datum|
|&T|Aktuell tid|
|&A|Arbetsbladets namn|
|&F|Filnamnet utan dess sökväg|
|&&Text| Visar &Text. Till exempel: &&WO kommer att visas som &WO|
|&"\<FontName>"|Representerar ett typsnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representerar typsnittsnamn med stil. Till exempel: &"Arial,Fetstil"|
|&\<FontSize>|Representerar teckensnittsstorlek. Till exempel: “&14abc”. Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i sidhuvudet, ska detta separeras med ett mellanslag från teckensnittsstorleken. Till exempel: “&14 123”|

### **Ställ in headers och footers**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klassen tillhandahåller två metoder, [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) och [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/), som används för att lägga till en sidhuvud och sidfot till ett arbetsblad. Dessa metoder tar endast två parametrar:

- **Avsnitt** – avsnittet där sidhuvudet eller sidfoten ska placeras. Det finns tre avsnitt: vänster, mitten och höger, representerade av 0, 1 och 2 respektive.
- **Skript** – skriptet som ska användas för sidhuvudet eller sidfoten. Detta skript innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Infoga en bild i en sidhuvud eller sidfot**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klassen har två ytterligare metoder, [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) och [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/), som används för att lägga till bilder i sidhuvud och sidfot. Dessa metoder tar parametrarna:

- **Avsnitt** – avsnittet för sidhuvudet eller sidfoten där bilden ska placeras. Det finns tre avsnitt, vänster, mitten och höger, representerade av värdena 0, 1 och 2 respektive.
- **Byte-arrayer** – de grafiska data (de binära data ska skrivas in i bufferten i en byte-array).

Efter att ha utfört koden nedan och öppnat filen, kontrollera arbetsbladets sidhuvud genom:

1. På **Arkiv**-menyn väljer du **Sidlayout**. En dialogruta visas.
1. Välj fliken **Sidhuvud/Sidfot**.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
