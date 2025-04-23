---
title: Leggere e Scrivere Connessioni Esterne di file XLS e XLSB
type: docs
weight: 80
url: /it/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells supporta già la lettura e la scrittura di connessioni esterne di file XLSX, ma ora supporta anche questa funzionalità per i file XLSB e XLS. Tuttavia, il codice è lo stesso per tutti i tipi di formati.

## **Leggere e Scrivere Connessioni Esterne di file XLS/XLSB**

Il seguente esempio di codice carica il file di esempio XLSB (è possibile caricare anche XLS) e legge la sua prima Connessione Esterna che è effettivamente una connessione Microsoft Access DB. Modifica quindi la proprietà [**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) e la salva come file di output XLS/XLSB. La schermata mostra l'effetto del codice sul [file di esempio XLSB](51740722.xlsb) e sul [file di output XLSB](51740723.xlsb) dopo la sua esecuzione. Si prega di consultare anche l'output della console del codice di esempio riportato di seguito per un riferimento.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Codice di Esempio**

Il seguente codice funzionerà sia per i file XLSB che per i file XLS, caricando e salvando i file con l'estensione appropriata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Output della console**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
