---
title: Vincular hoja de trabajo a un conjunto de datos usando GridWebs Worksheets Designer
type: docs
weight: 20
url: /es/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 Este artículo analiza un método sencillo para vincular hojas de trabajo a tablas de base de datos en modo GUI usando una herramienta especial provista con Aspose.Cells.GridWeb, el diseñador de hojas de trabajo.

{{% /alert %}} 
## **Vinculación de una hoja de trabajo con una base de datos mediante Worksheets Designer**
	**Paso 1: crear una base de datos de muestra**
1. Primero, creamos la base de datos de muestra que se usará en este artículo. Usamos Microsoft Access para crear una base de datos que contiene una tabla llamada Productos. Su esquema se muestra a continuación.
   **Información de diseño de la tabla de productos** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Se agregan algunos registros ficticios a la tabla Productos.
   **Registros en la tabla Productos** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Paso 2: Diseño de una aplicación de muestra**
 Se crea y diseña una aplicación web ASP.NET en Visual Studio.NET como se muestra a continuación.
**Aplicación de muestra diseñada** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Paso 3: Conexión con la base de datos mediante Server Explorer**
 Es hora de conectarse a la base de datos. Podemos hacerlo fácilmente usando Server Explorer en Visual Studio.NET.

1.  Seleccione**Conección de datos** en**Explorador de servidores** y haga clic derecho.
1.  Seleccione**Agregar conexión** del menú.
   **Seleccionando la opción Agregar conexión** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 Se muestra el cuadro de diálogo Propiedades de enlace de datos.
**El cuadro de diálogo Propiedades de enlace de datos** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 Con este cuadro de diálogo, puede conectarse a cualquier base de datos. De forma predeterminada, le permite conectarse a una base de datos de SQL Server. Para este ejemplo, necesitamos conectarnos con una base de datos de Access Microsoft.

1.  Haga clic en el**Proveedor** pestaña.
1.  Seleccione**Microsoft Jet 4.0 Proveedor OLE DB** desde el**Proveedores OLE DB** lista.
1.  Hacer clic**próximo**.
   **Hacer clic en Siguiente después de seleccionar un proveedor OLE DB** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 los**Conexión** se abre la página de pestañas.

1.  Seleccione el archivo de base de datos de Access Microsoft (en nuestro caso, db.mdb) y haga clic en**OK**.
   **Hacer clic en el botón Aceptar después de seleccionar el archivo de la base de datos** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 Después de hacer clic**OK** , se creará una conexión de base de datos a la base de datos de Access Microsoft en el**Explorador de servidores**Haga doble clic en la conexión para ver todas las tablas, vistas y procedimientos almacenados en la base de datos.

{{% /alert %}} 
### **Paso 4: crear objetos de conexión de base de datos gráficamente**
1.  Explore las tablas en la base de datos usando el**Explorador de servidores**.
 Solo hay una tabla, Productos.
1.  Arrastre y suelte la tabla Productos desde la**Explorador de servidores** hacia**Formulario web**.
   **Arrastrar la tabla Productos desde Server Explorer y colocarla en el formulario web** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Puede aparecer un cuadro de diálogo.
**Cuadro de diálogo para confirmar la inclusión de la contraseña de la base de datos en la cadena de conexión** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Decida si desea incluir una contraseña de base de datos en la cadena de conexión o no. Para este ejemplo, seleccionamos**No incluir contraseña**. 
Se crearon y agregaron dos objetos de conexión de base de datos (oleDbConnection1 y oleDbDataAdapter1).
**Objetos de conexión de base de datos (oleDbConnection1 y oleDbDataAdapter1) creados y mostrados** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Paso 5: Generación de DataSet**
Hasta ahora, hemos creado objetos de conexión a la base de datos, pero aún necesitamos un lugar para almacenar datos después de conectarnos a la base de datos. Un objeto DataSet puede almacenar datos con precisión y también podemos generarlos fácilmente usando VS.NET IDE.

