---
title: Загрузите или импортируйте файл CSV с формулами.
type: docs
weight: 350
url: /ru/python-net/load-or-import-csv-file-with-formulas/
description: Загрузите или импортируйте файл CSV с формулами, используя Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 Файл CSV в основном содержит текстовые данные и не содержит формул. Однако иногда случается, что файлы CSV содержат еще и формулы. Такие файлы CSV следует загружать, установив[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) как *правда**. Как только для этого свойства будет установлено значение *true**, Aspose.Cells не будет рассматривать формулу как простой текст. Они будут рассматриваться как формулы, и механизм расчета формул Aspose.Cells будет обрабатывать их как обычно.

{{% /alert %}} 

 Следующий код показывает, как можно загрузить и импортировать файл CSV с формулами. Вы можете использовать любой файл CSV. В целях иллюстрации мы используем[простой CSV-файл](5115034.csv)который содержит эти данные. Как видите, он содержит формулу.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 Код сначала загружает файл CSV, а затем снова импортирует его в ячейку D4. Наконец, объект книги сохраняется в формате XSLX.[выходной файл XLSX](5115052.xlsx) выглядит вот так. Как вы видите, ячейки C3 и F4 содержат формулу и ее результат 800.

|![задача: image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

