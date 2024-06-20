---
title: Reutilización de Objetos de Estilo
description: En Aspose.Cells for .NET, mediante la creación y el uso de objetos de estilo reutilizables, puede simplificar la gestión de estilos y mejorar la eficiencia del código. Nuestra guía le ayudará a aprovechar las ventajas de los objetos de estilo reutilizables e implementarlos en su aplicación.
keywords: Aspose.Cells for .NET, Reutilización de objetos de estilo, Gestión de estilos, Eficiencia del código, Estilos reutilizables, Desarrollo de aplicaciones, Referencia de la API, Código de ejemplo, Descarga, Soporte.
type: docs
weight: 3000
url: /es/net/reusing-style-objects/
---

{{% alert color="primary" %}}

Reutilizar objetos de estilo puede ahorrar memoria y hacer que un programa sea más rápido.

{{% /alert %}}

Para aplicar un formato a un gran rango de celdas en una hoja de cálculo:

1. Cree un objeto de estilo.
1. Especifique los atributos.
1. Aplique el estilo a las celdas en el rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

Debido a que el enfoque [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) utiliza mucha menos memoria y es eficiente, la propiedad Cell.Style más antigua que consumía mucha memoria innecesaria, se eliminó con el lanzamiento de Aspose.Cells 7.1.0.

{{% /alert %}}
