---
title: Создание иерархического представления листа
type: docs
weight: 30
url: /ru/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb,иерархический
description: В данной статье рассматривается создание иерархического представления в GridWeb.
---

{{% alert color="primary" %}} 

Привязка данных - мощная и удобная функция GridWeb. Данные, хранящиеся в таблицах базы данных, извлекаются в DataSet и заполняются данными, представляющими таблицы данных. Используя функцию привязки данных, вы можете создать иерархическое представление (мастер-дочернее представление) взаимосвязанных данных и отображать его в элементе управления, сделав его более элегантным. 

Создание листа с иерархическим представлением. Некоторые строки в листе имеют дочерние представления. Когда пользователь щелкает по строке **Развернуть** 

отобразите его в контроле, чтобы сделать его более элегантным. 

В этой статье обсуждается создание иерархического представления листа. У некоторых строк в листе есть дочерние представления. Когда пользователь нажимает на **Развернуть** строки

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**Таблица с иерархическим видом** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Создать отношения для DataTables**
Например, вы используете ADO.Net API и извлекаете данные из таблиц базы данных. Чтобы создать таблицу иерархического вида, вы должны спроектировать DataSet

объект на основе некоторых таблиц и сначала создать отношение между ними. Используйте **DataSet Designer** в VS.NET для создания отношения. В 

данном примере есть три DataTables: Customers, Orders, Order Details. Таблица по умолчанию отображает всю информацию о клиентах. Когда 

пользователь разворачивает клиента, сетка показывает все заказы, которые этот клиент разместил. Когда пользователь разворачивает заказ, сетка показывает детали 

этого заказа. Данные иерархичны: детали заказа перечислены под заказами, а заказы перечислены под клиентами.

Для этого необходимо установить следующие отношения между таблицами данных:

1. Создание внешнего ключа в DataTable Orders, где поле ключа - CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Создание внешнего ключа в DataTable Order Details, где поле ключа - OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



Теперь Designer DataSet выглядит так: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Привязать к рабочему листу**
Теперь используйте **Worksheets Designer** для установки источника данных и члена данных для рабочего листа и настройки привязки столбцов данных. 

Элемент управления автоматически добавляет значок + для каждой строки, которая соответствует записи, у которой связанный объект (как правило, объект DataRowView) имеет 

дочерние представления. Когда вы щелкаете значок +, запись разворачивается, чтобы показать дочернее представление. В приведенном ниже примере используется **Worksheets Designer** для привязки 

лист к корневой родительской DataTable Customers. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Настройка привязки дочерних столбцов таблиц**
Элемент управления предоставляет событие GridWeb.BindingChildView, которое разработчики используют для настройки привязки дочерних столбцов таблиц. В этом примере 

необходимо отображение поля **UnitPrice** деталей заказа в валютном формате. Добавьте обработчик событий для изменения числового формата привязки столбца. 

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
### **Загрузите данные из базы данных и привяжите их**
Как описано в [Привязка листа к набору данных с помощью конструктора листов GridWeb](/cells/ru/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
вам нужно добавить код в блок Page_Load для загрузки данных из базы данных в DataSet и привязки DataSet к листу на следующем шаге. 

Далее. 

У класса Asppose.Grid.Web.Data.WebWorksheet есть несколько полезных свойств.

- Например, свойство EnableCreateBindColumnHeader используется для создания заголовков привязанного столбца в листе или отображения заголовков столбцов,

связанные с именами столбцов. Оно принимает значения **true** или **false**. 

- Свойства BindStartRow и BindStartColumn указывают позицию в листе элемента управления GridWeb, который должен быть привязан к источнику.
- Свойство EnableExpandChildView используется для отключения расширенного дочернего представления для листа. По умолчанию оно установлено в true.

У класса также есть несколько полезных методов. 

- Метод DataBind() связывает лист с источником.
- Метод CreateNewBindRow() добавляет новую строку и привязывает ее к источнику данных.
- Метод DeleteBindRow() удаляет привязанную строку.
- Метод SetRowExpand() устанавливает расширенную строку и отображает содержимое дочернего представления в режиме привязки данных.
- Метод GetRowExpand() возвращает логическое значение, указывающее, расширена ли строка или нет.

В приведенном ниже коде объект DataSet "dataSet21" заполняется данными на основе трех таблиц. Таблица Customers фильтруется, чтобы стать 

первой таблицей в иерархическом отображении. Создается объект WebWorksheet с именем "sheet", который сначала очищает лист, а затем устанавливает его 

связанным с источником данных. 

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
