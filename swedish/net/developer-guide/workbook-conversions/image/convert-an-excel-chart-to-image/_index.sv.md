---
title: Konvertera ett Excel-diagram till bild
type: docs
weight: 20
url: /sv/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel, snarare än att analysera kolumner med kalkylbladsnummer, visar ett diagram med ett ögonkast om försäljningen faller eller stiger, eller hur den faktiska försäljningen jämför med den beräknade försäljningen. Människor uppmanas ofta att presentera statistisk och grafisk information på ett lättförståeligt och lättskött sätt. En bild hjälper.

Ibland behövs diagram i en applikation eller webbsidor. Eller det kan behövas för ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan applikation. I varje fall vill du rendera diagrammet som en bild så att du kan använda det någon annanstans.

{{% /alert %}}

## **Konvertera diagram till bilder**

I exemplen här konverteras ett cirkeldiagram och ett kolumndiagram till bilder.

### **Konvertera ett cirkeldiagram till en bildfil**

Skapa först ett cirkeldiagram i Microsoft Excel och konvertera det sedan till en bildfil med Aspose.Cells. Koden i det här exemplet skapar en EMF-bild baserat på cirkeldiagrammet i mallen Microsoft Excel-fil.

|**Utdata: cirkeldiagrambild**|
|:- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Skapa ett cirkeldiagram i Microsoft Excel:
 1. Öppnade en ny arbetsbok i Microsoft Excel.
 1. Mata in lite data i ett kalkylblad.
 1. Skapat ett cirkeldiagram baserat på data.
 1. Spara filen.

|**Inmatningsfilen.**|
|:- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells för .NET](https://downloads.aspose.com/cells/net).
 1. Installera det på din utvecklingsdator.

 Allt[Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i utdatadokument.

1. Skapa ett projekt:
 1. Starta Visual Studio.Net.
 1. Skapa en ny konsolapplikation. Det här exemplet använder en C#-konsolapplikation, men du kan också använda VB.NET.
 1. Lägg till en referens. Detta projekt använder Aspose.Cells så lägg till en referens till Aspose.Cells, till exempel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Skriv koden som hittar och konverterar diagrammet. Nedan visas koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Konvertera ett kolumndiagram till en bildfil**

Skapa först ett kolumndiagram i Microsoft Excel och konvertera det till en bildfil, enligt ovan. Efter exekvering av exempelkoden skapas en JPEG-fil baserat på kolumndiagrammet i mallens Excel-fil.

|**Utdatafil: en kolumndiagrambild.**|
|:- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Skapa ett kolumndiagram i Microsoft Excel:
 1. Öppna en ny arbetsbok i Microsoft Excel.
 1. Mata in lite data i ett kalkylblad.
 1. Skapa ett kolumndiagram baserat på data.
 1. Spara filen.

|**Indatafil.**|
|:- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Skapa ett projekt, med referenser, enligt beskrivningen ovan.
1. Konvertera diagrammet till en bild dynamiskt. Följande är koden som används av komponenten för att utföra uppgiften. Koden liknar den föregående:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
