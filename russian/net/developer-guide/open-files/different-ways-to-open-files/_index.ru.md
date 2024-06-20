---
title: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/net/different-ways-to-open-files/
description: Эта статья объясняет, как открыть файл Excel с использованием Aspose.Cells for .NET API.
keywords: C# Открыть файл Excel без Excel, как открыть файл Excel.
---

{{% alert color="primary" %}}

С помощью Aspose.Cells просто открывать файлы, например, чтобы извлечь данные или использовать шаблон дизайнера для ускорения процесса разработки.

{{% /alert %}}

## **Как открыть файл Excel через путь**

Разработчики могут открывать файл Microsoft Excel, используя его путь к файлу на локальном компьютере, указав его в конструкторе класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Просто передайте путь в конструктор как *строку*. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Как открыть файл Excel через поток**

Также просто открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, принимающую объект *Stream*, который содержит файл.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Как открыть файл только с данными**

Чтобы открыть файл только с данными, используйте классы [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) и [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter), чтобы установить соответствующий атрибут и параметры этих классов для загружаемого файла-шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Как загрузить только видимые листы**

При загрузке [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) иногда вам может понадобиться только данные в видимых листах книги. Aspose.Cells позволяет пропустить данные в невидимых листах при загрузке книги. Для этого создайте пользовательскую функцию, которая наследует класс [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) и передайте его экземпляр в свойство [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Вот реализация класса *CustomnLoad*, на которую ссылается вышеуказанный фрагмент.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Если вы попытаетесь открыть файлы формата Excel или другие файловые форматы Office (например, PPT/PPTX, DOC/DOCX и т. д.) с помощью Aspose.Cells, будет сгенерировано исключение.

{{% /alert %}} {{% alert color="primary" %}}

Существует вероятность того, что конструктор [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) может вызвать исключение *System.OutOfMemoryException* при загрузке больших таблиц. Это исключение говорит о том, что доступной памяти недостаточно для полной загрузки таблицы в память, поэтому для загрузки таблицы необходимо включить настройки памяти.

{{% /alert %}}
