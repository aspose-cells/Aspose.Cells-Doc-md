---
title: Agregar Fórmulas de Celdas
type: docs
weight: 30
url: /es/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb, fórmula
description: Este artículo presenta cómo agregar una fórmula en la celda en GridWeb.
---

{{% alert color="primary" %}} 

La característica más valiosa ofrecida por Aspose.Cells.GridWeb es el soporte para fórmulas o funciones. Aspose.Cells.GridWeb tiene su propio Motor de Fórmulas que calcula las fórmulas en las hojas de cálculo. Aspose.Cells.GridWeb soporta tanto funciones o fórmulas incorporadas como definidas por el usuario. Este tema discute agregar fórmulas a celdas utilizando la API de Aspose.Cells.GridWeb en detalle.

{{% /alert %}} 
## **Agregar Fórmulas a Celdas**
### **¿Cómo agregar y calcular una fórmula?**
Es posible agregar, acceder y modificar fórmulas en celdas utilizando la propiedad Formula de una celda. Aspose.Cells.GridWeb admite fórmulas definidas por el usuario que van desde simples a complejas. Sin embargo, se suministra también un gran número de funciones o fórmulas integradas (similar a Microsoft Excel) con Aspose.Cells.GridWeb. Para ver la lista completa de funciones integradas, consulte esta [lista de funciones admitidas](/cells/es/net/aspose-cells-gridweb/list-of-supported-functions/).

{{% alert color="primary" %}} 

La sintaxis de la fórmula debe ser compatible con la sintaxis de Microsoft Excel. Por ejemplo, todas las fórmulas deben comenzar con un signo igual (=).

Para agregar una fórmula dinámicamente, Aspose.Cells.GridWeb la reconocerá como fórmula incluso si no se utiliza el signo **=**, pero si los usuarios finales trabajan en la interfaz gráfica, deben usar el signo "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Fórmula agregada a la celda B3 pero no calculada por GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

En la captura de pantalla anterior, puede ver que se ha agregado una fórmula a B3 pero aún no se ha calculado. Para calcular todas las fórmulas, llame al método CalculateFormula de la colección de GridWorksheet del control GridWeb después de agregar fórmulas a las hojas de cálculo, como se muestra a continuación.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Los usuarios también pueden calcular fórmulas haciendo clic en **Enviar**.

**Haciendo clic en el botón Enviar de GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**IMPORTANTE**: Si un usuario hace clic en los botones **Guardar** o **Deshacer**, o en las pestañas de la hoja, todas las fórmulas son calculadas automáticamente por GridWeb.

**Resultado de la fórmula después del cálculo** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Referencia a Celdas de Otras Hojas de Cálculo**
Usando Aspose.Cells.GridWeb, es posible hacer referencia a los valores almacenados en diferentes hojas de cálculo en sus fórmulas, creando fórmulas complejas.

La sintaxis para hacer referencia al valor de una celda de una hoja de cálculo diferente es NombreDeLaHoja!NombreDeLaCelda.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
