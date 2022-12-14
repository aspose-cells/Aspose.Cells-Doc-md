---
title: Чтение и запись внешнего подключения файлов XLS и XLSB
type: docs
weight: 80
url: /ru/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **Возможные сценарии использования**

Aspose.Cells уже поддерживает внешнее подключение для чтения и записи файла XLSX, но теперь он также поддерживает эту функцию для файлов XLSB и XLS. Однако код одинаков для всех типов форматов.

## **Чтение и запись внешнего соединения файла XLS/XLSB**

 Следующий пример кода загружает образец файла XLSB (XLS также может быть загружен) и считывает его первое внешнее соединение, которое на самом деле является соединением Microsoft Access DB. Затем он изменяет[**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) свойство и сохраняет его как выходной файл XLS/XLSB. На скриншоте показано влияние кода на[образец XLSB-файла](51740722.xlsb) а также[выходной файл XLSB](51740723.xlsb) после его исполнения. См. также вывод на консоль примера кода, приведенного ниже, для справки.

![дело:изображение_альтернативный_текст](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Образец кода**

Следующий код должен работать как с файлами XLSB, так и с файлами XLS, загружая и сохраняя файлы с соответствующим расширением.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
