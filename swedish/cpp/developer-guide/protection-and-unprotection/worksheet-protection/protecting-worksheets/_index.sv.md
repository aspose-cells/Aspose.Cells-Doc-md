---
title: Skydda Arkbilder med C++
linktitle: Skydda kalkylbladen
type: docs
weight: 10
url: /sv/cpp/protecting-worksheets/
description: Lär dig hur du skyddar ark, rader, kolumner och specifika celler i Microsoft Excel filer med Aspose.Cells med C++.
---

{{% alert color="primary" %}}

När ett ark är skyddat begränsas användarens handlingar. Till exempel kan de inte mata in data, infoga eller radera rader eller kolumner, osv.

{{% /alert %}}

## **Skydda kalkylblad**

### **Introduktion**

De allmänna skyddsalternativen i Microsoft Excel är:

- Innehåll
- Objekt
- Scenarier

Skyddade arbetsblad döljer inte eller skyddar känsliga data, så det skiljer sig från filkryptering. I allmänhet passar arbetsbladsskydd för presentationsändamål. Det förhindrar slutanvändaren från att ändra data, innehåll och formatering i arbetsbladet.

### **Skydda ett arbetsblad**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller metoden [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) som används för att tillämpa skydd på arbetsbladet. [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)-metoden accepterar följande parametrar:

- Skyddstyp, typen av skydd att tillämpa på arbetsbladet. Skyddstypen appliceras med hjälp av [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/)-uppräkningen.
- Nya lösenordet, det nya lösenordet som används för att skydda kalkylbladet.
- Gammalt lösenord, det gamla lösenordet om arbetsbladet redan är lösenordsskyddat. Om arbetsbladet inte redan är skyddat, skicka bara null.

Uppräkningen [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) innehåller följande fördefinierade skydds typer:

|**Skydds typer**|**Beskrivning**|
| :- | :- |
|All|Användaren kan inte ändra något på detta arbetsblad|
|Contents|Användaren kan inte mata in data på detta arbetsblad|
|Objects|Användaren kan inte ändra ritobjekt|
|Scenarios|Användaren kan inte ändra sparade scenarier|
|Structure|Användaren kan inte ändra strukturen|
|Windows|Skyddet tillämpas på fönster|
|None|Inget skydd tillämpas|

Nedan följer ett exempel på hur man skyddar ett arbetsblad med lösenord.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Efter ovanstående kod används för att skydda arbetsbladet kan du kontrollera skyddet på arbetsbladet genom att öppna det. När du öppnar filen och försöker lägga till några data i arbetsbladet, kommer du att se följande dialogruta:

|**En dialogruta som varnar användaren om att den inte kan ändra arbetsbladet**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

För att arbeta med arbetsbladet, avse skyddet genom att välja **Skydd** och sedan **Avskydda ark** från menyalternativet **Verktyg**.

När du väljer menyalternativet Avskydda ark öppnas en dialogruta som uppmanar dig att ange lösenordet så att du kan arbeta med arbetsbladet som visas nedan:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Skydda ett fåtal celler i arbetsbladet med hjälp av Microsoft Excel**

Det kan finnas vissa scenarier där du behöver låsa endast några celler i arbetsbladet. Om du vill låsa några specifika celler i arbetsbladet måste du låsa upp alla andra celler i arbetsbladet. Alla celler i ett arbetsblad är redan initialiserade för låsning, du kan kontrollera detta genom att öppna vilken Excel-fil som helst i MS Excel och klicka på **Format | Celler…** för att visa dialogrutan **Formatera celler** och sedan klicka på fliken **Skydd** och se att kryssrutan märkt "Låst" är markerad som standard.

Följande punkter beskriver hur man låser några celler med hjälp av MS Excel. Denna metod gäller för Microsoft Office Excel 97, 2000, 2002, 2003 och senare versioner.

1. Markera hela arbetsbladet genom att klicka på knappen **Markera allt** (den grå rektangeln direkt ovanför radnumret för rad 1 och till vänster om kolumnbrevet A).
1. Klicka på **Celler** på **Format**-menyn, klicka på fliken **Skydd** och avmarkera sedan kryssrutan **Låst**.
   Det låser upp alla cellerna på arbetsbladet
   Om kommandot **Celler** inte är tillgängligt kan delar av arbetsbladet redan vara låst. På **Verktyg**-menyn, peka på **Skydd** och klicka sedan på **Avskydda ark**.
1. Välj bara de celler du vill låsa och upprepa steg 2, men den här gången markera kryssrutan **Låst**.
1. På **Verktyg**-menyn, peka på **Skydd**, klicka på **Skydda ark** och klicka sedan på **OK**.
1. I dialogrutan **Skydda ark** har du möjlighet att ange ett lösenord och välja de element som du vill att användarna ska kunna ändra.

### **Skydda en del celler i arbetsbladet med hjälp av Aspose Cells**

I denna metod använder vi endast Aspose.Cells API för att utföra uppgiften.

Exempel: Följande exempel visar hur man skyddar några celler i arbetsbladet. Det låser upp alla celler i arbetsbladet först och låser sedan 3 celler (A1, B1, C1) i den. Slutligen skyddar det arbetsbladet. Objektet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) innehåller en boolesk egenskap, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Du kan ange [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)-egenskapen till true eller false och tillämpa metoden *Column/Row.ApplyStyle()* för att låsa eller låsa upp rad/kolumn med dina önskade attribut.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Skydda en rad i kalkylarket**

Aspose.Cells gör det möjligt för dig att enkelt låsa någon rad i kalkylarket. Här kan vi använda [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) metoden av [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) på en specifik rad i kalkylarket. Denna metod tar två argument: en [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objekt och [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur du skyddar en rad i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första raden i det. Slutligen skyddar det kalkylarket. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektet innehåller en boolesk egenskap, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Du kan ställa in [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) egenskapen till true eller false för att låsa eller låsa upp rad/kolumn med hjälp av [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) objektet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Skydda en kolumn i kalkylarket**

Aspose.Cells gör det möjligt för dig att enkelt låsa en kolumn i kalkylarket. Här kan vi använda [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) metoden av [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) på en specifik kolumn i kalkylarket. Denna metod tar två argument: en [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objekt och [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur du skyddar en kolumn i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första kolumnen i det. Slutligen skyddar det kalkylarket. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektet innehåller en boolesk egenskap, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Du kan ställa in [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) egenskapen till true eller false för att låsa eller låsa upp rad/kolumn med hjälp av [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) objektet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Tillåt användare att redigera områden**

Följande exempel visar hur du tillåter användare att redigera ett område i ett skyddat kalkylark.

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
