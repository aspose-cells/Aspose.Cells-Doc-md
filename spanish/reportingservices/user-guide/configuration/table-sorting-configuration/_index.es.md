---
title: Configuración de clasificación de tablas
type: docs
weight: 90
url: /es/reportingservices/table-sorting-configuration/
---
La configuración incluye 5 tipos de propiedades. Estos incluyen el nombre del informe, el nombre de la tabla, el valor de desplazamiento de la fila, el índice de la columna y el tipo de orden.

- **nombre** representa el nombre del informe y el nombre de la tabla. El nombre representa el informe completo cuando el nombre está en blanco.
- **valor** representa el desplazamiento de fila.
- **Índice** representa la posición de la columna en la tabla.
- **Ordenar** representa el tipo de orden de clasificación.

Ejemplo de configuración ordenada por tabla:

*<ordenado por tabla>
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
