---
title: Öppning av olika Microsoft Excel versioner filer
type: docs
weight: 20
url: /sv/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kan öppna olika Microsoft Excel-versioner filer, som Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning av Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller Krypterade Excel-filer.

{{% /alert %}}

## **Öppning av filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95, 97 eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365. Du kan behöva ladda en fil i någon av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller TSV, CSV, ODS, och så vidare. Använd konstruktor eller specificera [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) klassens [**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/) metod för att ange formatet med hjälp av [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) enumen.

Enumeration [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) innehåller många fördefinierade filformat, varav några är listade nedan.

|**Filtyp**|**Beskrivning**|
| :- | :- |
|FileFormatType_CSV|Representerar en CSV-fil|
|FileFormatType_Excel97To2003|Representerar en Excel 97 - 2003 fil|
|FileFormatType_Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|FileFormatType_Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|FileFormatType_Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX-fil|
|FileFormatType_Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|FileFormatType_Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB-fil|
|FileFormatType_SpreadsheetML|Representerar en SpreadsheetML-fil|
|FileFormatType_Tsv|Representerar en tabseparatorvärdesfil|
|FileFormatType_TabDelimited|Representerar en flikskild textfil|
|FileFormatType_Ods|Representerar en ODS-fil|
|FileFormatType_Html|Representerar en HTML-fil|
|FileFormatType_MHtml|Representerar en MHTML-fil|

### **Öppna Microsoft Excel 95/5.0 Fil**

För att öppna en Microsoft Excel 95/5.0 fil, använd [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) och ställ in den relaterade attributen för [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/)-klassen för den mallfil som ska laddas. En provfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **Öppna Microsoft Excel 97 - 2003 Fil**

För att öppna en Microsoft Excel 97 - 2003 fil, använd [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) och ställ in den relaterade attributen för [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/)-klassen för den mallfil som ska laddas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365  XLSX Fil**

För att öppna en Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, dvs. XLSX eller XLSB, ange filvägen. Du kan också använda [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) och ställa in den relaterade attributen/alternativen för klassen [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) som ska laddas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cells stöder även att öppna lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019 och Office 365-filer.
