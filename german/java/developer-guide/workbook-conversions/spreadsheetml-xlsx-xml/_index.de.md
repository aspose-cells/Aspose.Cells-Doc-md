---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /de/java/spreadsheetml-xlsx-xml/
---

## **Über SpreadsheetML**
SpreadsheetML ist ein Name für eine Familie von XML-basierten Formaten für Tabellendokumente. Es gibt mehrere Versionen von SpreadsheetML:

1. Die Version 2003 von SpreadsheetML wurde in Microsoft Word 2003 eingeführt. SpreadsheetML war ein bedeutender Schritt von Microsoft, um das Dokumentenformat offen zu gestalten.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) ist das neue XML-basierte Format, das in den Anwendungen von Microsoft Office 2007 eingeführt wurde. Office Open XML ist ein Containerformat für mehrere spezialisierte XML-basierte Auszeichnungssprachen. Die Version 2007 von SpreadsheetML ist die Auszeichnungssprache, die von Microsoft Office Excel 2007 verwendet wird, um seine Dokumente zu speichern.
1. Microsoft Excel 2010 und spätere Versionen speichern Dokumente in der SpreadsheetML-Version 2010, wie sie im aktualisierten OOXML-Standard definiert ist.
## **SpreadsheetML in Aspose.Cells**
Es gibt drei "Versionen" von SpreadsheetML verfügbar:

|**SpreadsheetML “Version”**|**Anwendbarer Standard/Anforderung**|**Unterstützt in Aspose.Cells for Java**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Ja|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Ja|
|Microsoft Excel 2010 und spätere Versionen|OOXML ISO/IEC DIS 29500|Ja|
OOXML SpreadsheetML-Dokumente kommen meistens als XLSX-Dateien, die ZIP-Pakete sind. Neben XLSX bietet Aspose.Cells umfangreiche Unterstützung für das Laden, Speichern und Konvertieren von SpreadsheetML-Dokumenten. Eine solch umfassende Implementierung ist möglich, weil Aspose.Cells mit der Struktur von Microsoft Excel-Dokumenten im Hinterkopf konzipiert wurde (und bekanntermaßen SpreadsheetML die interne Darstellung von Microsoft Excel-Dokumenten nachahmt).

**Ein von Aspose.Cells generiertes XLSX-Dokument, das in Microsoft Excel geöffnet wird** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_1.png)

**Das von Aspose.Cells generierte XLSX-Dokument folgt der Open Packaging Convention und kann in einer ZIP-fähigen Anwendung geöffnet werden** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_2.png)
## **OOXML ist offen, warum also Aspose.Cells verwenden?**
Es ist wahr, dass die Office Open XML-Technologie es ermöglicht, Dokumentenverarbeitungs- und -generierungsanwendungen nur mit den XML-Klassen zu erstellen, ohne auf Drittanbieter-Bibliotheken wie Aspose.Cells angewiesen zu sein. Wir glauben jedoch nachdrücklich, dass es immer noch sehr vorteilhaft ist, Aspose.Cells zu verwenden, wenn Sie mit OOXML-Dokumenten umgehen müssen, anstatt über XML oder andere Bibliotheken zu arbeiten.

Die OOXML-Spezifikation umfasst mehrere tausend Seiten. Offen und standardisiert zu sein bedeutet nicht, dass es einfach ist. Um OOXML-Dokumente richtig zu verarbeiten oder zu generieren, muss man viel Zeit investieren, um das Format gut zu verstehen.

Neben der Vereinfachung der korrekten Verarbeitung und Generierung von gültigen Dokumenten bietet Aspose.Cells die folgenden wichtigen Funktionen, die Sie nicht haben würden, wenn Sie direkt mit OOXML-Dateien über XML oder andere Drittanbieter-Bibliotheken arbeiten:

- Qualitativ hochwertige Konvertierungen zwischen vielen gängigen Excel-Formaten, einschließlich der Konvertierung in PDF, HTML, TIFF und Drucken.
- Möglichkeit, Dokumente aus Fragmenten, aus einem oder mehreren Dokumenten, zu erstellen, während Daten automatisch durch stilistische Formatierung, Diagramme und Grafiken zusammengeführt werden.
- Hochrangige Funktionen, wie das Importieren von Daten aus verschiedenen Datenquellen einschließlich Array, ArrayList, DataTable, DataColumn, DataGrid, DataView und DataReader oder das Exportieren von Daten zur Befüllung einer DataTable oder eines Arrays mit nur einer Codezeile.
- Robuste Formel-Berechnungs-Engine, die fast alle Standard- und erweiterten Microsoft Excel Funktionen unterstützt.

Betrachten Sie das folgende Beispiel. Einige Zellen enthalten den Text "Hallo Welt" fettgedruckt. Stellen Sie sich nun vor, Sie müssen ein Programm schreiben, das alle "Hallo Welt"-Phrasen im Arbeitsblatt sucht und durch "Auf Wiedersehen Erde" ersetzt.
## **Ein Fragment eines Office Open XML-Dokuments**
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

Die Implementierung einer einfachen Suche und Ersetzung in einem Office Open XML-Dokument ist schwierig.

**Unser Rat:** Denken Sie daran, dass offen und standardisiert nicht gleich einfach bedeutet, und verwenden Sie Aspose.Cells.
{{< app/cells/assistant language="java" >}}
