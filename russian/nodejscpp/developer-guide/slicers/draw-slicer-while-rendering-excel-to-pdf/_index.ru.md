---
title: Нарисуйте фильтр при рендеринге Excel в PDF
type: docs
weight: 60
url: /ru/nodejs-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **Нарисуйте фильтр при рендеринге Excel в PDF**
Если у вас есть файл Excel с примененным срезом, и вы хотите экспортировать его в PDF с сохранением настроек среза, Aspose.Cells for Node.js via C++ теперь поддерживает это по умолчанию. Просто экспортируйте файл Excel с срезом в PDF, и сгенерированный PDF покажет применяемый срез.

Следующий образец кода загружает [образец файла Excel](94044165.xlsx), содержащий существующую срезку. Затем он сохраняет книгу как [выходной файл PDF](94044166.pdf). На следующем скриншоте сравниваются исходный файл Excel и сгенерированный файл PDF.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Образец кода**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-ExportSlicerToPDF-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
