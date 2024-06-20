---
title: Agregar Hojas de Cálculo
type: docs
weight: 20
url: /es/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: Este artículo presenta cómo agregar hojas de cálculo (GridWorksheet) en GridWeb.
---

{{% alert color="primary" %}} 

Las hojas de cálculo son una parte integral de Aspose.Cells.GridWeb. Todos los datos se gestionan y almacenan en forma de hojas de cálculo. Aspose.Cells.GridWeb permite a los desarrolladores agregar una o más hojas de cálculo al control Aspose.Cells.GridWeb. Este tema muestra enfoques simples para agregar hojas de cálculo a Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Agregando una hoja de cálculo**
### **Sin especificar nombre de hoja**
La forma más sencilla de agregar una hoja de cálculo a Aspose.Cells.GridWeb es llamar al método Agregar de la colección GridWorksheetCollection en el control GridWeb. Esto crea hojas de cálculo que utilizan nombres predeterminados (es decir, Hoja1, Hoja2, Hoja3, etc.) y las agrega al control GridWeb.

**Salida: se ha añadido una hoja de cálculo con nombre predeterminado a GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

El método Agregar devuelve el índice de la nueva hoja de cálculo que se puede utilizar para acceder a la instancia de esta hoja de cálculo. Para obtener más detalles sobre cómo acceder a las hojas de cálculo, lee [Acceder a Hojas de Cálculo](/cells/es/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **Con nombre de hoja especificado**
Para agregar una hoja de cálculo con un nombre específico al control GridWeb en lugar de usar el esquema de nombres predeterminado, llama a una versión sobrecargada del método Agregar que toma el nombre de hoja especificado. Por ejemplo, el siguiente ejemplo agrega una hoja de cálculo llamada 'Factura'.

**Salida: se ha añadido una hoja de cálculo con un nombre especificado a GridWeb** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

El método Agregar que acepta el nombre de la hoja de cálculo como cadena devuelve una instancia de GridWorksheet.

{{% /alert %}}
