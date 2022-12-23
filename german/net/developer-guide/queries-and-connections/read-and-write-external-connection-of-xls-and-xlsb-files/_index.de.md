---
title: Externe Verbindung von XLS- und XLSB-Dateien lesen und schreiben
type: docs
weight: 80
url: /de/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells unterstützt bereits das Lesen und Schreiben einer externen Verbindung der Datei XLSX, aber jetzt unterstützt es diese Funktion auch für die Dateien XLSB und XLS. Der Code ist jedoch für alle Formattypen gleich.

## **Externe Verbindung der Datei XLS/XLSB lesen und schreiben**

 Der folgende Beispielcode lädt die Beispieldatei XLSB (XLS kann auch geladen werden) und liest ihre erste externe Verbindung, die eigentlich eine Microsoft Access DB Connection ist. Es ändert dann die[**DBVerbindung.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) -Eigenschaft und speichert sie als Ausgabedatei XLS/XLSB. Der Screenshot zeigt die Auswirkung von Code auf[Beispieldatei XLSB](51740722.xlsb) und[Ausgabedatei XLSB](51740723.xlsb) nach seiner Hinrichtung. Siehe auch die Konsolenausgabe des unten angegebenen Beispielcodes als Referenz.

![todo: Bild_alt_Text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Beispielcode**

Der folgende Code funktioniert sowohl für XLSB- als auch für XLS-Dateien, indem Dateien mit der entsprechenden Erweiterung geladen und gespeichert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
