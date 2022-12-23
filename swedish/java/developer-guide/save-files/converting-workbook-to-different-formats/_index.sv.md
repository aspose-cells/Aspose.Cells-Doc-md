---
title: Konvertera arbetsbok till olika format
type: docs
weight: 20
url: /sv/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells stöder konvertering mellan många format. Tekniskt sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel till XPS**

Dokumentformatet XPS består av strukturerad XML-uppmärkning som definierar layouten för ett dokument och det visuella utseendet på varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

Markeringsspråket för XPS är en delmängd av XAML som gör att det kan inkorporera vektorgrafiska element i dokument, med XAML för att markera Windows Presentation Foundation (WPF) primitiver. Elementen som används beskrivs i termer av banor och andra geometriska primitiver.

En XPS-fil är i själva verket ett Unicoded ZIP-arkiv som använder Open Packaging Conventions, som innehåller filerna som utgör dokumentet. Dessa inkluderar en XML-uppmärkningsfil för varje sida, text, inbäddade typsnitt, rasterbilder, 2D-vektorgrafik samt information om hantering av digitala rättigheter. Innehållet i en XPS-fil kan granskas helt enkelt genom att öppna den i ett program som stöder ZIP-filer.

Från Aspose.Cells 6.0.0, Microsoft Excel tp XPS stöds konvertering.

### **Konvertera ett arbetsblad till XPS**

Följande exempel visar hur man konverterar ett enstaka kalkylblad i en Excel-fil till XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Exportera hela arbetsboken till XPS**

Följande exempel visar hur du konverterar hela arbetsboken till formatet XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Snabb konvertering av Excel till XPS**

Följande exempel visar ett enkelt sätt att direkt konvertera Excel-filen till XPS-format.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Konvertera Excel till MHTML-filer**

