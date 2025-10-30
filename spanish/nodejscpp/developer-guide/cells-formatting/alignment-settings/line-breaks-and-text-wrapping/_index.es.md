---  
title: Saltos de línea y ajuste de texto
linktitle: Saltos de línea y ajuste de texto  
description: Cómo implementar envoltura de texto y ajuste de palabra usando la biblioteca Aspose.Cells en Node.js vía C++. Al usar la biblioteca Aspose.Cells, puede insertar fácilmente texto en celdas y establecer el método de envoltura de texto, como ajuste manual de palabras, ajuste de palabra, etc. Este documento detalla cómo implementar estas funciones y proporciona código de ejemplo para su referencia.  
keywords: Aspose.Cells, saltos de línea, envoltura de texto, diseño de texto Node.js vía C++  
type: docs  
weight: 60  
url: /es/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
Para asegurarse de que el texto en una celda se pueda leer, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, mientras que los saltos de línea explícitos se colocan exactamente donde se desean.  
{{% /alert %}}  

## **Para ajustar texto en una celda**  
Para envolver texto en una celda, use el método [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **Para usar saltos de línea explícitos**  
Puede usar '\n' en JavaScript para insertar saltos de línea explícitos en una celda.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



{{< app/cells/assistant language="nodejs-cpp" >}}
