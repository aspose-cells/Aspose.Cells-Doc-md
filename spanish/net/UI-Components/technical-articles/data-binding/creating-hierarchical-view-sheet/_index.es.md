---
title: Crear hoja de vista jerárquica
type: docs
weight: 30
url: /es/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 El enlace de datos es una función potente y fácil de usar de GridWeb. Los datos almacenados en las tablas de la base de datos se obtienen en un DataSet y se llenan con datos

 representando las tablas de datos. Con la función de vinculación de datos, puede crear una vista jerárquica (una vista maestro-secundario) de datos interrelacionados y

 mostrarlo en el control para hacerlo más elegante.

 Este tema trata sobre la creación de una hoja de vista jerárquica. Algunas de las filas de la hoja tienen vistas secundarias. Cuando un usuario hace clic en la fila**Expandir**

 botón{{< emoticons/cross >}} , la tabla de vista secundaria de esa fila se expande hacia abajo. Esta función es muy útil para crear un informe de vista jerárquica.

**Una tabla con una vista jerárquica** 

![todo:imagen_alternativa_texto](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Crear relaciones para DataTables**
Por ejemplo, usa ADO.Net API y extrae datos de las tablas de la base de datos. Para crear una hoja de vista jerárquica, debe diseñar un DataSet

 objeto basado en algunas tablas y cree una relación entre ellos primero. Utilice los VS.NET**Diseñador de conjuntos de datos** para crear la relación. En

 En este ejemplo, hay tres DataTables: Clientes, Pedidos, Detalles del pedido. La hoja muestra toda la información del cliente por defecto. Cuando

 el usuario expande un cliente, la cuadrícula muestra todos los pedidos que ha realizado el cliente. Cuando el usuario expande un pedido, la grilla muestra los detalles

de ese orden. Los datos son jerárquicos: los detalles del pedido se enumeran en pedidos y los pedidos se enumeran en clientes.

Para que esto funcione, se deben establecer las siguientes relaciones entre las tablas de datos:

1.  Cree una clave externa en los pedidos de DataTable, el campo clave es CustomerID

![todo:imagen_alternativa_texto](creating-hierarchical-view-sheet_2.png)




1. Cree una clave externa en Detalles de pedido de DataTable, el campo clave es OrderID.

![todo:imagen_alternativa_texto](creating-hierarchical-view-sheet_3.png)



 El diseñador de conjuntos de datos ahora se ve así:

![todo:imagen_alternativa_texto](creating-hierarchical-view-sheet_4.png)
### **Encuadernar hoja de trabajo**
 Ahora usa el**Diseñador de hojas de trabajo** para establecer DataSource y DataMember para la hoja de trabajo y configurar las columnas de enlace de campo de datos.

 El control agrega automáticamente un ícono + para cada fila que corresponde a un registro cuyo objeto vinculante (generalmente un objeto DataRowView) tiene

 opiniones de niños. Cuando se hace clic en el ícono +, el registro se expande para mostrar la vista secundaria. El siguiente ejemplo utiliza el**Diseñador de hojas de trabajo** para atar el

 hoja de trabajo a los Clientes de DataTable padre raíz.

![todo:imagen_alternativa_texto](creating-hierarchical-view-sheet_5.png)
### **Personalizar las columnas de enlace de las tablas secundarias**
 El control proporciona un evento llamado GridWeb.BindingChildView que los desarrolladores usan para personalizar las columnas de vinculación de las tablas secundarias. este ejemplo

 necesita mostrar los detalles del pedido'**Precio unitario** campo en un formato de moneda. Agregue un controlador de eventos para cambiar el formato de número de la columna de vinculación.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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
Como se describe en[Vinculación de una hoja de trabajo a un conjunto de datos mediante el diseñador de hojas de trabajo de GridWeb](/cells/es/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 necesita agregar código al bloque Page_Load para cargar datos al DataSet desde una base de datos, y vincular el DataSet a la hoja en el

 próximo paso.

La clase Asppose.Grid.Web.Data.WebWorksheet tiene algunas propiedades útiles.

- Por ejemplo, la propiedad EnableCreateBindColumnHeader se usa para crear los encabezados de la columna enlazada dentro de la hoja, o la columna

 headers muestra los nombres de las columnas enlazadas. toma los valores**verdadero** o**falso**. 

- Las propiedades BindStartRow y BindStartColumn especifican la posición en la hoja del control GridWeb a la que debe vincularse el origen.
- La propiedad EnableExpandChildView se usa para deshabilitar la vista secundaria expandida para la hoja de cálculo. De forma predeterminada, se establece en verdadero.

 La clase también tiene algunos métodos útiles.

- El método DataBind() vincula una hoja con la fuente.
- CreateNewBindRow() agrega una nueva fila y la vincula a la fuente de datos.
- DeleteBindRow() elimina una fila enlazada.
- El método SetRowExpand() establece la fila expandida y muestra el contenido de la vista secundaria en el modo de enlace de datos.
- El método GetRowExpand() obtiene un valor booleano que indica si la fila se expande o no.

 En el siguiente código, el objeto DataSet "dataSet21" se llena con datos basados en tres tablas. La tabla Clientes se filtra para convertirla en la

 primera tabla en la visualización jerárquica. Se crea un objeto WebWorksheet llamado "hoja", que primero borra la hoja y luego la establece

 vinculado a la fuente de datos.

**C#**

{{< highlight "csharp" >}}

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

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

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

{{< highlight "csharp" >}}

 Private Sub Page_Load (ByVal sender As System.Object, ByVal e As System.EventArgs) Maneja MyBase.Load

 'Ponga el código de usuario para inicializar la página aquí

 If Not IsPostBack Entonces

 BindWithoutInSheetHeaders()

 Terminara si

Finalizar sub

Enlace secundario privado sin encabezados de hoja ()

 Dim db como DemoDatabase2 = Nueva DemoDatabase2()

Dim ruta como cadena = MapPath(".")

 ruta = ruta.Subcadena(0, ruta.LastIndexOf("\"))

 ruta = ruta.Subcadena(0, ruta.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Proveedor=Microsoft.Jet.OLEDB.4.0;Fuente de datos=" + ruta + "\Base de datos\Northwind.mdb"

 Probar

 ' Se conecta a la base de datos y obtiene datos.

 'Tabla de Clientes.

 db.OleDbDataAdapter1.Fill(DataSet21)

 'Tabla de pedidos.

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' TablaDetallesPedido.

 db.OleDbDataAdapter3.Fill(DataSet21)

 ' Filtrar datos

 DataSet21.Customers.DefaultView.RowFilter = "ID de cliente<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

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
