---
title: Сохранение файла в объект ответа
type: docs
weight: 50
url: /ru/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells делает возможным манипулирование файлами. В этой статье объясняются различные способы сохранения файлов в объект ответа.

{{% /alert %}}

## **Сохранение файла в объект ответа**

Также возможно динамически создавать файл и направлять его непосредственно в браузер клиента. Для этого используйте специальную перегруженную версию метода [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5), принимающую следующие параметры:

- ASP.NET объект [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8).
- Имя файла.
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition), тип содержания выводимого файла.
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions), тип формата файла

Перечисление [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) определяет, предоставляет ли файл, отправляемый в браузер, возможность открыть его непосредственно в браузере или в приложении, связанном с .xls/.xlsx или другим расширением.

Перечисление содержит следующие предопределенные типы сохранения:

|**Тип**|**Описание**|
| :- | :- |
|Attachment|Отправляет электронную таблицу в браузер и открывает ее в приложении в качестве вложения, связанного с .xls/.xlsx или другими расширениями|
|Inline|Отправляет документ в браузер и предоставляет возможность сохранить электронную таблицу на диск или открыть внутри браузера|

### **XLS Файлы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX Файлы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF Файлы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Примечание**

Из-за объекта"System.Web.HttpResponse", который не включен в .NET5 и .Netstandard,
Поэтому данная функция не существует в Aspose.Cells .NET5 и Netstandard версии, вы можете обратиться к следующему коду, чтобы сохранить файл в поток, а затем выполнить операцию с потоком.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
