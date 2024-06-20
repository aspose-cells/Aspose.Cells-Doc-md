---
title: Загрузка или импорт файла CSV с формулами
type: docs
weight: 350
url: /ru/python-net/load-or-import-csv-file-with-formulas/
description: Загрузите или импортируйте CSV файл с формулами с помощью Aspose.Cells для Python via .NET API.
keywords: Загрузите или импортируйте CSV файл с формулами в Python, Преобразуйте CSV с формулами в Excel в Python via NET, Преобразуйте CSV с формулами в xlsx в Python, Загрузите CSV с формулами в файл Excel.
---

{{% alert color="primary" %}} 

Файл CSV в основном содержит текстовые данные и не содержит формул. Однако иногда бывает, что в файлах CSV также содержатся формулы. Такие файлы CSV должны быть загружены путем установки [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) в значение **true**. Как только это свойство будет установлено в значение **true**, Aspose.Cells не будет рассматривать формулу как простой текст. Они будут рассматриваться как формула, и движок расчета формул Aspose.Cells будет обрабатывать их как обычно.

{{% /alert %}} 

Приведенный ниже код показывает, как можно загружать и импортировать CSV-файл с формулами. Можно использовать любой CSV-файл. Для иллюстрации мы используем [простой CSV-файл](5115034.csv), который содержит эти данные. Как видите, он содержит формулу.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



Код сначала загружает CSV-файл, затем снова импортирует его в ячейку D4. Наконец, он сохраняет объект рабочей книги в формате XSLX. [Выходной файл XLSX](5115052.xlsx) выглядит вот так. Как видите, ячейка C3 и F4 содержат формулу и ее результат 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

