---
title: Wandlung
type: docs
weight: 30
url: /de/net/conversion/
---
Aspose.Cells einzigartige Funktion, die Flexibilität bei Versionskonvertierungen bietet, ohne die Arbeit zu beeinträchtigen.
SaveFormat ist eine Aufzählung, die Dokumente in die unten in der Tabelle angegebenen Erweiterungen konvertieren kann.

|**Mitgliedsname** |**Wert** |**Beschreibung** |
|:- |:- |:- |
| CSV|1 | Stellt eine CSV-Datei dar.|
| XLSX|6 | Stellt eine xlsx-Datei dar.|
| XLSM|7 | Stellt eine xlsm-Datei dar, die Makros aktiviert.|
| Xltx|8 | Stellt eine xltx-Datei dar.|
| Xltm|9 | Stellt eine xltm-Datei dar, die Makros aktiviert.|
| Tabulatorgetrennt|11 | Stellt eine tabulatorgetrennte Textdatei dar.|
| HTML|12 | Stellt eine HTML-Datei dar.|
| HTML|17 | Stellt eine mhtml-Datei dar.|
| ODS|14 | Stellt eine ods-Datei dar.|
| Excel97To2003|5 | Stellt eine Excel97-2003-xls-Datei dar.|
| SpreadsheetML|15 | Stellt eine Excel 2003-XML-Datei dar.|
| XLSB|16 | Stellt eine xlsb-Datei dar.|
| Auto|0 |Wenn die Datei auf der Festplatte gespeichert wird, entspricht das Dateiformat der Erweiterung des Dateinamens.<br> Beim Speichern der Datei im Stream ist das Dateiformat xlsx.|
| Unbekannt|255 | Repräsentiert ein unbekanntes Format, kann nicht gespeichert werden.|
| Pdf|13 | Stellt eine PDF-Datei dar.|
| XPS|20 | Stellt eine XPS-Datei dar.|
| TIFF|21 | Stellt eine TIFF-Datei dar.|
| SVG|22 | Stellt eine SVG-Datei dar.|
| Dif|30 | Datenaustauschformat.|
Unten ist ein Code-Snippet, das die Konvertierung von xls nach xlsx zeigt, Sie können es auch umgekehrt machen

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
