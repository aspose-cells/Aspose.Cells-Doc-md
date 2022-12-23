---
title: Varför inte öppna XML SDK
type: docs
weight: 20
url: /sv/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

Ibland hör vi denna fråga:

**Varför ska vi använda Aspose-produkter snarare än gratis Open XML SDK?**

 Denna fråga är lätt att besvara:**funktioner och funktionalitet**.

{{% /alert %}} 
## ** Vad är Open XML SDK?**
Enligt MSDN-biblioteket definieras Open XML SDK som: Open XML SDK 2.0 förenklar uppgiften att manipulera Open XML-paket och de underliggande Open XML-schemaelementen i ett paket. Open XML SDK 2.0 kapslar in många vanliga uppgifter som utvecklare utför på Open XML-paket, så att du kan utföra komplexa operationer med bara några rader kod.OOXML-dokument är i huvudsak zippade XML-filer och Open XML SDK är en samling klasser som tillåter dig att arbeta med innehållet i OOXML-dokument på ett starkt skrivet sätt. Det är istället för att packa upp en fil för att extrahera XML, ladda den XML-en i ett DOM-träd och arbeta med XML-element och -attribut direkt, Open XML SDK tillhandahåller klasser för att göra det.
## ** Vad är Aspose.Cells?**
Aspose.Cells är ett klassbibliotek som låter din applikation utföra följande kalkylbladsbearbetningsuppgifter: Högkvalitativa konverteringar mellan alla populära Excel-format, inklusive konvertering till PDF, HTML, TIFF och utskrift. Programmering med en arbetsboksobjektmodell. Möjlighet att bygga dokument från fragment, från ett eller flera dokument, samtidigt som data automatiskt sammanfogas genom stilistisk formatering, diagram och grafik. Funktioner på hög nivå, såsom import av data från olika datakällor inklusive Array, ArrayList, DataTable / ResultSet. Robust formelberäkningsmotor som stöder nästan alla standard- och avancerade Microsoft Excel-funktioner.

{{% alert color="primary" %}}
## ** Jämför Open XML SDK och Aspose.Cells**
 Följande tabell jämför Open XML SDK och Aspose.Cells funktioner.{{% /alert %}}

|**Funktion eller funktionskategori**|**Öppna XML SDK**|**Aspose.Cells**|
|:- |:- |:- |
|Excel eller andra format som stöds|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tab Delimited, ODS, vanlig text (TXT), 0816143474|
|Konvertera mellan Excel-format|Nej|Ja|
|<p>Högnivåprogrammering med en arbetsboksobjektmodell:</p><p>- Hitta och ersätta.</p><p>- Sätt ihop kalkylblad.</p><p>- Kopiera fragment och kalkylblad mellan arbetsböcker.</p>|Nej|Ja|
|Detaljerad programmering med en dokumentobjektmodell, tillgång till enskilda element och formateringsegenskaper för alla kalkylbladselement.|Ja|Ja|
|Direkt och fullständig tillgång på låg nivå till de underliggande XML-elementen och attributen såsom relationsidentifierare, listidentifierare för ett OOXML-dokument.|Ja|Nej|
|<p>Generera rapporter, fyll i dokument med data:</p><p>- Importera/exportera data till/från en*Datatabell /*Resultatet satt.</p><p>- Funktionen Smart Markers.</p><p>- Infoga/ta bort rader/kolumner/intervall.</p><p>- Anpassade datakällor.</p>|Nej|Ja|
|<p>Rendering och utskrift:* Återge kalkylbladssidor till rasterbilder (TIFF, flersidiga TIFF, PNG, JPEG, BMP).*Återge kalkylbladssidor till vektorbilder (EMF).* Konvertera diagram till bilder (TIFF, flersidigt TIFF, PNG, JPEG, BMP, BMP, EMF, alternativ för bildkvalitet, <p>, etc.</p> andra kvalitet, komprimering etc.) </p><p>- Skriv ut kalkylblad med .NET utskriftsinfrastruktur. Komponenten har en inbyggd utskriftsmetod för att skriva ut kalkylbladen som visas i Förhandsgranskning av MS Excel.</p>|Nej|Ja|
|Beräkna/beräkna om formler dynamiskt| Nej| Ja|
|Plattformar som stöds|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Slutsats**
  {{% alert color="primary" %}}Open XML SDK och Aspose.Cells konkurrerar inte head to head eftersom de adresserar ganska olika behov och målgrupper. Open XML SDK är ett klassbibliotek för att tillhandahålla ett välskrivet sätt att arbeta med OOXML-dokument. Aspose.Cells är ett mycket användbart bibliotek för bearbetning av kalkylblad som ger bra stöd för alla Microsoft Excel och andra filformat. Om allt du behöver göra är en ganska grundläggande programmeringsoperation på ett XLSX-dokument, kan Open XML SDK vara ett lämpligt val. Med Open XML SDK kommer du att vara ganska bekväm med att göra enkla uppgifter som att skapa ett enkelt XLSX-dokument eller ta bort kommentarer, sidhuvuden/sidfötter, extrahera bilder eller annat. Vissa uppgifter kan uppnås med Open XML SDK, men kan inte uppnås med Aspose.Cells. Om du till exempel behöver direkt tillgång till XML-elementen och attributen för ett OOXML-dokument, bör du använda Open XML SDK. Men om du behöver utföra komplexa operationer på dokument, som några av följande uppgifter, då är det bästa alternativet att använda Aspose.Cells: Stöd andra filformat utöver XLSX. Kopiera fragment och kalkylblad mellan arbetsböcker eller sammanfoga arbetsböcker på ett sätt som kombinerar objekt, stilar och annat formatering på ett lämpligt sätt. Ersätt formaterad eller oformaterad text. Funktioner på hög nivå, såsom import av data från olika datakällor inklusive Array, ArrayList, DataTable / ResultSet. Skapa ett affärsdokument, till exempel en beställning med orderinformation från en datakälla. Konvertera ett dokument till PDF eller XPS så att det ser ut precis som Microsoft Excel skulle ha konverterat det. Utveckla en .NET- eller Java-applikation.{{% /alert %}}
