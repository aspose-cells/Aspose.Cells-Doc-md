---
title: Agregar hojas de trabajo
type: docs
weight: 20
url: /es/net/add-worksheets/
---
{{% alert color="primary" %}} 

Las hojas de trabajo son una parte integral de Aspose.Cells.GridWeb. Todos los datos se gestionan y almacenan en forma de hojas de cálculo. Aspose.Cells.GridWeb permite a los desarrolladores agregar una o más hojas de trabajo al control Aspose.Cells.GridWeb. Este tema muestra enfoques simples para agregar hojas de trabajo a Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Agregar una hoja de trabajo**
### **Sin especificar el nombre de la hoja**
La forma más sencilla de agregar una hoja de trabajo a Aspose.Cells.GridWeb es llamar al método Add de la colección GridWorksheetCollection en el control GridWeb. Esto crea hojas de cálculo que usan nombres predeterminados (es decir, Hoja1, Hoja2, Hoja3, etc.) y las agrega al control GridWeb.

**Salida: se ha agregado una hoja de trabajo con un nombre predeterminado a GridWeb** 

![todo:imagen_alternativa_texto](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 El método Add devuelve el índice de la nueva hoja de trabajo que se puede usar para acceder a la instancia de esta hoja de trabajo. Para obtener más detalles sobre cómo acceder a las hojas de trabajo, lea[Acceder a hojas de trabajo](/cells/es/net/access-worksheets/).

{{% /alert %}} 
### **Con nombre de hoja especificado**
Para agregar una hoja de cálculo con un nombre específico al control GridWeb en lugar de usar el esquema de nomenclatura predeterminado, llame a una versión sobrecargada del método Add que toma el SheetName especificado. Por ejemplo, el siguiente ejemplo agrega una hoja de cálculo denominada Factura.

**Salida: se ha agregado una hoja de trabajo con un nombre específico a GridWeb** 

![todo:imagen_alternativa_texto](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

El método Add que acepta el nombre de la hoja de cálculo como una cadena devuelve una instancia de GridWorksheet.

{{% /alert %}}
