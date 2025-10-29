---
title: Различные способы открытия файлов
linktitle: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

С помощью Aspose.Cells можно открывать файлы, например для извлечения данных или использования шаблона дизайнера для ускорения процесса разработки. Aspose.Cells может открывать ряд различных файлов, таких как электронные таблицы Microsoft Excel (XLS, XLSX, XLSM, XLSB), CSV или файлы с разделителями табуляции.

{{% /alert %}} 
## **Открытие файла по пути**
Разработчики могут открыть файл Microsoft Excel, используя путь к файлу на локальном компьютере, указав его в конструкторе класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) в качестве параметра. Просто передайте путь в конструктор как строку. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Открытие файла с использованием потока**
Также возможно открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, принимающую объект *Stream*, содержащий файл.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
