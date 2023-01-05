---
title: Spara en Excel-fil
type: docs
weight: 20
url: /sv/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Med hjälp av Aspose.Cells.GridDesktop-kontroll kan användare inte bara skapa nya Excel-filer utan också hantera befintliga. Men i båda fallen skulle det vara nödvändigt att spara innehållet i Aspose.Cells.GridDesktop. Så detta är ämnet för vår diskussion nu för att låta våra användare veta hur de kan spara sitt Grid-innehåll som en Excel-fil.

{{% /alert %}} 
## **Introduktion**
För att spara innehållet i Aspose.Cells.GridDesktop-kontroll som en Excel-fil, tillhandahåller Aspose.Cells.GridDesktop följande metoder.

1. **Sparar som en fil**
1. **Spara som en ström**
## **Sparar fil**
 Skapa ett skrivbordsprogram och lägg till två knappar med en GridControl-kontroll i formuläret. Ställ in textegenskaper för knappar som**Spara som fil** och**Spara som Stream** respektive.
### **Sparar som en fil**
 Skapa Click-händelsen för**Spara som fil** knappen och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: En viktig punkt att diskutera är att Aspose.Cells.GridDesktop-kontrollen också innehåller en metod som heter SaveToExcel , som också används för att ladda innehållet i en Excel-fil till Grid. Men denna metod är nu föråldrad. Så det rekommenderas för alla utvecklare att använda ExportExcelFile-metoden som är mer robust och effektiv än den föråldrade.

{{% /alert %}} 
### **Spara som en ström**
 Ibland kan det krävas av utvecklare att spara sitt Grid-innehåll i en ström (till exempel MemoryStream). För att underlätta denna uppgift stöder Aspose.Cells.GridDesktop-kontroll också att spara Grid-data i en ström. Skapa Click-händelsen för**Spara som Stream** knappen och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Microsoft Excel stöder Excel-ark kan innehålla max 65 536 rader och 256 kolumner. Aspose.Cells.GridDesktop följer också samma standarder. I kontrollen Aspose.Cells.GridDesktop kan utvecklare skapa fler rader och kolumner än standardgränsen, men när du sparar rutnätsdata i en Excel-fil kommer ett undantag att skapas. Det betyder att endast data som finns i de 65 536 raderna och 256 kolumnerna kan sparas i en Excel-fil med Aspose.Cells.GridDesktop.

{{% /alert %}}
