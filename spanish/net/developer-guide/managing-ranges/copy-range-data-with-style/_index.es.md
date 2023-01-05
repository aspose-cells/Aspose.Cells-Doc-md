---
title: Copiar datos de rango con estilo
type: docs
weight: 610
url: /es/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Copiar solo datos de rango](/cells/es/net/copy-range-data-only/) explicó cómo copiar los datos de un rango de celdas a otro rango. Específicamente, el proceso aplicó un nuevo conjunto de estilos a las celdas copiadas. Aspose.Cells también puede copiar un rango completo con formato. Este artículo explica cómo.

{{% /alert %}}

Aspose.Cells proporciona una gama de clases y métodos para trabajar con rangos, por ejemplo,[**CrearRango()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) y[**AplicarEstilo()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Este ejemplo:

1. Crea un libro de trabajo.
1. Llena un número de celdas en la primera hoja de cálculo con datos.
1.  Crea un[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Crea un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto con atributos de formato especificados.
1. Aplica el estilo al rango de datos.
1. Crea un segundo rango de celdas.
1. Copia datos con el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
