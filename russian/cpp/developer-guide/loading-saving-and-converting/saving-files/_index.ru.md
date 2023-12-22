---
title: Сохранение файлов
type: docs
weight: 20
url: /ru/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells позволяет создавать и сохранять файлы, а также манипулировать существующими файлами. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}} 
##  **Различные способы сохранения файлов**
 Aspose.Cells обеспечивает[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft и предоставляет методы, необходимые для работы с файлами Excel.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс обеспечивает[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) метод, используемый для сохранения файлов Excel.[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Метод имеет множество перегрузок, которые используются для сохранения файлов разными способами. Формат файла, в котором сохраняется файл, определяется[СохранитьФормат](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)перечисление.
##  **Сохранение файла в какое-то место**
Чтобы сохранить файлы в место хранения, укажите имя файла (вместе с путем к хранилищу) и желаемый формат файла (из[СохранитьФормат](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) перечисление) при вызове[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объекты[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Сохранение файла в потоке**
 Чтобы сохранить файлы в поток, создайте объект MemoryStream или FileStream и сохраните файл в этом объекте потока, вызвав метод[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объекты[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) метод. Укажите желаемый формат файла с помощью[СохранитьФормат](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) перечисление при вызове[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
