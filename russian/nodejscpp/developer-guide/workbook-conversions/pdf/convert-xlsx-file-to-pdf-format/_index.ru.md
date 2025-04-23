---
title: Преобразование XLSX файла в PDF с помощью Node.js через C++
linktitle: Преобразовать файл XLSX в формат PDF
type: docs
weight: 30
url: /ru/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Этот руководство объясняет, как конвертировать файл Excel (XLSX) в формат PDF с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) представляет документы независимо от используемого программного обеспечения, оборудования и операционной системы для создания этих документов. Файл PDF может быть документами с любой комбинацией текста, графики и изображений в устройство- и разрешение-независимом формате. Файлы PDF часто сжимаются, поэтому они занимают меньше места, чем оригинальный файл.

Иногда вам нужно преобразовать файл Microsoft Excel в PDF. Для этого необходим быстрое, безопасное, точное и надежное решение, которое позволяет рассылать PDF-документы по всему миру. Существует множество инструментов для преобразования, которые могут выполнить эту задачу. Но важно убедиться, что макет исходного документа Excel сохраняется в итоговом файле PDF. Изображения, графики, фигуры, форматирование данных, шрифты, атрибуты, цвета, настройки страницы, ориентация текста, границы, графики и др. должны отображаться точно и корректно. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) обеспечивает высокоточное преобразование.

Этот документ предназначен для предоставления всестороннего понимания того, как документ Microsoft Excel (с изображениями, графиками, форматированием и т.д.) может быть преобразован в PDF. Для этого показано, как создать простое консольное приложение в Node.js, которое преобразует файл Excel в PDF с помощью API Aspose.Cells. Преобразование выполняется с высокой точностью и точностью.

{{% /alert %}}

## **Преобразование Excel в PDF**

Этот пример использует файл Excel (SampleInput.xlsx) в качестве шаблона. Рабочая книга содержит листы с графиками и изображениями. Каждый лист содержит разные типы форматирования с использованием шрифтов, атрибутов, цветов, эффектов затенения и границ. На первом листе есть столбчатая диаграмма, а на последнем — изображение.

### **Файл шаблона Excel**

Шаблонный файл содержит три листа, включающие графики и изображения как медиа. Первый лист содержит графики, а последний — изображение, как показано на скриншотах ниже.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Первый лист **(Прогноз продаж)**|Второй лист **(Отчет о продажах)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Третий лист **(Ввод данных)**|Последний лист **(Изображение)**|

### **Процесс конвертации**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Если таблица содержит формулы, лучше всего вызвать метод [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в PDF. Это обеспечивает пересчет зависимых от формул значений и правильное отображение в PDF.

{{% /alert %}}

### **Результат**

После выполнения вышеуказанного кода создается PDF-файл в папке Files в вашем каталоге приложения.
Следующие скриншоты показывают страницы PDF. Обратите внимание, что в выходном PDF-файле также сохранены заголовки и нижние колонтитулы.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Первый лист **(Прогноз продаж)**|Второй лист **(Отчет о продажах)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Третий лист **(Ввод данных)**|Последний лист **(Изображение)**|
