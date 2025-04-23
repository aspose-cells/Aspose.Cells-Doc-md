---
title: Leggi e Scrivi la Connessione Esterna del file XLSB o XLS
type: docs
weight: 80
url: /it/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells supporta già la lettura e la scrittura della connessione esterna del file XLSX ma ora supporta anche questa funzione per i file XLSB e XLS. Tuttavia, il codice è lo stesso per entrambi i tipi di formati.

## **Leggi e Scrivi la Connessione Esterna del file XLSB/XLS**

Il seguente codice di esempio carica il file XLSB di esempio (anche il file XLS può essere caricato) e legge la sua prima Connessione Esterna che è in realtà una Connessione al Database di Microsoft Access. Poi modifica la proprietà [**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name) e la salva come file XLSB di output. La schermata mostra l'effetto del codice sul file XLSB di esempio e sul file XLSB di output dopo la sua esecuzione. Consulta anche l'output della console del codice di esempio fornito di seguito per un riferimento.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Codice di Esempio**

Il seguente codice funzionerà per entrambi i formati XLSB e XLS, caricando e salvando file con l'estensione appropriata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Output della console**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
