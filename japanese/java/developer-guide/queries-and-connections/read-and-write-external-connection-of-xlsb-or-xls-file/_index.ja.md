---
title: XLSBまたはXLSファイルの外部接続の読み書き
type: docs
weight: 80
url: /ja/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **可能な使用シナリオ**

Aspose.CellsはXLSXファイルの外部接続の読み書きをすでにサポートしていますが、現在、XLSBおよびXLSファイルのこの機能もサポートしています。ただし、コードは両方の形式で同じです。

## **XLSB/XLSファイルの外部接続の読み書き**

次のサンプルコードは、サンプルのXLSB（XLSも読み込むことができます）ファイルをロードし、実際にはMicrosoft Access DB接続である最初の外部接続を読み取ります。次に、それのプロパティを修正して出力XLSBファイルとして保存します。スクリーンショットは、このコードの[sample XLSB file](51740743.xlsb)および[output XLSB file](51740742.xlsb)への実行後の効果を示しています。参考のために以下で示されるサンプルコードのコンソール出力もご覧ください。

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **サンプルコード**

次のコードは、正しい拡張子のファイルを読み込んで保存することによって、XLSBおよびXLSの両方で動作します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **コンソール出力**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
