---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /sv/net/spreadsheetml-xlsx-xml/
---

## **Om SpreadsheetML**
SpreadsheetML är ett namn på en familj av XML-baserade format för kalkylbladsdokument. Det finns flera versioner av SpreadsheetML:

1. SpreadsheetML-version 2003 introducerades i Microsoft Word 2003. SpreadsheetML var ett betydande steg av Microsoft mot att göra dokumentformatet öppet.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) är det nya XML-baserade formatet som introducerades i Microsoft Office 2007-applikationer. Office Open XML är ett behållarformat för flera specialiserade XML-baserade märkningsspråk. SpreadsheetML-version 2007 är märkningsspråket som används av Microsoft Office Excel 2007 för att lagra sina dokument.
1. Microsoft Excel 2010 lagrar dokument i SpreadsheetML-version 2010 enligt den uppdaterade OOXML-standarden.
## **SpreadsheetML i Aspose.Cells**
Det finns tre ”versioner” av tillgängligt SpreadsheetML:

|**SpreadsheetML 'Version'**|**Tillämplig standard/specifikation**|**Stöds i Aspose.Cells for .NET**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Ja|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Ja|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|Ja|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|Ja|
OOXML SpreadsheetML-dokument kommer oftast som XLSX-filer, vilka är ZIP-paket. Förutom XLSX, tillhandahåller Aspose.Cells omfattande stöd för att ladda, spara och konvertera SpreadsheetML-dokument. En sådan allomfattande implementation är möjlig eftersom Aspose.Cells utformades med strukturen av Microsoft Excel-dokument i åtanke (och SpreadsheetML är känt för att efterlikna den interna representationen av Microsoft Excel-dokument).
### **OOXML är öppen, varför använda Aspose.Cells?**
Det är sant att Office Open XML-tekniken gör det möjligt att bygga dokumentbehandlings- och genereringsapplikationer med bara XML-klasser utan att förlita sig på tredjepartsbibliotek som Aspose.Cells. Dock tror vi starkt att det fortfarande är mycket fördelaktigt att använda Aspose.Cells när du måste hantera OOXML-dokument, snarare än att arbeta genom XML eller andra bibliotek.

Specifikationen för OOXML är flera tusen sidor lång. Att vara öppen och standard innebär inte att vara enkel. För att korrekt bearbeta eller generera OOXML-dokument måste man investera i att lära sig formatet väl.

Förutom att göra det enklare att korrekt behandla och generera giltiga dokument tillhandahåller Aspose.Cells följande viktiga funktioner som du inte skulle ha när du arbetar med OOXML-filer direkt via XML eller andra tredjepartsbibliotek:

- Kvalitativa konverteringar mellan många populära Excel-format, inklusive konvertering till PDF, HTML, TIFF och utskrift.
- Möjlighet att bygga dokument från fragment, från en eller flera dokument, samtidigt som data automatiskt sammanslås med stilistisk formatering, diagram och grafik.
- Avancerade funktioner, såsom att importera data från olika datakällor inklusive Array, ArrayList, DataTable, DataColumn, DataGrid, DataView och DataReader eller exportera data för att fylla en DataTable eller en Array med bara en kodrad.
- Robust formelberäkningsmotor som stöder nästan alla standard- och avancerade Microsoft Excel-funktioner.

Överväg följande exempel. Vissa celler innehåller texten ”Hello World” i fetstil. Tänk dig nu att du behöver skriva ett program som söker efter alla fraser ”Hello World” i kalkylbladet och ersätter dem med ”Goodbye Earth”.
### **Ett fragment av ett Office Open XML-dokument**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}


Att implementera även en enkel sök- och ersättningsoperation i ett Office Open XML-dokument är svårt. Vårt råd: kom ihåg att öppet och standardiserat inte betyder enkelt, och använd Aspose.Cells.
