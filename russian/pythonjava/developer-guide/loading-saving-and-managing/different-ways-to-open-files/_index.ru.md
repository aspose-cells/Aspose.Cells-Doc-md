---
title: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

С помощью Aspose.Cells просто открывать файлы, например, чтобы извлечь данные или использовать шаблон дизайнера для ускорения процесса разработки.

{{% /alert %}}

## **Открытие файла по пути**

Разработчики могут открывать файл Microsoft Excel, используя его путь к файлу на локальном компьютере, указав его в конструкторе класса [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Просто передайте путь в конструктор как *строку*. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Открытие файла через поток**

Также легко открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, которая принимает объект *BufferStream*, содержащий файл.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Открытие файла только с данными**

Чтобы открыть файл только с данными, используйте классы [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) и [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter), чтобы установить соответствующий атрибут и параметры этих классов для загружаемого файла-шаблона.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Если вы попытаетесь открыть файлы формата Excel или другие файловые форматы Office (например, PPT/PPTX, DOC/DOCX и т. д.) с помощью Aspose.Cells, будет сгенерировано исключение.

{{% /alert %}} {{% alert color="primary" %}}

Существует вероятность того, что конструктор [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) может вызвать исключение *System.OutOfMemoryException* при загрузке больших таблиц. Это исключение говорит о том, что доступной памяти недостаточно для полной загрузки таблицы в память, поэтому для загрузки таблицы необходимо включить настройки памяти.

{{% /alert %}}
