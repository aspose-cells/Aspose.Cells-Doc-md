---
title: Olika sätt att spara filer
linktitle: Spara filer
type: docs
weight: 40
url: /sv/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att skapa och spara filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}}

## **Olika sätt att spara filer**

 Aspose.Cells tillhandahåller**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** som representerar en Microsoft Excel-fil och tillhandahåller de egenskaper och metoder som krävs för att arbeta med Excel-filer. De**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** klass ger**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metod som används för att spara Excel-filer. De**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Metoden har många överbelastningar som används för att spara filer på olika sätt.

 Filformatet som filen sparas i bestäms av**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**uppräkning

|**Filformatstyper**|**Beskrivning**|
|:- |:- |
|CSV|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003-fil|
|Xlsx|Representerar en Excel 2007 XLSX-fil|
|Xlsm|Representerar en Excel 2007 XLSM-fil|
|Xltx|Representerar en Excel 2007 mall XLTX-fil|
|Xltm|Representerar en Excel 2007 makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007 binär XLSB-fil|
|SpreadsheetML|Representerar en XML-fil för kalkylblad|
|TSV|Representerar en tabbseparerad värdefil|
|TabDelimited|Representerar en tabbavgränsad textfil|
|ODS|Representerar en ODS-fil|
|Html|Representerar HTML-fil(er)|
|MHtml|Representerar en MHTML-fil(er)|
|Pdf|Representerar en PDF-fil|
|XPS|Representerar ett XPS-dokument|
|TIFF|Representerar Tagged Image File Format (TIFF)|

## **Spara fil i olika format**

 För att spara filer till en lagringsplats, ange filnamnet (komplett med lagringssökväg) och önskat filformat (från**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**uppräkning) när du anropar**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objekt**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Spara arbetsbok som pdf**
Portable Document Format (PDF) är en typ av dokument som skapades av Adobe redan på 1990-talet. Syftet med detta filformat var att införa en standard för representation av dokument och annat referensmaterial i ett format som är oberoende av applikationsprogramvara, hårdvara samt operativsystem. PDF-filformatet har full förmåga att innehålla information som text, bilder, hyperlänkar, formulärfält, rich media, digitala signaturer, bilagor, metadata, geospatiala funktioner och 3D-objekt i det som kan bli en del av källdokumentet.

Följande koder visar hur man sparar arbetsbok som pdf-fil med Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Spara arbetsbok i text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV, etc.), sparar både Microsoft Excel och Aspose.Cells endast innehållet i det aktiva kalkylbladet som standard.

Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda källarbetsboken som kan vara valfri Microsoft Excel- eller OpenOffice-kalkylarksfil (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med valfritt antal kalkylblad.

När koden exekveras konverterar den data från alla ark i arbetsboken till TXT-format.

 Du kan ändra samma exempel för att spara din fil i CSV. Som standard,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**är komma, så ange inte en avgränsare om du sparar i CSV-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkylbladsdata utan formatering. Filen är en sorts vanlig textfil som kan ha några anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Spara fil till en ström**

 För att spara filer i en stream, skapa en*MemoryStream* eller*FileStream* objekt och spara filen till det strömobjektet genom att anropa**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objekt**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metod. Ange önskat filformat med hjälp av**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** uppräkning när du ringer till**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Spara filer som HTML- och Mht-filer**
Aspose.Cells kan helt enkelt spara en Excel-fil, JSON, CSV eller andra filer som kan laddas av Aspose.Cells som .html- och .mht-filer.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **Spara som OpenOffice (ODS, SXC, FODS, OTS)**
Vi kan spara filerna som öppet kontorsformat: ODS, SXC, FODS, OTS etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Sparar Excel-fil som JSON eller XML**

JSON (JavaScript Object Notation) är ett öppet standardfilformat för att dela data som använder läsbar text för att lagra och överföra data. JSON-filer lagras med tillägget .json. JSON kräver mindre formatering och är ett bra alternativ för XML. JSON härrör från JavaScript men är ett språkoberoende dataformat. Generering och analys av JSON stöds av många moderna programmeringsspråk. application/json är mediatypen som används för JSON.

Aspose.Cells stöder att spara filer till JSON eller XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Förhandsämnen**
- [Justera arbetsbokens komprimeringsnivå](/cells/sv/net/adjust-workbook-compression-level/)
- [Spara arbetsboken i strikt öppet XML-kalkylbladsformat](/cells/sv/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Sparar fil till svarsobjekt](/cells/sv/net/saving-file-to-response-object/)