1.  Seleccione**oleDbDataAdaper1** y haga clic derecho.
1.  Seleccione**Generar conjunto de datos** opción del menú.
   **Seleccionando la opción Generar conjunto de datos** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 Se muestra el cuadro de diálogo Generar conjunto de datos.
 Aquí, es posible seleccionar un nombre para el nuevo objeto DataSet que se creará y qué tablas se le deben agregar.

1.  Selecciona el**Agregar este conjunto de datos al diseñador** opción.
1.  Hacer clic**OK**.
   **Al hacer clic en el botón Aceptar para generar DataSet** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Se agrega un objeto dataSet11 al diseñador.
**DataSet generado y agregado al diseñador** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Paso 6: Usar el Diseñador de hojas de trabajo**
 Ahora, es hora de abrir el secreto.

1. Seleccione el control GridWeb y haga clic con el botón derecho.
1.  Seleccione**Diseñador de hojas de trabajo** opción del menú.

   **Selección de la opción Diseñador de hojas de trabajo** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 Se muestra el Editor de colección de hojas de trabajo (también llamado Diseñador de hojas de trabajo).
**Cuadro de diálogo Editor de colección de hojas de trabajo** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



El cuadro de diálogo contiene varias propiedades que se pueden configurar para vincular Sheet1 a cualquier tabla de la base de datos.

1.  Selecciona el**Fuente de datos** propiedad.
 El objeto dataSet11 generado en el paso anterior aparece en el menú.
1. Seleccione dataSet11.
1.  Haga clic en el**miembro de datos** propiedad.
 Worksheets Designer muestra automáticamente una lista de tablas en dataSet11. Solo hay una tabla, Productos.
1. Seleccione la tabla Productos.
   **Configuración de las propiedades DataSource y DataMember** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  Comprobar el**BindColumns** propiedad.
   **Hacer clic en la propiedad BindColumns** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 Al hacer clic en el**BindColumns** La propiedad abre el editor de la colección BindColumn.
**El editor de la colección BindColumn** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 En BindColumn Collection Editor, todas las columnas del**productos** se agregan automáticamente a la colección BindColumns.

1. Seleccione cualquier columna y personalice sus propiedades.
 Por ejemplo, puede modificar el título de cada columna.
   **Modificación del título de la columna ProductID** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  Después de hacer los cambios, haga clic en**OK**.
1.  Cierre todos los cuadros de diálogo haciendo clic en**OK**.
 Finalmente, regresa a la página WebForm1.aspx.
   **Volver a la página WebForm1.aspx después de usar el Diseñador de hojas de trabajo** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 Arriba, se muestra el nombre de la columna de la tabla Productos. El ancho de las columnas es pequeño, por lo que los nombres completos de algunas columnas no son completamente visibles.
### **Paso 7: agregar código al controlador de eventos Page_Load**
 Usamos Worksheets Designer y ahora solo tenemos que agregar código al controlador de eventos Page_Load para llenar el objeto dataSet11 con datos de la base de datos (usando oleDbDataAdapter1) y vincular el control GridWeb a dataSet11 llamando a su método DataBind.

1.  Agrega el código:

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing Page_Load event handler

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub



{{< /highlight >}}

1. Verifique el código agregado al controlador de eventos Page_Load.
   **Código agregado al controlador de eventos Page_Load** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Paso 8: Ejecución de la aplicación**
 Compile y ejecute la aplicación: presione**Ctrl+F5** o haga clic**comienzo**. 
**Ejecutando la aplicación** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Después de la compilación, la página WebForm1.aspx se abre en una ventana del navegador con todos los datos cargados desde la base de datos.
**Datos cargados en el control GridWeb desde la base de datos** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Trabajar con el control GridWeb**
 Cuando los datos se cargan en el control GridWeb, proporciona a los usuarios control sobre los datos. GridWeb ofrece varios tipos diferentes de funciones de manipulación de datos.
