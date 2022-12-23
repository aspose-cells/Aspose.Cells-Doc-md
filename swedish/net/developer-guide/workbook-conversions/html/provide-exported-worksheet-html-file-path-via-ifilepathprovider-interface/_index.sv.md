---
title: Ge exporterad kalkylblads html-filsökväg via IFilePathProvider-gränssnittet
type: docs
weight: 70
url: /sv/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Möjliga användningsscenarier**
 Anta att du har en excel-fil med flera ark och du vill exportera varje ark till en individuell HTML-fil. Om något av dina ark har länkar till andra ark, kommer dessa länkar att brytas i den exporterade HTML. För att hantera detta problem tillhandahåller Aspose.Cells[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)gränssnitt som du kan implementera för att fixa de trasiga länkarna.
## **Ange exporterat kalkylblad HTML filsökväg via IFilePathProvider-gränssnittet**
 Vänligen ladda ner[exempel på excel-fil](5115213.zip)används i följande kod och dess exporterade HTML-filer. Alla dessa filer finns i Temp-katalogen. Du bör extrahera den på C:-enhet. Då blir det C:\Temp-katalogen. Sedan öppnar du filen Sheet1.html i webbläsaren och klickar på de två länkarna i den. Dessa länkar hänvisar till dessa två exporterade HTML-kalkylblad som finns i katalogen C:\Temp\OtherSheets.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Följande skärmdump visar hur C:\Temp\Sheet1.html och dess länkar ser ut

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Följande skärmdump visar källan HTML. Som du kan se att länkarna nu hänvisar till katalogen C:\Temp\OtherSheets. Detta uppnåddes med hjälp av[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)gränssnitt.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Exempelkod**
 Observera att C:\Temp-katalogen bara är för illustrationsändamål. Du kan använda valfri katalog och plats[exempel på excel-fil](5115211.xlsx)inuti där och kör den medföljande exempelkoden. Det kommer sedan att skapa OtherSheets-underkatalogen i din katalog och exportera andra och tredje kalkylblad HTML inuti den. Ändra dirPath-variabeln i den medföljande koden och hänvisa den till den katalog du väljer innan du kör den.

{{% alert color="primary" %}} 

Exempelkoden fungerar bara när du ställer in Aspose.Cells licens. Om du försöker köra koden utan att ställa in licensen kommer den att gå in i en oändlig loop. Därför har vi lagt till en bock för att skriva ut ett meddelande och stoppa körningen när licensen inte är inställd. Du kan antingen köpa en licens eller begära en 30-dagars tillfällig licens från Aspose.Purchase-teamet.

{{% /alert %}} 

Se att kommentera dessa rader i koden kommer att bryta länkarna i Sheet1.html och Sheet2.html eller Sheet3.html kommer inte att öppnas när deras länkar klickas i Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Här är den kompletta exempelkoden som du kan köra med den medföljande[exempel på excel-fil](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
