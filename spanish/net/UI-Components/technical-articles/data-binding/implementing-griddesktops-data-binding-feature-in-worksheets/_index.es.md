---
title: Implementación de la función de enlace de datos de GridDesktop en hojas de cálculo
type: docs
weight: 10
url: /es/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop, enlace de datos, datos, enlazar
description: Este artículo explica cómo hacer el enlace de datos en GridDesktop.
---

{{% alert color="primary" %}} 

El enlace de datos es una función emocionante ofrecida por el Framework de Microsoft .NET. Sabemos que el control DataGrid ofrecido por Microsoft admite el enlace de datos, lo que significa que un DataGrid puede estar enlazado a cualquier fuente de datos (usando objetos DataSet, DataTable y DataView). Esta función ha facilitado mucho la vida de los desarrolladores. Basado en el mismo concepto, Aspose.Cells.GridDesktop también admite el enlace de datos, lo que permite a los desarrolladores enlazar hojas de cálculo a cualquier fuente de datos. Este artículo explora la función.

{{% /alert %}} 
## **Creación de una base de datos de ejemplo**
1. Cree una base de datos de ejemplo para usar con el ejemplo. Utilizamos Microsoft Access para crear una base de datos de ejemplo con una tabla de Productos (esquema a continuación). 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Se agregan tres filas ficticias a la tabla de Productos.
   **Registros en la tabla de Productos** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Crear una aplicación de ejemplo**
Ahora cree una aplicación de escritorio sencilla en Visual Studio y haga lo siguiente.

1. Arrastre el control "GridControl" desde el cuadro de herramientas y suéltelo en el formulario.
1. Suelte cuatro botones desde el cuadro de herramientas en la parte inferior del formulario y establezca su propiedad de texto como **Vincular hoja de cálculo**, **Agregar fila**, **Eliminar fila** y **Actualizar a base de datos** respectivamente.
## **Agregar espacios de nombres y declarar variables globales**
Debido a que este ejemplo utiliza una base de datos de Microsoft Access, agregue el espacio de nombres System.Data.OleDb en la parte superior del código.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Ahora puede usar las clases empaquetadas bajo este espacio de nombres.

1. Declare variables globales.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Llenando DataSet con datos de la base de datos**
Ahora conectarse a la base de datos de muestra para buscar y llenar datos en un objeto DataSet.

1. Utilice el objeto OleDbDataAdapter para conectarse con nuestra base de datos de muestra y llenar un DataSet con datos extraídos de la tabla Products en la base de datos, como se muestra en el código a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Vinculando Hoja de cálculo con DataSet**
Vincular la hoja de cálculo con la tabla Products del DataSet:

1. Acceda a una hoja de cálculo deseada.
1. Vincule la hoja de cálculo con la tabla Products del DataSet.

Agregue el siguiente código al evento click del botón **Vincular Hoja de cálculo**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Configurando Encabezados de Columna de la Hoja de cálculo**
La hoja de cálculo vinculada ahora carga datos correctamente, pero los encabezados de columna están etiquetados por defecto como A, B y C. Sería mejor configurar los encabezados de columna con los nombres de columna en la tabla de la base de datos.

Para configurar los encabezados de columna de la hoja de cálculo:

1. Obtenga los títulos para cada columna del DataTable (Products) en el DataSet.
1. Asigne los títulos a los encabezados de las columnas de la hoja de cálculo.

Agregue el código escrito en el evento click del botón **Vincular Hoja de cálculo** con el siguiente fragmento de código. Al hacer esto, los antiguos encabezados de columna (A, B y C) serán reemplazados por ProductID, ProductName y ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Personalizando el Ancho y Estilos de las Columnas**
Para mejorar el aspecto de la hoja de cálculo aún más, es posible establecer el ancho y estilos de las columnas. Por ejemplo, a veces, el encabezado de columna o el valor dentro de la columna consiste en un gran número de caracteres que no caben dentro de la celda. Para solucionar tales problemas, Aspose.Cells.GridDesktop  admite el cambio de los anchos de las columnas.

Agregue el siguiente código al botón **Vincular Hoja de cálculo**. Los anchos de las columnas se personalizarán de acuerdo con la nueva configuración.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop también admite la aplicación de estilos personalizados a las columnas. El siguiente código, agregado al botón **Vincular Hoja de cálculo**, personaliza los estilos de las columnas para hacerlos más presentables.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Ahora ejecute la aplicación y haga clic en el botón **Vincular Hoja de cálculo**.
## **Añadiendo Filas**
Para agregar nuevas filas a una hoja de cálculo, use el método AddRow de la clase Worksheet. Esto agrega una fila vacía en la parte inferior y se agrega un nuevo DataRow a la fuente de datos (aquí, se agrega un nuevo DataRow a la DataTable del DataSet). Los desarrolladores pueden agregar tantas filas como quieran llamando al método AddRow una y otra vez. Una vez que se ha agregado una fila, los usuarios pueden ingresar valores en ella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Eliminación de Filas**
Aspose.Cells.GridDesktop también admite la eliminación de filas mediante el método RemoveRow de la clase Worksheet. Para eliminar una fila usando Aspose.Cells.GridDesktop, se requiere el índice de la fila a eliminar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Agregue el código anterior al botón **Eliminar fila** y ejecute la aplicación. Aparecen algunos registros antes de que se elimine la fila. Seleccionar una fila y hacer clic en el botón **Eliminar fila** elimina la fila seleccionada.
## **Guardar cambios en la base de datos**
Finalmente, para guardar cualquier cambio realizado por los usuarios en la hoja de cálculo de vuelta a la base de datos, use el método Update del objeto OleDbDataAdapter. El método Update toma la fuente de datos (DataSet, DataTable, etc.) de la hoja de cálculo para actualizar la base de datos.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Agregue el código anterior al botón **Actualizar en la base de datos**.
1. Ejecute la aplicación.
1. Realice algunas operaciones en los datos de la hoja de cálculo, quizás agregando nuevas filas y editando o eliminando datos existentes.
1. Luego haga clic en **Actualizar en la base de datos** para guardar los cambios en la base de datos.
1. Revise la base de datos para ver que los registros de la tabla se hayan actualizado en consecuencia.
