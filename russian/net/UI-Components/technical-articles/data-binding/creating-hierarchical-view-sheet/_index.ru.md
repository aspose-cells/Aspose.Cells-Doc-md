---
title: Создание иерархического представления листа
type: docs
weight: 30
url: /ru/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 Привязка данных — это мощная и удобная функция GridWeb. Данные, хранящиеся в таблицах базы данных, извлекаются в DataSet и заполняются данными.

 представляющие таблицы данных. Используя функцию привязки данных, вы можете создать иерархическое представление (представление главный-дочерний) взаимосвязанных данных и

 отобразите его в элементе управления, чтобы сделать его более элегантным.

 В этом разделе обсуждается создание иерархического листа представления. Некоторые строки на листе имеют дочерние представления. Когда пользователь щелкает строку**Расширять**

 кнопка{{< emoticons/cross >}} , дочерняя таблица представления этой строки разворачивается вниз. Эта функция очень полезна для создания иерархического отчета.

**Таблица с иерархическим представлением** 

![дело:изображение_альтернативный_текст](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Создание отношений для таблиц данных**
Например, вы используете ADO.Net API и извлекаете данные из таблиц базы данных. Чтобы создать лист с иерархическим представлением, необходимо спроектировать набор данных.

 объект на основе некоторых таблиц и сначала создайте связь между ними. Используйте VS.NET**Конструктор наборов данных** для создания отношений. В

 В этом примере есть три таблицы данных: «Клиенты», «Заказы», «Сведения о заказе». По умолчанию на листе отображается вся информация о клиенте. Когда

 пользователь раскрывает клиента, в сетке отображаются все заказы, размещенные клиентом. Когда пользователь расширяет заказ, в сетке отображаются детали

того порядка. Данные иерархичны: сведения о заказе перечислены под заказами, а заказы — под клиентами.

Чтобы это работало, между таблицами данных должны быть установлены следующие отношения:

1.  Создайте внешний ключ для DataTable Orders, ключевое поле — CustomerID.

![дело:изображение_альтернативный_текст](creating-hierarchical-view-sheet_2.png)




1. Создайте внешний ключ в DataTable Order Details, ключевое поле — OrderID.

![дело:изображение_альтернативный_текст](creating-hierarchical-view-sheet_3.png)



 Конструктор набора данных теперь выглядит так:

![дело:изображение_альтернативный_текст](creating-hierarchical-view-sheet_4.png)
### **Связать рабочий лист**
 Теперь используйте**Дизайнер рабочих листов** чтобы установить DataSource и DataMember для рабочего листа и настроить столбцы привязки полей данных.

 Элемент управления автоматически добавляет значок + для каждой строки, соответствующей записи, объект привязки которой (обычно объект DataRowView) имеет

 просмотры ребенка. При нажатии значка + запись расширяется, чтобы показать дочернее представление. В приведенном ниже примере используется**Дизайнер рабочих листов** связать

 листа в корневой родительский DataTable Customers.

![дело:изображение_альтернативный_текст](creating-hierarchical-view-sheet_5.png)
### **Настройка столбцов привязки дочерних таблиц**
 Элемент управления предоставляет событие с именем GridWeb.BindingChildView, которое разработчики используют для настройки столбцов привязки дочерних таблиц. Этот пример

 необходимо отобразить детали заказа'**Цена за единицу** поле в формате валюты. Добавьте обработчик событий, чтобы изменить числовой формат столбца привязки.

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
### **Загрузка данных из базы данных и привязка**
Как описано в[Привязка рабочего листа к набору данных с помощью конструктора рабочих листов GridWeb](/cells/ru/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 вам нужно добавить код в блок Page_Load для загрузки данных в DataSet из базы данных и привязать DataSet к листу в

 следующий шаг.

Класс Asppose.Grid.Web.Data.WebWorksheet имеет несколько полезных свойств.

- Например, свойство EnableCreateBindColumnHeader используется для создания заголовков связанного столбца на листе или столбца

 headers отображает имена связанных столбцов. Он принимает значения**истинный** или же**ЛОЖЬ**. 

- Свойства BindStartRow и BindStartColumn указывают положение на листе элемента управления GridWeb, к которому должен быть привязан источник.
- Свойство EnableExpandChildView используется для отключения расширенного дочернего представления для рабочего листа. По умолчанию установлено значение true.

 Класс также имеет несколько полезных методов.

- Метод DataBind() связывает лист с источником.
- CreateNewBindRow() добавляет новую строку и привязывает ее к источнику данных.
- DeleteBindRow() удаляет связанную строку.
- Метод SetRowExpand() задает расширенную строку и показывает содержимое дочернего представления в режиме привязки данных.
- Метод GetRowExpand() получает логическое значение, указывающее, расширена строка или нет.

 В приведенном ниже коде объект DataSet «dataSet21» заполняется данными на основе трех таблиц. Таблица Customers фильтруется, чтобы сделать ее

 первая таблица в иерархическом отображении. Создается объект WebWorksheet с именем «лист», который сначала очищает лист, а затем устанавливает его.

 привязан к источнику данных.

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

 Private Sub Page_Load (отправитель ByVal As System.Object, ByVal e As System.EventArgs) обрабатывает MyBase.Load

 'Поместите код пользователя для инициализации страницы здесь

 Если не IsPostBack, то

 BindWithoutInSheetHeaders()

 Конец, если

Конец сабвуфера

Частный Sub BindWithoutInSheetHeaders()

 Dim db As DemoDatabase2 = New DemoDatabase2()

Тусклый путь As String = MapPath(".")

 путь = путь.Подстрока(0, путь.LastIndexOf("\"))

 путь = путь.Подстрока(0, путь.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Источник данных=" + путь + "\Database\Northwind.mdb"

 Пытаться

 ' Подключается к базе данных и получает данные.

 «Таблица клиентов.

 db.OleDbDataAdapter1.Fill(DataSet21)

 «Таблица заказов.

 db.OleDbDataAdapter2.Fill(DataSet21)

 'Таблица деталей заказа.

 db.OleDbDataAdapter3.Fill(DataSet21)

 ' Данные фильтра

 DataSet21.Customers.DefaultView.RowFilter = "Код клиента<'BSAAA'"

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
