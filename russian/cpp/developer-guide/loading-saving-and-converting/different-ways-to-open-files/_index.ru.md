---
title: Различные способы открытия файлов
linktitle: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

С помощью Aspose.Cells можно открывать файлы, например, для получения данных или использовать шаблон конструктора для ускорения процесса разработки. Aspose.Cells может открывать ряд различных файлов, таких как Microsoft электронные таблицы Excel (XLS, XLSX, XLSM, XLSB), CSV или файлы TabDelimited.

{{% /alert %}} 
## **Открытие файла через путь**
 Разработчики могут открыть файл Excel Microsoft, используя его путь к файлу на локальном компьютере, указав его в[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)конструктор класса. Просто передайте путь в конструкторе как строку. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **Открытие файла с помощью потока**
 Также можно открыть файл Excel в виде потока. Для этого используйте перегруженную версию конструктора, который принимает*Ручей*объект, содержащий файл.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

