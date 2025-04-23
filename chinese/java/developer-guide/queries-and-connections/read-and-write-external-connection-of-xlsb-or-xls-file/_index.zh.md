---
title: 读取和写入XLSB或XLS文件的外部连接
type: docs
weight: 80
url: /zh/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **可能的使用场景**

Aspose.Cells已经支持对XLSX文件进行读取和写入外部连接，现在也支持XLSB和XLS文件的这一功能。然而，对于这两种格式，代码是相同的。

## **读取和写入XLSB/XLS文件的外部连接**

以下示例代码加载了示例XLSB文件（也可以加载XLS文件），读取其第一个外部连接，实际上是一个Microsoft Access DB连接。然后修改[**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)属性，并将其保存为输出XLSB文件。屏幕截图显示了代码在执行后对[sample XLSB file](51740743.xlsb)和[output XLSB file](51740742.xlsb)的影响。请查看下面给出的示例代码的控制台输出以供参考。

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **示例代码**

以下代码将适用于加载和保存相应扩展名的XLSB和XLS文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **控制台输出**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
