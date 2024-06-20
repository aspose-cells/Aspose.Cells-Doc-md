---
title: Чтение и запись внешнего подключения XLSB или XLS файла
type: docs
weight: 80
url: /ru/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **Возможные сценарии использования**

Aspose.Cells уже поддерживает чтение и запись внешнего подключения к файлу XLSX, а теперь он также поддерживает эту функцию для файлов XLSB и XLS. Однако код остается тем же для обоих типов формата.

## **Чтение и запись внешнего подключения к файлу XLSB/XLS**

Следующий образец кода загружает образецный файл XLSB (XLS также можно загрузить) и считывает его первое внешнее подключение, которое на самом деле является подключением к базе данных Microsoft Access. Затем он изменяет свойство [**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name) и сохраняет его как выходной файл XLSB. Снимок экрана показывает эффект кода на [образцовом файле XLSB](51740743.xlsb) и [выходном файле XLSB](51740742.xlsb) после его выполнения. Пожалуйста, также обратите внимание на вывод консоли образца кода, приведенного ниже для справки.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Образец кода**

Следующий код будет работать как для XLSB, так и для XLS, загружая и сохраняя файлы с соответствующим расширением.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
