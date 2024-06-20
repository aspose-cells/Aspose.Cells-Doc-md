---
title: Configuración de ordenación de tabla
type: docs
weight: 90
url: /es/reportingservices/table-sorting-configuration/
---

La configuración incluye 5 tipos de propiedades. Estas incluyen el nombre del informe, el nombre de la tabla, el valor de desplazamiento de fila, el índice de columna y el tipo de orden.

- **name** representa el nombre del informe y el nombre de la tabla. name representa el informe completo cuando name está en blanco.
- **value** representa el desplazamiento de fila.
- **Index** representa la posición de la columna en la tabla.
- **Order** representa el tipo de orden de clasificación.

Ejemplo de configuración de tabla ordenada:

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
