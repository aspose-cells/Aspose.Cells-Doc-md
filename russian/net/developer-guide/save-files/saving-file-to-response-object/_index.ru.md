---
title: Сохранение файла в объект ответа
type: docs
weight: 50
url: /ru/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет манипулировать файлами. В этой статье объясняются различные способы сохранения файлов в объекте ответа.

{{% /alert %}}

## **Сохранение файла в объект ответа**

 Также можно динамически генерировать файл и отправлять его непосредственно в клиентский браузер. Для этого используйте специальную перегруженную версию**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**метод, который принимает следующие параметры:

-  ASP.NET**[HttpResponse] (https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**объект.
- Имя файла.
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, тип содержимого выходного файла.
- **[Параметры сохранения] (https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, тип формата файла

**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**перечисление определяет, предоставляет ли файл, отправляемый в браузер, возможность открытия непосредственно в браузере или в приложении, связанном с .xls/.xlsx или другим расширением.

Перечисление содержит следующие предопределенные типы сохранения:

|**Тип**|**Описание**|
|:- |:- |
|Вложение|Отправляет электронную таблицу в браузер и открывает в приложении как вложение, связанное с .xls/.xlsx или другими расширениями.|
|В линию|Отправляет документ в браузер и предоставляет возможность сохранить электронную таблицу на диск или открыть ее в браузере.|

### **XLS Файлы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX Файлы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF Файлы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Запись**

Из-за того, что объект «System.Web.HttpResponse» не содержится в .NET5 и .Netstandard,
Таким образом, эта функция не существует в версии Aspose.Cells .NET5 и .Netstandard, вы можете обратиться к следующему коду, чтобы сохранить файл в потоке, а затем выполнить операцию в потоке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

