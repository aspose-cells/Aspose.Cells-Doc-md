---
title: Implementación de la función de enlace de datos de GridDesktop en las hojas de trabajo
type: docs
weight: 10
url: /es/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

El enlace de datos es una característica interesante que ofrece el marco Microsoft .NET. Sabemos que el control DataGrid que ofrece Microsoft admite el enlace de datos, lo que significa que un DataGrid se puede vincular a cualquier fuente de datos (utilizando objetos DataSet, DataTable y DataView). Esta función ha facilitado mucho la vida de los desarrolladores. Basado en el mismo concepto, Aspose.Cells. GridDesktop también admite el enlace de datos, lo que permite a los desarrolladores vincular hojas de trabajo a cualquier fuente de datos. Este artículo explora la función.

{{% /alert %}} 
## **Creación de una base de datos de muestra**
1.  Cree una base de datos de muestra para usar con el ejemplo. Usamos Microsoft Access para crear una base de datos de muestra con una tabla de productos (esquema a continuación).

![todo:imagen_alternativa_texto](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Se agregan tres registros ficticios a la tabla Productos.
   **Registros en la tabla Productos** 

![todo:imagen_alternativa_texto](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Crear una aplicación de muestra**
Ahora cree una aplicación de escritorio simple en Visual Studio y haga lo siguiente.

1. Arrastre el control "GridControl" desde la caja de herramientas y suéltelo en el formulario.
1. Coloque cuatro botones de la caja de herramientas en la parte inferior del formulario y establezca su propiedad de texto como**Encuadernar hoja de trabajo**, **Añadir fila**, **Borrar fila** y**Actualizar a la base de datos** respectivamente.
## **Agregar espacio de nombres y declarar variables globales**
Dado que este ejemplo usa una base de datos de Access Microsoft, agregue el espacio de nombres System.Data.OleDb en la parte superior del código.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Ahora puede usar las clases empaquetadas en este espacio de nombres.

1. Declarar variables globales.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Llenar DataSet con datos de la base de datos**
Ahora conéctese a la base de datos de muestra para obtener y completar datos en un objeto DataSet.

1. Utilice el objeto OleDbDataAdapter para conectarse con nuestra base de datos de muestra y completar un conjunto de datos con datos obtenidos de la tabla de productos en la base de datos, como se muestra en el código a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Hoja de trabajo vinculante con DataSet**
Vincule la hoja de trabajo con la tabla Productos del conjunto de datos:

1. Acceda a una hoja de trabajo deseada.
1. Vincule la hoja de trabajo con la tabla Productos del conjunto de datos.

 Agregue el siguiente código a la**Encuadernar hoja de trabajo** evento de clic del botón.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Configuración de encabezados de columna de la hoja de trabajo**
La hoja de trabajo enlazada ahora carga los datos correctamente, pero los encabezados de las columnas están etiquetados como A, B y C de forma predeterminada. Sería mejor establecer los encabezados de las columnas en los nombres de las columnas en la tabla de la base de datos.

Para establecer los encabezados de columna de la hoja de trabajo:

1. Obtenga los títulos para cada columna de DataTable (Productos) en el DataSet.
1. Asigne los títulos a los encabezados de las columnas de la hoja de trabajo.

 Añada el código escrito en el**Encuadernar hoja de trabajo** evento de clic del botón con el siguiente fragmento de código. Al hacer esto, los encabezados de columna antiguos (A, B y C) se reemplazarán con ProductID, ProductName y ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Personalización del ancho y los estilos de las columnas**
Para mejorar aún más el aspecto de la hoja de trabajo, es posible establecer el ancho y los estilos de las columnas. Por ejemplo, a veces, el encabezado de la columna o el valor dentro de la columna consta de una gran cantidad de caracteres que no caben dentro de la celda. Para resolver estos problemas, Aspose.Cells.GridDesktop admite cambiar el ancho de las columnas.

 Agregue el siguiente código a la**Encuadernar hoja de trabajo** botón. Los anchos de columna se personalizarán de acuerdo con la nueva configuración.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop también admite la aplicación de estilos personalizados a las columnas. El siguiente código, adjunto al**Encuadernar hoja de trabajo** botón, personaliza los estilos de columna para hacerlos más presentables.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Ahora ejecute la aplicación y haga clic en el**Encuadernar hoja de trabajo** Botón.
## **Adición de filas**
Para agregar nuevas filas a una hoja de trabajo, use el método AddRow de la clase Worksheet. Esto agrega una fila vacía en la parte inferior y se agrega una nueva DataRow a la fuente de datos (aquí, se agrega una nueva DataRow a la DataTable del DataSet). Los desarrolladores pueden agregar tantas filas como deseen llamando al método AddRow una y otra vez. Cuando se ha agregado una fila, los usuarios pueden ingresar valores en ella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Eliminación de filas**
Aspose.Cells.GridDesktop también admite la eliminación de filas llamando al método RemoveRow de la clase Worksheet. Eliminar una fila con Aspose.Cells.GridDesktop requiere que se elimine el índice de la fila.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Agregando el código anterior al**Borrar fila** y ejecute la aplicación. Se muestran algunos registros antes de que se elimine la fila. Seleccionando una fila y haciendo clic en el**Borrar fila** El botón elimina la fila seleccionada.
## **Guardar cambios en la base de datos**
Finalmente, para guardar los cambios realizados por los usuarios en la hoja de trabajo en la base de datos, use el método Update del objeto OleDbDataAdapter. El método Update toma la fuente de datos (DataSet, DataTable, etc.) de la hoja de trabajo para actualizar la base de datos.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  Agregue el código anterior al**Actualizar a la base de datos** botón.
1. Ejecute la aplicación.
1. Realice algunas operaciones en los datos de la hoja de trabajo, tal vez agregando nuevas filas y editando o eliminando datos existentes.
1.  Luego haga clic**Actualizar a la base de datos** para guardar los cambios en la base de datos.
1. Verifique la base de datos para ver que los registros de la tabla se hayan actualizado en consecuencia.
