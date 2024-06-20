---
title: Exportera Microsoft Excel fil
type: docs
weight: 50
url: /sv/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb, export
description: Denna artikel introducerar hur man exporterar fil i GridWeb.
---

{{% alert color="primary" %}} 

Det är möjligt att skapa nya eller manipulera befintliga Microsoft Excel-filer på webbplatser i GUI-läge med hjälp av Aspose.Cells.GridWeb-kontrollen. Filerna kan sedan sparas till Excel-filer. Aspose.Cells.GridWeb fungerar effektivt som en onlinekalkylbladsredigerare. Detta ämne beskriver hur man sparar gridinnehåll till Excel-filer.

{{% /alert %}} 
## **Exportera Excel-filer**
### **Exportera som en fil**
För att spara innehållet i Aspose.Cells.GridWeb-kontrollen som en Excel-fil:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på din webbformulär.
1. Spara ditt arbete som en Excel-fil på en angiven sökväg.
1. Kör programmet.

{{% alert color="primary" %}} 

Om du inte vet hur du lägger till Aspose.Cells.GridWeb-kontrollen på din webbformulär bör du se [Lägg till GridWeb på Web Formulär](/cells/sv/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

När Aspose.Cells.GridWeb-kontrollen läggs till ett Windows-formulär instansieras kontrollen automatiskt och läggs till formuläret med en standardstorlek. Du behöver inte skapa ett objekt för Aspose.Cells.GridWeb-kontrollen, allt du behöver göra är att dra och släppa kontrollen och börja använda den.

Exemplet nedan illustrerar hur du sparar innehållet i GridWeb som en Excel-fil.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Om ditt filsystem är NTFS, ge läs/skrivrättigheter till användarkontona ASPNET eller Everyone, annars får du ett access nekat undantag vid körning.

{{% /alert %}} 

Ovanstående kodsnutt kan användas på flera sätt. Ett vanligt sätt är att lägga till en knapp som sparar gridinnehållet till en Excel-fil vid klick. Aspose.Cells.GridWeb erbjuder ett enklare tillvägagångssätt för uppgiften. Aspose.Cells.GridWeb har en händelse som heter SaveCommand. Ovanstående kodsnitt kan läggas till i händelsehanteraren för SaveCommand-händelsen, vilket låter användare spara sitt arbete genom att klicka på Aspose.Cells.GridWeb's inbyggda **Spara**-knapp.

**GridWeb's SaveCommand-händelse** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Spara gridinnehåll till Excel genom att klicka på GridWeb's inbyggda Spara-knapp** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Om du arbetar i Visual Studio kan du enkelt skapa händelsehanteraren för SaveCommand-händelsen genom att dubbelklicka på händelsen i **Egenskaper**-fönstret. För att lära dig mer om detta, se [Arbeta med GridWeb-händelser](/cells/sv/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **Exportera som en ström**
Det är också möjligt att spara gridinnehållet till en ström (till exempel MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
