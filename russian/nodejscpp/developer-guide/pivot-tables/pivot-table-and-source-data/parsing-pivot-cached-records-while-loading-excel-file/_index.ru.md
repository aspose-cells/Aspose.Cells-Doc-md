---
title: Анализ кэшированных записей сводной таблицы при загрузке файла Excel
type: docs
weight: 70
url: /ru/nodejs-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Возможные сценарии использования**

При создании сводной таблицы Microsoft Excel делает копию исходных данных и хранит их в кэше сводной таблицы. Кэш сводной таблицы хранится в памяти Microsoft Excel. Вы его не видите, но это данные, на которые ссылается сводная таблица при построении или изменении выбора среза или перемещении строк/столбцов. Это позволяет Microsoft Excel очень быстро реагировать на изменения сводной таблицы, но также может удвоить размер вашего файла. В конце концов, кэш сводной таблицы просто дублирует ваши исходные данные, поэтому логично, что размер вашего файла может увеличиться вдвое.

При загрузке файла Excel в объект Workbook можно решить, хотите ли вы также загружать записи из кэша сводной таблицы или нет, используя свойство [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-). Значение по умолчанию этого свойства - **false**. Если кэш сводной таблицы довольно большой, это может улучшить производительность. Но если вы также хотите загрузить записи кэша сводной таблицы, вы должны установить это свойство как **true**.

## **Анализ кэшированных записей сводной таблицы при загрузке файла Excel**

Приведенный ниже образец кода объясняет использование свойства [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-). Он загружает [образец файла Excel](61767773.xlsx), разбирая кэшированные записи сводной таблицы. Затем он обновляет сводную таблицу и сохраняет ее как [выходной файл Excel](61767774.xlsx).

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
