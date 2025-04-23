---
title: 读取和写入XLS和XLSB文件的外部连接
type: docs
weight: 80
url: /zh/python-net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET已支持读取和写入XLSX文件的外部连接，但现在也支持XLSB和XLS文件的此功能。不过，所有格式的代码相同。

## **读取和写入XLS/XLSB文件的外部连接**

以下示例代码加载了示例XLSB文件（XLS也可以被加载），并读取其第一个外部连接，这实际上是一个Microsoft Access DB连接。然后修改了[**DBConnection.name**](https://reference.aspose.com/cells/python-net/aspose.cells.externalconnections/externalconnection/name)属性并将其保存为输出的XLS/XLSB文件。截屏展示了在执行代码后[示例XLSB文件](51740722.xlsb)和[输出XLSB文件](51740723.xlsb)上的效果。请还参阅下面给出的示例代码的控制台输出以供参考。

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **示例代码**

以下代码可以加载和保存具有适当扩展名的XLSB和XLS文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadAndWriteExternalConnectionOfXLSBFile.py" >}}

## **控制台输出**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}

