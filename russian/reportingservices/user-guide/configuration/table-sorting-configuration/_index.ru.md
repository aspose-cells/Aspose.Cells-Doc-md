---
title: Конфигурация сортировки таблиц
type: docs
weight: 90
url: /ru/reportingservices/table-sorting-configuration/
---
Конфигурация включает 5 видов свойств. К ним относятся имя отчета, имя таблицы, значение смещения строки, индекс столбца и тип заказа.

- **имя** представляет имя отчета и имя таблицы. имя представляет весь отчет, когда имя не указано.
- **ценность** представляет смещение строки.
- **Индекс** представляет позицию столбца в таблице.
- **Заказ** представляет тип порядка сортировки.

Пример конфигурации TableSorted:

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
