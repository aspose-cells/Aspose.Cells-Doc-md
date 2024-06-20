---
title: Copiar Datos de Rango con Estilo
type: docs
weight: 610
url: /es/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Copiar solo datos de rango](/cells/es/net/copiar-solo-datos-de-rango/) explicó cómo copiar los datos de un rango de celdas a otro. Específicamente, el proceso aplicó un nuevo conjunto de estilos a las celdas copiadas. Aspose.Cells también puede copiar un rango completo con formato. Este artículo explica cómo.

{{% /alert %}}

Aspose.Cells proporciona una serie de clases y métodos para trabajar con rangos, por ejemplo, [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) y [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Este ejemplo:

1. Crea un libro de trabajo.
1. Rellena un número de celdas en la primera hoja de cálculo con datos.
1. Crea un [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) con atributos de formato especificados.
1. Aplica el estilo al rango de datos.
1. Crea un segundo rango de celdas.
1. Copia datos con el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
