---
title: Konvertera en Excel diagram till bild
type: docs
weight: 20
url: /sv/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel visar ett diagram på ett överskådligt sätt om försäljningen ökar eller minskar, eller hur faktisk försäljning jämförs med projicerad försäljning. Människor ombeds ofta att presentera statistisk och grafisk information på ett lättförståeligt och lätt underhållet sätt. En bild hjälper till.

Ibland behövs diagram i en applikation eller webbsidor. Eller så kan det behövas för en Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan applikation. I varje fall vill du rendera diagrammet som en bild så att du kan använda det någon annanstans.

{{% /alert %}}

## **Konvertera diagram till bilder**

I exemplen här konverteras en cirkeldiagram och ett stapeldiagram till bilder.

### **Konvertera ett cirkeldiagram till en bildfil**

Skapa först ett cirkeldiagram i Microsoft Excel och konvertera det sedan till en bildfil med Aspose.Cells. Koden i detta exempel skapar en EMF-bild baserad på cirkeldiagrammet i den befintliga Microsoft Excel-filen.

|**Utgång: cirkeldiagramsbild**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Skapa ett cirkeldiagram i Microsoft Excel:
   1. Öppnade en ny arbetsbok i Microsoft Excel.
   1. Ange några data i ett kalkylblad.
   1. Skapade ett cirkeldiagram baserat på datan.
   1. Spara filen.

|**Ingångsfilen.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ned Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Installera det på din utvecklingsdator.

Alla [Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det lägger bara vattenstämplar i utdata dokument.

1. Skapa ett projekt:
   1. Starta Visual Studio.Net.
   1. Skapa en ny konsollapplikation. Detta exempel använder en C#-konsollapplikation, men du kan också använda VB.NET.
   1. Lägg till en referens. Det här projektet använder Aspose.Cells, så lägg till en referens till Aspose.Cells, till exempel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
   1. Skriv koden som hittar och konverterar diagrammet. Nedan är koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Konvertera ett kolumndiagram till en bildfil**

Skapa först ett kolumndiagram i Microsoft Excel och konvertera det till en bildfil, enligt ovan. Efter att ha kört exempelkoden, skapas en JPEG-fil baserad på kolumndiagrammet i mall-Excel-filen.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
