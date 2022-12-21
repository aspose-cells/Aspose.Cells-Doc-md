---
title: XLS および XLSB ファイルの外部接続の読み取りと書き込み
type: docs
weight: 80
url: /ja/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **考えられる使用シナリオ**

Aspose.Cells は既に XLSX ファイルの読み取りと書き込みの外部接続をサポートしていますが、今回は XLSB と XLS ファイルのこの機能もサポートしています。ただし、コードはすべてのタイプの形式で同じです。

## **XLS/XLSB ファイルの外部接続の読み取りと書き込み**

次のサンプル コードは、サンプル XLSB ファイル (XLS もロード可能) をロードし、実際には Microsoft Access DB 接続である最初の外部接続を読み取ります。次に、[**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name)プロパティを取得し、出力 XLS/XLSB ファイルとして保存します。スクリーンショットは、コードの効果を示しています[サンプル XLSB ファイル](51740722.xlsb)と[出力XLSBファイル](51740723.xlsb)その実行後。以下のサンプル コードのコンソール出力も参照してください。

![todo:画像_代替_文章](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **サンプルコード**

次のコードは、適切な拡張子を付けてファイルをロードおよび保存することにより、XLSB ファイルと XLS ファイルの両方で機能します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
