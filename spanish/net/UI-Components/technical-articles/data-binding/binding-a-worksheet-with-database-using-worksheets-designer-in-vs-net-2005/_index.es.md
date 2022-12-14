---
title: Vinculación de una hoja de trabajo con una base de datos mediante Worksheets Designer en VS.Net 2005
type: docs
weight: 40
url: /es/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 Este artículo analiza un enfoque más sencillo para enlazar hojas de trabajo con tablas de base de datos en**Visual Studio.Net 2005** utilizando una herramienta especial suministrada con Aspose.Cells. GridWeb denominada como**Diseñador de hojas de trabajo** . Este artículo definitivamente lo hará sentir lo fácil que es usar la función de enlace de datos en Aspose.Cells.GridWeb con la ayuda de**Diseñador de hojas de trabajo** .

{{% /alert %}}

## **Vinculación de una hoja de trabajo con una base de datos mediante Worksheets Designer en VS.Net 2005**

 El propósito de este artículo es permitir que todos los desarrolladores aprendan cómo crear una aplicación de enlace de datos en**VS.Net 2005** y comprender el uso y la función de**Diseñador de hojas de trabajo** editor. La mejor manera de aprender y entender cualquier cosa es a través de ejemplos. Entonces, en este artículo, también sería mejor para nosotros crear una aplicación de muestra para demostrar el uso de**Diseñador de hojas de trabajo**en hojas de trabajo vinculantes con base de datos. Vamos a crear una aplicación paso a paso.

### **Paso 1: crear una base de datos de muestra**

 En primer lugar, crearemos una base de datos de muestra que se utilizará en este artículo. Hemos utilizado MS Access para crear una base de datos de muestra que contiene**productos** tabla cuyo esquema se muestra a continuación:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**Figura:** Información de diseño de**productos** mesa

 Se agregan pocos registros ficticios al**productos** tabla como se muestra a continuación en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**Figura:** Registros en**productos** mesa

### **Paso 2: Diseño de una aplicación de muestra**

 Un**ASP.NET Aplicación web** está creado y diseñado en Visual Studio.NET 2005 como se muestra en las siguientes figuras. Estas capturas de pantalla son útiles para aquellos desarrolladores que no están muy familiarizados con el uso de Aspose.Cells.GridWeb en Visual Studio.Net 2005.

Primero inicie VS.Net 2005.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**Figura:** A partir de VS.Net 2005

Cree un nuevo sitio web desde el menú Archivo|Nuevo|Sitio web....

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**Figura:** Creación de un nuevo sitio web

 Después de hacer clic en la opción de menú Archivo|Nuevo|Sitio web...,**Nuevo sitio web** se muestra el cuadro de diálogo. Haga clic en el**Navegar** botón en él.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**Figura:**Cuadro de diálogo Nuevo sitio web

 Después de hacer clic en el**Navegar** , elija la carpeta de ubicación en el IIS local. Puede crear una nueva carpeta y convertirla en una carpeta virtual como se muestra en la figura.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**Figura:** Crear una nueva carpeta


 Después de hacer clic en el**Abierto** botón en el**Elegir la ubicación** diálogo,**Nuevo sitio web** se verá el diálogo.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**Figura:** Configuración de la ubicación del proyecto

Ahora el proyecto está creado.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**Figura:** Proyecto creado

### **Modos XHTML y HTML**

**Aspose.Cells.GridWeb** es totalmente compatible con el modo XHTML que se implementa de forma predeterminada en VS.Net 2005 desde el**Modo Xhtml** propiedad de la**GridWeb** el control está puesto en**Verdadero** por defecto cuando coloca el control en la página web. Pero si desea implementar el modo HTML para el control en VS.Net 2005, puede hacerlo con bastante facilidad. Tienes que modificar el**<!DOCTYPE>** etiquetar un poco en el código fuente de la página web y configurar el**Modo Xhtml** propiedad de la**GridWeb** controlar a**Falso** .

#### **En este tema usaremos el Modo HTML para el control. Así que sigue los pasos a continuación**

##### **1. Cambie a la vista Fuente de la página web y busque la siguiente etiqueta <!DOCTYPE> en el código fuente.**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

Una vez que encuentre esa etiqueta, seleccione esa etiqueta completa en el código fuente como se muestra a continuación.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**Figura:** Seleccionando**etiqueta <!DOCTYPE>**

 Reemplace la**<!DOCTYPE>** etiqueta de su código fuente con la siguiente.

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**Figura:** modificando**etiqueta <!DOCTYPE>**

