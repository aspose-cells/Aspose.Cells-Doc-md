---
title: Различные способы открытия файлов
type: docs
weight: 10
url: /ru/python-net/different-ways-to-open-files/
description: В этой статье объясняется, как открыть файл Excel с помощью API Aspose.Cells для Python via .NET.
keywords: Python Открыть файл Excel без Excel, как открыть файл Excel.
---

{{% alert color="primary" %}}

С Aspose.Cells для Python via .NET открывать файлы просто, например, получать данные или использовать дизайн-шаблон для ускорения процесса разработки.

{{% /alert %}}

## **Как открыть файл Excel через путь**

Разработчики могут открыть файл Microsoft Excel, указав путь к нему на локальном компьютере через конструктор класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Просто передайте путь в качестве строки. Aspose.Cells для Python via .NET автоматически определит тип формата файла.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Как открыть файл Excel через поток**

Также просто открыть файл Excel как поток. Для этого используйте перегруженную версию конструктора, принимающую объект *Stream*, который содержит файл.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Как открыть файл только с данными**

Чтобы открыть файл только с данными, используйте классы [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) и [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter), чтобы установить соответствующий атрибут и параметры этих классов для загружаемого файла-шаблона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

