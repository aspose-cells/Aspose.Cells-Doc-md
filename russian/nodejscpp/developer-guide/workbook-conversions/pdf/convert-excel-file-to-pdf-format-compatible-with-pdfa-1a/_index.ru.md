---  
title: Конвертация Excel файла в формат PDF, совместимый с PDF/A 1a с помощью Node.js через C++  
linktitle: Конвертация Excel файла в формат PDF, совместимый с PDF/A 1a  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Узнайте, как преобразовать файлы Excel в PDF, совместимые с PDF/A, с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

PDF/A — это уникальный вариант PDF, предназначенный для долгосрочного хранения документов. PDF/A — это стандартизированная ISO-версия Portable Document Format (PDF), которая является архивным форматом PDF, встроенным всеми используемыми в документе шрифтами внутри файла PDF. PDF/A отличается от PDF запретом на некоторые функции, такие как подключение шрифтов (в отличие от их встраивания) и шифрование. Aspose.Cells for Node.js via C++ позволяет сохранять файлы Excel в архивных PDF/A файлы (поддерживаются PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u). Эта тема описывает, как сохранить рабочую книгу Excel в PDF-файл, совместимый с PDF/A (PDF/A-1a).  

## **Преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a**  

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) для установки различных атрибутов для преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) дает контроль над настройками печати, шрифтов, безопасности и сжатия для создаваемого PDF. Самым важным свойством является [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), позволяющее сохранять файлы Excel в архивные PDF-файлы.  

Следующий пример объясняет, как преобразовать файл Excel в PDF-совместимый с PDF/A-1a. См. его [выходной PDF](outputCompliancePdfA1a.pdf) и скриншот для справки.  

## **Снимок экрана**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
