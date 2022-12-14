---
title: Сохранение файлов
type: docs
weight: 20
url: /ru/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells позволяет создавать и сохранять файлы, а также управлять существующими файлами. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}} 
## **Различные способы сохранения файлов**
 Aspose.Cells обеспечивает[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет файл Excel Microsoft и предоставляет методы, необходимые для работы с файлами Excel.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)класс обеспечивает[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) метод, используемый для сохранения файлов Excel.[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) Метод имеет множество перегрузок, которые используются для сохранения файлов разными способами. Формат файла, в котором сохраняется файл, определяется[СохранитьФормат](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)перечисление.
## **Сохранение файла в каком-либо месте**
 Чтобы сохранить файлы в месте хранения, укажите имя файла (вместе с путем хранения) и желаемый формат файла (из[СохранитьФормат](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) перечисление) при вызове[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) объекты[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Сохранение файла в поток**
 Чтобы сохранить файлы в потоке, создайте объект MemoryStream или FileStream и сохраните файл в этом объекте потока, вызвав метод[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) объекты[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) метод. Укажите желаемый формат файла с помощью[СохранитьФормат](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) перечисление при вызове[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
