---
title: Añadir Cell Fórmulas
type: docs
weight: 30
url: /es/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

La característica más valiosa que ofrece Aspose.Cells.GridWeb es el soporte para fórmulas o funciones. Aspose.Cells.GridWeb tiene su propio motor de fórmulas que calcula las fórmulas en las hojas de cálculo. Aspose.Cells.GridWeb admite funciones o fórmulas integradas y definidas por el usuario. Este tema trata sobre cómo agregar fórmulas a las celdas mediante Aspose.Cells.GridWeb API en detalle.

{{% /alert %}} 
## **Adición de fórmulas al Cells**
### **¿Cómo agregar y calcular una fórmula?**
 Es posible agregar, acceder y modificar fórmulas en celdas usando la propiedad Fórmula de una celda. Aspose.Cells. GridWeb admite fórmulas definidas por el usuario que van desde simples hasta complejas. Sin embargo, una gran cantidad de funciones o fórmulas integradas (similares a Microsoft Excel) también se proporcionan con Aspose.Cells.GridWeb. Para ver la lista completa de funciones integradas, consulte este[lista de funciones compatibles.](/cells/es/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintaxis de la fórmula debe ser compatible con la sintaxis de Excel Microsoft. Por ejemplo, todas las fórmulas deben comenzar con un signo igual (=).

Para agregar una fórmula dinámicamente, Aspose.Cells.GridWeb la reconocerá como una fórmula incluso si no usa un signo **=**, pero si los usuarios finales trabajan en la GUI, deben usar el signo "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Fórmula agregada a la celda B3 pero no calculada por GridWeb** 

![todo:imagen_alternativa_texto](add-cell-formulas_1.png)

En la captura de pantalla anterior, puede ver que se agregó una fórmula a B3 pero aún no se calculó. Para calcular todas las fórmulas, llame al método CalculateFormula de GridWorksheetCollection del control GridWeb después de agregar fórmulas a las hojas de trabajo como se muestra a continuación.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 Los usuarios también pueden calcular fórmulas haciendo clic en**Enviar**.

**Al hacer clic en el botón Enviar de GridWeb** 

![todo:imagen_alternativa_texto](add-cell-formulas_2.png)

**IMPORTANTE** : si un usuario hace clic en el**Ahorrar** o**Deshacer** o las pestañas de las hojas, todas las fórmulas son calculadas por GridWeb automáticamente.

**Resultado de la fórmula después del cálculo** 

![todo:imagen_alternativa_texto](add-cell-formulas_3.png)

{{% /alert %}} 
### **Haciendo referencia a Cells de otras hojas de trabajo**
Usando Aspose.Cells.GridWeb, es posible hacer referencia a valores almacenados en diferentes hojas de trabajo en sus fórmulas, creando fórmulas complejas.

La sintaxis para hacer referencia a un valor de celda de una hoja de trabajo diferente es SheetName!CellName.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
