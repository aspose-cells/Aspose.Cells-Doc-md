---
title: Загрузить или импортировать CSV файл с формулами с помощью C++
linktitle: Загрузка или импорт файла CSV с формулами
type: docs
weight: 350
url: /ru/go-cpp/load-or-import-csv-file-with-formulas/
description: Загружать или импортировать CSV файл, содержащий формулы, с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}} 

CSV-файлы обычно содержат только текстовые данные и не включают формулы. Однако бывают ситуации, когда CSV-файлы могут содержать формулы. Такие CSV-файлы следует загружать, установив [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) в значение **true**. После установки этого свойства в **true**, Aspose.Cells не будет рассматривать формулы как обычный текст. Они будут обрабатываться как формулы, и движок вычислений формул Aspose.Cells будет их обрабатывать как обычно.

{{% /alert %}} 

Следующий пример показывает, как можно загрузить и импортировать CSV-файл с формулами. Можно использовать любой CSV. В примере используется [простой CSV-файл](5115034.csv), содержащий эти данные. Как видно, он содержит формулу.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
Сначала код загружает CSV-файл, затем импортирует его заново в ячейку D4. В конце он сохраняет рабочую книгу в формате XLSX. [Выходной XLSX-файл](5115052.xlsx) выглядит так. Как видно, ячейки C3 и F4 содержат формулы, а их результат — 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
