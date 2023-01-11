﻿---
title: Konvertieren Sie das Arbeitsblatt in CSV
type: docs
weight: 30
url: /de/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Konvertieren Sie das Arbeitsblatt in CSV**
Wenn Entwickler ihre Dateien an einem Speicherort speichern müssen, können sie einfach den Dateinamen (mit vollständigem Speicherpfad) und das gewünschte Dateiformat (unter Verwendung der**Dateiformattyp**Aufzählung) beim Aufrufen der**speichern**Methode von**Arbeitsmappe**Objekt.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Konvertieren Sie das Arbeitsblatt in CSV**
Der folgende Code zeigt, wie das Arbeitsblatt mit Apache POI HSSF und XSSF API in CSV konvertiert werden kann, im Vergleich zu Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Ein rudimentärer XLSX -> CSV Prozessor nach Vorbild des

\* POI-Beispielprogramm XLS2CSVmra von Nick Burch aus der

\* Paket org.apache.poi.hssf.eventusermodel.examples.

\* Im Gegensatz zur HSSF-Version ignoriert diese vollständig

\* fehlende Zeilen.

\* <p/>

\* Datenblätter werden mit einem SAX-Parser gelesen, um die

\* Speicherbedarf relativ klein, also sollte das sein

\* in der Lage, riesige Arbeitsmappen zu lesen. Die Stiltabelle und

\* Die Shared-String-Tabelle muss im Speicher gehalten werden. Das

\* Standard-POI-Stiltabellenklasse wird verwendet, aber eine benutzerdefinierte

\* (schreibgeschützte) Klasse wird für die gemeinsam genutzte Zeichenfolgentabelle verwendet

\* weil die Standard POI SharedStringsTable sehr wächst

\* schnell mit der Anzahl der eindeutigen Zeichenfolgen.

\* <p/>

\* Danke an Eric Smith für einen Patch, der ein Problem behebt

\* ausgelöst durch Zellen mit mehreren "t"-Elementen, das heißt

\* wie Excel verschiedene Formate darstellt (z. B. ein Wort

\* einfach und ein Wort fett).

\*

\* @Autor Chris Lott

*/

öffentliche Klasse ApacheXLSX2CSV {