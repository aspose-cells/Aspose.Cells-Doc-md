---
title: Чтение и запись внешнего соединения файлов XLS и XLSB
type: docs
weight: 80
url: /ru/python-net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **Возможные сценарии использования**

Aspose.Cell для Python via .NET уже поддерживает чтение и запись внешних соединений XLSX файла, теперь он также поддерживает эту функцию для XLSB и XLS. Однако код одинаков для всех типов форматов.

## **Чтение и запись внешнего соединения файлов XLS/XLSB**

Следующий образец кода загружает образец файла XLSB (также можно загружать XLS) и считывает его первое внешнее подключение, которое на самом деле является подключением к базе данных Microsoft Access. Затем он изменяет свойство [**DBConnection.name**](https://reference.aspose.com/cells/python-net/aspose.cells.externalconnections/externalconnection/name) и сохраняет его в качестве выходного файла XLS/XLSB. Снимок экрана показывает эффект кода на [образцовый файл XLSB](51740722.xlsb) и [выходной файл XLSB](51740723.xlsb) после его выполнения. Также обратите внимание на вывод консоли образца кода ниже для справки.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Образец кода**

Следующий код будет работать как для файлов XLSB, так и для файлов XLS, загружая и сохраняя файлы с соответствующим расширением.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadAndWriteExternalConnectionOfXLSBFile.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}

