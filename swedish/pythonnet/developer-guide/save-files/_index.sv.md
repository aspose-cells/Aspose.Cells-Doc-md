---
title: Olika sätt att spara filer
linktitle: Spara filer
type: docs
weight: 40
url: /sv/python-net/different-ways-to-save-files/
description: Aspose.Cells för Python via .NET kan spara filer i olika format. Spara filer till PDF. Spara filer till HTML. Spara filer till DOCX. Spara filer till PPTX. Spara filer till JSON. Spara filer till MHTML.
keywords: Aspose.Cells för Python via .NET sparar Excel till PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML och andra format med C#, Spara eller konvertera arbetsbok till PDF, HTML, JSON, TXT SQL i C#.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET gör det möjligt att skapa och spara filer. Den här artikeln förklarar de olika sätten filer kan sparas på.

{{% /alert %}}

## **Olika sätt att spara filer**

Aspose.Cells för Python via .NET tillhandahåller [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil och ger egenskaper och metoder som är nödvändiga för att arbeta med Excel-filer. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) ger [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)-metoden som används för att spara Excel-filer. Metoden [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) har många överbelastningar som används för att spara filer på olika sätt.

Filen format som filen sparas till bestäms av [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) uppräkningen

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

För att spara filer till en lagringsplats, ange filnamnet (komplett med lagringsväg) och önskat filformat (från [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) uppräkningen) vid anrop av [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) objektets [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)metod.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **Så här sparar du arbetsbok till Pdf**
Portable Document Format (PDF) är en typ av dokument som skapades av Adobe på 1990-talet. Syftet med detta filformat var att införa en standard för representation av dokument och annat referensmaterial i ett format som är oberoende av applikationsprogramvara, hårdvara samt operativsystem. PDF-filformatet har full kapacitet att innehålla information som text, bilder, hyperlänkar, formulärfält, rika medier, digitala signaturer, bilagor, metadata, geospatiala funktioner och 3D-objekt som kan bli en del av käll-dokumentet.

Följande kod visar hur man sparar arbetsboken som PDF-fil med Aspose.Cells för Python via .NET:
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **Så här sparar du arbetsboken till Text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV, osv.) sparar både Microsoft Excel och Aspose.Cells for Python via .NET som standard endast innehållet i det aktiva kalkylbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil till CSV. Som standard är [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator) komma, så specificera inte en separator om du sparar i CSV-format. Observera: Om du använder utvärderingsversionen och till och med egenskapen [**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/) är inställd på true, kommer programmet fortfarande bara att exportera ett kalkylblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Så här sparar du filen till textfiler med anpassad avskiljare**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **Så här sparar du Excel-filen till HTML- och MHT-filer**
Aspose.Cells för Python via .NET kan enkelt spara en Excel-fil, JSON, CSV eller andra filer som kan laddas av Aspose.Cells för Python via .NET som .html- och .mht-filer.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **Så här sparar du Excel-filen till OpenOffice (ODS, SXC, FODS, OTS)**
Vi kan spara filerna i öppet offce-format: ODS, SXC, FODS, OTS osv.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **Så här sparar du Excel-filen till JSON eller XML**

JSON (JavaScript Object Notation) är ett öppet standardfilformat för att dela data som använder mänskligt läsbar text för att lagra och överföra data. JSON-filer lagras med filändelsen .json. JSON kräver mindre formatering och är ett bra alternativ till XML. JSON härstammar från JavaScript men är ett språkoberoende dataformat. Generering och tolkning av JSON stöds av många moderna programmeringsspråk. application/json är mediatypen som används för JSON.

Aspose.Cells för Python via .NET stöder att spara filer till JSON eller XML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **Fortsatta ämnen**
- [Justera arbetsbokens kompressionsnivå](/cells/sv/python-net/adjust-workbook-compression-level/)
- [Spara arbetsbok i strikt öppet XML-kalkylbladsformat](/cells/sv/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

