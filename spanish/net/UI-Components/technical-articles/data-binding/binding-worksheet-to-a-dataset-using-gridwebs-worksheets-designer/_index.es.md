---
title: Vinculación de la hoja de cálculo a un DataSet utilizando el diseñador de hojas de cálculo de GridWeb
type: docs
weight: 20
url: /es/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: Este artículo introduce cómo utilizar el diseñador de hojas de cálculo para vincular una hoja de cálculo a un DataSet en GridWeb.
---

{{% alert color="primary" %}} 

Este artículo discute un enfoque sencillo para vincular hojas de cálculo a tablas de base de datos en modo GUI utilizando una herramienta especial suministrada con Aspose.Cells.GridWeb, el diseñador de hojas de cálculo. 

{{% /alert %}} 
## **Vinculación de una hoja de cálculo con base de datos utilizando el diseñador de hojas de cálculo**
	**Paso 1: Crear una base de datos de muestra**
1. Primero, creamos la base de datos de muestra que se utilizará en este artículo. Estamos utilizando Microsoft Access para crear una base de datos que contiene una tabla llamada Productos. Su esquema se muestra a continuación.
   **Información de diseño de la tabla de Productos** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Se agregan algunos registros ficticios a la tabla Productos.
   **Registros en la tabla de Productos** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Paso 2: Diseño de la aplicación de muestra**
Se crea y diseña una aplicación web ASP.NET en Visual Studio.NET como se muestra a continuación. 
**Aplicación de muestra diseñada** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Paso 3: Conexión con la base de datos utilizando el Explorador de servidores**
Es hora de conectarse a la base de datos. Podemos hacerlo fácilmente utilizando el Explorador de servidores en Visual Studio.NET. 

1. Seleccione **Conexión de datos** en el **Explorador de servidores** y haga clic derecho.
1. Seleccione **Agregar Conexión** en el menú.
   **Seleccionar la opción Agregar Conexión** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



Se muestra el cuadro de diálogo Propiedades del vínculo de datos. 
**El cuadro de diálogo Propiedades del vínculo de datos** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



Usando este cuadro de diálogo, puede conectarse a cualquier base de datos. De forma predeterminada, le permite conectarse a una base de datos de SQL Server. Para este ejemplo, necesitamos conectarnos con una base de datos de Microsoft Access. 

1. Haga clic en la pestaña **Proveedor**.
1. Seleccione **Proveedor OLE DB Microsoft Jet 4.0** de la lista de **Proveedor(es) OLE DB**.
1. Haga clic en **Siguiente**.
   **Hacer clic en Siguiente después de seleccionar un proveedor OLE DB** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


Se abre la página de pestaña **Conexión**. 

1. Seleccione el archivo de base de datos de Microsoft Access (en nuestro caso, db.mdb) y haga clic en **Aceptar**.
   **Hacer clic en el botón Aceptar después de seleccionar el archivo de la base de datos** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

Después de hacer clic en **Aceptar**, se creará una conexión de base de datos a la base de datos de Microsoft Access en el **Explorador de servidores**. Haga doble clic en la conexión para ver todas las tablas, vistas y procedimientos almacenados en la base de datos.

{{% /alert %}} 
### **Paso 4: Crear objetos de conexión de base de datos gráficamente**
1. Explore las tablas en la base de datos usando el **Explorador de servidores**.
   Solo hay una tabla, Productos. 
1. Arrastre y suelte la tabla Productos desde el **Explorador de servidores** al **Formulario web**.
   **Arrastrar la tabla Productos desde el Explorador de servidores y soltarla en el formulario web** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Puede aparecer un cuadro de diálogo.
