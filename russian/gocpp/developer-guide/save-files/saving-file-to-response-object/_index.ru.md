---
title: Сохранение файла в объект Response с помощью Golang через C++
linktitle: Сохранение файла в объект ответа
type: docs
weight: 50
url: /ru/go-cpp/saving-file-to-response-object/
description: Узнайте, как динамически сохранять файлы и отправлять их напрямую в браузер клиента с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells делает возможным манипулирование файлами. В этой статье объясняются различные способы сохранения файлов в объект ответа.

{{% /alert %}}

## **Сохранение файла в объект ответа**

Также возможно динамически создавать файл и направлять его непосредственно в браузер клиента. Для этого используйте специальную перегруженную версию метода [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/), принимающую следующие параметры:

- Объект `HttpResponse`.
- Имя файла.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), тип содержания выводимого файла.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), тип формата файла.

Перечисление [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) определяет, предоставляет ли файл, отправляемый в браузер, возможность открыть его непосредственно в браузере или в приложении, связанном с .xls/.xlsx или другим расширением.

Перечисление содержит следующие предопределенные типы сохранения:

|**Тип**|**Описание**|
| :- | :- |
|Attachment|Отправляет электронную таблицу в браузер и открывает ее в приложении в качестве вложения, связанного с .xls/.xlsx или другими расширениями|
|Inline|Отправляет документ в браузер и предоставляет возможность сохранить электронную таблицу на диск или открыть внутри браузера|

### **XLS Файлы**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **XLSX Файлы**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **PDF Файлы**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Примечание**

Из-за объекта"System.Web.HttpResponse", который не включен в .NET5 и .Netstandard,
Поэтому данная функция не существует в Aspose.Cells .NET5 и Netstandard версии, вы можете обратиться к следующему коду, чтобы сохранить файл в поток, а затем выполнить операцию с потоком.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
