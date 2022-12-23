---
title: Ange exporterat kalkylblad HTML filsökväg via IFilePathProvider-gränssnittet
type: docs
weight: 870
url: /sv/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Möjliga användningsscenarier**
 Anta att du har en excel-fil med flera ark och du vill exportera varje ark till en individuell HTML-fil. Om något av dina ark har länkar till andra ark, kommer dessa länkar att brytas i den exporterade HTML. För att hantera detta problem tillhandahåller Aspose.Cells[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)gränssnitt som du kan implementera för att fixa de trasiga länkarna.
## **Ange exporterat kalkylblad HTML filsökväg via IFilePathProvider-gränssnittet**
 Vänligen ladda ner[exempel på excel-fil](5473417.zip) används i följande kod och dess exporterade HTML-filer. Alla dessa filer finns inuti*Temp* katalog. Du borde extrahera den*C:* kör. Då blir det*C:\Temp* katalog. Då öppnar du*Blad1.html* filen i webbläsaren och klicka på de två länkarna i den. Dessa länkar hänvisar till dessa två exporterade HTML kalkylblad som finns inuti*C:\Temp\OtherSheets*katalog.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Följande skärmdump visar hur*C:\Temp\Sheet1.html*och dess länkar ser ut

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Följande skärmdump visar källan HTML. Som du kan se att länkarna nu syftar på*C:\Temp\OtherSheets* katalog. Detta uppnåddes med hjälp av[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)gränssnitt.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Exempelkod**
 Vänligen notera*C:\Temp* katalogen är bara för illustrationsändamål. Du kan använda valfri katalog och plats[exempel på excel-fil](5473414.xlsx) inuti där och kör den medföljande exempelkoden. Det kommer då att skapas*OtherSheets* underkatalog i din katalog och exportera andra och tredje kalkylblad HTML inuti den. Vänligen ändra*dirPath*variabel inuti den medföljande koden och hänvisa den till den katalog du väljer innan du kör den.

{{% alert color="primary" %}} 

Exempelkoden fungerar bara när du ställer in Aspose.Cells licens. Om du försöker köra koden utan att ställa in licensen kommer den att gå in i en oändlig loop. Därför har vi lagt till en bock för att skriva ut ett meddelande och stoppa körningen när licensen inte är inställd. Du kan antingen köpa en licens eller begära en 30-dagars tillfällig licens från Aspose.Purchase-teamet.

{{% /alert %}} 

 Se att kommentera dessa rader i koden kommer att bryta in länkarna*Blad1.html* och*Blad2.html* eller*Blad3.html*kommer inte att öppnas när deras länkar kommer att klickas inuti*Blad1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 Här är den kompletta exempelkoden som du kan köra med den medföljande[exempel på excel-fil](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
