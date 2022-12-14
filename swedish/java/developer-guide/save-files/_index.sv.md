---
title: Spara Excel-filer till CSV, PDF och andra format
linktitle: Spara filer
type: docs
weight: 20
url: /sv/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**tillåter utvecklare att skapa Excel-filer från grunden med hjälp av dess flexibla API. När du väl har skapat Excel-filer måste du också spara din arbetsbok (fil). Aspose.Cells tillhandahåller en mängd olika sätt att spara dessa filer. I det här ämnet kommer vi att diskutera alla möjliga sätt som utvecklare kan använda för att spara sina filer.

{{% /alert %}}

## **Olika sätt att spara dina filer**

 Aspose.Cells API tillhandahåller en klass med namnet[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)som representerar en Excel-fil och tillhandahåller alla nödvändiga egenskaper och metoder som utvecklare kan behöva för att arbeta med sina Excel-filer. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klass ger en[**spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) metod som används för att spara Excel-filer. De[**spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) metod har många överbelastningar som används för att spara Excel-filer på olika sätt.

 Utvecklare kan också ange i vilket filformat deras filer ska sparas. Filerna kan sparas i flera format som XLS, SpreadsheetML, CSV, Tab Delimited, Tab-separated values TSV, XPS och många fler. Dessa filformat specificeras med hjälp av[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) uppräkning.

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)uppräkningen innehåller många fördefinierade filformat (som kan väljas av dig) enligt följande:

|**Filformatstyper**|**Beskrivning**|
|:- |:- |
|[**BIL**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API försöker hitta rätt format från filtillägget som anges i den första parametern till sparmetoden|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Representerar en CSV-fil|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Representerar en Office Open XML SpreadsheetML-fil|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Representerar XML-baserad XLSM-fil|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Representerar en Excel-mallfil|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Representerar en Excel-makroaktiverad mallfil|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Representerar en Excel XLAM-fil|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Representerar en tabbseparerad värdefil|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Representerar en tabbavgränsad textfil|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Representerar en HTML-fil(er)|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Representerar en MHTML-fil(er)|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Representerar en OpenDocument Spreadsheet-fil|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Representerar en XLS-fil som är standardformatet för Excel 1997 till 2003-revisioner|
|[**Kalkylblad_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Representerar en SpreadSheetML-fil|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Representerar en Excel 2007 binär XLSB-fil|
|[**OKÄND**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Representerar okänt format, kan inte sparas.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Representerar ett PDF-dokument|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Representerar en XML Paper Specification-fil (XPS).|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Representerar en TIFF-fil (Tagged Image File Format).|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Representerar en XML-baserad SVG-fil (Scalable Vector Graphics).|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Representerar Data Interchange Format.|
|[**TAL**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Representerar en nummerfil.|
|[**PRISSÄNKNING**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Representerar ett nedskrivningsdokument.|
**Normalt finns det två sätt att spara Excel-filer på följande sätt:**

1. **Sparar filen på någon plats**
1. **Sparar filen i en stream**

## **Sparar fil på någon plats**

 Om utvecklare behöver spara sina filer på någon lagringsplats kan de helt enkelt ange filnamnet (med dess fullständiga lagringssökväg) och önskat filformat (med hjälp av[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) uppräkning) medan du anropar[**spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) metod av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objekt.

**Exempel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Spara arbetsbok i text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV etc.) sparar både Microsoft Excel och Aspose.Cells endast innehållet i det aktiva kalkylbladet som standard.

Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda källarbetsboken som kan vara valfri Microsoft Excel- eller OpenOffice-kalkylarksfil (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med valfritt antal kalkylblad.

När koden exekveras konverterar den data från alla ark i arbetsboken till TXT-format.

 Du kan ändra samma exempel för att spara din fil i CSV. Som standard,[**TextSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) är ett kommatecken, så ange inte en avgränsare om du sparar i CSV-format.

**Exempel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkylbladsdata utan formatering. Filen är en sorts vanlig textfil som kan ha några anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Spara fil till en ström**

 Om utvecklare behöver spara sina filer till en**Ström** då borde de skapa en**FileOutputStream** objekt och spara sedan filen till det**Ström** objekt genom att anropa[**spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) metod av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objekt. Utvecklare kan också ange önskat filformat (med hjälp av[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) uppräkning) medan du anropar[**spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) metod.

**Exempel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Sparar fil till annat format**

### **XLS-filer**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX-filer**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF-filer**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Ställ in alternativet ContentCopyForAccessibility**

 Med[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) klass, kan du hämta eller ställa in PDF:en[**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) alternativet för att kontrollera innehållsåtkomsten i den konverterade PDF-filen. Det betyder att det tillåter skärmläsarprogramvara att använda texten i PDF-filen för att läsa PDF-filen. Du kan inaktivera det genom att använda ett lösenord för ändring av behörigheter och avmarkera de två objekten på skärmdumpen[här](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exportera anpassade egenskaper till PDF**

Med[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) klass, kan du exportera de anpassade egenskaperna i källarbetsboken till PDF:en.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)Enumerator tillhandahålls för att specificera hur egenskaper exporteras. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Arkiv och sedan egenskaper alternativ som visas i följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ner[här](sourceWithCustProps.xlsx)för testning och utdata PDF-filen "outSourceWithCustProps" är tillgänglig[här](outSourceWithCustProps.pdf)för analys.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells API ger stöd för export av kalkylblad till Markdown-format. För att exportera det aktiva kalkylbladet till Markdown, godkänn[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)som den andra parametern för[**Arbetsbok.Spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) metod. Du kan också använda[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)klass för att ange ytterligare inställningar för export av kalkylblad till Markdown.

Följande kodexempel visar export av aktivt kalkylblad till Markdown med hjälp av[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)uppräkningsmedlem. Vänligen se[output Markdown-fil](Book1.txt)genereras av koden för referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Förhandsämnen**
- [Justera arbetsbokens komprimeringsnivå](/cells/sv/java/adjust-workbook-compression-level/)
- [Konvertera arbetsbok till olika format](/cells/sv/java/converting-workbook-to-different-formats/)
- [Spara arbetsboken i strikt öppet XML-kalkylbladsformat](/cells/sv/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Spåra konverteringsförlopp för Excel till TIFF](/cells/sv/java/track-conversion-progress-of-excel-to-tiff/)
- [Spåra dokumentkonverteringsförlopp](/cells/sv/java/track-document-conversion-progress/)
