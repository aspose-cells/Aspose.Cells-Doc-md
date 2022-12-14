---
title: Exportación de datos desde la cuadrícula
type: docs
weight: 60
url: /es/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

En nuestro tema anterior, hablamos sobre la importación del contenido de un DataTable al control Aspose.Cells.GridDesktop, pero no mencionamos a propósito que Aspose.Cells.GridDesktop también admite el proceso inverso. Entonces, en este tema, hablaremos sobre cómo exportar los datos dentro del control Aspose.Cells.GridDesktop a un DataTable.

{{% /alert %}} 
## **Exportación de contenido de cuadrícula**
### **Exportación a una tabla de datos específica**
 Para exportar el contenido de Grid a un objeto DataTable específico, siga los pasos a continuación: Agregue el control Aspose.Cells.GridDesktop a su**Forma**.

- Cree un objeto DataTable específico según sus necesidades.
-  Exportar los datos de un seleccionado**Hoja de cálculo** a su objeto DataTable especificado.

En el ejemplo que se muestra a continuación, hemos creado un objeto DataTable específico que tiene cuatro columnas en su interior. Finalmente, exportamos los datos de la hoja de trabajo (comenzando desde la primera celda con 69 filas y 4 columnas) a un objeto DataTable ya creado por nosotros.

**Ejemplo:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportación a una nueva tabla de datos**
veces, los desarrolladores pueden no estar interesados en crear su propio objeto DataTable y pueden tener una simple necesidad de exportar los datos de la hoja de trabajo a un nuevo objeto DataTable. Sería la forma más rápida para que los desarrolladores simplemente exporten los datos de la hoja de trabajo.

En el ejemplo que se muestra a continuación, hemos probado una forma diferente de explicar el uso del método ExportDataTable. Hemos tomado la referencia de la hoja de trabajo que está actualmente activa y luego exportamos los datos completos de esa hoja de trabajo activa a un nuevo objeto DataTable. Ahora, este objeto DataTable se puede usar de cualquier forma que desee un desarrollador. Solo por ejemplo, un desarrollador puede vincular este objeto DataTable a un DataGrid para ver los datos.

**Ejemplo:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

En el caso anterior, utilizaremos una versión sobrecargada del método ExportDataTable que simplemente devolverá un nuevo objeto DataTable que contiene datos exportados desde la hoja de trabajo.

{{% /alert %}}