##### **2. Después, agregará el control GridWeb al formulario web. Debe seleccionar el control y elegir la propiedad XhtmlMode de la ventana Propiedades para establecerlo en Falso.**

**Agregar GridWeb al WebForm** 

 Haga clic derecho en**Caja de herramientas** y seleccione**Elija elementos...** del menú.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**Figura:** Elección de artículos

 Ahora seleccione**GridWeb** componente y haga clic**OK**

{{% alert color="primary" %}}

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**Figura:** Seleccionando**GridWeb** componente en el cuadro de diálogo de componentes

 Ahora el**GridWeb** se agrega como se muestra en la siguiente figura.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**Figura:** **GridWeb** se agrega en la caja de herramientas

 Colocar el**GridWeb** en el formulario web como se muestra a continuación.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**Figura:** Colocación**GridWeb** en la página web

{{% /alert %}} {{% alert color="primary" %}}

**Procedimiento** : Seleccione el control, Ahora, elija el**Modo Xhtml** propiedad de la**Propiedades** ventana y configúrelo en**Falso** valor.

{{% /alert %}}

##### **Paso 3: Conexión con la base de datos usando Server Explorer y configuración del objeto de conexión**

 Primero agregamos la base de datos de MS Access al proyecto que creamos previamente en**Paso 1** . Puedes ver eso**db.mdb** El archivo se agrega al proyecto.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**Figura:** Base de datos agregada a la carpeta del proyecto.

 Ahora, vamos a**Diseñador de componentes** ventana del formulario web utilizando la opción de menú contextual de la página web.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**Figura:** Seleccionando**Ver diseñador de componentes** opción

La ventana Diseñador de componentes se muestra a continuación.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**Figura:** Ventana del diseñador de componentes

 Haga doble clic en el**Conexión OleDb** componente del panel Datos para colocar el objeto oleDbConnection1 en la ventana.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**Figura:** objeto oleDbConnection1

 Ahora, es el momento de conectarse con la base de datos. Podemos hacerlo fácilmente usando**Explorador de servidores** en Visual Studio.NET 2005. Simplemente seleccione**Conección de datos** en**Explorador de servidores** y clic derecho. Verá un menú contextual que aparece frente a usted. Seleccione**Añadir conexión...**opción del menú como se muestra a continuación en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**Figura:** Seleccionando**Añadir conexión...** opción del menú


 Después de seleccionar**Añadir conexión...** opción del menú,**Agregar conexión** se abrirá el cuadro de diálogo y**Navegar** para seleccionar el archivo de base de datos como se muestra a continuación.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**Figura:** Selección del archivo de la base de datos

Puede probar la conexión.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**Figura:** Probando la conexión

Puede navegar por la conexión para comprobar la tabla y sus campos.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**Figura:** Comprobación de la tabla y sus campos de la conexión.

 Ahora si seleccionas**oleDbConnection1** objeto en el**Diseñador de componentes** ventana, puede seleccionar la cadena de conexión relacionada con la conexión existente que se acaba de crear, está allí en la propiedad "Cadena de conexión" de la**oleDbConnection1** objeto en la ventana Propiedades.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**Figura:** Selección de la cadena de conexión para el objeto

 Finalmente, el modificador del objeto se cambia a**Protegido** para una mejor accesibilidad.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**Figura:** Establecer el modificador del objeto

##### **Paso 4: Configuración del objeto del adaptador de datos**

 Ahora, agrega un**OleDbDataAdapterOleDbDataAdapter** componente del panel Datos en la caja de herramientas para configurarlo. Haga doble clic en el**OleDbDataAdapterOleDbDataAdapter** en el panel Datos de la caja de herramientas, iniciará su asistente de configuración y seleccionará la conexión existente como se muestra en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**Figura:** Asistente de configuración del adaptador de datos

 Después de hacer clic**próximo** botón, haga clic en el**Consultor de construcción** para agregar el**productos** tabla, seleccione Todas las columnas y haga clic en**OK** botón.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**Figura:** Agregar tabla de productos

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**Figura:** Consultor de construcción

 Ahora haga clic**Finalizar** botón para finalizar el asistente.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**Figura:** Terminando el mago

 Después de configurar el asistente, el oleDbDataAdapter1 se agrega automáticamente a la ventana como se muestra a continuación. Además, puede establecer su modificador en**Protegido**.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**Figura:** Recuperando el objeto OleDbDataAdapter en la ventana del diseñador