[MHTML](https://en.wikipedia.org/wiki/MHTML) kombinerar normal HTML med externa resurser; det vill säga innehåll som vanligtvis länkas in som bilder, animationer, ljud och så vidare till en fil. De används för e-postmeddelanden med filtillägget .mht.

{{% alert color="primary" %}}

Aspose.Cells stöder läsning och skrivning av MHTML filer.

{{% /alert %}}

Att konvertera ett kalkylblad till MHTML är en snabb operation, som visas nedan.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Konvertera Excel-filer till HTML**

 API:erna Aspose.Cells ger stöd för export av kalkylblad till formatet HTML. För detta ändamål använder Aspose.Cells**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**klass som tillåter utvecklare att kontrollera flera aspekter av utdata HTML.

Koden nedan visar hur man använder**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**klass för att exportera Microsoft Excel-filer till HTML format utan att ange ytterligare parametrar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Du kan uppnå samma resultat genom att klara av**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** till**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** metod.

{{% /alert %}}

### **Ställa in bildinställningar för HTML**

 Från och med 8.0.2 har Aspose.Cells exponerats**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**för**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**klass, vilket gör att utvecklare kan ange bildpreferenser när de sparar kalkylblad i formatet HTML.

Bildinställningarna som kan tillämpas är:

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Hämtar eller ställer in bildtypen. Observera att alla former, inklusive diagram, återges som bilder i utgången HTML.
- **[Kvalitet](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: Hämtar eller ställer in bildkvaliteten mellan 0 och 100, när ImageFormat anges som Jpeg.
- **[VerticalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: Hämtar eller ställer in bildens vertikala upplösning i punkter per tum.
- **[HorizontalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: Hämtar eller ställer in bildens horisontella upplösning i punkter per tum.
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**Hämtar eller ställer in komprimeringstypen för bilderna när ImageFormat anges som Tiff.
- **[Transparent](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**: Indikerar om bakgrunden för en bild ska vara genomskinlig när ImageFormat anges som Png.

 Koden nedan visar hur man använder**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** för att ange olika preferenser.

|**Kalkylbladsvy före export**|**HTML vy efter export**|
|:- |:- |
|![Kalkylbladsvy före export](converting-workbook-to-different-formats_1.png)|![HTML vy efter export](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Konvertera Excel till PDF-filer**

PDF dokument används ofta som standardformat för utbyte av dokument mellan organisationer, statliga sektorer och individer. Mjukvaruutvecklare uppmanas ofta att skapa ett sätt att enkelt konvertera Microsoft Excel-filer till PDF-dokument. Aspose.Cells stöder dessa funktioner. Den här artikeln visar hur.

### **Konvertera Excel till PDF**

Microsoft Excel till PDF konvertering introducerades med Aspose.Cells for Java 2.3.0. Från den versionen kan Aspose.Cells[konvertera kalkylblad till PDF direkt](#direct-conversion) (Inklusive[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files) ), utan annan produkt. För att konvertera kalkylblad med äldre versioner av Aspose.Cells,[använd Aspose.PDF för konverteringen](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell konverterar kalkylblad till PDF med en hög grad av noggrannhet och trohet. Det finns dock några[begränsningar](/cells/sv/java/converting-workbook-to-different-formats/#conversion-attributes), listad i slutet av den här artikeln.

{{% alert color="primary" %}}

 Aspose.Cells for Java skriver direkt informationen om API och versionsnummer i utdatadokument. Till exempel, när dokument återges till PDF, fylls Aspose.Cells for Java i**Ansökan** fält med värdet 'Aspose.Cells' och**PDF Producent** fält med ett värde, t.ex. 'Aspose.Cells for Java v17.9'.

Observera att du inte kan instruera Aspose.Cells for Java att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}}

#### **Direkt konvertering**

Spara en Excel-fil direkt till PDF med hjälp av**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** metod och tillhandahålla**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**gränssnittsmedlem. Direkt konvertering som denna är den mest effektiva konverteringsmetoden. Det förlorar inte data eller formatering men gör att utdata PDF ser ut som indatafilen i Excel.

 För att ange säkerhetsalternativ när du sparar till PDF, använd**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Avancerad konvertering**

Du kan också välja att använda**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** klass för att ställa in olika attribut för konverteringen. Ställa in olika egenskaper för**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** klass ger dig kontroll över inställningarna för utskrift, typsnitt, säkerhet och komprimering för den resulterande PDF-filen. Mest anmärkningsvärd egendom är**[Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**som gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.

##### **Spara Excel-kalkylblad till PDF/A-kompatibla filer**

Nedan medföljande kodavsnitt visar användningen av**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** klass för att spara Excel-filerna i PDF/A-kompatibelt PDF-format.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Konvertering med Aspose.Pdf: Aspose.Cells före 2.3.0**

 För Aspose.Cells versioner före version 2.3.0 måste du använda en komponent som t.ex.[Aspose.PDF for Java](/pdf/java/)för att konvertera kalkylblad till PDF-filer. Aspose.Cells och Aspose.PDF arbetar tillsammans för att konvertera ett kalkylblad till PDF via ett mellansteg.

Så här konverterar du kalkylark till PDF med Aspose.Cells och Aspose.PDF:

1.  Instantiera ett objekt av**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)**klass genom att anropa dess tomma konstruktor.
1. Gör önskat arbete på kalkylarket med hjälp av Aspose.Cells API.
1. Ring**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**metod för att spara kalkylarket:
 1. Ställ in filformatet till XML.
 1. Välj Aspose_Pdf (ett fördefinierat värde) från FileFormatType-gränssnittet. Detta styr sparmetoden att generera ett kalkylblad i XML-format som är kompatibelt med Aspose.PDF-schemat så att Aspose.PDF for Java sedan kan generera ett PDF-dokument.
1. När XML-filen har skapats, skapa ett objekt av Pdf-klassen i paketet aspose.pdf.
1. Anropa Pdf-klassens bindXML-metod och skicka namnet på den utgående XML-filen.
1. Anropa Pdf-klassens sparmetod för att generera dokumentet PDF.

Ovanstående steg implementeras nedan i ett exempel.

{{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att ringa**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** metod precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}

#### **Konverteringsattribut**

Vi arbetar hårt för att förbättra konvertering och andra aspekter av Aspose.Cells med varje utgåva. Omvandlingen av Excel till PDF har några begränsningar. Vissa formatinställningar som anges i ett kalkylblad kan gå förlorade, och alla ritobjekt stöds inte.

Tabellen nedan listar alla funktioner som helt eller delvis stöds vid export till PDF med Aspose.Cells. Den här tabellen är inte slutgiltig och täcker inte alla kalkylbladsattribut. Den kan också identifiera de funktioner som kanske inte stöds eller som delvis stöds för konverteringen.

{{% alert color="primary" %}}

|**Dokumentelement**|**Attribut**|**Nätstödd**|**Anteckningar**|
|:- |:- |:- |:- |
|Inriktning||Ja||
|Rotation||Delvis|Stöder endast 90 och -90.|
|Bakgrundsinställningar||Ja||
|Gräns|Färg|Ja||
|Gräns|Linjestil|Ja||
|Gräns|Linjebredd|Ja||
|Cell Data||Ja||
|Kommentarer||Nej||
|Villkorlig formatering||Ja||
|Dokument egenskaper||Ja||
|Rita objekt||Ja||
|Font|Storlek|Ja||
|Font|Färg|Ja||
|Font|Stil|Ja||
|Font|Understrykning|Ja||
|Font|Effekter|Delvis|Endast genomslagseffekten stöds|
|Bilder||Ja||
|Hyperlänk||Ja||
|Diagram||Ja||
|Sammanslagna Cells||Ja||
|Sidbrytning||Ja||
|Utskriftsformat|Sidhuvud/sidfot|Ja||
|Utskriftsformat|Marginaler|Ja||
|Utskriftsformat|Sidorientering|Ja||
|Utskriftsformat|Sidstorlek|Ja||
|Utskriftsformat|Utskriftsområde|Ja||
|Utskriftsformat|Skriv ut titlar|Ja||
|Utskriftsformat|Skalning|Ja||
|Radhöjd/kolumnbredd||Ja||
{{% /alert %}}
