---
title: Import Microsoft Excel fil
type: docs
weight: 40
url: /sv/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb, import
description: Den här artikeln introducerar hur man importerar filen i GridWeb.
---

{{% alert color="primary" %}} 

Som Aspose.Cells.GridDesktop kan Aspose.Cells.GridWeb-kontrollen öppna och ladda Microsoft Excel-filer - komplett med data, format, diagram, bilder etc. - men i webbapplikationer. Detta ämne förklarar hur.

{{% /alert %}} 
## **Importera Excel-filer**
### **Importera från fil**
För att öppna en Excel-fil med hjälp av Aspose.Cells.GridWeb-kontrollen:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär.
1. Importera Excel-filen genom att ange filens sökväg.
1. Kör programmet.

{{% alert color="primary" %}} 

Om du inte vet hur du lägger till kontrollen på ett webbformulär, se [Lägg till GridWeb på webbformulär](/cells/sv/net/aspose-cells-gridweb/add-gridweb-to-web-form/).

{{% /alert %}} 

När Aspose.Cells.GridWeb-kontrollen har lagts till ett webbformulär, skapas och läggs kontrollen automatiskt till formuläret med en standardstorlek. Du behöver inte skapa ett Aspose.Cells.GridWeb-kontrollobjekt, allt du behöver göra är att dra och släppa kontrollen och börja använda den.

För att ladda innehållet från en Excel-fil till Aspose.Cells.GridWeb-kontrollen måste du dock anropa metoden ImportExcelFile för att ange sökvägen till Excel-filen. Efter det kommer Aspose.Cells.GridWeb-kontrollen automatiskt att hitta filen från den angivna sökvägen och visa dess innehåll. Ett kodsnutt som laddar innehållet i en Excel-fil tillhandahålls nedan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Ovanstående kodsnutt kan användas på vilket sätt du vill. Till exempel, för att ladda en Excel-fil automatiskt när ett webbformulär laddas, lägg till denna kod i formulärets Page_Load-händelse. Om du vill öppna en fil när en knapp klickas, lägg till en knapp på webbformuläret och skriv ovanstående kod under knappens Click-händelse.

**En Excel-fil laddas när en knapp klickas** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Om ditt filsystem är NTFS ska du bevilja läsrättigheter för behörigheterna ASPNET eller Everyone användarkonton eller så får du ett access nekas-undantag vid körning.

{{% /alert %}} 
### **Importera från stream**
Förutom att öppna Excel-filer från fil kan Aspose.Cells.GridWeb-kontrollen ladda Excel-filer från en ström. Att använda fil som en ström är ett bättre tillvägagångssätt för att förbjuda några typer av filåtkomst eller delningsproblem eftersom detta tillvägagångssätt säkerställer att alla anslutningar till filerna stängs genom att stänga strömmen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
