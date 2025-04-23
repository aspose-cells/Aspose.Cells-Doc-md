---
title: Konvertera Arbetsbok till Olika Format
type: docs
weight: 20
url: /sv/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells stödjer konvertering mellan många format. Tekniskt sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel till XPS**

XPS-dokumentformatet består av strukturerad XML-markering som definierar layouten för ett dokument och sidans visuella utseende, tillsammans med renderingregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

Märkspråket för XPS är en delmängd av XAML som gör att det kan innehålla vektorgrafikelement i dokument genom att använda XAML för att markera Windows Presentation Foundation (WPF) primitiver. De använda elementen beskrivs i termer av banor och andra geometriska primitiver.

En XPS-fil är faktiskt en Unicode ZIP-arkiv som använder Open Packaging Conventions, som innehåller filer som utgör dokumentet. Dessa inkluderar en XML-markering för varje sida, text, inbäddade typsnitt, rasterbilder, 2D-vektorgrafik, såväl som digitala rättighetsinformation. Innehållet i en XPS-fil kan undersökas enkelt genom att öppna den i en applikation som stöder ZIP-filer.

Från Aspose.Cells 6.0.0 stöds konvertering från Microsoft Excel till XPS.

### **Konvertera enskilt arbetsblad till XPS**

Följande exempel visar hur du konverterar ett enskilt arbetsblad i en Excel-fil till XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Exportera hela arbetsboken till XPS**

Följande exempel visar hur du konverterar hela arbetsboken till XPS-format.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Snabb konvertering från Excel till XPS**

Följande exempel visar ett enkelt sätt att direkt konvertera Excel-filen till XPS-format.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Konvertera Excel till MHTML-filer**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) kombinerar vanlig HTML med externa resurser; dvs. innehåll som vanligtvis länkas in, som bilder, animationer, ljud osv, i en fil. De används för e-postmeddelanden med filtypen .mht.

{{% alert color="primary" %}}

Aspose.Cells stödjer att läsa och skriva MHTML-filer.

{{% /alert %}}

Att konvertera en kalkyl till MHTML är en snabb operation, som visas nedan.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Konvertera Excel-filer till HTML**

Aspose.Cells API: er ger stöd för att exportera kalkylblad till HTML-format. För detta ändamål använder Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)-klassen, som låter utvecklare styra flera aspekter av det utdata-HTML.

Koden nedan visar hur man använder [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)-klassen för att exportera Microsoft Excel-filer till HTML-format utan att ange ytterligare parametrar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Du kan uppnå samma resultat genom att skicka [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) till metoden [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-).

{{% /alert %}}

### **Inställning av bildpreferenser för HTML**

Från och med 8.0.2 har Aspose.Cells exponerat [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) för [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)-klassen, vilket låter utvecklare specificera bildpreferenser när de sparar kalkylblad till HTML-format.

Bildinställningarna som kan tillämpas är:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): Hämtar eller anger bildtypen. Observera att alla former, inklusive diagram, renderas som bilder i det slutgiltiga HTML-utdata.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): Hämtar eller anger kvaliteten på bilder mellan 0 till 100, när ImageFormat är specificerad som Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): Hämtar eller anger den vertikala upplösningen för bilden i punkter per tum.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): Hämtar eller anger den horisontella upplösningen för bilden i punkter per tum.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): Hämtar eller anger komprimeringstypen för bilderna när ImageFormat är specificerad som Tiff.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): Indikerar om bakgrunden på en bild bör vara transparent när ImageFormat är specificerad som Png.

Koden nedan visar hur man använder [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) för att ange olika preferenser.

