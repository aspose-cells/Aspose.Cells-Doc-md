---
title: Copiar solo datos del rango con Golang a través de C++
linktitle: Copiar Solo Datos de Rango
type: docs
weight: 600
url: /es/go-cpp/copy-range-data-only/
description: Aprende cómo copiar solo datos de rango sin formato usando Aspose.Cells con Golang mediante C++.
---

{{% alert color="primary" %}}

A veces, necesitas copiar datos de un rango de celdas a otro, copiando solo los datos, no el formato. Aspose.Cells ofrece esta función.

Este artículo proporciona un código de ejemplo que utiliza Aspose.Cells para copiar un rango de datos.

{{% /alert %}}

Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Crear un [**Range**](https://reference.aspose.com/cells/go-cpp/range/).
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) con atributos de formato especificados.
1. Aplica el formato de estilo al rango.
1. Crear otro rango de celdas.
1. Copiar datos del primer rango a este segundo rango.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataOnly.go" >}}
