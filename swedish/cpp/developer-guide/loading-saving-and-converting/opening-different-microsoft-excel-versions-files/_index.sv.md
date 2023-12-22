---
title: Öppna olika Microsoft Excel-versionsfiler
type: docs
weight: 20
url: /sv/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells kan öppna en rad olika Microsoft Excel-versionsfiler, t.ex. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning Microsoft Excel 2007/2010/2010/2013/56130/561320 och 9613/2010/2010/561320 och 9613/2010/561320 eller 96133481 Krypterade Excel-filer.

{{% /alert %}}

##  **Öppna filer av olika Microsoft Excel-versioner**

 En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95,97, eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 . Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller 0761934611, 0418, 0418, 0418, 0418 och Använd konstruktorn eller ange**[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**klass'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** metod för att specificera formatet med hjälp av**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**uppräkning.
	
 De**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**uppräkningen innehåller många fördefinierade filformat av vilka några ges nedan.

|**Filformatstyper**|**Beskrivning**|
| :- | :- |
|FileFormatType_CSV|Representerar en CSV-fil|
|FileFormatType_Excel97To2003|Representerar en Excel 97 - 2003-fil|
|FileFormatType_Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|FileFormatType_Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|FileFormatType_Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|FileFormatType_Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|FileFormatType_Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB fil|
|FileFormatType_SpreadsheetML|Representerar en SpreadsheetML-fil|
|FileFormatType_Tsv|Representerar en tabbseparerad värdefil|
|FileFormatType_TabDelimited|Representerar en tabbavgränsad textfil|
|FileFormatType_Ods|Representerar en ODS-fil|
|FileFormatType_Html|Representerar en HTML-fil|
|FileFormatType_MHtml|Representerar en MHTML-fil|

###  **Öppnar Microsoft Excel 95/5.0-filer**

För att öppna en Microsoft Excel 95/5.0-fil, använd**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**och ställ in det relaterade attributet för**LoadOptions**klass för mallfilen som ska laddas. En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Öppnar Microsoft Excel 97 - 2003-filer**

 För att öppna en Microsoft Excel 97 - 2003-fil, använd**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** och ställ in det relaterade attributet för**LoadOptions**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX filer**

För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, anger du filsökvägen. Du kan också använda**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** och ställ in relaterade attribut/alternativ för**LoadOptions**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells stöder även öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-filer.


