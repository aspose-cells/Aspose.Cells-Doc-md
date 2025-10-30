---
title: Varför inte Open XML SDK
type: docs
weight: 20
url: /sv/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

Vi hör ibland den här frågan:

**Varför ska vi använda Aspose-produkter istället för den gratis Open XML SDK?**

Den här frågan är lätt att besvara: **funktioner och funktionalitet**.

{{% /alert %}} 
## **Vad är Open XML SDK?**
Enligt MSDN Library definieras Open XML SDK som: Open XML SDK 2.0 förenklar uppgiften att manipulera Open XML-paket och de underliggande Open XML-schemaelementen inom ett paket. Open XML SDK 2.0 kapslar in många vanliga uppgifter som utvecklare utför på Open XML-paket, så att du kan utföra komplexa operationer med bara några få rader kod. OOXML-dokument är i huvudsak zippade XML-filer och Open XML SDK är en samling klasser som gör det möjligt för dig att arbeta med innehållet i OOXML-dokument på ett starkt typat sätt. Det vill säga istället för att packa upp en fil för att extrahera XML, ladda in den XML i ett DOM-träd och arbeta med XML-element och attribut direkt, tillhandahåller Open XML SDK klasser för att göra det.
## **Vad är Aspose.Cells?**
Aspose.Cells är ett klassbibliotek som tillåter din applikation att utföra följande kalkylbladsbehandling: Högkvalitativa konverteringar mellan alla populära Excel-format, inklusive konvertering till PDF, HTML, TIFF och utskrift. Programmering med arbetsbokobjektmodell. Möjlighet att bygga dokument från fragment, från en eller flera dokument, samtidigt som data automatiskt sammanfogas med stilistisk formatering, diagram och grafik. Högnivåfunktioner, såsom import av data från olika datakällor inklusive Array, ArrayList, DataTable / ResultSet. Robust formelberäkningssystem som stöder nästan alla standard- och avancerade Microsoft Excel-funktioner.


## **Jämför Open XML SDK och Aspose.Cells**
Följande tabell jämför funktioner mellan Open XML SDK och Aspose.Cells. 

|**Funktion eller funktionskategori**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Stödda Excel- eller andra format|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tab-separerad, ODS, vanlig text (TXT), PDF, XPS|
|Konvertera mellan Excel-format|Nej|Ja|
|<p>Högnivåprogrammering med arbetsboksobjektmodellen:</p><p>- Hitta och ersätta.</p><p>- Sammanställa kalkylblad.</p><p>- Kopiera fragment och kalkylblad mellan arbetsböcker.</p>|Nej|Ja|
|Detaljerad programmering med dokumentobjektmodellen, åtkomst till individuella element och formateringsegenskaper för alla kalkylbladselement.|Ja|Ja|
|Lågnivå direkt och fullständig åtkomst till de underliggande XML-elementen och attributen som relationsidentifierare, listidentifierare för ett OOXML-dokument.|Ja|Nej|
|<p>Generera rapporter, fylla dokument med data:</p><p>- Importera/exportera data till/från en *DataTable / *ResultSet.</p><p>- Smart Markers-funktion.</p><p>- Infoga/Ta bort rader/kolumner/omfång.</p><p>- Anpassade datakällor.</p>|Nej|Ja|
|<p>Rendering och utskrift:* Rendera kalkylbladssidor till rasterbilder (TIFF, multipage TIFF, PNG, JPEG, BMP).* Rendera kalkylbladssidor till vektorbilder (EMF).* Konvertera diagram till bilder (TIFF, multipage TIFF, PNG, JPEG, BMP, EMF etc.)</p><p>- Ange bildupplösning, kvalitet, komprimering och andra alternativ.</p><p>- Skriv ut kalkylblad med .NET-utskriftsinfrastructure. Komponenten har inbyggd utskriftsmetod för att skriva ut kalkylbladen som visas i utskriftsgranskningen av MS Excel.</p>|Nej|Ja|
|Beräkna/dynamiskt omberäkna formler|Nej|Ja|
|Stödda plattformar|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Slutsats**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
