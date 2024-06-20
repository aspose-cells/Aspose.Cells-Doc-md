---
title: Utilizar el Pincel de Formato
type: docs
weight: 80
url: /es/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: Este artículo presenta el pincel de formato en GridDesktop.
---

{{% alert color="primary" %}} 

El pincel de formato es una característica de MS Excel que se ha adaptado en Aspose.Cells.GridDesktop. Es una característica muy útil. Para aquellas personas que aún no han utilizado esta característica, el pincel de formato les permite aplicar los ajustes de formato de cualquier celda enfocada a otra celda. La implementación de esta función es muy simple. En este tema, también cubriremos eso.

{{% /alert %}} 
## **Usar el Pincel de Formato**
La función de **Pincel de Formato** requiere que los usuarios seleccionen una celda cuyos ajustes de formato deseen aplicar en otras celdas y luego llamar al método **StartFormatPainter** en **GridDesktop**. Hay dos modos de pincel de formato de la siguiente manera:

- **Usar el pincel de formato una vez**
- **Usar el Pincel de Formato Siempre**
### **Usar el Pincel de Formato una vez**
Si los desarrolladores desean usar la función del pincel de formato solo una vez para aplicar los ajustes de formato de una celda enfocada a una sola celda, pueden hacerlo llamando al método **StartFormatPainter** y pasando un valor **falso**. Este valor **falso** prohibirá que el pincel de formato pinte para siempre.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Usar siempre el formato de pintor**
Usar siempre el formato de pintor es una característica útil cuando necesitamos aplicar la configuración de formato en más de una celda. Los desarrolladores pueden lograr esta característica simplemente llamando al método **StartFormatPainter** y pasando un valor **true**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


Este tipo de formato de pintor sigue pintando para siempre a menos que lo detengamos. Entonces, para detener el formato de pintor de pintar siempre, simplemente podemos llamar al método **EndFormatPainter** de **GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
