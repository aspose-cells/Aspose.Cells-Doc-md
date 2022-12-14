---
title: Importera Microsoft Excel-fil
type: docs
weight: 40
url: /sv/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Som Aspose.Cells.GridDesktop, Aspose.Cells.GridWeb control kan öppna och ladda Microsoft Excel-filer - komplett med data, formatering, diagram, bilder etc. - men i webbapplikationer. Det här ämnet förklarar hur.

{{% /alert %}} 
## **Importera Excel-filer**
### **Importera från fil**
Så här öppnar du en Excel-fil med Aspose.Cells.GridWeb-kontroll:

1. Lägg till kontrollen Aspose.Cells.GridWeb i ett webbformulär.
1. Importera Excel-filen genom att ange sökvägen.
1. Kör programmet.

{{% alert color="primary" %}} 

 Om du inte vet hur man lägger till kontrollen i ett webbformulär, se[Lägg till GridWeb till webbformulär](/cells/sv/net/add-gridweb-to-web-form/).

{{% /alert %}} 

När Aspose.Cells.GridWeb-kontroll läggs till i ett webbformulär, instansieras kontrollen automatiskt och läggs till i formuläret med en standardstorlek. Du behöver inte skapa ett Aspose.Cells.GridWeb kontrollobjekt, allt du behöver göra är att dra och släppa kontrollen och börja använda den.

Men för att ladda innehållet från en Excel-fil till Aspose.Cells.GridWeb-kontrollen måste du anropa metoden ImportExcelFile för att ange sökvägen till Excel-filen. Därefter kommer Aspose.Cells.GridWeb control automatiskt att hitta filen från den angivna sökvägen och visa dess innehåll. Ett kodavsnitt som laddar innehållet i en Excel-fil finns nedan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Ovanstående kodavsnitt kan användas hur du vill. Till exempel, för att ladda en Excel-fil automatiskt när ett webbformulär laddas, lägg till den här koden i formulärets Page_Load-händelse. Om du vill öppna en fil när en knapp klickas, lägg till en knapp i webbformuläret och skriv ovanstående kod under knappens klickhändelse.

**En Excel-fil laddas när en knapp klickas** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Om ditt filsystem är NTFS bör du ge läsbehörighet till ASPNET- eller Everyone-användarkontona, annars får du ett undantag för nekad åtkomst vid körning.

{{% /alert %}} 
### **Importera från Stream**
Förutom att öppna Excel-filer från fil, kan Aspose.Cells.GridWeb-kontrollen ladda Excel-filer från en ström. Att använda fil som en ström är ett bättre tillvägagångssätt för att förbjuda alla typer av filåtkomst eller delningsproblem eftersom detta tillvägagångssätt säkerställer att alla anslutningar till filerna stängs genom att stänga strömmen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