##### **Paso 5: Generación de DataSet**

 Como hemos creado una conexión de base de datos y objetos de adaptador de datos, aún necesitamos algo donde podamos almacenar datos después de conectarnos con la base de datos. A**conjunto de datos**El objeto puede almacenar datos con precisión y también podemos generarlos fácilmente usando VS.NET 2005 IDE. Para hacerlo, seleccione**oleDbDataAdaper1** y clic derecho. Aparecerá un menú contextual con algunas opciones. Seleccione**Generar** **Conjunto de datos...** opción del menú como se muestra a continuación en la figura.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**Figura:** Seleccionando**Generar** **Conjunto de datos...** opción del menú

 Después de seleccionar**Generar** **Conjunto de datos...** opción del menú, una**Generar conjunto de datos** se abriría el diálogo. Usando este diálogo, podemos seleccionar cuál sería el nombre del nuevo**conjunto de datos** objeto que se creará y qué tablas se deben agregar a**conjunto de datos** . Controlar**Agregar este conjunto de datos al diseñador** opción y haga clic**OK** como se muestra a continuación en la figura.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**Figura:** haciendo clic**OK** botón para generar**conjunto de datos**

 Ahora, puedes ver un**dataSet11** objeto agregado al diseñador como se muestra a continuación en la figura. Establezca el modificador de objeto en**Protegido**.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**Figura:** **conjunto de datos** generado y agregado a la ventana del diseñador

Cierto código se genera automáticamente en la conexión relacionada con el archivo .cs, el adaptador de datos, el objeto del conjunto de datos.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**Figura:** Código generado

##### **Paso 6: Usar el Diseñador de hojas de trabajo**

 Ahora, es hora de abrir el secreto. Seleccione el control y haga clic derecho. Se abriría un menú contextual. Seleccione la opción Worksheets Designer... del menú como se muestra a continuación en la figura.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**Figura:** Seleccionando**Diseñador de hojas de trabajo...** opción del menú

 Después**Editor de colección de hojas de trabajo** diálogo (también llamado**Diseñador de hojas de trabajo** ) se abrirá, puede ver varias propiedades que se pueden configurar para enlazar el**Hoja1** con cualquier tabla de la base de datos. seleccionemos**Fuente de datos** propiedad. Escribe**dataSet11** en él (que generamos y agregamos a la ventana del diseñador en el paso anterior). Luego haga clic en**miembro de datos** propiedad. Escribe**productos** como un nombre de tabla aquí como se muestra a continuación en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**Figura:** Ajuste**Fuente de datos** y**miembro de datos** propiedades

 Ahora, puedes configurar**BindColumns** propiedad. Después de hacer clic en él, ahora puede agregar las columnas de enlace y configurar el**Subtítulo** , **Campo de datos** (Debe ser igual que**productos** campos de tabla) y otras propiedades. Puede configurar el**EsAutoCreado** a**verdadero** y aplicar**Validación** y establecer el**NúmeroTipo**de diferentes campos para sus necesidades.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**Figura:** haciendo clic**BindColumns** propiedad

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**Figura:** **Editor de la colección BindColumn** diálogo

##### **Paso 7: agregar algunas líneas de código para la página web**

 Hemos usado**Diseñador de hojas de trabajo** fácilmente y ahora solo tenemos que agregar algunas líneas de código

 Primero agregaremos**OnInit** código relacionado con el evento para inicializar**InitializeComponent** método para inicializar y crear objetos de conexión, comando, adaptador de datos y conjunto de datos. Estas líneas de código no se agregan con el código generado automáticamente, por lo que debemos agregarlas manualmente.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**Figura:** Agregando algo de código1

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**Figura:** Agregando algo de código2

 Ahora agregamos algo de código en el**Cargar página** manejador de eventos para llenar**dataSet11** objeto con datos de la base de datos (usando**oleDbDataAdapter1** ) y vinculante**GridWeb** controlar con**dataSet11** llamando a su**enlace de datos** método.

{{% alert color="primary" %}}   {{% /alert %}}

##### **Ejemplo:**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

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

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

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

 También puede comprobar el código añadido a**Cargar página** controlador de eventos como se muestra a continuación en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**Figura:** Código añadido a**Cargar página** controlador de eventos

De lejos, hemos creado una aplicación de base de datos muy útil. Pero, esta aplicación solo le permite ver los datos de la tabla. Aunque puede editar datos en**GridWeb** pero cuando cerrará la ventana de su navegador y abrirá su base de datos. Usted encontraría que nada ha cambiado. Significa que los cambios que realizó no se guardan en la base de datos. Entonces, hay algo que tienes que hacer.

 Ahora agregaremos algo de código a nuestra aplicación para que**GridWeb** puede guardar sus cambios en la base de datos real. Vamos a abrir**Propiedades** panel y seleccione**GuardarComando** evento de la**GridWeb** control de la lista de sus eventos. Si hace doble clic en**GuardarComando** evento entonces VS.NET 2005 IDE creará**GridWeb1_SaveCommand** controlador de eventos para usted. Agregue código a este controlador de eventos para actualizar la base de datos con datos modificados contenidos en**conjunto de datos** (encuadernado con la hoja de trabajo) usando**oleDbDataAdapter1**.

