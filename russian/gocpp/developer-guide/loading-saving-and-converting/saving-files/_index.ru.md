---
title: Сохранение файлов
type: docs
weight: 20
url: /ru/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет создавать и сохранять файлы, а также изменять существующие файлы. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}}

## **Различные способы сохранения файлов**

Aspose.Cells предоставляет [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет собой файл Microsoft Excel и содержит методы для работы с файлами Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) включает метод [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/), используемый для сохранения файлов Excel. У метода [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) есть множество перегрузок, позволяющих сохранять файлы разными способами. Формат файла, в который сохраняется файл, определяется перечислением [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

## **Сохранение файла в указанное местоположение**

Чтобы сохранить файлы в хранилище, укажите имя файла (включая путь к хранилищу) и желаемый формат файла (из перечисления [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)) при вызове метода [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)) объекта [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Сохранение файла в поток**

Для сохранения файла в поток создайте объект MemoryStream или FileStream и сохраните файл в этот поток, вызвав метод [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)) у объекта [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Укажите желаемый формат файла, используя перечисление [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/), при вызове метода [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Сохранение файла в PDF**

Чтобы сохранить необходимое содержимое в PDF-файл, используя библиотеку Aspose.Cells for Go via C++, создайте новый объект [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) или откройте существующий Excel-файл, затем вызовите метод [save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveOptions/) для сохранения в PDF. При вызове метода Save укажите формат файла, использовав перечисление [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
