---
title: Tillhandahålla sökväg för exporterad kalkylblads HTML fil via IFilePathProvider gränssnitt
type: docs
weight: 870
url: /sv/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Möjliga användningsscenario**
Anta att du har en Excel-fil med flera ark och du vill exportera varje ark till enskild HTML-fil. Om något av dina ark har länkar till andra ark kommer dessa länkar att vara brutna i den exporterade HTML:n. För att hantera detta problem tillhandahåller Aspose.Cells [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)gränssnitt som du kan implementera för att åtgärda de brutna länkarna.
## **Tillhandahålla sökväg för exporterad kalkylblads-HTML-fil via IFilePathProvider-gränssnitt**
Ladda ner den [exempel excel-filen](5473417.zip) som används i följande kod och dess exporterade HTML-filer. Alla dessa filer finns inuti *Temp*-mappen. Du bör packa upp den på *C:*-enheten. Då blir den *C:\Temp*-mappen. Sedan öppnar du *Sheet1.html*-filen i webbläsaren och klickar på de två länkarna däri. Dessa länkar hänvisar till de två exporterade HTML-kalkylbladen som finns inuti *C:\Temp\OtherSheets*-mappen.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Följande skärmbild visar hur *C:\Temp\Sheet1.html* och dess länkar ser ut

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Följande skärmbild visar HTML-källan. Som du kan se hänvisar länkarna nu till *C:\Temp\OtherSheets*-mappen. Detta uppnåddes genom att använda [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)-gränssnittet.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Exempelkod**
Observera att *C:\Temp*-mappen endast är för illustrationssyfte. Du kan använda valfri mapp och placera [exempel excel-filen](5473414.xlsx) där och köra den medföljande provkoden. Det kommer sedan skapa *OtherSheets*-undermappen inuti din mapp och exportera andra och tredje arks HTML inuti den. Vänligen ändra variabeln *dirPath* i den medföljande koden och hänvisa den till den mapp du valt innan körning.

{{% alert color="primary" %}} 

Provlicensen för Aspose.Cells måste vara inställd för att det här exempelkoden ska fungera. Om du försöker köra koden utan att ha ställt in licensen, kommer den att fastna i en oändlig loop. Därför har vi lagt till en kontroll för att skriva ut ett meddelande och stoppa utförandet när licensen inte är inställd. Du kan antingen köpa en licens eller begära en 30-dagars tillfällig licens från Aspose.Purchase team.

{{% /alert %}} 

Observera att kommentera de här raderna i koden kommer att bryta länkarna i *Sheet1.html* och *Sheet2.html* eller *Sheet3.html*, vilket innebär att de inte kommer att öppnas när deras länkar klickas inuti *Sheet1.html*



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



Här är det kompletta exempelkod som du kan köra med den tillhandahållna [exempel-excelfilen](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
