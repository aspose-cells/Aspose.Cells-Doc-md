---
title: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

С Aspose.Cells легко открывать файлы, например, для получения данных или использовать шаблон конструктора для ускорения процесса разработки.

{{% /alert %}}

## **Открытие файла через путь**

 Разработчики могут открыть файл Excel Microsoft, используя его путь к файлу на локальном компьютере, указав его в**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)**конструктор класса. Просто передайте путь в конструкторе как*нить*. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Открытие файла через поток**

Также просто открыть файл Excel в виде потока. Для этого используйте перегруженную версию конструктора, который принимает*Транслировать*объект, содержащий файл.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Открытие файла только с данными**

 Чтобы открыть файл только с данными, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** и**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**классы, чтобы установить связанные атрибуты и параметры классов для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Загрузка только видимых листов**

 При загрузке**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)**иногда вам могут понадобиться данные только на видимых листах в книге. Aspose.Cells позволяет пропускать данные в невидимых листах при загрузке книги. Для этого создайте пользовательскую функцию, которая наследует**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**класс и передать его экземпляр в**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Вот реализация этого*CustomnLoad*класс, указанный в приведенном выше фрагменте.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Будет выдано исключение, если вы попытаетесь открыть неродные файлы Excel или файлы других форматов (например, PPT/PPTX, DOC/DOCX и т. д.) по номеру Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Есть хорошие шансы, что**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** конструктор может бросить*System.OutOfMemoryException* при загрузке больших электронных таблиц. Это исключение предполагает, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому электронную таблицу необходимо загрузить при включении настроек памяти.

{{% /alert %}}