**Cuadro de diálogo para confirmar la inclusión de la contraseña de la base de datos en la cadena de conexión** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Decide si desea incluir la contraseña de la base de datos en la cadena de conexión o no. Para este ejemplo, seleccionamos **No incluir contraseña**. 
Se han creado y agregado dos objetos de conexión a la base de datos (oleDbConnection1 y oleDbDataAdapter1).
**Objetos de conexión a la base de datos (oleDbConnection1 y oleDbDataAdapter1) creados y mostrados** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Paso 5: Generando DataSet**
Hasta ahora, hemos creado objetos de conexión a la base de datos, pero aún necesitamos un lugar para almacenar los datos después de conectar a la base de datos. Un objeto DataSet puede almacenar datos de manera precisa y también podemos generarlo fácilmente utilizando el entorno de desarrollo integrado (IDE) de VS.NET. 

1. Selecciona **oleDbDataAdaper1** y haz clic derecho.
1. Selecciona la opción **Generar DataSet** en el menú.
   **Seleccionando la opción Generar DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



Se muestra el diálogo Generar DataSet. 
Aquí es posible seleccionar un nombre para el nuevo objeto DataSet que se creará, y qué tablas deben ser agregadas a él. 

1. Selecciona la opción **Agregar este conjunto de datos al diseñador**.
1. Haz clic en **Aceptar**.
   **Hacer clic en el botón OK para generar DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Se agrega un objeto dataSet11 al diseñador.
**DataSet generado y agregado al diseñador** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Paso 6: Usando el diseñador de hojas de cálculo**
Ahora, es hora de desvelar el secreto. 

1. Selecciona el control GridWeb y haz clic derecho.
1. Selecciona la opción **Diseñador de hojas de cálculo** en el menú. 

   **Seleccionando la opción Diseñador de hojas de cálculo** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



Se muestra el Editor de la Colección de Hojas de Trabajo (también llamado Diseñador de Hojas de Trabajo). 
**Cuadro de diálogo del Editor de Colección de Hojas de Trabajo** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



El cuadro de diálogo contiene varias propiedades que se pueden configurar para vincular Sheet1 a cualquier tabla en la base de datos.

1. Selecciona la propiedad **DataSource**.
   El objeto dataSet11 generado en el paso anterior está listado en el menú. 
1. Selecciona dataSet11.
1. Haz clic en la propiedad **DataMember**.
   El Diseñador de Hojas de Trabajo muestra automáticamente una lista de tablas en dataSet11. Solo hay una tabla, Productos.
1. Selecciona la tabla Productos.
   **Configuración de las propiedades DataSource y DataMember** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. Marca la propiedad **BindColumns**.
   **Haciendo clic en la propiedad BindColumns** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



Hacer clic en la propiedad **BindColumns** abre el Editor de la Colección de BindColumns.
**El Editor de la Colección de BindColumns** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



En el Editor de la Colección de BindColumns, todas las columnas de la tabla **Productos** se agregan automáticamente a la colección BindColumns. 

1. Selecciona cualquier columna y personaliza sus propiedades.
   Por ejemplo, puedes modificar la leyenda de cada columna.
   **Modificando la Leyenda de la columna ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. Después de hacer cambios, haz clic en **Aceptar**.
1. Cierra todos los cuadros de diálogo haciendo clic en **Aceptar**.
   Finalmente, vuelves a la página WebForm1.aspx. 
   **Regresando a la página WebForm1.aspx después de usar el diseñador de hojas de cálculo** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Arriba se muestra el nombre de la columna de la tabla Productos. La anchura de las columnas es pequeña, por lo que los nombres completos de algunas columnas no son completamente visibles. 
### **Paso 7: Agregar Código al Controlador de Eventos Page_Load**
Hemos utilizado el diseñador de hojas de cálculo y ahora solo tenemos que agregar código al controlador de eventos Page_Load para llenar el objeto dataSet11 con datos de la base de datos (usando oleDbDataAdapter1) y asociar el control GridWeb a dataSet11 llamando a su método DataBind. 

