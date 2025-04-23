---
title: Spara Excel filer i CSV, PDF och andra format
linktitle: Spara filer
type: docs
weight: 20
url: /sv/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** låter utvecklare skapa Excel-filer från grunden med hjälp av dess flexibla API. När du skapar Excel-filer behöver du också spara din arbetsbok (fil). Aspose.Cells tillhandahåller olika sätt att spara dessa filer. I det här ämnet kommer vi att diskutera alla de möjliga sätten som utvecklare kan använda för att spara sina filer.

{{% /alert %}}

## **Olika sätt att spara dina filer**

Aspose.Cells API tillhandahåller en klass som heter [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Excel-fil och tillhandahåller alla nödvändiga egenskaper och metoder som utvecklare kan behöva arbeta med sina Excel-filer. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-klassen tillhandahåller en [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-metod som används för att spara Excel-filer. [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-metoden har många överbelastningar som används för att spara Excel-filer på olika sätt.

Utvecklare kan också ange filformatet som deras filer ska sparas i. Filerna kan sparas i flera format som XLS, SpreadsheetML, CSV, tabulatoravgränsad, tabbseparerade värden TSV, XPS och många fler. Dessa filformat specificeras med hjälp av [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-uppräkningen.

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-uppräkningen innehåller många fördefinierade filformat (som kan väljas av dig) enligt följande:

|**Filtyp**|**Beskrivning**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API försöker att upptäcka lämpligt format från filändelsen som anges i det första parametern till spar-metoden|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Representerar en CSV-fil|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Representerar en Office Open XML SpreadsheetML-fil|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Representerar XML-baserad XLSM-fil|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Representerar en Excelformatsfil|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Representerar en Excelfil med aktiverad makro|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Representerar en Excel XLAM-fil|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Representerar en flikbaserad värdefil|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB-DELIMITED)|Representation av en tabbavgränsad textfil|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Representerar en HTML-fil(ar)|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M-HTML)|Representation av en MHTML-fil|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Representerar en OpenDocument Spreadsheet-fil|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL-97-TO-2003)|Representation av en XLS-fil som är standardformatet för Excel 1997 till 2003-uppdateringar|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET-ML)|Representerar en SpreadSheetML-fil|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Representerar en Excel 2007 binär XLSB-fil|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Representerar oigenkändt format, kan inte sparas.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Representerar en PDF-dokument|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Representerar en XML Paper Specification (XPS) fil.
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Representerar en Tagged Image File Format (TIFF) fil|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Representerar en XML-baserad Scaleable Vector Graphics (SVG) fil|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Representerar Data Interchange Format.|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Representerar en nummerfil.|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Representerar en markdown-dokument.|
**Vanligtvis finns det två sätt att spara Excel-filer enligt följande:**

1. **Spara filen till någon plats**
1. **Spara filen till en ström**

## **Spara fil till en plats**

Om utvecklare behöver spara sina filer till någon lagringsplats kan de helt enkelt ange filnamnet (med dess kompletta lagringsväg) och önskat filformat (med hjälp av [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-uppräkningen) när de anropar [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-objektets [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-metod.

**Exempel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad i textformat. För textformat (till exempel TXT, TabDelim, CSV etc.) sparar både Microsoft Excel och Aspose.Cells innehållet i endast det aktiva kalkylbladet som standard.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den data från alla kalkylblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil till CSV. Som standard är [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) ett komma, så ange inte någon separator om du sparar i CSV-format. Observera: Om du använder utvärderingsversionen och även om parametern för metoden [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) är satt till true, kommer programmet fortfarande bara att exportera ett kalkblad.

**Exempel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Spara fil till en ström**

Om utvecklare behöver spara sina filer till en **Ström** bör de skapa ett **FileOutputStream**-objekt och sedan spara filen till det **Ström**-objektet genom att anropa [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-objektets [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-metod. Utvecklare kan också ange önskat filformat (med hjälp av [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-uppräkningen) när de anropar [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-metoden.

**Exempel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Spara fil till annat format**

### **XLS-filer**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX-filer**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF-filer**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Ange alternativet för att kopiera innehållet för tillgänglighet**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-klassen kan du få eller ställa in PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)-alternativet för att kontrollera åtkomsten till innehållet i den konverterade PDF:en. Det innebär att det tillåter skärmläsarprogramvara att använda texten inom PDF-filen för att läsa filen. Du kan inaktivera det genom att tillämpa ett åtkomstbehörighetslösenord och avmarkera de två objekten på skärmbilden [här](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exportera anpassade egenskaper till PDF**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-klassen kan du exportera de anpassade egenskaperna i källarbetboken till PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)-uppräkningen tillhandahålls för att specificera sättet genom vilket egenskaper exporteras. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Fil och sedan egenskaper som visas i följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ner [här](sourceWithCustProps.xlsx) för testning och utdata-PDF-filen "outSourceWithCustProps" finns tillgänglig [här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells API ger stöd för att exportera kalkylblad till Markdown-format. För att exportera det aktiva kalkylbladet till Markdown, skicka [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) som andra parameter av [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.lang.String-int-)-metoden. Du kan också använda [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)-klassen för att specificera ytterligare inställningar för att exportera kalkylblad till Markdown.

Följande kodexempel visar hur du exporterar det aktiva kalkylbladet till Markdown genom att använda [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)-uppräkningens medlem. Se den [utdata-Markdown-filen](Book1.txt) genererad av koden för referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Fortsatta ämnen**
- [Justera arbetsbokens kompressionsnivå](/cells/sv/java/adjust-workbook-compression-level/)
- [Konvertera arbetsbok till olika format](/cells/sv/java/converting-workbook-to-different-formats/)
- [Spara arbetsbok i strikt öppet XML-kalkylbladsformat](/cells/sv/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Spåra konverteringsframsteg för Excel till TIFF](/cells/sv/java/track-conversion-progress-of-excel-to-tiff/)
- [Spåra Dokumentkonverteringsframsteg](/cells/sv/java/track-document-conversion-progress/)
{{< app/cells/assistant language="java" >}}
