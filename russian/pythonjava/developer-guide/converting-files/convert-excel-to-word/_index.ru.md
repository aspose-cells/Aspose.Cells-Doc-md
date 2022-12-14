---
title: Преобразовать эксель в ворд
type: docs
weight: 300
url: /ru/python-java/convert-excel-to-word/
description: Преобразуйте файл Excel в слово, используя Python.
keywords: Exporting Workbook to word without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells для Python через Java поддерживает преобразование файлов Excel (.xls, xlsx, .xlsb,xlsm), CSV и OpenOffice (.ods) в файл Word.

{{% /alert %}}

## **Преобразование книги Excel в Word**

 Не нужно задаваться вопросом, как преобразовать книгу Excel в Word, потому что Aspose.Cells для Python через библиотеку Java имеет лучшее решение. Aspose.Cells для Python через Java API обеспечивает поддержку преобразования электронных таблиц в формат Word. Чтобы экспортировать книгу в Word, передайте[**СохранитьФормат.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) в качестве второго параметра[**Книга.сохранить**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ) метод. Вы также можете использовать[**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions) класс, чтобы указать дополнительные параметры для экспорта рабочего листа в файл .docx.

 В следующем примере кода демонстрируется экспорт книги Excel в Word. Пожалуйста, посмотрите код для преобразования[исходный файл](sample.xlsx) в файл Word, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


