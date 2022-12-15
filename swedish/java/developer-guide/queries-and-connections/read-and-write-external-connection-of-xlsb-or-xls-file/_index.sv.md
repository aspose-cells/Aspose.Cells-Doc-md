---
title: Läs och skriv extern anslutning av XLSB- eller XLS-fil
type: docs
weight: 80
url: /sv/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **Möjliga användningsscenarier**

Aspose.Cells stöder redan läs och skriv extern anslutning av XLSX-fil men nu stöder den även denna funktion för XLSB- och XLS-filer. Koden är dock samma för båda typerna av format.

## **Läs och skriv extern anslutning av XLSB/XLS-fil**

Följande exempelkod laddar exempelfilen XLSB (XLS kan också laddas) och läser dess första externa anslutning som faktiskt är en Microsoft Access DB-anslutning. Den modifierar sedan[**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)egenskap och sparar den som output XLSB-fil. Skärmdumpen visar effekten av kod på[exempel på XLSB-fil](51740743.xlsb)och[output XLSB-fil](51740742.xlsb)efter dess utförande. Se även konsolutgången för exempelkoden nedan för en referens.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Exempelkod**

Följande kod ska fungera för både XLSB och XLS genom att ladda och spara filer med lämplig förlängning.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
