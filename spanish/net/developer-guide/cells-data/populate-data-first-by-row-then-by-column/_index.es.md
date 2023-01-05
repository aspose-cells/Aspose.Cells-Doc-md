---
title: Complete los datos primero por fila y luego por columna
type: docs
weight: 1000
url: /es/net/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}} 

Llenar una hoja de cálculo con datos primero por fila y luego por columna mejora el rendimiento general.

{{% /alert %}} 

Poner datos en la secuencia A1, B1, A2, B2 es más rápido que A1, A2, B1, B2. Si hay muchas celdas en una hoja de trabajo y sigues la segunda secuencia, es decir, estás llenando los datos fila por fila, este consejo puede hacer que el programa sea mucho más rápido.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-PopulateDataEfficiently-PopulateDataFirstByRowThenColumns.cs" >}}
