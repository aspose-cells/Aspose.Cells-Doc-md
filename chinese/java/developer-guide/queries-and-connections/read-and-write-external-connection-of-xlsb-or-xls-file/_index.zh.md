---
title: XLSB 或 XLS 文件的读写外部连接
type: docs
weight: 80
url: /zh/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **可能的使用场景**

Aspose.Cells已经支持XLSX文件的读写外部连接，现在，它也支持XLSB和XLS文件的这个功能。但是，两种格式的代码相同。

## **XLSB/XLS文件的读写外部连接**

下面的示例代码加载示例XLSB（也可以加载XLS）文件并读取它的第一个External Connection，它实际上是一个Microsoft Access DB Connection。然后它修改了[**数据库连接名称**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)属性并将其保存为输出 XLSB 文件。截图展示了代码的效果[示例 XLSB 文件](51740743.xlsb)和[输出 XLSB 文件](51740742.xlsb)执行后。另请参阅下面给出的示例代码的控制台输出以供参考。

![待办事项：图片_替代_文本](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **示例代码**

通过加载和保存具有适当扩展名的文件，以下代码适用于 XLSB 和 XLS。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **控制台输出**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
