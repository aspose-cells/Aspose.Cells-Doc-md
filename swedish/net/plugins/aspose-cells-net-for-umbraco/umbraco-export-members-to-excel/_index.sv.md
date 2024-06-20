---
title: Umbraco Exportera medlemmar till Excel
type: docs
weight: 10
url: /sv/net/umbraco-export-members-to-excel/
---

## **Introduktion**

Exportera medlemmar till Excel är en tillägg för Umbraco som gör det möjligt att exportera medlemmar från din Umbraco CMS till en Excel och öppna documentkalkyl med [Aspose.Cells](https://products.aspose.com/cells/net/). En ny nod med namnet **Exportera medlemmar till Excel** visas under Medlemmar i Umbracos backend efter installation där du enkelt kan välja medlemmar att exportera och utmatningsformat för att få medlemmar i valt utmatningsdokumentformat.

### **Modulfunktioner**

Denna första version av tillägget har följande funktioner:

- Exportera medlemmar till Microsoft Excel-dokument (.xls, .xlsx och .xlsb)
- Exportera medlemmar till tabbavgränsad textdokument (.txt)
- Exportera medlemmar till CSV (kommaavgränsad) (*.csv)
- Exportera medlemmar till OpenDocument Spreadsheet (*.ods)
- Alternativ att välja önskat utdataformat innan export
- Alternativ att exportera alla eller valda medlemmar till valt utdataformat för dokument.
- Fungerar med alla .NET-versioner från och med .NET 2.0.
- Exporterat dokument skickas automatiskt till webbläsaren för nedladdning
- Om valt kopieras det exporterade dokumentet till mappen App_Data/AsposeMemberExport på servern för senare användning.
- Kompatibel med ett brett utbud av Umbraco-versioner **4.5**+ **inklusive Version 6 och 7.**

## **Systemkrav och stödda plattformar**

### **Systemkrav**

För att installera denna modul måste du uppfylla följande krav:

- Umbraco 6.0 +

Tveka inte att kontakta oss om du önskar installera denna modul på andra versioner av Umbraco.

### **Stödda plattformar**

Modulen stöds på alla versioner av

- Umbraco som körs på ASP.NET 4.0

## **Nedladdning**

Du kan ladda ner Export Members to Excel Add-on från en av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installation**

När du har laddat ner, följ dessa steg för att installera detta paket på din Umbraco-webbplats:

1. Logga in på Umbraco **Developer** -avsnittet, till exempel `http://www.myblog.com/umbraco/`
1. I trädet, expandera **Paket**-mappen.
1. Här finns det två sätt att installera ett paket: välj **Install local package** eller bläddra i **Umbraco Package Repository.**
1. Om du installerar ett **lokalt paket**, packa inte upp paketet utan ladda in zip-filen i Umbraco.
1. Följ instruktionerna på skärmen.

**Observera:** Du kan få ett fel med ‘Maximalt förfrågningslängdsöverskridande’ när du installerar. Du kan enkelt lösa detta genom att uppdatera värdet ‘maxRequestLength’ i din Umbraco web.config-fil.

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Användning**

När du har installerat makrot är det väldigt enkelt att börja använda det på din webbplats:

1. Se till att du är inloggad på Umbraco **Developer** -avsnittet, till exempel `http://www.myblog.com/umbraco/`
1. Klicka på **Medlemmar** i listan över avsnitt i botten till vänster på skärmen.
1. I slutet av trädet kommer du att se en nod titulerad **Export Members To Excel** klicka på den för att starta Export to Excel-add-on.
1. Välj önskat utdataformat för dokument och välj medlemmar att exportera. Om du önskar att exportera alla medlemmar lämna medlemsvalet eller klicka i kryssrutan i rubrikraden.
1. Klicka på **Export** -knappen längst ner och du kommer att uppmanas att ladda ned den exporterade filen.

## **Video Demonstration**

Kolla in [videon](https://www.youtube.com/watch?v=6PxZFvjWr2Y) nedan för att se modulen i aktion:

## **Support, Utvidga och Bidra**

### **Support**

Från allra första början av Aspose visste vi att det inte bara skulle räcka med att ge våra kunder bra produkter. Vi behövde också leverera en bra service. Vi är själva utvecklare och förstår hur frustrerande det är när en teknisk fråga eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem. 

Detta är anledningen till att vi erbjuder kostnadsfri support. Alla som använder våra produkter, vare sig de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga alla problem eller förslag relaterade till Aspose.Words .NET för Umbraco-moduler med hjälp av någon av följande plattformar

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Utvidga och Bidra**

Exportera medlemmar till Excel är ett öppen källkodillägg och dess källkod finns tillgänglig på de största sociala kodningswebbplatserna som listas nedan. Utvecklare uppmanas att ladda ner källkoden och utöka funktionaliteten enligt sina egna krav.

#### **Källkod**

Du kan få den senaste källkoden från någon av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Hur man konfigurerar källkoden**

Du måste ha följande installerat för att öppna och utöka källkoden

- Visual Studio 2010 eller högre

Följ dessa enkla steg för att komma igång

1. Ladda ner/Klona källkoden.
1. Öppna Visual Studio 2010 och välj **Fil** > **Öppna projekt**
1. Bläddra till den senaste källkoden som du har laddat ner och öppna **t.ex. Aspose.UmbracoMemberExportToExcel.sln**
