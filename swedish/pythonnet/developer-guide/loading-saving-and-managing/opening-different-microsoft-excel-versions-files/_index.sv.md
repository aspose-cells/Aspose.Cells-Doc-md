---
title: Öppna olika Microsoft Excel-versionsfiler
type: docs
weight: 20
url: /sv/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells kan öppna en rad olika Microsoft Excel-versionsfiler, såsom Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller krypterade Excel-filer.

{{% /alert %}}

## **Öppna filer av olika Microsoft Excel-versioner**

 En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95,97, eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 . Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller TSV, CSV, ODS och så vidare. Använd konstruktorn eller ange**Arbetsbok** klass'**filformat** typattribut som anger formatet med hjälp av**FileFormatType**uppräkning.

 De**FileFormatType**uppräkningen innehåller många fördefinierade filformat av vilka några ges nedan.

|**Filformatstyper**|**Beskrivning**|
|:- |:- |
|CSV|Representerar en CSV-fil|
|EXCEL_97_TO_2003|Representerar en Excel 97 - 2003-fil|
|XLSX|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|XLSM|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX-fil|
|XLTX|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|XLSB|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB-fil|
|Kalkylblad_ML|Representerar en SpreadsheetML-fil|
|TSV|Representerar en tabbseparerad värdefil|
|TAB_DELIMITED|Representerar en tabbavgränsad textfil|
|ODS|Representerar en ODS-fil|
|HTML|Representerar en HTML-fil|
|M_HTML|Representerar en MHTML-fil|

### **Öppna Microsoft Excel 95/5.0-filer**

För att öppna en Microsoft Excel 95/5.0-fil, använd**LoadOptions**och ställ in det relaterade attributet för**LoadOptions**klass för mallfilen som ska laddas. En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Öppna Microsoft Excel 97 - 2003-filer**

 För att öppna en Microsoft Excel 97 - 2003-fil, använd**LoadOptions** och ställ in det relaterade attributet för**LoadOptions**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-filer**

 För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, anger du filsökvägen. Du kan också använda**LoadOptions** och ställ in relaterade attribut/alternativ för**LoadOptions**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Öppna krypterade Excel-filer**

 Det är möjligt att skapa krypterade Excel-filer med Microsoft Excel. För att öppna en krypterad fil, använd**LoadOptions**och ställ in dess attribut och alternativ (till exempel ange ett lösenord) för mallfilen som ska laddas.
En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[Krypterad Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells stöder också öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-filer.


