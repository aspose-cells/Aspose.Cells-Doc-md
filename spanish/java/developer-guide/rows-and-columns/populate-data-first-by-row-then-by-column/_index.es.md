---
title: Primero llenar datos por fila y luego por columna
type: docs
weight: 10
url: /es/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

Llenar una hoja de cálculo con datos primero por fila y luego por columna mejora el rendimiento general.

{{% /alert %}}

## Llenar datos primero por fila y luego por columna

Poner datos en la secuencia A1, B1, A2, B2 es más rápido que A1, A2, B1, B2. Si hay muchas celdas en una hoja de cálculo y sigues la segunda secuencia, es decir, estás llenando los datos fila por fila, este consejo puede hacer que el programa sea mucho más rápido.

## Código Java para llenar datos primero por fila y luego por columna

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
