---
title: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/net/different-ways-to-open-files/
description: В этой статье объясняется, как открыть файл Excel с помощью Aspose.Cells for .NET API.
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

С Aspose.Cells легко открывать файлы, например, для получения данных, или использовать шаблон дизайнера для ускорения процесса разработки.

{{% /alert %}}

##  **Как открыть файл Excel по пути**

 Разработчики могут открыть файл Excel Microsoft, используя его путь к файлу на локальном компьютере, указав его в поле**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**конструктор класса. Просто передайте путь в конструкторе как *строку*. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **Как открыть файл Excel через поток**

 Открыть файл Excel как поток также просто. Для этого используйте перегруженную версию конструктора, который принимает*Транслировать*объект, содержащий файл.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **Как открыть файл только с данными**

 Чтобы открыть файл только с данными, используйте команду**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** и**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**классы, чтобы установить связанный атрибут и параметры классов для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **Как загрузить только видимые листы**

 Во время загрузки**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**иногда вам могут понадобиться данные только на видимых листах книги. Aspose.Cells позволяет пропускать данные на невидимых листах при загрузке книги. Для этого создайте пользовательскую функцию, которая наследует**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**класс и передать его экземпляр**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Вот реализация*Пользовательская загрузка*класс, указанный в приведенном выше фрагменте.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Исключение будет выдано, если вы попытаетесь открыть файлы Excel или другие форматы файлов (например, PPT/PPTX, DOC/DOCX и т. д.) по номеру Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Есть хорошие шансы, что**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**конструктор может выкинуть*System.OutOfMemoryException* при загрузке больших таблиц. Это исключение предполагает, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому электронную таблицу необходимо загружать при включении настроек памяти.

{{% /alert %}}
