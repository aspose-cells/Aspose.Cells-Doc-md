﻿---
title: Извлечение объектов OLE из книги
type: docs
weight: 110
url: /ru/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

Иногда вам нужно извлечь объекты OLE из книги. Aspose.Cells поддерживает извлечение и сохранение этих объектов Ole.

В этой статье показано, как создать консольное приложение в Visual Studio.Net и извлечь различные объекты OLE из книги с помощью нескольких простых строк кода.

{{% /alert %}}

## **Извлечение объектов OLE из книги**

### **Создание шаблона рабочей книги**

1. Создал книгу в Microsoft Excel.
1. Добавьте документ Word Microsoft, книгу Excel и документ PDF в качестве объектов OLE на первый рабочий лист.

|**Шаблон документа с объектами OLE (OleFile.xls)**|
|:- |
|![дело:изображение_альтернативный_текст](extract-ole-objects-from-workbook_1.png)|

Затем извлеките объекты OLE и сохраните их на жестком диске с соответствующими типами файлов.

### **Загрузите и установите Aspose.Cells**

1. [Скачать Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Установите его на свой компьютер разработки.

Все компоненты Aspose после установки работают в ознакомительном режиме. Режим оценки не имеет ограничения по времени и только вставляет водяные знаки в создаваемые документы.

### **Создать проект**

Начинать**Visual Studio.Net** и создайте новое консольное приложение. В этом примере показано консольное приложение C#, но вы также можете использовать VB.NET.

1. Добавить ссылки
 1. Добавьте в проект ссылку на компонент Aspose.Cells, например, добавьте ссылку на ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Извлечение OLE-объектов**

Приведенный ниже код выполняет фактическую работу по поиску и извлечению объектов OLE. Объекты OLE (файлы DOC, XLS и PDF) сохраняются на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}