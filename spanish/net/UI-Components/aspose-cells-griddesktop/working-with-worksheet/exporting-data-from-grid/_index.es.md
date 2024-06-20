---
title: Exportar datos desde Grid
type: docs
weight: 60
url: /es/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop, exportar, datos, exportar datos
description: Este artículo presenta cómo exportar datos en GridDesktop.
---

{{% alert color="primary" %}} 

En nuestro tema anterior, hemos hablado acerca de importar el contenido de un DataTable al control Aspose.Cells.GridDesktop, pero no mencionamos a propósito que Aspose.Cells.GridDesktop también soporta el proceso inverso. Por lo tanto, en este tema, discutiremos sobre la exportación de los datos dentro del control Aspose.Cells.GridDesktop a un DataTable.

{{% /alert %}} 
## **Exportar contenido de Grid**
### **Exportar a un DataTable específico**
Para exportar el contenido del Grid a un objeto DataTable específico, siga los siguientes pasos: Agregue el control Aspose.Cells.GridDesktop a su **Formulario**.

- Cree un objeto DataTable específico según sus necesidades.
- Exporte los datos de una **Hoja de cálculo** seleccionada a su objeto DataTable especificado.

En el ejemplo a continuación, hemos creado un objeto DataTable específico con cuatro columnas. Finalmente, exportamos los datos de la hoja de cálculo (comenzando desde la primera celda con 69 filas y 4 columnas) a un objeto DataTable que ya hemos creado.

**Ejemplo:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportar a un nuevo DataTable**
A veces, los desarrolladores pueden no estar interesados en crear su propio objeto DataTable y podrían tener la simple necesidad de exportar los datos de la hoja de cálculo a un nuevo objeto DataTable. Sería la forma más rápida para los desarrolladores de exportar los datos de la hoja de cálculo.

En el ejemplo a continuación, hemos intentado una forma diferente de explicar el uso del método ExportDataTable. Hemos tomado la referencia de la hoja de cálculo que está actualmente activa y luego exportamos los datos completos de esa hoja de cálculo activa a un nuevo objeto DataTable. Ahora, este objeto DataTable puede ser utilizado de la forma que el desarrollador desee. Por ejemplo, un desarrollador puede vincular este objeto DataTable a un DataGrid para ver los datos.

**Ejemplo:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

En el caso anterior, utilizaremos una versión sobrecargada del método ExportDataTable que simplemente devolverá un nuevo objeto DataTable conteniendo los datos exportados de la hoja de cálculo.

{{% /alert %}}
