---
title: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

С Aspose.Cells легко открывать файлы, например, для получения данных или использовать шаблон конструктора для ускорения процесса разработки.

{{% /alert %}}

## **Открытие файла через путь**

 Разработчики могут открыть файл Excel Microsoft, используя его путь к файлу на локальном компьютере, указав его в**[Рабочая книга] (https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**конструктор класса. Просто передайте путь в конструкторе как*нить*. Aspose.Cells автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Открытие файла через поток**

Также просто открыть файл Excel в виде потока. Для этого используйте перегруженную версию конструктора, который принимает*BufferStream*объект, содержащий файл.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Открытие файла только с данными**

 Чтобы открыть файл только с данными, используйте**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** и**[Загрузить фильтр] (https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**классы, чтобы установить связанные атрибуты и параметры классов для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Будет выдано исключение, если вы попытаетесь открыть неродные файлы Excel или файлы других форматов (например, PPT/PPTX, DOC/DOCX и т. д.) по номеру Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Есть хорошие шансы, что**[Рабочая книга] (https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** конструктор может бросить*System.OutOfMemoryException* при загрузке больших электронных таблиц. Это исключение предполагает, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому электронную таблицу необходимо загрузить при включении настроек памяти.

{{% /alert %}}
