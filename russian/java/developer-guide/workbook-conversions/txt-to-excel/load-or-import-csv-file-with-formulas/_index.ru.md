---
title: Загрузка или импорт файла CSV с формулами
type: docs
weight: 500
url: /ru/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Файл CSV в основном содержит текстовые данные и не содержат никаких формул. Однако иногда бывает, что файлы CSV также содержат формулы. Такие файлы CSV должны быть загружены, установив [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) в **true**. Как только это свойство будет установлено в **true**, Aspose.Cells не будет рассматривать формулу как простой текст. Они будут рассматриваться как формулы, и движок расчета формул Aspose.Cells будет обрабатывать их как обычно.

{{% /alert %}} 
## **Загрузить или импортировать файл CSV с формулами**
Следующий код иллюстрирует, как вы можете загрузить и импортировать файл CSV с формулами. Вы можете использовать любой файл CSV. Для иллюстрации мы используем [простой CSV файл](5472505.csv), который содержит эти данные. Как вы видите, он содержит формулу.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Код сначала загружает файл CSV, затем импортирует его снова в ячейку D4. Наконец, он сохраняет объект книги в формате XSLX. [Файл XLSX вывода](5472503.xlsx) выглядит так. Как вы видите, ячейка C3 и F4 содержат формулу и ее результат 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
