---
title: Экспорт данных Excel в DataTable и проверка смешанного типа данных
type: docs
weight: 280
url: /ru/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Узнайте, как экспортировать данные Excel в DataTable и проверить смешанный тип данных с помощью Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Возможные сценарии использования**
 Если столбец содержит данные разных типов, программа выдаст исключение типа при экспорте данных в DataTable. При экспорте таблицы данных по умолчанию Aspose.Cells оценивает тип данных для значений на основе самого первого значения (ячейки) в столбце. Итак, если значением является число, это означает, что тип данных столбца будет числовым, что вполне разумно. Если самое первое значение — число, но в столбце есть буквенно-цифровые данные или значения, следует назначить строковый тип данных. Чтобы справиться с этим, используйте[Перегрузка ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) который включает в себя[Экспортдататаблеоптионс](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) и попробуй установить[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Логический атрибут имеет значение «истина», если столбец имеет как числовые, так и строковые значения, чтобы избежать ошибки.

##  **Экспорт данных Excel в DataTable и проверка смешанного типа данных**

 В следующем примере объясняется использование[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) свойство для экспорта данных Excel в таблицу данных. Пожалуйста, ознакомьтесь с[образец файла Excel](sample.xlsx), его снимок экрана и вывод консоли для справки.

###  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Скриншот**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Консольный вывод**

Ниже приведен вывод консольной отладки приведенного выше примера кода.

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
