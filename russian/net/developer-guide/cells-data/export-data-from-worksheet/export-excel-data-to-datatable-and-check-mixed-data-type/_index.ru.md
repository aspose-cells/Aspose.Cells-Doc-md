---
title: Экспорт данных из Excel в DataTable и проверка смешанного типа данных
type: docs
weight: 280
url: /ru/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Узнайте, как экспортировать данные из Excel в DataTable и проверить смешанный тип данных через API Aspose.Cells for .NET.
keywords: Экспорт данных из Excel в DataTable и проверка смешанного типа данных, Экспорт данных рабочей книги в DataTable и проверка смешанного типа данных, Экспорт данных в DataTable и проверка смешанного типа данных, Экспорт данных листа в DataTable и проверка смешанного типа данных.
---

## **Возможные сценарии использования**
Если столбец содержит данные различных типов, программа выбросит исключение типа при экспорте данных в DataTable. При экспорте данных таблицы, по умолчанию Aspose.Cells оценивает тип данных для значений на основе самого первого (ячейки) значения в столбце. Так что, если значение является числом, это означает, что тип данных столбца будет числовым, что разумно. Если самое первое значение является числом, но в столбце есть алфанумерические данные или значения, стоит назначить тип данных строки. Чтобы справиться с этим, используйте [перегрузку ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1), которая включает [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) и попробуйте установить логический атрибут [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype) в "true", если в столбце есть числовые и строковые значения, чтобы избежать ошибок.

## **Экспорт данных из Excel в DataTable и проверка смешанного типа данных**

Следующий образец объясняет использование свойства [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) для экспорта данных из Excel в DataTable. Пожалуйста, ознакомьтесь с [образцом Excel-файла](sample.xlsx), его скриншотом и выводом на консоль для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Снимок экрана**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Вывод в консоль**

Ниже приведен вывод отладки консоли вышеприведенного образца кода

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
