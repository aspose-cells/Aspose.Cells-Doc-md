---
title: Анализ сводных кэшированных записей при загрузке файла Excel
type: docs
weight: 70
url: /ru/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Как проанализировать сводные кэшированные записи при загрузке файла Excel с номерами Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Возможные сценарии использования**

Когда вы создаете сводную таблицу, Microsoft Excel берет копию исходных данных и сохраняет ее в сводном кэше. Кэш сводной таблицы хранится в памяти Microsoft Excel. Вы не можете его видеть, но это данные, на которые ссылается сводная таблица, когда вы создаете сводную таблицу, меняете выбор среза или перемещаете строки/столбцы. Это позволяет Microsoft Excel очень быстро реагировать на изменения в сводной таблице, но также может удвоить размер вашего файла. В конце концов, Pivot Cache — это всего лишь дубликат ваших исходных данных, поэтому вполне логично, что размер вашего файла потенциально увеличится вдвое.

Когда вы загружаете файл Excel внутри объекта Workbook, вы можете решить, хотите ли вы также загружать записи сводного кэша или нет, используя[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)свойство. Значение этого свойства по умолчанию — *false**. Если Pivot Cache достаточно большой, это может повысить производительность. Но если вы также хотите загрузить записи сводного кэша, вам следует установить для этого свойства значение *true**.

##  **Анализ сводных кэшированных записей при загрузке файла Excel**

В следующем примере кода объясняется использование[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)свойство. Он загружает[образец файла Excel](61767773.xlsx) при анализе сводных кэшированных записей. Затем он обновляет сводную таблицу и сохраняет ее как[выходной файл Excel](61767774.xlsx).

##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
