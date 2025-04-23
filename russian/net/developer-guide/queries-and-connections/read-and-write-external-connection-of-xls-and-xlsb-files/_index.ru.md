---
title: Чтение и запись внешнего соединения файлов XLS и XLSB
type: docs
weight: 80
url: /ru/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **Возможные сценарии использования**

Aspose.Cells уже поддерживает чтение и запись внешних соединений в файлах XLSX, но теперь мы также поддерживаем эту функцию для файлов XLSB и XLS. Однако код остается тем же для всех типов форматов.

## **Чтение и запись внешнего соединения файлов XLS/XLSB**

Следующий образец кода загружает образец файла XLSB (также можно загружать XLS) и считывает его первое внешнее подключение, которое на самом деле является подключением к базе данных Microsoft Access. Затем он изменяет свойство [**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) и сохраняет его в качестве выходного файла XLS/XLSB. Снимок экрана показывает эффект кода на [образцовый файл XLSB](51740722.xlsb) и [выходной файл XLSB](51740723.xlsb) после его выполнения. Также обратите внимание на вывод консоли образца кода ниже для справки.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Образец кода**

Следующий код будет работать как для файлов XLSB, так и для файлов XLS, загружая и сохраняя файлы с соответствующим расширением.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