1. Agregar el código: 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Paso 8: Ejecutar la Aplicación**
Compilar y ejecutar la aplicación: presione **Ctrl+F5** o haga clic en **Iniciar**. 
**Ejecutar la aplicación** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Después de la compilación, la página WebForm1.aspx se abre en una ventana del navegador con todos los datos cargados desde la base de datos.
**Datos cargados en el control GridWeb desde la base de datos** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Trabajar con el Control GridWeb**
Cuando se cargan datos en el control GridWeb, proporciona a los usuarios un control sobre los datos. El GridWeb ofrece una variedad de características de manipulación de datos. 
### **Validación de datos**
Aspose.Cells.GridWeb crea automáticamente reglas de validación apropiadas para todas las columnas vinculadas según los tipos de datos definidos en la base de datos. Vea el tipo de validación de una celda al pasar el cursor sobre ella.
**Comprobando el tipo de validación de una celda** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Eliminación de Filas**
Para eliminar una fila, selecciona una fila (o cualquier celda en la fila), haz clic derecho y selecciona **Eliminar fila**.
**Seleccionar la opción Eliminar fila del menú** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


La fila se eliminará instantáneamente.
**Datos de la cuadrícula (después de eliminar una fila)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Editando Filas**
Edita datos en celdas o filas y luego haz clic en **Guardar** o **Enviar** para guardar los cambios. 
### **Añadiendo Filas**
1. Para agregar una fila, haz clic derecho en una celda y selecciona **Agregar fila**.
   **Seleccionando la opción Agregar fila del menú** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Se agrega una nueva fila a la hoja al final de las otras filas.
**Nueva fila agregada a la cuadrícula** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Agrega valores a la nueva fila.
1. Haz clic en **Guardar** o **Enviar** para confirmar el cambio.
   **Guardando cambios en los datos haciendo clic en el botón *Guardar** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Configuración de formato numérico**
En este momento, los precios en la columna de **Precio del producto** se muestran como valores numéricos. Es posible hacer que se vean como moneda.

1. Regresa a Visual Studio.NET.
1. Abre el Editor de la Colección de la Columna de Vinculación.
   La propiedad **Tipo de número** de la columna **Precio del producto** está establecida en **General**.
   **La propiedad Tipo de número establecida en General** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. Haga clic en **DropDownList** y seleccione **Currency4** de la lista.
   **La propiedad NumberType cambió a Currency4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Ejecute la aplicación nuevamente.
   Los valores en la columna de **Precio del Producto** ahora son en moneda.
   **Precios de productos en formato Numérico de Moneda** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Editando Datos**
Hasta ahora, la aplicación solo permite a sus usuarios ver datos de la tabla. Los usuarios pueden editar datos en el control GridWeb, pero al cerrar el navegador y abrir la base de datos, nada ha cambiado. Los cambios realizados no se guardan en la base de datos. 

El siguiente ejemplo añade código a la aplicación para que la GridWeb pueda guardar cambios en la base de datos. 

1. Abra el panel de **Propiedades** y seleccione el evento SaveCommand del control GridWeb de la lista.
   **Seleccionando el evento SaveCommand de GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. Haga doble clic en el evento **SaveCommand** y VS.NET creará el manejador de eventos GridWeb1_SaveCommand.
1. Agregue código a este manejador de eventos que actualizará la base de datos con cualquier dato modificado en el DataSet vinculado a la hoja de cálculo usando oleDbDataAdapter1. 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

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

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

También puede revisar el código añadido al manejador de eventos GridWeb1_SaveCommand
**Código añadido al manejador de eventos GridWeb1_SaveCommand** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Guardar cambios en la base de datos usando el botón **Guardar** ahora definitivamente los guarda.
## **Conclusión**
{{% alert color="primary" %}} 

La vinculación de datos es una característica importante de Aspose.Cells.GridWeb. Es fácil vincular hojas de cálculo a una base de datos utilizando la utilidad Worksheets Designer ofrecida por Aspose.Cells.GridWeb. Aspose.Cells.GridWeb ahorra tiempo y esfuerzo al crear soluciones potentes de Grid. 

{{% /alert %}}
