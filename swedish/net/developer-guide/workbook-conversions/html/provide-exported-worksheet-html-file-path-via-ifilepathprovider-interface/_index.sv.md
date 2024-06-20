---
title: Ange sökvägen till den exporterade arbetsbladshtml filen via IFilePathProvider gränssnittet
type: docs
weight: 70
url: /sv/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Möjliga användningsscenario**
Anta att du har en Excel-fil med flera blad och vill exportera varje blad till en individuell HTML-fil. Om något av dina blad har länkar till andra blad kommer dessa länkar att vara trasiga i den exporterade HTML:n. För att hantera detta problem tillhandahåller Aspose.Cells [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) gränssnittet som du kan implementera för att åtgärda de trasiga länkarna.
## **Tillhandahålla sökväg för exporterad kalkylblads-HTML-fil via IFilePathProvider-gränssnitt**
Vänligen ladda ner [exempel Excel-filen](5115213.zip) använd i följande kod och dess exporterade HTML-filer. Alla dessa filer finns inom Temp-katalogen. Du ska extrahera den på C: enheten. Då kommer det att bli C:\Temp-katalogen. Öppna sedan Sheet1.html-filen i webbläsaren och klicka på de två länkarna i den. Dessa länkar refererar till de två exporterade HTML-arbetsbladen som ligger inuti C:\Temp\OtherSheets-katalogen.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Den följande skärmbilden visar hur C:\Temp\Sheet1.html och dess länkar ser ut

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Den följande skärmbilden visar HTML-källan. Som du kan se refererar länkarna nu till C:\Temp\OtherSheets-katalogen. Detta åstadkoms med [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) gränssnittet.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Exempelkod**
Observera att C:\Temp-katalogen endast är för illustrationssyfte. Du kan använda vilken katalog du vill och placera [exempel Excel-filen](5115211.xlsx) där och köra den angivna exempelkoden. Den skapar sedan en OtherSheets-underkatalog inom din katalog och exportera andra och tredje bladens HTML-filer i den. Ändra dirPath-variabeln inuti den angivna koden och hänvisa till katalogen du vill innan körning.

{{% alert color="primary" %}} 

Provlicensen för Aspose.Cells måste vara inställd för att det här exempelkoden ska fungera. Om du försöker köra koden utan att ha ställt in licensen, kommer den att fastna i en oändlig loop. Därför har vi lagt till en kontroll för att skriva ut ett meddelande och stoppa utförandet när licensen inte är inställd. Du kan antingen köpa en licens eller begära en 30-dagars tillfällig licens från Aspose.Purchase team.

{{% /alert %}} 

Vänligen observera att kommentera ut dessa rader inuti koden kommer att bryta länkarna i Sheet1.html och Sheet2.html eller Sheet3.html kommer inte att öppnas när deras länkar klickas i Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Här är den kompletta exempelkoden som du kan köra med den medföljande [exempel Excel-filen](5115211.xlsx)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
