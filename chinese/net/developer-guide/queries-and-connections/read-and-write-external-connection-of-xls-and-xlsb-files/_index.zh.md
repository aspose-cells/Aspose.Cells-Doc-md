---
title: XLS和XLSB文件的读写外部连接
type: docs
weight: 80
url: /zh/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **可能的使用场景**

Aspose.Cells已经支持XLSX文件的读写外部连接，现在，它也支持XLSB和XLS文件的这个功能。但是，代码对于所有类型的格式都是相同的。

## **XLS/XLSB文件的读写外部连接**

下面的示例代码加载示例 XLSB 文件（也可以加载 XLS）并读取它的第一个外部连接，它实际上是一个 Microsoft Access DB 连接。然后它修改了[**数据库连接名称**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name)属性并将其保存为输出 XLS/XLSB 文件。截图展示了代码的效果[示例 XLSB 文件](51740722.xlsb)和[输出 XLSB 文件](51740723.xlsb)执行后。另请参阅下面给出的示例代码的控制台输出以供参考。

![待办事项：图片_替代_文本](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **示例代码**

通过加载和保存具有适当扩展名的文件，以下代码适用于 XLSB 和 XLS 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
