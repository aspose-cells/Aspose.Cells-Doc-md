---
title: Öppna olika Microsoft Excel versioners filer
type: docs
weight: 20
url: /sv/net/opening-different-microsoft-excel-versions-files/
description: Den här artikeln förklarar hur man öppnar olika excelversioners filer med hjälp av Aspose.Cells for .NET API.
keywords: C# Öppna olika Microsoft Excel filer, Hur öppnar jag krypterade Excel filer.
---

{{% alert color="primary" %}}

Aspose.Cells kan öppna olika Microsoft Excel-versioner filer, som Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning av Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller Krypterade Excel-filer.

{{% /alert %}}

## **Hur man öppnar filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95,97, eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365. Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller TSV, CSV, ODS och så vidare. Använd konstruktören, eller ange [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class' [**FileFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat) typ attribut som anger formatet med hjälp av [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) uppräkningen.

[**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)uppräkningen innehåller många fördefinierade filformat varav några ges nedan.

|**Filtyp**|**Beskrivning**|
| :- | :- |
|Csv|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX fil|
|Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM fil|
|Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB fil|
|SpreadsheetML|Representerar en SpreadsheetML fil|
|Tsv|Representerar en tabb-separerad värden fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|Ods|Representerar en ODS fil|
|Html|Representerar en HTML fil|
|Mhtml|Representerar en MHTML fil|

### **Öppna Microsoft Excel 95/5.0 filer**

För att öppna en Microsoft Excel 95/5.0 fil, använd [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) och ställ in den relaterade attributen för [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)-klassen för den mallfil som ska laddas. En provfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Öppna Microsoft Excel 97-2003 filer**

För att öppna en Microsoft Excel 97 - 2003 fil, använd [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) och ställ in den relaterade attributen för [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)-klassen för den mallfil som ska laddas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-filer**

För att öppna en Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, dvs. XLSX eller XLSB, ange filvägen. Du kan också använda [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) och ställa in den relaterade attributen/alternativen för klassen [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) som ska laddas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Öppna krypterade Excel-filer**

Det är möjligt att skapa krypterade Excel-filer med hjälp av Microsoft Excel. För att öppna en krypterad fil, använd [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) och ställ in dess attribut och alternativ (till exempel, ange ett lösenord) för mönsterfilen som ska laddas.
En testfil för att testa den här funktionen kan laddas ner från följande länk:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells stöder också öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 filer.


