---
title: Konvertera mellan Excel-format
type: docs
weight: 20
url: /sv/net/convert-between-excel-formats/
---
## **Konvertera Excel till PDF**

**PDF** filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till**PDF** dokument.
**Aspose.Cells** stöder konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

Aspose.Cells för .NET stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara en Excel-fil till PDF med hjälp av arbetsbokklassens Spara-metod. Spara-metoden tillhandahåller enum-medlemmen SaveFormat.Pdf som konverterar de ursprungliga Excel-filerna till PDF-format.

**Konverterar** direkt från kalkylblad till PDF, istället för att använda ett tredjepartsverktyg eller extern API, har flera**fördelar**:

1. Direkt konvertering kräver inte tillfälliga filer eftersom hela processen kan göras i minnet.
1. Ingen XML-fil behövs så stora filer kan enkelt konverteras.
1. Konverteringshastigheten är mycket snabbare.

**Så här konverterar du filer till PDF:**

1.  Instantiera ett objekt av**Arbetsbok** klass genom att anropa dess tomma konstruktor.
1.  Du får**öppna/ladda** en befintlig mallfil eller hoppa över det här steget om du skapar arbetsboken från början.
1. Gör ditt önskade arbete (mata in data, tillämpa formatering, ställ in formler, infoga bilder eller andra ritobjekt och så vidare) på kalkylarket med hjälp av Aspose.Cells' API:er.
1.  När kalkylarkskoden är klar ringer du**Arbetsboksklass Spara metod** för att spara kalkylarket. Filformatet bör vara PDF så välj Pdf (ett fördefinierat värde) från SaveFormat-uppräkningen för att generera det slutliga PDF-dokumentet.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Konvertera Excel till MHTML**

**MHTML** kombinerar normal HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljud och så vidare) till en fil. De används för e-postmeddelanden med filtillägget .mht.
Aspose.Cells stöder läsning och skrivning av MHTML-filer.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Konvertera Excel till XPS**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV etc.) sparar både Microsoft Excel och Aspose.Cells endast innehållet i det aktiva kalkylbladet som standard.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Ladda ner exempelkod**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
