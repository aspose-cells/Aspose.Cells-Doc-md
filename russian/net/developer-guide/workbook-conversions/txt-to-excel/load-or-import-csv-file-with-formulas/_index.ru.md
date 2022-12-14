---
title: Загрузить или импортировать файл CSV с формулами
type: docs
weight: 350
url: /ru/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 Файл CSV в основном содержит текстовые данные и не содержит никаких формул. Однако иногда бывает так, что файлы CSV также содержат формулы. Такие CSV-файлы следует загружать, установив[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) в качестве**истинный** . Как только это свойство будет установлено**истинный**, Aspose.Cells не будет рассматривать формулу как простой текст. Они будут обработаны как формулы, и механизм расчета формул Aspose.Cells обработает их как обычно.

{{% /alert %}} 

 В следующем коде показано, как можно загружать и импортировать CSV-файл с формулами. Вы можете использовать любой CSV-файл. Для наглядности мы используем[простой CSV-файл](5115034.csv) который содержит эти данные. Как видите, он содержит формулу.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



 Код сначала загружает CSV-файл, а затем снова импортирует его в ячейку D4. Наконец, он сохраняет объект книги в формате XSLX.[выходной файл XLSX](5115052.xlsx) выглядит так. Как видите, ячейки C3 и F4 содержат формулу и ее результат 800.

|![дело:изображение_альтернативный_текст](load-or-import-csv-file-with-formulas_1.png)|
|:- |

