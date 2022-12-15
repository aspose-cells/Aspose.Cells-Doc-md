---
title: Leggere e scrivere connessione esterna di file XLS e XLSB
type: docs
weight: 80
url: /it/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **Possibili scenari di utilizzo**

Aspose.Cells supporta già la lettura e la scrittura della connessione esterna del file XLSX ma ora supporta anche questa funzione per i file XLSB e XLS. Tuttavia, il codice è lo stesso per tutti i tipi di formati.

## **Leggere e scrivere la connessione esterna del file XLS/XLSB**

 Il seguente codice di esempio carica il file XLSB di esempio (è possibile caricare anche XLS) e legge la sua prima connessione esterna che è effettivamente una connessione DB di Microsoft Access. Quindi modifica il file[**DBConnection.Nome**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) proprietà e lo salva come file XLS/XLSB di output. Lo screenshot mostra l'effetto del codice su[file XLSB di esempio](51740722.xlsb) e[file XLSB di output](51740723.xlsb) dopo la sua esecuzione. Si prega di consultare anche l'output della console del codice di esempio fornito di seguito per un riferimento.

![cose da fare:immagine_alt_testo](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Codice di esempio**

Il seguente codice funzionerà sia per i file XLSB che XLS caricando e salvando i file con l'estensione appropriata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
