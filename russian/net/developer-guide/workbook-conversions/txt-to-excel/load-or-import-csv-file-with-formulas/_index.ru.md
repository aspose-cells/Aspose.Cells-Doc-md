---
title: Загрузка или импорт файла CSV с формулами
type: docs
weight: 350
url: /ru/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV-файл в основном содержит текстовые данные и не содержит формул. Однако иногда бывает так, что CSV-файлы также содержат формулы. Такие CSV-файлы должны быть загружены с установкой [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) в **true**. Как только это свойство будет установлено в **true**, Aspose.Cells не будет рассматривать формулу как простой текст. Они будут рассматриваться как формула, и расчетная машина формул Aspose.Cells будет обрабатывать их как обычно.

{{% /alert %}} 

Приведенный ниже код показывает, как можно загружать и импортировать CSV-файл с формулами. Можно использовать любой CSV-файл. Для иллюстрации мы используем [простой CSV-файл](5115034.csv), который содержит эти данные. Как видите, он содержит формулу.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Код сначала загружает CSV-файл, затем снова импортирует его в ячейку D4. Наконец, он сохраняет объект рабочей книги в формате XSLX. [Выходной файл XLSX](5115052.xlsx) выглядит вот так. Как видите, ячейка C3 и F4 содержат формулу и ее результат 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="csharp" >}}
