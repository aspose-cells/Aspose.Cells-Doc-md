---
title: Öppna olika Microsoft Excel-versionsfiler
type: docs
weight: 20
url: /sv/net/opening-different-microsoft-excel-versions-files/
description: Den här artikeln förklarar hur du öppnar olika Excel-versionsfiler med Aspose.Cells for .NET API.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells kan öppna en rad olika Microsoft Excel-versionsfiler, t.ex. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning Microsoft Excel 2007/2010/2010/2013/56130/561320 och 9613/2010/2010/561320 och 9613/2010/561320 eller 96133481 Krypterade Excel-filer.

{{% /alert %}}

##  **Hur man öppnar filer med olika Microsoft Excel-versioner**

 En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95,97, eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 . Du kan behöva ladda en fil i något av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller 0761934611, 0418, 0418, 0418, 0418 och Använd konstruktorn eller ange**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)**klass'**[Filformat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** typattribut som anger formatet med hjälp av**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**uppräkning.

 De**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**uppräkningen innehåller många fördefinierade filformat av vilka några ges nedan.

|**Filformatstyper**|**Beskrivning**|
| :- | :- |
|Csv|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003-fil|
|Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB fil|
|SpreadsheetML|Representerar en SpreadsheetML-fil|
|Tsv|Representerar en tabbseparerad värdefil|
|TabDelimited|Representerar en tabbavgränsad textfil|
|Odds|Representerar en ODS-fil|
|Html|Representerar en HTML-fil|
|Mhtml|Representerar en MHTML-fil|

###  **Öppna Microsoft Excel 95/5.0-filer**

För att öppna en Microsoft Excel 95/5.0-fil, använd**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**och ställ in det relaterade attributet för**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**klass för mallfilen som ska laddas. En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Öppna Microsoft Excel 97 - 2003-filer**

 För att öppna en Microsoft Excel 97 - 2003-fil, använd**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** och ställ in det relaterade attributet för**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-filer**

För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, anger du filsökvägen. Du kan också använda**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** och ställ in relaterade attribut/alternativ för**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**klass för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Öppna krypterade Excel-filer**

 Det är möjligt att skapa krypterade Excel-filer med Microsoft Excel. För att öppna en krypterad fil, använd**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**och ställ in dess attribut och alternativ (till exempel ange ett lösenord) för mallfilen som ska laddas.
En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[Krypterad Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells stöder även öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-filer.


