---
title: Uso de Format Painter
type: docs
weight: 80
url: /es/net/using-format-painter/
---
{{% alert color="primary" %}} 

El pintor de formato es la función de MS Excel que se ha adaptado en Aspose.Cells.GridDesktop. Es una característica muy agradable. Para aquellas personas que aún no han utilizado esta función, el pintor de formato permite a los usuarios aplicar la configuración de formato de cualquier celda enfocada a otra celda. La implementación de esta característica es muy simple. En este tema, también lo cubriremos.

{{% /alert %}} 
## **Uso de Format Painter**
 La característica de**Copiar formato** requiere que los usuarios seleccionen una celda cuya configuración de formato desea aplicar en otras celdas y luego llamar**Pintar formato de inicio** método**GridEscritorio**. Hay dos modos de pintor de formato de la siguiente manera:

- **Usando Format Painter una vez**
- **Usar Format Painter siempre**
### **Usando Format Painter una vez**
 Si los desarrolladores quieren usar la función de pintor de formato solo una vez para aplicar la configuración de formato de una celda enfocada a una sola celda, pueden hacerlo llamando**Pintar formato de inicio** método y pasando un**falso** valor para ello. Este**falso** El valor prohibirá que Format Painter pinte para siempre.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Usar Format Painter siempre**
Usar Format Painter siempre es una característica útil cuando necesitamos aplicar la configuración de formato en más de una celda. Los desarrolladores pueden lograr esta función simplemente llamando**Pintar formato de inicio** método y pasando un**verdadero** valor para ello.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 Este tipo de pintor de formato sigue pintando para siempre a menos que lo detengamos. Entonces, para evitar que el pintor de formato pinte siempre, simplemente podemos llamar**EndFormatPainter** método de**GridEscritorio**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
