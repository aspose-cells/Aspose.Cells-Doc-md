---
title: Öppnar en Excel fil
type: docs
weight: 10
url: /sv/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop,öppna,filer
description: Den här artikeln introducerar hur man öppnar fil i GridDesktop.
---

{{% alert color="primary" %}} 

En unik funktion med Aspose.Cells Grid Suite är dess kompatibilitet med Excel-filer. I det här ämnet kommer vi att visa hur användare kan öppna Excel-filer i sina Windows-applikationer med hjälp av Aspose.Cells.GridDesktop-kontrollen.

{{% /alert %}} 
## **Introduktion**
För att öppna en Excel-fil med Aspose.Cells.GridDesktop måste du skapa en skrivbordsapplikation med GridDesktop-kontroll i den. Om du inte vet hur du lägger till Aspose.Cells.GridDesktop-kontroll i din windows-formulär bör du hänvisa till [Hur man använder Aspose.Cells.GridDesktop](/cells/sv/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop tillhandahåller tre olika sätt att öppna en Excel-fil.

1. **Öppna från fil**
1. **Öppna en CSV-fil**
1. **Öppna från en ström**
## **Öppna Excel-fil**
I det här exemplet skapar du en skrivbordsapplikation och gör följande.

- Lägg till en GridControl-kontroll på formuläret.
- Lägg till tre knappar med deras textegenskaper inställda enligt följande:
  - **Öppna Excel-fil**
  - **Öppna CSV-fil**
  - **Öppna från ström**
### **Öppna från fil**
För att ladda innehållet från en Excel-fil till Aspose.Cells.GridDesktop-kontrollen måste du anropa en metod för att ange sökvägen till Excel-filen. Därefter kommer Aspose.Cells.GridDesktop-kontrollen automatiskt att hitta filen från den angivna sökvägen och visa dess innehåll. Kodsnyttet för att ladda innehållet i en Excel-fil är angivet i det följande exemplet. Skapa klickhändelsen för knappen **Öppna Excel-fil** och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Ovanstående kodsnytt kan användas av utvecklare på vilket sätt de vill. Till exempel, om du vill ladda in en Excel-fil automatiskt när ett windows-formulär laddas kan du lägga till denna kod under Händelsen för laddning av ditt formulär.
### **Öppna en CSV-fil**
Aspose.Cells.GridDesktop-kontrollen stöder även inläsning av CSV-filer. Skapa klickhändelsen för knappen **Öppna CSV-fil** och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Öppna från en ström**
I vår ovanstående diskussion har vi diskuterat inläsning av en Excel-fil med hjälp av dess filväg, men Aspose.Cells.GridDesktop-kontrollen stöder även inläsning av Excel-fil från en ström. Skapa klickhändelsen för knappen **Öppna från ström** och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Att använda fil som en ström är ett bättre tillvägagångssätt för att förhindra någon form av filåtkomst eller delningsproblem eftersom detta tillvägagångssätt säkerställer stängning av alla anslutningar till filerna genom att stänga strömmen.

{{% alert color="primary" %}} 

VIKTIGT: En viktig punkt att diskutera är att Aspose.Cells.GridDesktop-kontrollen också innehåller en metod med namnet LoadFromExcel, vilken också används för att ladda innehållet i en Excel-fil till griden. Men, denna metod är nu föråldrad. Så, det rekommenderas att alla utvecklare använder metoden ImportExcelFile som är mer robust och effektiv än den föråldrade.

{{% /alert %}}
