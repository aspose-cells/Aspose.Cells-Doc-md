---
title: Öppna en Excel-fil
type: docs
weight: 10
url: /sv/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

En unik egenskap hos Aspose.Cells Grid Suite är dess kompatibilitet med Excel-filer. I det här ämnet kommer vi att visa hur användare kan öppna Excel-filer i sina Windows-program med hjälp av Aspose.Cells.GridDesktop-kontroll.

{{% /alert %}} 
## **Introduktion**
 För att öppna en Excel-fil med Aspose.Cells.GridDesktop måste du skapa ett skrivbordsprogram med GridDesktop Control i det. Om du inte vet hur du lägger till Aspose.Cells.GridDesktop-kontroll i ditt Windows-formulär bör du referera till[Hur man använder Aspose.Cells.GridDesktop](/cells/sv/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop tillhandahåller tre följande olika sätt att öppna en Excel-fil.

1. **Öppna från en fil**
1. **Öppna en CSV-fil**
1. **Öppna från en ström**
## **Öppnar Excel-fil**
det här exemplet skapar du ett skrivbordsprogram och gör följande.

- Lägg till en GridControl-kontroll i formuläret.
- Lägg till tre knappar med deras textegenskaper inställda enligt följande:
  - **Öppna Excel-fil**
  - **Öppna CSV-fil**
  - **Öppna från Stream**
### **Öppna från en fil**
 För att ladda innehållet från en Excel-fil till Aspose.Cells.GridDesktop-kontroll, måste du anropa en metod för kontrollen för att ange sökvägen till Excel-filen. Efter det kommer Aspose.Cells.GridDesktop control automatiskt att hitta filen från den angivna sökvägen och visa dess innehåll. Kodavsnittet för att ladda innehållet i en Excel-fil finns i exemplet nedan. Skapa Click-händelsen för**Öppna Excel-fil** knappen och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Ovanstående kodavsnitt kan användas av utvecklare på vilket sätt de vill. Till exempel, om du vill ladda en Excel-fil automatiskt när ett Windows-formulär laddas kan du lägga till den här koden under Load-händelsen i ditt formulär.
### **Öppna en CSV-fil**
Aspose.Cells.GridDesktop-kontroll stöder också inläsning av CSV-fil. Skapa Click-händelsen för**Öppna CSV-fil** knappen och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Öppna från en ström**
 I vår diskussion ovan har vi diskuterat hur man laddar en Excel-fil genom att använda dess sökväg, men Aspose.Cells.GridDesktop-kontroll stöder också att ladda Excel-fil från en ström. Skapa Click-händelsen för**Öppna från Stream** knappen och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Att använda fil som en ström är ett bättre tillvägagångssätt för att förbjuda alla typer av filåtkomst eller delningsproblem eftersom detta tillvägagångssätt säkerställer att alla anslutningar till filerna stängs genom att stänga strömmen.

{{% alert color="primary" %}} 

VIKTIGT: En viktig punkt att diskutera är att Aspose.Cells.GridDesktop-kontrollen också innehåller en metod som heter LoadFromExcel, som också används för att ladda innehållet i en Excel-fil till Grid. Men denna metod är nu föråldrad. Så det rekommenderas för alla utvecklare att använda ImportExcelFile-metoden som är mer robust och effektiv än den föråldrade.

{{% /alert %}}
