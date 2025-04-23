---
title: Läs och skriv extern anslutning för XLS och XLSB filer
type: docs
weight: 80
url: /sv/python-net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **Möjliga användningsscenario**

Aspose.Cell för Python via .NET stöder redan att läsa och skriva externa anslutningar till XLSX-fil men nu stöder det även denna funktion för XLSB och XLS filer. Koden är dock densamma för alla format.

## **Läs och skriv extern anslutning för XLS/XLSB-fil**

Det följande kodexemplet laddar den provisoriska XLSB-filen (XLS kan också laddas) och läser den första externa anslutningen som faktiskt är en Microsoft Access DB-anslutning. Det ändrar sedan egenskapen [**DBConnection.name**](https://reference.aspose.com/cells/python-net/aspose.cells.externalconnections/externalconnection/name) och sparar den som utdata XLS/XLSB-fil. Skärmbilden visar effekten av koden på [prov-XLSB-filen](51740722.xlsb) och [utdata-XLSB-filen](51740723.xlsb) efter att den har körts. Se även konsoloutputen för kodexemplet nedan för referens.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Exempelkod**

Följande kod ska fungera för både XLSB- och XLS-filer genom att ladda och spara filer med rätt tillägg.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadAndWriteExternalConnectionOfXLSBFile.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}

