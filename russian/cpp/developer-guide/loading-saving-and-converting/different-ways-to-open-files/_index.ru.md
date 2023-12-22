---
title: Различные способы открытия файлов
linktitle: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

С помощью Aspose.Cells можно открывать файлы, например, для получения данных, или использовать шаблон дизайнера для ускорения процесса разработки. Aspose.Cells может открывать ряд различных файлов, например электронные таблицы Excel Microsoft (XLS, XLSX, XLSM, XLSB), CSV или TabDelimited файлы.

{{% /alert %}} 
##  **Открытие файла по пути**
 Разработчики могут открыть файл Excel Microsoft, используя его путь к файлу на локальном компьютере, указав его в поле[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)конструктор класса. Просто передайте путь в конструкторе как строку. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **Открытие файла с использованием потока**
 Также можно открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, который принимает*Транслировать*объект, содержащий файл.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