|**Kalkylblads vy före export**|**HTML-vy efter export**|
| :- | :- |
|![Kalkylblads vy före export](converting-workbook-to-different-formats_1.png)|![HTML-vy efter export](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Konvertera Excel till PDF-filer**

PDF-dokument används allmänt som ett standardformat för att utbyta dokument mellan organisationer, regeringen och enskilda. Programutvecklare ombeds ofta att hitta ett sätt att enkelt konvertera Microsoft Excel-filer till PDF-dokument. Aspose.Cells stöder dessa funktioner. Den här artikeln visar hur.

### **Konvertera Excel till PDF**

Microsoft Excel till PDF-konvertering introducerades med Aspose.Cells for Java 2.3.0. Från den utgåvan kan Aspose.Cells [konvertera kalkylblad direkt till PDF](#direct-conversion) (inklusive [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), utan en annan produkt. För att konvertera kalkylblad med äldre versioner av Aspose.Cells, [använd Aspose.PDF för konvertering](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cells konverterar kalkylblad till PDF med hög noggrannhet och trohet. Det finns dock några [begränsningar](/cells/sv/java/converting-workbook-to-different-formats/#conversion-attributes), som listas i slutet av den här artikeln.

{{% alert color="primary" %}}

Aspose.Cells for Java skriver direkt informations om API och versionsnummer i utdata dokument. Till exempel, när dokumentet renderas till PDF, fyller den i **Applikation**-fältet med värdet 'Aspose.Cells' och **PDF-producent**-fältet med ett värde, t.ex. 'Aspose.Cells for Java v17.9'.

Observera att du inte kan instruera Aspose.Cells for Java att ändra eller ta bort denna information från utdatafiler.

{{% /alert %}}

#### **Direkt konvertering**

Spara en Excel-fil direkt till PDF med metoden [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) och tillhandahålla gränssnittsmedlemmen [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF). Direktkonvertering på detta sätt är den mest effektiva konverteringsmetoden. Den förlorar inte data eller formatering men håller den utdata PDF: en liknande den inmatade Excel-filen.

För att ange säkerhetsalternativ när du sparar till PDF, använd [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Avancerad konvertering**

Du kan också välja att använda [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-klassen för att ange olika attribut för konverteringen. Att ange olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-klassen ger dig kontroll över utskrift, teckensnitt, säkerhets- och komprimeringsinställningar för den resulterande PDF-filen. Mest märkbara egenskapen är [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) som ger dig möjlighet att spara Excel-filerna till PDF/A-kompatibla PDF-filer.

##### **Spara Excel-kalkylblad till PDF/A-kompatibla filer**

Nedan anges kodning som visar användningen av [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-klassen för att spara Excel-filer i PDF/A-kompatibilt PDF-format.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Konvertering med Aspose.Pdf: Aspose.Cells Före 2.3.0**

För Aspose.Cells versioner före version 2.3.0 behöver du använda en komponent som [Aspose.PDF för Java](/pdf/java/) för att konvertera kalkylblad till PDF-filer. Aspose.Cells och Aspose.PDF samarbetar för att konvertera ett kalkylblad till PDF via ett mellansteget.

För att konvertera kalkylblad till PDF med Aspose.Cells och Aspose.PDF:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) -klassen genom att anropa dess tomma konstruktor.
1. Gör ditt önskade arbete på kalkylarket med hjälp av Aspose.Cells API.
1. Anropa metoden [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) för att spara kalkylarket:
   1. Ange filformatet till XML.
   1. Välj Aspose_Pdf (ett fördefinierat värde) från gränssnittet FileFormatType. Detta leder spar metoden att generera ett kalkylblad i XML-format kompatibelt med Aspose.PDF-schema så att Aspose.PDF för Java sedan kan generera ett PDF-dokument.
1. När XML-filen har skapats, skapa en objekt av klassen Pdf i paketet aspose.pdf.
1. Anropa metoden bindXML i klassen Pdf och skicka namnet på den resulterande XML-filen.
1. Anropa metoden save i klassen Pdf för att generera PDF-dokumentet.

Ovanstående steg implementeras nedan i ett exempel.

{{% alert color="primary" %}}

Om din kalkylblad innehåller formler är det bäst att anropa [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) metoden strax före rendering av kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden omberäknas och de korrekta värdena visas i PDF:n.

{{% /alert %}}

#### **Konverteringsattribut**

Vi arbetar hårt med att förbättra konvertering och andra aspekter av Aspose.Cells vid varje versionssläpp. Konvertering från Excel till PDF har vissa begränsningar. Vissa formateringsinställningar som specificerats i ett kalkylblad kan gå förlorade, och inte alla ritobjekt stöds.

Tabellen nedan listar alla funktioner som helt eller delvis stöds vid export till PDF med Aspose.Cells. Denna tabell är inte slutgiltig och täcker inte alla kalkylbladsegenskaper. Den kan också identifiera de funktioner som kanske inte stöds eller delvis stöds för konverteringen.

{{% alert color="primary" %}}

|**Dokumentelement**|**Egenskap**|**Nät Stödd**|**Noteringar**|
| :- | :- | :- | :- |
|Justering| |Ja| |
|Rotation| |Delvis|Endast stöder 90 och -90.|
|Bakgrundsin...  |Ja| 
|Gräns|Färg|Ja| 
|Gräns|Linjestil|Ja| 
|Gräns|Linjebredd|Ja| 
|Cell Data| |Ja| 
|Kommentarer| |Nej| |
|Villkorlig formatering| |Ja| 
|Dokumentegenskaper| |Ja| 
|Ritobjekt| |Ja| |
|Teckensnitt|Storlek|Ja| 
|Teckensnitt|Färg|Ja| 
|Teckensnitt|Stil|Ja| 
|Teckensnitt|Understrykning|Ja| 
|Teckensnitt|Effekter|Delvis|Endast strykningseffekten stöds|
|Bilder| |Ja| 
|Hypertextlänk| |Ja| 
|Diagram| |Ja| |
|Sammanfogade celler| |Ja| |
|Sidbrytning| |Ja| |
|Sidoppsett|Sidhuvud/-fot|Ja| |
|Sidoppsett|Marginaler|Ja| |
|Sidoppsett|Sidorientering|Ja| |
|Sidoppsett|Sidstorlek|Ja| |
|Sidoppsett|Utskriftsområde|Ja| |
|Sidoppsett|Utskriftsrubriker|Ja| |
|Sidoppsett|Skalning|Ja| |
|Radhöjd/Kolumnbredd| |Ja| |
{{% /alert %}}
{{< app/cells/assistant language="java" >}}
