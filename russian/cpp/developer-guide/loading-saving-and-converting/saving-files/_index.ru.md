---
title: Сохранение файлов
type: docs
weight: 20
url: /ru/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells позволяет создавать и сохранять файлы, а также изменять существующие файлы. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}} 
## **Различные способы сохранения файлов**
Aspose.Cells предоставляет [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет собой файл Microsoft Excel и предоставляет необходимые методы для работы с файлами Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) предоставляет метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/), используемый для сохранения файлов Excel. Метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) имеет много вариантов, используемых для сохранения файлов различными способами. Формат файла, в который файл сохраняется, определяется перечислением [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).
## **Сохранение файла в указанное местоположение**
Чтобы сохранить файлы в месте хранения, укажите имя файла (вместе с путем к хранению) и желаемый формат файла (из перечисления [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) при вызове метода [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save) объекта [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Сохранение файла в поток**
Чтобы сохранить файлы в поток, создайте объект MemoryStream или FileStream и сохраните файл в этот объект потока, вызвав метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save) объекта [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Укажите желаемый формат файла с использованием перечисления [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) при вызове метода [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Сохранение файла в PDF**
Чтобы сохранить необходимое содержимое в файле PDF, используя библиотеку Aspose.Cells for C++, создайте новый [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объект или сконструируйте [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объект путем чтения существующего файла Excel, а затем [сохраните](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) файл в PDF, вызвав метод Save объекта [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). При вызове метода Save используйте перечисление [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) для указания желаемого формата файла.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
