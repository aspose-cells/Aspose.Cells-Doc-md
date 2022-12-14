---
title: SpreadsheetML – XLSX, XML
type: docs
weight: 10
url: /de/java/spreadsheetml-xlsx-xml/
---
## **Über SpreadsheetML**
SpreadsheetML ist ein Name für eine Familie von XML-basierten Formaten für Tabellenkalkulationsdokumente. Es gibt mehrere Versionen von SpreadsheetML:

1. SpreadsheetML Version 2003 wurde in Microsoft Word 2003 eingeführt. SpreadsheetML war ein bedeutender Schritt von Microsoft, um das Dokumentformat offen zu machen.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) ist das neue XML-basierte Format, das in Microsoft Office 2007-Anwendungen eingeführt wurde. Office Open XML ist ein Containerformat für mehrere spezialisierte XML-basierte Auszeichnungssprachen. SpreadsheetML Version 2007 ist die Auszeichnungssprache, die von Microsoft Office Excel 2007 zum Speichern seiner Dokumente verwendet wird.
1. Microsoft Excel 2010 und höhere Versionen speichern Dokumente in der SpreadsheetML-Version 2010, wie im aktualisierten OOXML-Standard definiert.
## **SpreadsheetML in Aspose.Cells**
Es sind drei "Versionen" von SpreadsheetML verfügbar:

|**SpreadsheetML „Version“**|**Anwendbare Norm/Spezifikation**|**Unterstützt in Aspose.Cells for Java**|
|:- |:- |:- |
|MicrosoftExcel 2003|[Microsoft Excel 2003-XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Ja|
|MicrosoftExcel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Ja|
|Microsoft Excel 2010 und höhere Versionen|OOXML ISO/IEC DIS 29500|Ja|
OOXML SpreadsheetML-Dokumente liegen meistens als XLSX-Dateien vor, bei denen es sich um ZIP-Pakete handelt. Neben XLSX. Aspose.Cells bietet umfassende Unterstützung für das Laden, Speichern und Konvertieren von SpreadsheetML-Dokumenten. Eine solche allumfassende Implementierung ist möglich, weil Aspose.Cells mit Blick auf die Struktur von Microsoft-Excel-Dokumenten entworfen wurde (und SpreadsheetML ist dafür bekannt, die interne Darstellung von Microsoft-Excel-Dokumenten nachzuahmen).

**Ein XLSX-Dokument, das von Aspose.Cells erstellt und in Microsoft Excel geöffnet wurde** 

![todo: Bild_alt_Text](spreadsheetml-xlsx-xml_1.png)

**Das von Aspose.Cells generierte XLSX-Dokument folgt der Open Packaging Convention und kann in einer ZIP-fähigen Anwendung geöffnet werden** 

![todo: Bild_alt_Text](spreadsheetml-xlsx-xml_2.png)
## **OOXML ist offen, warum Aspose.Cells verwenden?**
Es stimmt, dass die Office Open XML-Technologie das Erstellen von Dokumentenverarbeitung und Generieren von Anwendungen nur mithilfe der XML-Klassen ermöglicht, ohne auf Bibliotheken von Drittanbietern wie Aspose.Cells angewiesen zu sein. Wir sind jedoch der festen Überzeugung, dass es immer noch sehr vorteilhaft ist, Aspose.Cells zu verwenden, wenn Sie dies getan haben um mit OOXML-Dokumenten umzugehen, anstatt mit XML oder anderen Bibliotheken zu arbeiten.

Die OOXML-Spezifikation ist mehrere tausend Seiten lang. Offen und standardisiert zu sein bedeutet nicht, einfach zu sein. Um OOXML-Dokumente korrekt zu verarbeiten oder zu generieren, muss man in das Erlernen des Formats investieren.

Neben der Vereinfachung der korrekten Verarbeitung und Generierung gültiger Dokumente bietet Aspose.Cells die folgenden wichtigen Funktionen, die Sie bei der Arbeit mit OOXML-Dateien direkt über XML oder andere Bibliotheken von Drittanbietern nicht hätten:

- Hochwertige Konvertierungen zwischen vielen gängigen Excel-Formaten, einschließlich Konvertierung in PDF, HTML, TIFF und Drucken.
- Fähigkeit, Dokumente aus Fragmenten, aus einem oder mehreren Dokumenten zu erstellen, während Daten durch stilistische Formatierung, Diagramme und Grafiken automatisch zusammengeführt werden.
- High-Level-Funktionen wie das Importieren von Daten aus verschiedenen Datenquellen, einschließlich Array, ArrayList, DataTable, DataColumn, DataGrid, DataView und DataReader, oder das Exportieren von Daten, um eine DataTable oder ein Array mit nur einer Codezeile zu füllen.
- Robustes Formelberechnungsmodul, das fast alle standardmäßigen und erweiterten Microsoft-Excel-Funktionen unterstützt.

Betrachten Sie das folgende Beispiel. Einige Zellen enthalten den Text „Hello World“ in Fettschrift. Stellen Sie sich nun vor, Sie müssten ein Programm schreiben, das nach allen „Hello World“-Phrasen im Arbeitsblatt sucht und sie durch „Goodbye Earth“ ersetzt.
## **Ein Fragment eines Office Open XML-Dokuments**
**XML**

{{< highlight "csharp" >}}

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

Selbst die Implementierung eines einfachen Such- und Ersetzungsvorgangs in einem Office Open XML-Dokument ist schwierig.

**Unser Rat:** Denken Sie daran, dass offen und Standard nicht einfach bedeutet, und verwenden Sie Aspose.Cells.
