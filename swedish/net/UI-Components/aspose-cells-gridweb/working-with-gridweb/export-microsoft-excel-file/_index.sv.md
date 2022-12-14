---
title: Exportera Microsoft Excel-fil
type: docs
weight: 50
url: /sv/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Det är möjligt att skapa nya, eller manipulera befintliga Microsoft Excel-filer, på webbplatser i GUI-läge med hjälp av Aspose.Cells.GridWeb-kontroll. Filerna kan sedan sparas i Excel-filer. Aspose.Cells.GridWeb fungerar effektivt som kalkylarksredigerare online. Det här avsnittet beskriver hur du sparar rutnätsinnehåll i Excel-filer.

{{% /alert %}} 
## **Exportera Excel-filer**
### **Exportera som en fil**
Så här sparar du innehållet i Aspose.Cells.GridWeb-kontrollen som en Excel-fil:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Spara ditt arbete som en Excel-fil på en angiven sökväg.
1. Kör programmet.

{{% alert color="primary" %}} 

 Om du inte vet hur du lägger till Aspose.Cells.GridWeb-kontroll i ditt webbformulär bör du hänvisa till[Lägg till GridWeb till webbformulär](/cells/sv/net/add-gridweb-to-web-form/)

{{% /alert %}} 

När Aspose.Cells.GridWeb-kontroll läggs till i ett Windows-formulär, instansieras kontrollen automatiskt och läggs till i formuläret med en standardstorlek. Du behöver inte skapa ett Aspose.Cells.GridWeb kontrollobjekt, allt du behöver göra är att dra och släppa kontrollen och börja använda den.

Kodexemplet nedan illustrerar hur man sparar rutnätsinnehåll till en Excel-fil.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Om ditt filsystem är NTFS, bevilja läs-/skrivåtkomst till ASPNET- eller Everyone-användarkontona, annars får du ett undantag för nekad åtkomst vid körning.

{{% /alert %}} 

Ovanstående kodavsnitt kan användas på flera sätt. Ett vanligt sätt är att lägga till en knapp som sparar rutnätsinnehållet i en Excel-fil när du klickar på den. Aspose.Cells.GridWeb erbjuder ett enklare tillvägagångssätt för uppgiften. Aspose.Cells.GridWeb har en händelse som heter SaveCommand. Ovanstående kodavsnitt kan läggas till i SaveCommand-händelsens händelsehanterare, vilket tillåter användare att spara sitt arbete genom att klicka på Aspose.Cells.GridWebs inbyggda**Spara** knapp.

**GridWebs SaveCommand-händelse** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Spara rutnätsinnehåll till Excel genom att klicka på GridWebs inbyggda Spara-knapp** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 Om du arbetar i Visual Studio kan du enkelt skapa SaveCommand-händelsens händelsehanterare genom att dubbelklicka på händelsen i**Egenskaper** rutan. För att lära dig mer om detta, se[Arbeta med GridWeb Events](/cells/sv/net/working-with-gridweb-events/)

{{% /alert %}} 
### **Exportera som en ström**
Det är också möjligt att spara grid-innehåll till en stream (till exempel MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
