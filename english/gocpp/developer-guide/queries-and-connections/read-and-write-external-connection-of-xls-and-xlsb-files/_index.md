---
title: Read and Write External Connection of XLS and XLSB files with Golang via C++
linktitle: Read and Write External Connection of XLS and XLSB files
type: docs
weight: 80
url: /go-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Learn how to read and modify external database connections in XLS/XLSB files using Aspose.Cells for Go via C++.
---

## **Possible Usage Scenarios**

Aspose.Cells for Go via C++ supports reading and writing external connections for XLSX files and now extends this capability to XLSB and XLS formats. The same code structure works for all supported file types.

## **Read and Write External Connections of XLS/XLSB Files**

The following sample code loads a sample XLSB file (also works with XLS) and modifies its first external connection (typically a Microsoft Access DB connection). The code demonstrates how to:

1. Load the spreadsheet file.
2. Access external connections.
3. Modify connection properties.
4. Save the modified file.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Sample Code**

This code works for both XLSB and XLS files by adjusting input/output file extensions.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAndWriteExternalConnectionOfXlsAndXlsbFiles.go" >}}

**C++ Equivalent:**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAndWriteExternalConnectionOfXlsAndXlsbFiles-1.go" >}}

## **Console Output**

{{< highlight go >}}
Connection Name: Cust
Command: Customer
Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False
{{< /highlight >}}
