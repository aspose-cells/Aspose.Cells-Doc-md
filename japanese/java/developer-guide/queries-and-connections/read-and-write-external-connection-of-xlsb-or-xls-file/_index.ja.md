---
title: XLSB または XLS ファイルの外部接続の読み取りと書き込み
type: docs
weight: 80
url: /ja/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **考えられる使用シナリオ**

Aspose.Cells は既に XLSX ファイルの読み取りと書き込みの外部接続をサポートしていますが、現在は XLSB と XLS ファイルのこの機能もサポートしています。ただし、コードは両方のタイプの形式で同じです。

## **XLSB/XLS ファイルの外部接続の読み取りと書き込み**

次のサンプル コードは、サンプル XLSB (XLS もロード可能) ファイルをロードし、実際には Microsoft Access DB 接続である最初の外部接続を読み取ります。次に、[**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)プロパティを取得し、出力 XLSB ファイルとして保存します。スクリーンショットは、コードの効果を示しています[サンプル XLSB ファイル](51740743.xlsb)と[出力 XLSB ファイル](51740742.xlsb)その実行後。以下のサンプル コードのコンソール出力も参照してください。

![todo:画像_代替_文章](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **サンプルコード**

次のコードは、適切な拡張子のファイルを読み込んで保存することにより、XLSB と XLS の両方で機能します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
