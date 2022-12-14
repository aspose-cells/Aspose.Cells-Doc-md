---
title: Umbraco Exportera medlemmar till Excel
type: docs
weight: 10
url: /sv/net/umbraco-export-members-to-excel/
---
## **Introduktion**

 Exportera medlemmar till Excel är ett tillägg för Umbraco som låter dig exportera medlemmar från ditt Umbraco CMS till ett Excel- och OpenDocument-kalkylblad med[Aspose.Cells](https://products.aspose.com/cells/net/) . En ny nod med titeln**Exportera medlemmar till Excel** visas under Medlemsträdet i Umbracos backend efter installationen där du helt enkelt kan välja medlemmar att exportera och mata ut format för att få medlemmar i valt utdatadokumentformat.

### **Modulfunktioner**

Denna första version av tillägget har följande funktioner:

- Exportera medlemmar till Microsoft Excel-dokument (.xls, .xlsx och .xlsb)
- Exportera medlemmar till tabbavgränsat textdokument (.txt)
- Exportera medlemmar till CSV (kommaavgränsad) (*.csv)
- Exportera medlemmar till OpenDocument Spreadsheet (*.ods)
- Möjlighet att välja önskat utdataformat innan export
- Möjlighet att exportera alla eller valda medlemmar till valt utdatadokumentformat.
- Fungerar med alla .NET-versioner från och med .NET 2.0.
- Exporterat dokument skickas automatiskt till webbläsaren för nedladdning
- Om det väljs sparas en kopia av det exporterade dokumentet i mappen App_Data/AsposeMemberExport på servern för senare användning.
-  Kompatibel med ett brett utbud av Umbraco-versioner**4.5**+ **inklusive version 6 och 7.**

## **Systemkrav och plattformar som stöds**

### **Systemkrav**

För att kunna ställa in denna modul måste du ha följande krav uppfyllda:

- Umbraco 6.0+

Kontakta oss gärna om du vill installera denna modul på andra versioner av Umbraco.

### **Plattformar som stöds**

Modulen stöds på alla versioner av

- Umbraco körs på ASP.NET 4.0

## **Laddar ner**

Du kan ladda ner Export Members to Excel Add-on från en av följande platser

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installerar**

När du har laddat ner, följ dessa steg för att installera det här paketet på din Umbraco-webbplats:

1.  Logga in på Umbraco**Utvecklaren** sektion, till exempel `http://www.myblog.com/umbraco/`
1.  Från trädet, expandera**Paket** mapp.
1.  Härifrån finns det två sätt att installera ett paket: välj**Installera det lokala paketet** eller bläddra i**Umbraco Package Repository.**
1.  Om du installerar**lokalt paket**, packa inte upp paketet utan ladda blixtlåset i Umbraco.
1. Följ instruktionerna på skärmen.

**Notera:** Du kan få felet 'Maximal begäranslängd överskriden' när du installerar. Du kan enkelt åtgärda det här problemet genom att uppdatera värdet 'maxRequestLength' i din Umbraco web.config-fil.

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Använder sig av**

När du har installerat makrot är det väldigt enkelt att börja använda det på din webbplats:

1. Se till att du är inloggad på Umbraco**Utvecklaren** sektion, till exempel `http://www.myblog.com/umbraco/`
1.  Klick**Medlemmar** i listan med avsnitt längst ner till vänster på skärmen.
1.  I slutet av trädet ser du en nod med titeln**Exportera medlemmar till Excel** klicka på den för att starta tillägget Exportera till Excel.
1. Välj önskat utdatadokument och välj Medlemmar att exportera. Om du vill kan du exportera alla medlemmar lämna medlemsvalet eller klicka på kryssrutan i rubrikraden.
1.  Klick**Exportera** knappen längst ner och du kommer att uppmanas att ladda ner den exporterade filen.

## **Videodemo**

 Vänligen kontrollera[videon](https://www.youtube.com/watch?v=6PxZFvjWr2Y) nedan för att se modulen i aktion.

## **Stödja, utöka och bidra**

### **Stöd**

Från de allra första dagarna av Aspose visste vi att det inte skulle räcka att bara ge våra kunder bra produkter. Vi behövde också leverera bra service. Vi är själva utvecklare och förstår hur frustrerande det är när ett tekniskt problem eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem.

Det är därför vi erbjuder gratis support. Alla som använder vår produkt, oavsett om de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga alla problem eller förslag relaterade till Aspose.Words .NET för Umbraco-moduler med någon av följande plattformar

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Utöka och bidra**

Exportera medlemmar till Excel är ett tillägg med öppen källkod och dess källkod är tillgänglig på de stora sociala kodningswebbplatserna nedan. Utvecklare uppmanas att ladda ner källkoden och utöka funktionaliteten enligt sina egna krav.

#### **Källkod**

Du kan få den senaste källkoden från en av följande platser

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Hur man konfigurerar källkoden**

Du måste ha följande installerat för att kunna öppna och utöka källkoden

- Visual Studio 2010 eller senare

Följ dessa enkla steg för att komma igång

1. Ladda ner/klona källkoden.
1.  Öppna Visual Studio 2010 och välj**Fil** > **Öppet projekt**
1.  Bläddra till den senaste källkoden som du har laddat ner och öppna**ex Aspose.UmbracoMemberExportToExcel.sln**
