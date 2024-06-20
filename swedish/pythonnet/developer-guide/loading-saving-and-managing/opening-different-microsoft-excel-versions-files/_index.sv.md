---
title: Öppning av olika Microsoft Excel versioner filer
type: docs
weight: 20
url: /sv/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kan öppna olika Microsoft Excel-versioner filer, som Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning av Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller Krypterade Excel-filer.

{{% /alert %}}

## **Öppning av filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95, 97, eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365. Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tabellimiterad eller TSV, CSV, ODS och så vidare. Använd konstruktören, eller ange attributet **file_format** i **Workbook**-klassen för att ange formatet med hjälp av **FileFormatType**-uppräkningen.

Uppräkningen **FileFormatType** innehåller många fördefinierade filformat, varav några ges nedan.

|**Filtyp**|**Beskrivning**|
| :- | :- |
|CSV|Representerar en CSV-fil|
|EXCEL_97_TO_2003|Representerar en Excel 97 - 2003-fil|
|XLSX|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|XLSM|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|XLTX|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|XLSB|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB-fil|
|SPREADSHEET_ML|Representerar en SpreadsheetML-fil|
|TSV|Representerar en tab-separated values-fil|
|TAB_DELIMITED|Representerar en tabellavgränsad textfil|
|ODS|Representerar en ODS-fil|
|HTML|Representerar en HTML-fil|
|M_HTML|Representerar en MHTML-fil|

### **Öppna Microsoft Excel 95/5.0 Fil**

För att öppna en Microsoft Excel 95/5.0-fil, använd **LoadOptions** och ställ in det relaterade attributet för klassen **LoadOptions** för den mallfil som ska laddas. En testfil för att testa denna funktion kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Öppna Microsoft Excel 97 - 2003 Fil**

För att öppna en Microsoft Excel 97 - 2003-fil, använd **LoadOptions** och ställ in det relaterade attributet för klassen **LoadOptions** för den mallfil som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365  XLSX Fil**

För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, specificera filvägen. Du kan också använda **LoadOptions** och ställa in relaterade attribut/alternativ för klassen **LoadOptions** för den mallfil som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Öppna krypterade Excelfiler**

Det är möjligt att skapa krypterade Excel-filer med Microsoft Excel. För att öppna en krypterad fil, använd **LoadOptions** och ställ in dess attribut och alternativ (till exempel ange ett lösenord) för den mallfil som ska laddas.
En testfil för att testa den här funktionen kan laddas ner från följande länk:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells stöder också öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 filer.


