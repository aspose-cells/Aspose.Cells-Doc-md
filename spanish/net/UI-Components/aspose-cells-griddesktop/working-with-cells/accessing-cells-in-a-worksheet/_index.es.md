---
title: Acceso a Cells en una hoja de trabajo
type: docs
weight: 10
url: /es/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

Hemos discutido sobre trabajar con hojas de trabajo, filas y columnas hasta ahora, pero este es el momento de profundizar más y hablar sobre las celdas. Entonces, en este tema, comenzaríamos nuestra discusión sobre las celdas con una característica básica de acceso a las celdas.

{{% /alert %}} 
## **Acceso a Cells en una hoja de trabajo**
Podemos acceder a cualquier celda de una hoja de trabajo utilizando el API de Aspose.Cells.GridDesktop. Podría haber tres formas posibles de acceder a las celdas de la siguiente manera:

- **Usando Cell Nombre**
- **Uso de los índices de fila y columna de Cell**
- **Centrándose Cell**

Analicemos los tres enfoques anteriores uno por uno.
### **Usando Cell Nombre**
 Todas las celdas de una hoja de trabajo tienen un nombre único. Por ejemplo, A1, A2, B1, B2, etc. Aspose.Cells.GridDesktop permite a los desarrolladores acceder a cualquier celda deseada usando su nombre de celda. Todo lo que tenemos que hacer es simplemente pasar el nombre de la celda (como un índice) al**Cells** colección de la**Hoja de cálculo**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Uso de los índices de fila y columna de Cell**
 Una celda en una hoja de trabajo también se puede reconocer usando su ubicación en términos de sus índices de fila y columna. Todo lo que tenemos que hacer es simplemente pasar los índices de fila y columna de la celda al**Cells** colección de la**Hoja de cálculo**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Centrándose Cell**
 Si no sabe con precisión a qué celda se debe acceder. Entonces Aspose.Cells.GridDesktop también le permite acceder a una celda que está actualmente en el foco de un usuario. Con esta función, puede permitir que un usuario seleccione cualquier celda y luego puede acceder a esa celda en el backend. Simplemente se puede lograr usando**ObtenerCeldaEnfocada** metodo de la**Hoja de cálculo**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