### **Validación de datos**
Aspose.Cells.GridWeb crea automáticamente reglas de validación adecuadas para todas las columnas vinculadas según los tipos de datos definidos en la base de datos. Vea el tipo de validación de una celda pasando el cursor sobre ella.
**Verificando el tipo de validación de una celda** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Aquí, la celda seleccionada contiene el**<INT>** validación, lo que significa que los usuarios solo pueden ingresar valores enteros en él. Si introducen otro valor, se produce un error de validación. Es más,**<OBLIGATORIO>** muestra que se debe enviar el ID de producto de valor.
### **Eliminación de filas**
 Para eliminar una fila, seleccione una fila (o cualquier celda de la fila), haga clic con el botón derecho y seleccione**Borrar fila**.
**Seleccionar la opción Eliminar fila del menú** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


La fila se eliminaría instantáneamente.
**Datos de cuadrícula (después de eliminar una fila)** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Edición de filas**
Edite los datos en celdas o filas y luego haga clic en**Ahorrar** o**Enviar** para guardar los cambios.
### **Adición de filas**
1.  Para agregar una fila, haga clic derecho en una celda y seleccione**Añadir fila**.
   **Seleccionar la opción Agregar fila del menú** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Se agrega una nueva fila a la hoja al final de otras filas.
**Nueva fila agregada a Grid** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 A la izquierda de la nueva fila hay un asterisco{{< emoticons/cross >}} , indicando que la fila es nueva.

1. Agregue valores a la nueva fila.
1.  Hacer clic**Ahorrar** o**Enviar** para confirmar el cambio.
   **Guardar cambios en los datos haciendo clic en *Guardar** botón*

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Configuración del formato de número**
 Por el momento, los precios en el**Precio del producto** columna se muestran como valores numéricos. Es posible hacer que parezcan moneda.

1. Vuelva a Visual Studio.NET.
1. Abra el editor de la colección BindColumn.
 los**NúmeroTipo** propiedad de la**Precio del producto** la columna se establece en**General**.
   **La propiedad NumberType establecida en General** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Hacer clic**La lista desplegable** y seleccione**Moneda4** de la lista.
   **La propiedad NumberType cambió a Moneda4** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Vuelva a ejecutar la aplicación.
 Los valores en el**Precio del producto** la columna ahora es moneda.
   **Precios de productos en moneda Formato de número** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Edición de datos**
 La aplicación hasta ahora solo permite a sus usuarios ver los datos de la tabla. Los usuarios pueden editar datos en el control GridWeb pero, al cerrar el navegador y abrir la base de datos, nada ha cambiado. Los cambios realizados no se guardan en la base de datos.

 El siguiente ejemplo agrega código a la aplicación para que GridWeb pueda guardar los cambios en la base de datos.

1. Abre el**Propiedades** panel y seleccione el evento SaveCommand del control GridWeb de la lista.
   **Seleccionando el evento SaveCommand de GridWeb** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  Haga doble clic en el**GuardarComando** y VS.NET crea el controlador de eventos GridWeb1_SaveCommand.
1.  Agregue código a este controlador de eventos que actualizará la base de datos con cualquier dato modificado en el DataSet vinculado a la hoja de trabajo mediante oleDbDataAdapter1.

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

También puede verificar el código agregado al controlador de eventos GridWeb1_SaveCommand
**Código agregado al controlador de eventos GridWeb1_SaveCommand** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 Guarde los cambios en la base de datos utilizando el**Ahorrar** botón ahora definitivamente los salva.
## **Conclusión**
{{% alert color="primary" %}} 

El enlace de datos es una característica importante de Aspose.Cells.GridWeb. Es fácil vincular hojas de trabajo a una base de datos utilizando la utilidad Worksheets Designer que ofrece Aspose.Cells.GridWeb. Aspose.Cells.GridWeb ahorra tiempo y esfuerzo al crear potentes soluciones Grid.

{{% /alert %}}
