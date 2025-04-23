---  
title: Reutilización de Objetos de Estilo
linktitle: Reutilización de Objetos de Estilo  
description: En Aspose.Cells for Node.js via C++, creando y usando objetos de estilo reutilizables, puedes simplificar la gestión de estilos y mejorar la eficiencia del código. Nuestra guía te ayudará a aprovechar las ventajas de los objetos de estilo reutilizables e implementarlos en tu aplicación.  
keywords: Aspose.Cells for Node.js via C++, Reutilización de objetos de estilo, Gestión de estilos, Eficiencia del código, Estilos reutilizables, Desarrollo de aplicaciones, Referencia a API, Código de ejemplo, Descargar, Soporte.  
type: docs  
weight: 3000  
url: /es/nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
Reutilizar objetos de estilo puede ahorrar memoria y hacer que un programa sea más rápido.  
{{% /alert %}}  

Para aplicar un formato a un gran rango de celdas en una hoja de cálculo:

1. Cree un objeto de estilo.
1. Especifique los atributos.
1. Aplique el estilo a las celdas en el rango.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ReusingStyleObjects.js" >}}


{{% alert color="primary" %}}  
Debido a que el enfoque [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) usa mucho menos memoria y es más eficiente, la propiedad Cell.style, que consumía mucha memoria innecesariamente, fue eliminada con la versión Aspose.Cells 7.1.0.  
{{% /alert %}}  

