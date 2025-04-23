---
title: Lesen und Schreiben externer Verbindung einer XLSB oder XLS Datei
type: docs
weight: 80
url: /de/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells unterstützt bereits das Lesen und Schreiben externer Verbindungen von XLSX-Dateien, jetzt jedoch auch für XLSB- und XLS-Dateien. Der Code ist jedoch für beide Formate gleich.

## **Lesen und Schreiben externer Verbindung von XLSB-/XLS-Dateien**

Der folgende Beispielcode lädt die Beispieldatei XLSB (XLS kann ebenfalls geladen werden) und liest ihre erste externe Verbindung, die tatsächlich eine Microsoft Access DB-Verbindung ist. Anschließend wird die [**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name) Eigenschaft geändert und als Ausgabedatei XLSB gespeichert. Der Screenshot zeigt die Auswirkungen des Codes auf die [Beispieldatei XLSB](51740743.xlsb) und die [Ausgabedatei XLSB](51740742.xlsb) nach dessen Ausführung. Lesen Sie auch die Konsolenausgabe des untenstehenden Beispielcodes als Referenz.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Beispielcode**

Der folgende Code funktioniert sowohl für XLSB als auch für XLS, indem Dateien mit entsprechender Erweiterung geladen und gespeichert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
