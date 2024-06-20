---
title: Konvertera mellan Excel format
type: docs
weight: 20
url: /sv/net/convert-between-excel-formats/
---

## **Konvertera Excel till PDF**

**PDF**-filer används ofta för att utbyta dokument mellan organisationer, myndigheter och enskilda personer. Det är ett standarddokumentformat och mjukvaruutvecklare ombeds ofta att hitta ett sätt att konvertera Microsoft Excel-filer till **PDF**-dokument.
**Aspose.Cells** stödjer konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

Aspose.Cells for .NET stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara en Excel-fil som PDF med hjälp av Workbook-klassens Save-metod. Save-metoden tillhandahåller enummedlemmen SaveFormat.Pdf som konverterar de nativa Excel-filerna till PDF-format.

**Direkt konvertering** från kalkylblad till PDF, istället för att använda ett tredjepartsverktyg eller extern API, har flera **fördelar**:

1. Direkt konvertering kräver inte temporära filer eftersom hela processen kan göras i minnet.
2. Ingen XML-fil behövs så stora filer kan enkelt konverteras.
3. Konverteringshastigheten är mycket snabbare.

**För att konvertera filer till PDF:**

1. Skapa en instans av **Workbook**-klassen genom att anropa dess tomma konstruktor.
2. Du kan **öppna/ladda** en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
3. Gör ditt önskade arbete (ange data, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt osv) på kalkylbladet med hjälp av Aspose.Cells' API.
4. När kalkylbladskoden är klar, anropa **Workbook-klassens Save-metod** för att spara kalkylbladet. Filformatet ska vara PDF så välj Pdf (ett fördefinierat värde) från SaveFormat-uppräkningen för att generera det slutgiltiga PDF-dokumentet.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Konvertera Excel till MHTML**

**MHTML** kombinerar vanlig HTML med externa resurser (det vill säga innehåll som vanligtvis är länkat, som bilder, animationer, ljud osv) till en fil. De används för e-postmeddelanden med filändelsen .mht.
Aspose.Cells stödjer att läsa och skriva MHTML-filer.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Konvertera Excel till XPS**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad i textformat. För textformat (till exempel TXT, TabDelim, CSV etc.) sparar både Microsoft Excel och Aspose.Cells innehållet i endast det aktiva kalkylbladet som standard.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Ladda ned provkoden**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
