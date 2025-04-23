---
title: Различные способы открытия файлов
linktitle: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

С Aspose.Cells вы можете открывать файлы, например, для получения данных или использования шаблона дизайнера для ускорения разработки. Aspose.Cells может открывать различные типы файлов, такие как Microsoft Excel (XLS, XLSX, XLSM, XLSB), CSV или файлы с табуляцией.

{{% /alert %}}

## **Открытие файла по пути**

Разработчики могут открыть файл Microsoft Excel по его пути на локальном компьютере, указав его в конструкторе класса [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Передайте путь как строку. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Открытие файла с помощью потока**

Также возможно открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, принимающую объект *Stream*, содержащий файл.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
