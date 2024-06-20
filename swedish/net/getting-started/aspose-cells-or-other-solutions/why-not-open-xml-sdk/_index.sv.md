---
title: Varför inte Open XML SDK
type: docs
weight: 90
url: /sv/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

Vi hör ibland den här frågan:

**Varför ska vi använda Aspose-produkter istället för den gratis Open XML SDK?**

Denna fråga är lätt att besvara: funktioner och funktionalitet.

{{% /alert %}}

## **Vad är Open XML SDK?**

Enligt [MSDN Library](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN) definieras Open XML SDK som:

"Open XML SDK 2.5 förenklar uppgiften att manipulera Open XML-paket och de underliggande Open XML-schemaelementen inom ett paket. Open XML SDK 2.5 kapslar in många vanliga uppgifter som utvecklare utför på Open XML-paket, så att du kan utföra komplexa operationer med bara några få rader kod."

OOXML-dokument är i grunden zippade XML-filer och Open XML SDK är en samling av klasser som låter dig arbeta med innehållet i OOXML-dokument på ett starkt typat sätt. Istället för att packa upp en fil för att extrahera XML, ladda den XML-filen in i ett DOM-träd och arbeta med XML-element och attribut direkt, ger Open XML SDK klasser för att göra detta.

## **Vad är Aspose.Cells?**

Aspose.Cells är en klassbibliotek som tillåter applikationer att utföra följande kalkylbladsbehandlingar:

- Högkvalitativa konverteringar mellan alla populära Microsoft Excel-format, inklusive konvertering till PDF, HTML, TIFF och utskrift.
- Programmering med en arbetsbok-objektmodell.
- Förmåga att bygga dokument från fragment, från en eller flera dokument, samtidigt som data automatiskt sammanfogas med stilistisk formatering, diagram och grafik.
- Funktioner på hög nivå, såsom importera data från olika datakällor inklusive Array, ArrayList, DataTable / ResultSet.
- Robust Formelberäkningsmotor som stödjer nästan alla vanliga och avancerade Microsoft Excel-funktioner.

## **Jämför Open XML SDK och Aspose.Cells**

Följande tabell jämför Open XML SDK och Aspose.Cells-funktioner.

|**Funktion eller funktionskategori**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Stödda Excel- eller andra format|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tab-separerad, ODS, vanlig text (TXT), PDF, XPS|
|Konvertera mellan Excel-format|Nej|Ja|
|<p>Högnivåprogrammering med arbetsboksobjektmodellen:</p><p>- Hitta och ersätta.</p><p>- Sammanställa kalkylblad.</p><p>- Kopiera fragment och kalkylblad mellan arbetsböcker.</p>|Nej|Ja|
|Detaljerad programmering med dokumentobjektmodellen, åtkomst till individuella element och formateringsegenskaper för alla kalkylbladselement.|Ja|Ja|
|Lågnivå direkt och fullständig åtkomst till de underliggande XML-elementen och attributen som relationsidentifierare, listidentifierare för ett OOXML-dokument.|Ja|Nej|
|<p>Generera rapporter, fyll dokument med data:</p><p>- Importera/exportera data till/från en DataTable / _ResultSet.</p><p>- Smarta markörer.</p><p>- Infoga/ta bort rader/kolumner/områden.</p><p>- Anpassade datakällor.</p>|Nej|Ja|
|<p>Rendering och utskrift:* Rendera kalkylbladssidor till rasterbilder (TIFF, flersidig TIFF, PNG, JPEG, BMP).* Rendera kalkylbladssidor till vektorbilder (EMF).</p><p>- Konvertera diagram till bilder (TIFF, flersidig TIFF, PNG, JPEG, BMP, EMF, etc.)</p><p>- Ange bildupplösning, kvalitet, komprimering och andra alternativ.</p><p>- Skriv ut kalkylblad med .NET-utskriftsinfrastrukturen. Komponenten har en inbyggd utskriftsmetod för att skriva ut kalkylbladen enligt Visningsutskrift i Microsoft Excel.</p>|Nej|Ja|
|Beräkna/omberäkna formler dynamiskt|Nej|Ja|
|Stödda plattformar|Windows, .NET|Windows, Linux, Java, .NET, Mono|

Du kan jämföra OpenXML med Aspose.Cells för att göra detta föreslår vi att du bekantar dig med Aspose.Cells for OpenXML-projektet - det visar hur olika uppgifter kan utföras med Aspose.Cells for .NET API jämfört med OpenXML. Projektet täcker även funktioner för att arbeta med textdokument som endast är tillgängliga i Aspose.Cells, men inte i OpenXML.

Detta projekt är också användbart för utvecklare som vill migrera från OpenXML till Aspose.Cells.

{{% alert color="primary" %}}

Utforska [tillägget med källkodsexempel på Aspose.Cells for .NET-funktioner jämfört med OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Detta tillägg använder utvärderingsversionen av Aspose.Cells. När du är nöjd med din utvärdering kan du köpa en licens från [Aspose webbplats](https://purchase.aspose.com/buy). För att ta bort utvärderingsmeddelanden och funktionsbegränsningar måste du tillämpa en produktlicens. Efter att ha köpt produkten kommer du att få en licensfil. Följ anvisningarna i ["Licensiering och prenumeration"](/cells/sv/net/licensing/) för att göra detta.

{{% /alert %}}

**Slutsats**: Open XML SDK och Aspose.Cells konkurrerar inte direkt eftersom de adresserar ganska olika behov och målgrupper.

## **Varför inte Open XML SDK**
Open XML SDK är ett klassbibliotek som ger ett starkt typat sätt att arbeta med OOXML-dokument. Aspose.Cells är ett mycket användbart kalkylbladsbehandlingsbibliotek som ger bra support för alla Microsoft Excel och andra filformat.

Om allt du behöver göra är en ganska grundläggande programmeringsåtgärd på ett XLSX-dokument kan Open XML SDK vara ett lämpligt val. Med Open XML SDK kommer du att vara ganska bekväm med att utföra enkla uppgifter som att generera ett enkelt XLSX-dokument eller ta bort kommentarer, rubriker/fotnoter, extrahera bilder eller andra. 
Vissa uppgifter kan uppnås med Open XML SDK, men kan inte uppnås med Aspose.Cells. Till exempel, om du behöver direkt åtkomst till XML-element och attribut för ett OOXML-dokument, bör du använda Open XML SDK.

Om du däremot behöver utföra komplexa operationer på dokument, som några av följande uppgifter, är användning av Aspose.Cells det bästa alternativet:

- Stöd för andra filformat utöver XLSX.
- Kopiera fragment och kalkylblad mellan arbetsböcker eller sammanfoga arbetsböcker på ett sätt som kombinerar objekt, format och annan formatering på lämpligt sätt.
- Ersätta formaterad eller oformaterad text.
- Funktioner på hög nivå, såsom importera data från olika datakällor inklusive Array, ArrayList, DataTable / ResultSet.
- Generera ett affärsdokument, såsom en order med orderdetaljer från en datakälla.
- Konvertera ett dokument till PDF eller XPS så att det visas precis som Microsoft Excel skulle ha konverterat det.
- Utveckla en .NET- eller Java-applikation.

