---
title: Öppna olika Microsoft Excel-versionsfiler
type: docs
weight: 20
url: /sv/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells kan öppna en rad olika Microsoft Excel-versionsfiler, till exempel Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2010/2013/20196 Office 2015LS.

{{% /alert %}}

## **Öppna filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95,97, eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 . Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller TSV, CSV, ODS och så vidare. Använd konstruktorn eller ange**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** klass'**[SetFileFormat](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)** metod för att specificera formatet med hjälp av**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**uppräkning.
	
 De**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**uppräkningen innehåller många fördefinierade filformat av vilka några ges nedan.

|**Filformatstyper**|**Beskrivning**|
|:- |:- |
|FileFormatType_CSV|Representerar en CSV-fil|
|FileFormatType_Excel97To2003|Representerar en Excel 97 - 2003-fil|
|FileFormatType_Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|FileFormatType_Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|FileFormatType_Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX-fil|
|FileFormatType_Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|FileFormatType_Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB-fil|
|FileFormatType_SpreadsheetML|Representerar en SpreadsheetML-fil|
|FileFormatType_Tsv|Representerar en tabbseparerad värdefil|
|FileFormatType_TabDelimited|Representerar en tabbavgränsad textfil|
|FileFormatType_Ods|Representerar en ODS-fil|
|FileFormatType_Html|Representerar en HTML-fil|
|FileFormatType_MHtml|Representerar en MHTML-fil|

### **Öppnar Microsoft Excel 95/5.0-filer**

För att öppna en Microsoft Excel 95/5.0-fil, använd**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**och ställ in det relaterade attributet för**ILoadOptions**klass för mallfilen som ska laddas. En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Öppnar Microsoft Excel 97 - 2003-filer**

 För att öppna en Microsoft Excel 97 - 2003-fil, använd**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** och ställ in det relaterade attributet för**ILoadOptions**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-filer**

 För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, ange filsökvägen. Du kan också använda**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** och ställ in relaterade attribut/alternativ för**ILoadOptions**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells stöder även öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-filer.