##### **Ejemplo:**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

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

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

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

 También puede comprobar el código añadido a**GridWeb1_SaveCommand** controlador de eventos como se muestra a continuación en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**Figura:** Código añadido a**GridWeb1_SaveCommand** controlador de eventos

 Ahora, si guardará sus cambios en la base de datos usando**Ahorrar** botón de la**GridWeb** , definitivamente se salvarían.

##### **Paso 8: ejecutar su aplicación**

 Finalmente, podemos compilar y ejecutar nuestra aplicación presionando**Ctrl+F5** o haciendo clic**comienzo** botón. En el cuadro de diálogo de depuración, puede especificar la opción de depuración adecuada y hacer clic en**OK** como se muestra a continuación en la figura.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**Figura:** Aplicación en ejecución

 Después de la compilación,**Predeterminado.aspx** La página de nuestra aplicación web se abrirá en una nueva ventana del navegador donde podemos ver todos los datos cargados desde la base de datos como se muestra a continuación:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**Figura:** Datos cargados en**GridWeb** controlar desde la base de datos

 Cuando se cargan datos en**GridWeb** control entonces sentiría que Aspose.Cells.GridWeb proporciona un control implícito de datos a sus usuarios. Verifiquemos qué tipo de funciones de manipulación de datos ofrece**GridWeb** a sus usuarios.

##### **Validación de datos**

Aspose.Cells.GridWeb crea automáticamente reglas de validación apropiadas para todas las columnas enlazadas de acuerdo con sus tipos de datos definidos en la base de datos. Puede ver el tipo de validación de una celda al pasar el puntero del mouse sobre ella como se muestra a continuación en la figura:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**Figura:**Verificando el tipo de validación de una celda

 En la figura anterior, podemos ver que la celda seleccionada contiene**\<INT>** tipo de validación, lo que significa que los usuarios solo pueden ingresar un valor entero; de lo contrario, se producirá un error de validación. Es más,**\<OBLIGATORIO>** muestra que el valor de**identificación de producto** se requiere que sea enviado por el usuario.

##### **Eliminación de filas**

 Para eliminar una fila, primero debe seleccionar una fila (o cualquier celda de la fila) y seleccionar**Borrar fila** opción del menú contextual como se muestra a continuación:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**Figura:** Seleccionando**Borrar fila** opción del menú

 Después de seleccionar**Borrar fila** del menú, la fila se elimina de la**GridWeb** . Ahora haga clic**ahorrar** botón de la**GridWeb** para eliminar ese registro en la tabla de la base de datos original.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**Figura:** Datos de cuadrícula (después de eliminar una fila)

##### **Edición de filas**

 También puede editar datos en celdas o filas y luego hacer clic en**Ahorrar** botón para guardar los cambios.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**Figura:** Datos de cuadrícula (edición de registro 1)

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**Figura:** Datos de cuadrícula (edición de registro 2)

##### **Adición de filas**

 Para agregar una fila, seleccione**Añadir fila** opción del menú contextual como se muestra a continuación:

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**Figura:** Seleccionando**Añadir fila** opción del menú

Se agregará una nueva fila a la hoja al final de las filas después de seleccionar**Añadir fila** opción del menú. A la izquierda de la fila recién agregada, notará una**asterisco** marca, lo que indica que la fila es una recién agregada.

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**Figura:** Nueva fila agregada a Grid

 Después de ingresar los valores en la nueva fila, haga clic en**Ahorrar** botón para confirmar los cambios en la tabla de base de datos original como se muestra a continuación

![todo:imagen_alternativa_texto](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**Figura:** Guardar cambios en la tabla de la base de datos haciendo clic en**Ahorrar** botón

{{% alert color="primary" %}}   {{% /alert %}}

##### **Conclusión**

{{% alert color="primary" %}}

**El enlace de datos** es una característica importante de Aspose.Cells.GridWeb. Es muy fácil para los desarrolladores vincular sus hojas de trabajo con la base de datos usando**Diseñador de hojas de trabajo** utilidad ofrecida por Aspose.Cells.GridWeb. Aspose.Cells.GridWeb es muy útil para que los desarrolladores ahorren tiempo y esfuerzo en la creación de potentes soluciones Grid.

{{% /alert %}}
