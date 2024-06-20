---
title: Creando vista jerárquica de hoja
type: docs
weight: 30
url: /es/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb, jerárquico
description: Este artículo introduce cómo crear una vista jerárquica en GridWeb.
---

{{% alert color="primary" %}} 

La vinculación de datos es una característica poderosa y fácil de usar de GridWeb. Los datos almacenados en tablas de base de datos se recuperan a un DataSet y se llenan con datos 

representando las tablas de datos. Utilizando la característica de vinculación de datos, puedes crear una vista jerárquica (una vista maestro-hijo) de datos interconectados y 

mostrarla en el control para que sea más elegante. 

Este tema trata sobre la creación de una hoja de vista jerárquica. Algunas de las filas en la hoja tienen vistas secundarias. Cuando un usuario hace clic en **Expandir** de la fila

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**Una tabla con vista jerárquica** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Crear Relaciones para Tablas de Datos**
Por ejemplo, puedes usar la API de ADO.Net y extraer datos de las tablas de base de datos. Para crear una hoja de vista jerárquica, primero debes diseñar un DataSet

basado en algunas tablas y crear una relación entre ellas. Usa el **Diseñador de DataSet** de VS.NET para crear la relación. En 

este ejemplo, hay tres DataTables: Clientes, Órdenes, Detalles de la Órden. La hoja muestra toda la información del cliente por defecto. Cuando 

el usuario expande un cliente, el grid muestra todas las órdenes que ese cliente ha realizado. Cuando el usuario expande una orden, el grid muestra los detalles 

de esa orden. Los datos son jerárquicos: los detalles de la orden se enumeran bajo las órdenes, y las órdenes se enumeran bajo los clientes.

Para que esto funcione, las siguientes relaciones deben establecerse entre las tablas de datos:

1. Crear una clave foránea en el DataTable de Órdenes, el campo clave es CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




2. Crear una clave foránea en el DataTable de Detalles de la Órden, el campo clave es OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



El Diseñador de DataSet ahora se ve así: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Vincular Hoja de Cálculo**
Ahora usa el **Diseñador de Hojas de Cálculo** para establecer el Origen de Datos y el Miembro de Datos para la hoja de cálculo y configurar las columnas de enlace de campo de datos. 

El control agrega automáticamente un icono + para cada fila que corresponde a un registro cuyo objeto de enlace (generalmente un objeto DataRowView) tiene 

vistas secundarias. Cuando se hace clic en el icono +, el registro se expande para mostrar la vista secundaria. El ejemplo a continuación usa el **Diseñador de Hojas de Cálculo** para vincular el 

hoja de cálculo en la raíz del DataTable principal de Clientes. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Personalizar las columnas de vinculación de tablas secundarias**
El control provee un evento llamado GridWeb.BindingChildView que los desarrolladores utilizan para personalizar las columnas de vinculación de las tablas secundarias. Este ejemplo 

necesita mostrar el campo **Precio unitario** de los detalles del pedido en un formato de moneda. Agregar un manejador de eventos para cambiar el formato de número de la columna de vinculación. 

**C#**

{{< highlight csharp >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Cargar datos desde la base de datos y vinculación**
Como se describe en [Vincular Hoja de Cálculo a un Conjunto de Datos usando el Diseñador de Hojas de Cálculo de GridWeb](/cells/es/net/vincular-hoja-de-calculo-a-un-conjunto-de-datos-usando-el-diseñador-de-hojas-de-calculo-de-gridweb/),
necesitas agregar código al bloque Page_Load para cargar datos al DataSet desde una base de datos, y vincular el DataSet a la hoja en el 

próximo paso. 

La Clase Asppose.Grid.Web.Data.WebWorksheet tiene algunas propiedades útiles.

- Por ejemplo, la propiedad EnableCreateBindColumnHeader se utiliza para crear los encabezados de la columna vinculada dentro de la hoja, o los encabezados de columna

muestran los nombres de la columna vinculada. Toma los valores **true** o **false**. 

- Las propiedades BindStartRow y BindStartColumn especifican la posición en la hoja del control GridWeb que debería estar vinculado a la fuente.
- La propiedad EnableExpandChildView se utiliza para deshabilitar la vista secundaria expandida para la hoja. Por defecto está configurado en true.

La clase también tiene algunos métodos útiles. 

- El método DataBind() vincula una hoja con la fuente de datos.
- El método CreateNewBindRow() agrega una nueva fila y la vincula a la fuente de datos.
- El método DeleteBindRow() elimina una fila vinculada.
- El método SetRowExpand() establece la fila expandida y muestra el contenido de la vista secundaria en el modo de vinculación de datos.
- El método GetRowExpand() obtiene un valor booleano que indica si la fila está expandida o no.

En el código a continuación, el objeto DataSet "dataSet21" se llena con datos basados en tres tablas. La tabla de Clientes se filtra para que sea la primera tabla en la vista jerárquica. Se crea un objeto WebWorksheet llamado "sheet", que primero borra la hoja y luego la establece 

vinculada a la fuente de datos. 

**VB.NET** 

**C#**

{{< highlight csharp >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
