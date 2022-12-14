---
title: Läs och skriv extern anslutning av XLS- och XLSB-filer
type: docs
weight: 80
url: /sv/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **Möjliga användningsscenarier**

Aspose.Cells stöder redan läs och skriv extern anslutning av XLSX-fil men nu stöder den även denna funktion för XLSB- och XLS-filer. Koden är dock densamma för alla typer av format.

## **Läs och skriv extern anslutning av XLS/XLSB-fil**

Följande exempelkod laddar XLSB-exemplet (XLS kan också laddas) och läser dess första externa anslutning som egentligen är en Microsoft Access DB-anslutning. Den ändrar sedan[**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) egenskap och sparar den som output XLS/XLSB-fil. Skärmdumpen visar effekten av kod på[exempel på XLSB-fil](51740722.xlsb) och[output XLSB-fil](51740723.xlsb) efter dess utförande. Se även konsolutgången för exempelkoden nedan för en referens.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Exempelkod**

Följande kod ska fungera för både XLSB- och XLS-filer genom att ladda och spara filer med rätt tillägg.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
