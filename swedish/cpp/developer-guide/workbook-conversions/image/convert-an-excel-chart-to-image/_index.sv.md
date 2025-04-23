---
title: Konvertera ett Excel diagram till bild med C++
linktitle: Konvertera en Excel diagram till bild
type: docs
weight: 20
url: /sv/cpp/convert-an-excel-chart-to-image/
description: Lär dig hur du konverterar Excel diagram till bilder med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel, snarare än att analysera kolumner av kalkylbladsnummer, visar ett diagram på ett ögonblick om försäljningen faller eller stiger, eller hur faktiska försäljningssiffror jämförs med prognoser. Folk ombeds ofta att presentera statistisk och grafisk information på ett lättförståeligt och lättunderhållet sätt. En bild hjälper.

Ibland behövs diagram i en applikation eller på webbsidor. Eller de kan behövas för ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat program. I varje fall vill du rendera diagrammet som en bild för att kunna använda den på andra platser.

{{% /alert %}}

## **Konvertera diagram till bilder**

I exemplen här konverteras en pajdiagram och ett kolumndiagram till bilder.

### **Konvertera ett cirkeldiagram till en bildfil**

Skapa först ett cirkeldiagram i Microsoft Excel och konvertera det sedan till en bildfil med Aspose.Cells. Koden i detta exempel skapar en EMF-bild baserad på cirkeldiagrammet i den befintliga Microsoft Excel-filen.

|**Utgång: cirkeldiagramsbild**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Skapa ett cirkeldiagram i Microsoft Excel:
   1. Öppna en ny arbetsbok i Microsoft Excel.
   1. Ange några data i ett kalkylblad.
   1. Skapa ett cirkeldiagram baserat på data.
   1. Spara filen.

|**Ingångsfilen.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. Installera det på din utvecklingsdator.

Alla [Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det lägger bara vattenstämplar i utdata dokument.

1. Skapa ett projekt:
   1. Starta din C++-utvecklingsmiljö (t.ex. Visual Studio).
   1. Skapa en ny konsolapplikation.
   1. Lägg till en referens till Aspose.Cells. Detta projekt använder Aspose.Cells, så lägg till en referens till Aspose.Cells-biblioteket.
   1. Skriv koden som hittar och konverterar diagrammet. Nedan är koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konvertera ett kolumndiagram till en bildfil**

Först, skapa ett kolumndiagram i Microsoft Excel och konvertera det till en bildfil, som ovan. Efter att ha kört exempel koden, skapas en JPEG-fil baserad på kolumndiagrammet i mall-Excel-filen.

|**Utmatningsfil: en kolumndiagramsbild.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Skapa ett kolumndiagram i Microsoft Excel:
   1. Öppna en ny arbetsbok i Microsoft Excel.
   1. Ange några data i ett kalkylblad.
   1. Skapa ett kolumndiagram baserat på datan.
   1. Spara filen.

|**Ingångsfil.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Bygg ett projekt, med referenser, enligt beskrivningen ovan.
1. Konvertera diagrammet till en bild dynamiskt. Följande är koden som används av komponenten för att utföra uppgiften. Koden är liknande den tidigare:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
