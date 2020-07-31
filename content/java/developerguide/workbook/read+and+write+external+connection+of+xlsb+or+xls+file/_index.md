---
title : "Read and Write External Connection of XLSB or XLS file" 
description : "" 
weight : 12107 
toc : false
type: docs
url: /java/developerguide/workbook/read+and+write+external+connection+of+xlsb+or+xls+file/
---

# Aspose.Cells for Java : Read and Write External Connection of XLSB or XLS file


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Read and Write External Connection of XLSB/XLS file](#read-and-write-external-connection-of-xlsb/xls-file)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells already supports read and write external connection of XLSX file but now, it also supports this feature for XLSB and XLS file. However, the code is same for both types of format.

## Read and Write External Connection of XLSB/XLS file

The following sample code loads the sample XLSB(XLS can also be loaded) file and reads its first External Connection which is actually a Microsoft Access DB Connection. It then modifies the [DBConnection.Name](https://apireference.aspose.com/java/cells/com.aspose.cells/dbconnection#Name) property and saves it as output XLSB file. The screenshot shows the effect of code on [sample XLSB file](https://docs2.aspose.com/cells/java/attachments/51480070/51740743.xlsb) and [output XLSB file](https://docs2.aspose.com/cells/java/attachments/51480070/51740742.xlsb) after its execution. Please also see the console output of the sample code given below for a reference.

![](https://docs2.aspose.com/cells/java/attachments/51480070/51740741.png)

## Sample Code

Following code shall work for both XLSB and XLS by loading and saving files with appropriate extension.

## Console Output

Connection Name: CustCommand: CustomerConnection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\\TempSha\\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

