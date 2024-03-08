---
title: Konvertera ett Excel-diagram till bild
type: docs
weight: 20
url: /sv/python-net/convert-an-excel-chart-to-image/
description: Konvertera ett Excel-diagram till bild genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel, snarare än att analysera kolumner med kalkylbladsnummer, visar ett diagram med ett ögonkast om försäljningen faller eller stiger, eller hur den faktiska försäljningen jämför med den beräknade försäljningen. Människor uppmanas ofta att presentera statistisk och grafisk information på ett lättförståeligt och lättskött sätt. En bild hjälper.

Ibland behövs diagram i en applikation eller webbsidor. Eller det kan behövas för ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat program. I varje fall vill du rendera diagrammet som en bild så att du kan använda det någon annanstans.

{{% /alert %}}

##  **Konvertera diagram till bilder**

I exemplen här konverteras ett cirkeldiagram och ett kolumndiagram till bilder.

###  **Konvertera ett cirkeldiagram till en bildfil**

Skapa först ett cirkeldiagram i Microsoft Excel och konvertera det sedan till en bildfil med Aspose.Cells for Python via .NET. Koden i det här exemplet skapar en EMF-bild baserat på cirkeldiagrammet i mallen Microsoft Excel-fil.

|**Utdata: cirkeldiagrambild**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Skapa ett cirkeldiagram i Microsoft Excel:
 1. Öppnade en ny arbetsbok i Microsoft Excel.
 1. Mata in lite data i ett kalkylblad.
 1. Skapat ett cirkeldiagram baserat på data.
 1. Spara filen.

|**Inmatningsfilen.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

Vi är värd för våra Python-paket i PyPi-förråd.

Installera Aspose.Cells for Python från pypi, använd kommandot som: $ pip install aspose-cells-python.

Och du kan också följa steg-för-steg-instruktionerna om hur du installerar "Aspose.Cells for Python via .NET" i din utvecklarmiljö.
1. Ladda ner och installera Aspose.Cells for Python via .NET:
 1. Installera Aspose.Cells for Python via .NET från[pypi](https://pypi.org/project/aspose-cells-python/)använd kommandot som: $ pip installera aspose-cells-python.
 1. Och du kan också följa[steg-för-steg instruktioner](https://docs.aspose.com/cells/python-net/getting-started/)om hur du installerar "Aspose.Cells for Python via .NET" i din utvecklarmiljö.

 Allt[Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i utdatadokument.

1. Skapa ett projekt:
 1. Starta Visual Studio.
 1. Lägg till en biblioteksreferens (importera biblioteket) till ditt Python-projekt.
 1. Skriv koden som hittar och konverterar diagrammet. Nedan visas koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **Konvertera ett kolumndiagram till en bildfil**

Skapa först ett kolumndiagram i Microsoft Excel och konvertera det till en bildfil, enligt ovan. Efter exekvering av exempelkoden skapas en JPEG-fil baserat på kolumndiagrammet i Excel-mallen.

|**Utdatafil: en kolumndiagrambild.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Skapa ett kolumndiagram i Microsoft Excel:
 1. Öppna en ny arbetsbok i Microsoft Excel.
 1. Mata in lite data i ett kalkylblad.
 1. Skapa ett kolumndiagram baserat på data.
 1. Spara filen.

|**Indatafil.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Skapa ett projekt, med referenser, enligt beskrivningen ovan.
1. Konvertera diagrammet till en bild dynamiskt. Följande är koden som används av komponenten för att utföra uppgiften. Koden liknar den föregående:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
