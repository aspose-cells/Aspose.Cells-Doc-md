---
title: Spara en Excel fil
type: docs
weight: 20
url: /sv/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop,spara,filer
description: Den här artikeln introducerar hur man sparar fil i GridDesktop.
---

{{% alert color="primary" %}} 

Genom att använda Aspose.Cells.GridDesktop-kontrollen kan användare inte bara skapa nya Excel-filer utan även hantera befintliga. Men, i båda fallen skulle det vara nödvändigt att spara innehållet i Aspose.Cells.GridDesktop. Så detta är ämnet för vår diskussion nu för att låta våra användare veta hur de kan spara sitt grid-innehåll som en Excel-fil.

{{% /alert %}} 
## **Introduktion**
För att spara innehållet i Aspose.Cells.GridDesktop-kontrollen som en Excel-fil tillhandahåller Aspose.Cells.GridDesktop följande metoder.

1. **Spara som en fil**
1. **Spara som en ström**
## **Sparar fil**
Skapa en skrivbordsapplikation och lägg till två knappar med en GridControl-kontroll på formuläret. Ange textegenskaperna för knapparna som **Spara som fil** och **Spara som ström** respektive.
### **Spara som en fil**
Skapa Klick-händelsen för knappen **Spara som fil** och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: En viktig punkt att diskutera är att Aspose.Cells.GridDesktop-kontrollen också innehåller en metod som heter SaveToExcel, som också används för att ladda innehållet i en Excel-fil till rutan. Men, denna metod är nu föråldrad. Det rekommenderas därför för alla utvecklare att använda ExportExcelFile-metoden som är mer robust och effektiv än den föråldrade.

{{% /alert %}} 
### **Sparar som en ström**
Ibland kan det krävas av utvecklare att spara sina gridinnehåll till en ström (t.ex. MemoryStream). För att underlätta denna uppgift stöder även Aspose.Cells.GridDesktop-kontrollen att spara griddata till en ström. Skapa Klick-händelsen för knappen **Spara som ström** och klistra in följande kod i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Microsoft Excel stödjer Excel-ark som kan innehålla högst 65 536 rader och 256 kolumner. Aspose.Cells.GridDesktop följer också samma standarder. I Aspose.Cells.GridDesktop-kontrollen kan utvecklare skapa fler rader och kolumner än det standardgränsen men när griddata sparas till en Excel-fil, kastas ett undantag. Det betyder att endast data som finns i 65 536 rader och 256 kolumner kan sparas till en Excel-fil med hjälp av Aspose.Cells.GridDesktop.

{{% /alert %}}
