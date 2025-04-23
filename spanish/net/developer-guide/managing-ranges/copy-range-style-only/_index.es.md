---
title: Copiar solo estilo de rango
type: docs
weight: 620
url: /es/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[Copiar solo datos de rango](/cells/es/net/copiar-solo-datos-de-rango/) y [Copiar datos de rango con estilo](/cells/es/net/copiar-datos-de-rango-con-estilo/) explicaron cómo copiar datos de un rango a otro por sí solos o con formato completo. También es posible copiar solo el formato. Este artículo muestra cómo.

{{% /alert %}} 

Este ejemplo crea un libro de trabajo, lo llena con datos y copia solo el estilo de un rango.

1. Crear un rango.
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) con atributos de formato especificados.
1. Aplica el formato de estilo al rango.
1. Crear un segundo rango de celdas.
1. Copiar el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
