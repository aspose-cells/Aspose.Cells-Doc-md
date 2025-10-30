---
title: Externe Verbindung von XLS und XLSB Dateien lesen und schreiben
type: docs
weight: 80
url: /de/python-net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cell für Python via .NET unterstützt bereits das Lesen und Schreiben externer Verbindungen in XLSX-Dateien, jetzt unterstützt es diese Funktion auch für XLSB- und XLS-Dateien. Der Code ist jedoch für alle Formate gleich.

## **Externe Verbindung von XLS/XLSB-Dateien lesen und schreiben**

Der folgende Beispielcode lädt die Beispiel-XLSB-Datei (XLS kann ebenfalls geladen werden) und liest ihre erste externe Verbindung, die tatsächlich eine Microsoft Access DB-Verbindung ist. Dann wird die [**DBConnection.name**](https://reference.aspose.com/cells/python-net/aspose.cells.externalconnections/externalconnection/name)-Eigenschaft geändert und die Datei als Ausgabe-XLS/XLSB-Datei gespeichert. Der Screenshot zeigt die Auswirkungen des Codes auf die [Beispiel-XLSB-Datei](51740722.xlsb) und die [Ausgabe-XLSB-Datei](51740723.xlsb) nach ihrer Ausführung. Bitte beachten Sie auch die Konsolenausgabe des Beispielcodes unten als Referenz.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Beispielcode**

Der folgende Code funktioniert sowohl für XLSB- als auch für XLS-Dateien, indem die Dateien mit der entsprechenden Erweiterung geladen und gespeichert werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadAndWriteExternalConnectionOfXLSBFile.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
