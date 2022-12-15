---
title: Leggere e scrivere connessione esterna di file XLSB o XLS
type: docs
weight: 80
url: /it/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **Possibili scenari di utilizzo**

Aspose.Cells supporta già la lettura e la scrittura della connessione esterna del file XLSX ma ora supporta anche questa funzione per i file XLSB e XLS. Tuttavia, il codice è lo stesso per entrambi i tipi di formato.

## **Leggere e scrivere la connessione esterna del file XLSB/XLS**

Il seguente codice di esempio carica il file di esempio XLSB (XLS può essere caricato anche) e legge la sua prima connessione esterna che è effettivamente una connessione DB di Microsoft Access. Quindi modifica il file[**DBConnection.Nome**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)proprietà e lo salva come file XLSB di output. Lo screenshot mostra l'effetto del codice su[file XLSB di esempio](51740743.xlsb)e[file XLSB di output](51740742.xlsb)dopo la sua esecuzione. Si prega di consultare anche l'output della console del codice di esempio fornito di seguito per un riferimento.

![cose da fare:immagine_alt_testo](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Codice di esempio**

Il seguente codice funzionerà sia per XLSB che per XLS caricando e salvando i file con l'estensione appropriata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Uscita console**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
