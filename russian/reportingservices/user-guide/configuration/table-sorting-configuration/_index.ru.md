---
title: Конфигурация сортировки таблицы
type: docs
weight: 90
url: /ru/reportingservices/table-sorting-configuration/
---

Конфигурация включает 5 видов свойств. Это название отчета, название таблицы, значение смещения строк, индекс столбца и тип порядка.

- **name** представляет название отчета и название таблицы. name представляет весь отчет, когда name пуст.
- **value** представляет смещение строки.
- **Index** представляет позицию столбца в таблице.
- **Order** представляет тип порядка сортировки.

Пример конфигурации отсортированной таблицы:

*<TableSorted>
<Report name=”report name” >
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
</Report>
</TableSorted>*
