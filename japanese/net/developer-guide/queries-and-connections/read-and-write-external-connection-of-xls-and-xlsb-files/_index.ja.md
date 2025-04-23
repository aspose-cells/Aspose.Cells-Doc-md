---
title: XLSおよびXLSBファイルの外部接続の読み取りと書き込み
type: docs
weight: 80
url: /ja/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **可能な使用シナリオ**

Aspose.CellsはすでにXLSXファイルの外部接続の読み取りと書き込みをサポートしていますが、現在はXLSBおよびXLSファイルの外部接続の読み取りと書き込みもサポートしています。ただし、すべての種類の形式に対してコードは同じです。

## **XLS/XLSBファイルの外部接続の読み取りと書き込み**

以下のサンプルコードでは、サンプルのXLSBファイル（XLSもロードできます）をロードし、実際にはMicrosoft Access DB接続である最初の外部接続を取得します。その後、[**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) プロパティを変更し、出力されたXLS/XLSBファイルとして保存します。スクリーンショットは、コードの [サンプルXLSBファイル](51740722.xlsb) および [出力XLSBファイル](51740723.xlsb) への影響を示しています。以下に示すサンプルコードのコンソール出力も参照してください。

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **サンプルコード**

このコードは、適切な拡張子のファイルを読み込んで保存することにより、XLSBおよびXLSファイルの両方で動作します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
