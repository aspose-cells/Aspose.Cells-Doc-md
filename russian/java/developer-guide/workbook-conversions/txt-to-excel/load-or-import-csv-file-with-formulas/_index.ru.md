---
title: Загрузите или импортируйте файл CSV с формулами
type: docs
weight: 500
url: /ru/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV в основном содержит текстовые данные и не содержит никаких формул. Однако иногда бывает так, что файлы CSV также содержат формулы. Такие файлы CSV следует загружать, установив[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) к**истинный** . Как только это свойство будет установлено в**истинный**, Aspose.Cells не будет рассматривать формулу как простой текст. Они будут обработаны как формулы, и механизм расчета формул Aspose.Cells обработает их как обычно.

{{% /alert %}} 
## **Загрузите или импортируйте файл CSV с формулами**
 В следующем коде показано, как можно загружать и импортировать файл CSV с формулами. Вы можете использовать любой файл CSV. Для наглядности мы используем[простой CSV-файл](5472505.csv) который содержит эти данные. Как видите, он содержит формулу.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Код сначала загружает файл CSV, а затем снова импортирует его в ячейку D4. Наконец, он сохраняет объект книги в формате XSLX.[выходной файл XLSX](5472503.xlsx) выглядит так. Как видите, ячейки C3 и F4 содержат формулу и ее результат 800.

![дело:изображение_альтернативный_текст](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
