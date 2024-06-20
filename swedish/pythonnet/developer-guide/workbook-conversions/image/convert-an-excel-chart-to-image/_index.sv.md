---
title: Konvertera en Excel diagram till bild
type: docs
weight: 20
url: /sv/python-net/convert-an-excel-chart-to-image/
description: Konvertera en Excel diagram till bild genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Konvertera en Excel diagram till bild, Exportera en Excel diagram till bild i Python via NET, Python Spara en Excel diagram till bild.
---

{{% alert color="primary" %}}

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel visar ett diagram på ett överskådligt sätt om försäljningen ökar eller minskar, eller hur faktisk försäljning jämförs med projicerad försäljning. Människor ombeds ofta att presentera statistisk och grafisk information på ett lättförståeligt och lätt underhållet sätt. En bild hjälper till.

Ibland behövs diagram i en applikation eller webbsidor. Eller så kan det behövas för en Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan applikation. I varje fall vill du rendera diagrammet som en bild så att du kan använda det någon annanstans.

{{% /alert %}}

## **Konvertera diagram till bilder**

I exemplen här konverteras en cirkeldiagram och ett stapeldiagram till bilder.

### **Konvertera ett cirkeldiagram till en bildfil**

Skapa först ett cirkeldiagram i Microsoft Excel och konvertera det sedan till en bildfil med Aspose.Cells for Python via .NET. Koden i det här exemplet skapar en EMF-bild baserad på cirkeldiagrammet i mallen Microsoft Excel-filen.

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

Vi värd våra Python paket i PyPi repositories.

Installera Aspose.Cells for Python från pypi, använd kommandot: $ pip install aspose-cells-python.

Och du kan också följa steg för steg instruktionerna om hur du installerar “Aspose.Cells for Python via .NET” till din utvecklingsmiljö.
1. Ladda ner och installera Aspose.Cells for Python via .NET:
   1. Installera Aspose.Cells for Python via .NET från [pypi](https://pypi.org/project/aspose-cells-python/), använd kommandot: $ pip install aspose-cells-python.
   1. Och du kan också följa [steg för steg-instruktionerna](https://docs.aspose.com/cells/python-net/getting-started/) om hur du installerar "Aspose.Cells for Python via .NET" till din utvecklingsmiljö.

Alla [Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det lägger bara vattenstämplar i utdata dokument.

1. Skapa ett projekt:
   1. Starta Visual Studio.
   1. Lägg till en biblioteksreferens (importera biblioteket) till ditt Python-projekt.
   1. Skriv koden som hittar och konverterar diagrammet. Nedan är koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
