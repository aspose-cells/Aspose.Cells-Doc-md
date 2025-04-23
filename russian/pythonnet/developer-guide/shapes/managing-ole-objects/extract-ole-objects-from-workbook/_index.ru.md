---
title: Извлечение объектов OLE из книги
type: docs
weight: 110
url: /ru/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Иногда необходимо извлечь OLE-объекты из книги. Aspose.Cells для Python via .NET поддерживает извлечение и сохранение этих Ole-объектов.

В этой статье показано, как создать консольное приложение в Visual Studio.Net и извлечь различные объекты OLE из книги всего с несколькими простыми строками кода.

{{% /alert %}}

## **Извлечение объектов OLE из книги**

### **Создание шаблонной книги Excel**

1. Создайте книгу в Microsoft Excel.
1. Добавьте документ Microsoft Word, книгу Excel и документ PDF в качестве объектов OLE на первом листе.

|**Образец документа с объектами OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Затем извлеките объекты OLE и сохраните их на жесткий диск с их соответствующими типами файлов.

### **Извлечение OLE-объектов с помощью библиотеки Aspose.Cells для Python Excel**

Приведенный ниже код фактически выполняет поиск и извлечение объектов OLE. Объекты OLE (файлы DOC, XLS и PDF) сохраняются на диск.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
