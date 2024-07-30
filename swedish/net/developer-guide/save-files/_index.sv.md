---
title: Olika sätt att spara filer
linktitle: Spara filer
type: docs
weight: 40
url: /sv/net/different-ways-to-save-files/
description: Aspose.Cells for .NET kan spara filer i olika format. Spara filer till PDF. Spara filer till HTML. Spara filer till DOCX. Spara filer till PPTX. Spara filer till JSON. Spara filer till MHTML.
keywords: Aspose.Cells Spara Excel till PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML och så vidare med C#, Spara eller konvertera arbetsboken till PDF HTML JSON TXT SQL i C#.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att skapa och spara filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}}

## **Olika sätt att spara filer**

Aspose.Cells tillhandahåller [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil och tillhandahåller de egenskaper och metoder som krävs för att arbeta med Excel-filer. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) tillhandahåller metoden [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) som används för att spara Excel-filer. Metoden [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) har många överbelastningar som används för att spara filer på olika sätt.

Filen format som filen sparas till bestäms av [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) uppräkningen

|**Filtyp**|**Beskrivning**|
| :- | :- |
|CSV|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007 XLSX-fil|
|Xlsm|Representerar en Excel 2007 XLSM-fil|
|Xltx|Representerar en Excel 2007-mall XLTX-fil|
|Xltm|Representerar en Excel 2007 med makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007 binär XLSB-fil|
|SpreadsheetML|Representerar en kalkyl XML-fil|
|TSV|Representerar en tab-separated values-fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|ODS|Representerar en ODS-fil|
|Html|Representerar HTML-fil(er)|
|MHtml|Representerar MHTML-fil(er)|
|Pdf|Representerar en PDF-fil|
|XPS|Representerar ett XPS-dokument|
|TIFF|Representerar Tagged Image File Format (TIFF)|

## **Så här sparar du filen i olika format**

För att spara filer till en lagringsplats, ange filnamnet (komplett med lagringsväg) och önskat filformat (från [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) uppräkningen) vid anrop av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objektets [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Så här sparar du arbetsbok till Pdf**
Portable Document Format (PDF) är en typ av dokument som skapades av Adobe på 1990-talet. Syftet med detta filformat var att införa en standard för representation av dokument och annat referensmaterial i ett format som är oberoende av applikationsprogramvara, hårdvara samt operativsystem. PDF-filformatet har full kapacitet att innehålla information som text, bilder, hyperlänkar, formulärfält, rika medier, digitala signaturer, bilagor, metadata, geospatiala funktioner och 3D-objekt som kan bli en del av käll-dokumentet.

Följande koder visar hur man sparar arbetsbok som Pdf-fil med Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Så här sparar du arbetsboken till Text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil till CSV. Som standard är [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) kommatecken, så ange inte en avskiljare om du sparar till CSV-format. Observera: Om du använder utvärderingsversionen och även om egenskapen [**TxtSaveOptions.ExportAllSheets**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/exportallsheets/) är inställd på true kommer programmet ändå bara exportera ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Så här sparar du filen till textfiler med anpassad avskiljare**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Så här sparar du filen till en ström**

För att spara filer till en ström, skapa en *MemoryStream* eller *FileStream* objekt och spara filen till det strömobjektet genom att anropa [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objektets [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)metod. Ange önskat filformat med hjälp av [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) uppräkningen vid anrop av [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)metoden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Så här sparar du Excel-filen till HTML- och MHT-filer**
Aspose.Cells kan enkelt spara en Excel-fil, JSON, CSV eller andra filer som kan laddas av Aspose.Cells som .html och .mht-filer.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **Så här sparar du Excel-filen till OpenOffice (ODS, SXC, FODS, OTS)**
Vi kan spara filerna i öppet offce-format: ODS, SXC, FODS, OTS osv.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Så här sparar du Excel-filen till JSON eller XML**

JSON (JavaScript Object Notation) är ett öppet standardfilformat för att dela data som använder mänskligt läsbar text för att lagra och överföra data. JSON-filer lagras med filändelsen .json. JSON kräver mindre formatering och är ett bra alternativ till XML. JSON härstammar från JavaScript men är ett språkoberoende dataformat. Generering och tolkning av JSON stöds av många moderna programmeringsspråk. application/json är mediatypen som används för JSON.

Aspose.Cells stöder att spara filer i JSON eller XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Fortsatta ämnen**
- [Justera arbetsbokens kompressionsnivå](/cells/sv/net/adjust-workbook-compression-level/)
- [Spara arbetsbok i strikt öppet XML-kalkylbladsformat](/cells/sv/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Spara fil till responsobjekt](/cells/sv/net/saving-file-to-response-object/)
