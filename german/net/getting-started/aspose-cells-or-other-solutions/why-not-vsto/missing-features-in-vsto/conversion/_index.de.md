---
title: Konvertierung
type: docs
weight: 30
url: /de/net/conversion/
---

Eine einzigartige Funktion von Aspose.Cells, die Flexibilität bei Versionskonvertierungen bietet, ohne die Arbeit zu beeinträchtigen.
SaveFormat ist eine Enumeration, die das Dokument in den unten in der Tabelle angegebenen Erweiterungen konvertieren kann.

|**Mitgliedsname** |**Wert** |**Beschreibung** |
| :- | :- | :- |
|CSV |1 |Stellt eine CSV-Datei dar. |
|Xlsx |6 |Stellt eine xlsx-Datei dar. |
|Xlsm |7 |Stellt eine xlsm-Datei dar, die Makros aktiviert. |
|Xltx |8 |Stellt eine xltx-Datei dar. |
|Xltm |9 |Stellt eine xltm-Datei dar, die Makros aktiviert. |
|TabDelimited |11 |Stellt eine tabulatorgetrennte Textdatei dar. |
|Html |12 |Stellt eine HTML-Datei dar. |
|MHtml |17 |Stellt eine MHTML-Datei dar. |
|ODS |14 |Stellt eine ods-Datei dar. |
|Excel97To2003 |5 |Stellt eine Excel97-2003 xls-Datei dar. |
|SpreadsheetML |15 | Stellt eine Excel 2003-XML-Datei dar. |
|Xlsb |16 | Stellt eine xlsb-Datei dar. |
|Auto |0 | Wenn die Datei auf dem Datenträger gespeichert wird, entspricht das Dateiformat der Erweiterung des Dateinamens. <br> Wenn die Datei in den Stream gespeichert wird, ist das Dateiformat xlsx. |
|Unknown |255 | Stellt ein nicht erkanntes Format dar, das nicht gespeichert werden kann. |
|Pdf |13 | Stellt eine Pdf-Datei dar. |
|XPS |20 | Stellt eine XPS-Datei dar. |
|TIFF |21 | Stellt eine TIFF-Datei dar. |
|SVG |22 | Stellt eine SVG-Datei dar. |
|Dif |30 | Datenaustauschformat. |
Im Folgenden finden Sie einen Code-Schnipsel, der die Konvertierung von xls nach xlsx zeigt. Sie können es auch umgekehrt tun.

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
