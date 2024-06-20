---
title: Öppning av olika Microsoft Excel versioner filer
type: docs
weight: 20
url: /sv/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kan öppna olika Microsoft Excel-versioner filer, som Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning av Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller Krypterade Excel-filer.

{{% /alert %}}

## **Öppning av filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95,97 eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365. Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tabulator-avgränsat eller TSV, CSV, ODS osv. Använd konstruktorn eller specificera [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)klassens [**setFileFormat**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat)metod för att ange formatet med hjälp av [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)uppräkningen.

[**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)uppräkningen innehåller många fördefinierade filformat varav några ges nedan.

|**Filtyp**|**Beskrivning**|
| :- | :- |
|CSV|Representerar en CSV-fil|
|EXCEL_97_TO_2003|Representerar en Excel 97 - 2003-fil|
|XLSX|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|XLSM|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|XLTX|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365-mall XLTX-fil|
|XLTM|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|XLSB|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB-fil|
|SPREADSHEET_ML|Representerar en SpreadsheetML-fil|
|TSV|Representerar en tab-separated values-fil|
|TAB_DELIMITED|Representerar en tabellavgränsad textfil|
|ODS|Representerar en ODS-fil|
|HTML|Representerar en HTML-fil|
|M_HTML|Representerar en MHTML-fil|

### **Öppna Microsoft Excel 95/5.0 Fil**

För att öppna en Microsoft Excel 95/5.0-fil, använd [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) och ställ in de relaterade attributen för **LoadOptions** klassen för mönsterfilen som ska laddas. En testfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Öppna Microsoft Excel 97 - 2003 Fil**

För att öppna en Microsoft Excel 97 - 2003-fil, använd [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) och ställ in de relaterade attributen för **LoadOptions** klassen för mönsterfilen som ska laddas.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365  XLSX Fil**

För att öppna en Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga, XLSX eller XLSB, ange filvägen. Du kan också använda [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) och ställ in de relaterade attributen/alternativen för **LoadOptions** klassen för mönsterfilen som ska laddas.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Öppna krypterade Excelfiler**

Det är möjligt att skapa krypterade Excel-filer med hjälp av Microsoft Excel. För att öppna en krypterad fil, använd [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) och ställ in dess attribut och alternativ (till exempel, ange ett lösenord) för mönsterfilen som ska laddas.
En testfil för att testa den här funktionen kan laddas ner från följande länk:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells stöder också öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 filer.


