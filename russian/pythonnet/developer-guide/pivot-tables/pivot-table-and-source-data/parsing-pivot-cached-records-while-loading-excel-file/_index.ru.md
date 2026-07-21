---
title: Анализ кэшированных записей сводной таблицы при загрузке файла Excel
type: docs
weight: 70
url: /ru/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Как разобрать кешированные записи сводной таблицы при загрузке файла Excel с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Как разобрать кешированные записи сводной таблицы при загрузке файла Excel с использованием библиотеки Aspose.Cells для Python Excel.
---

## **Возможные сценарии использования**

При создании сводной таблицы Microsoft Excel делает копию исходных данных и хранит их в кэше сводной таблицы. Кэш сводной таблицы хранится в памяти Microsoft Excel. Вы его не видите, но это данные, на которые ссылается сводная таблица при построении или изменении выбора среза или перемещении строк/столбцов. Это позволяет Microsoft Excel очень быстро реагировать на изменения сводной таблицы, но также может удвоить размер вашего файла. В конце концов, кэш сводной таблицы просто дублирует ваши исходные данные, поэтому логично, что размер вашего файла может увеличиться вдвое.

При загрузке файла Excel в объект Workbook можно решить, хотите ли вы также загружать записи из кэша сводной таблицы или нет, используя свойство [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). Значение по умолчанию этого свойства - **false**. Если кэш сводной таблицы довольно большой, это может улучшить производительность. Но если вы также хотите загрузить записи кэша сводной таблицы, вы должны установить это свойство как **true**.

## **Как разобрать кешированные записи сводной таблицы при загрузке файла Excel**

Приведенный ниже образец кода объясняет использование свойства [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). Он загружает [образец файла Excel](61767773.xlsx), разбирая кэшированные записи сводной таблицы. Затем он обновляет сводную таблицу и сохраняет ее как [выходной файл Excel](61767774.xlsx).

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
