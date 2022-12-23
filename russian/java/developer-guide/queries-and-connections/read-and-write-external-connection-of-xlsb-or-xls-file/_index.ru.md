---
title: Чтение и запись внешнего соединения файла XLSB или XLS
type: docs
weight: 80
url: /ru/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **Возможные сценарии использования**

Aspose.Cells уже поддерживает чтение и запись внешнего соединения файла XLSX, но теперь он также поддерживает эту функцию для файлов XLSB и XLS. Однако код одинаков для обоих типов формата.

## **Чтение и запись внешнего соединения файла XLSB/XLS**

Следующий пример кода загружает пример файла XLSB (XLS также может быть загружен) и считывает его первое внешнее соединение, которое на самом деле является соединением Microsoft Access DB. Затем он изменяет[**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)свойство и сохраняет его как выходной файл XLSB. На скриншоте показано влияние кода на[образец файла XLSB](51740743.xlsb)и[выходной файл XLSB](51740742.xlsb)после его выполнения. См. также вывод на консоль примера кода, приведенного ниже, для справки.

![дело:изображение_альтернативный_текст](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Образец кода**

Следующий код должен работать как для XLSB, так и для XLS путем загрузки и сохранения файлов с соответствующим расширением.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
