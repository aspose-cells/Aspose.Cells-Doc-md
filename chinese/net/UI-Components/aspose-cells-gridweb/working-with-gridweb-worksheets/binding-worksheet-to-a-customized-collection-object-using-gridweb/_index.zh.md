---
title: 使用 GridWeb 将工作表绑定到自定义集合对象
type: docs
weight: 130
url: /zh/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Microsoft .NET Framework 提供了很多集合类，但有时它们不能满足开发需求，因此开发人员创建**自定义集合**，并且可能需要将此类自定义集合与 Aspose.Cells.GridWeb 绑定。

{{% /alert %}} 
## **将工作表与自定义集合绑定**
为了说明此功能，本文逐步介绍了如何创建示例应用程序。首先，创建一个自定义集合，然后使用该集合与工作表进行绑定。
### **第 1 步：创建自定义记录**
在创建自定义集合之前，创建一个类来保存将存储在集合中的自定义记录。本文的目的是让您了解如何创建自己的自定义集合并将它们与 Aspose.Cells.GridWeb 绑定，因此如何创建自定义记录由您决定。

下面的示例使用 MyCustomRecord 类，它包含五个私有字段和五个控制对私有字段的访问的公共属性。这是属性的结构：

-  StringField1 属性读写**字符串字段 1** （细绳）。
-  ReadonlyField2 属性只读**字符串字段2** （细绳）。
-  DateField1 属性读写**日期字段 1** （约会时间）。
-  IntField1 属性读写**场域1** （整数）。
-  DoubleField1 属性读写**双场1** （双倍的）。

**C#**

{{< highlight "csharp" >}}

 //Creating a class that will act as record for the custom collection

public class MyCustomRecord

{

    //Private data members

    private string stringfield1;

    private string stringfield2 = "ABC";

    private DateTime datefield1;

    private int intfield1;

    private double doublefield1;

    //Creating a string property

    public string StringField1

    {

        get { return stringfield1; }

        set { stringfield1 = value; }

    }

    //Creating a readonly string property

    public string ReadonlyField2

    {

        get { return stringfield2; }

    }

    //Creating a DateTime property

    public DateTime DateField1

    {

        get { return datefield1; }

        set { datefield1 = value; }

    }

    //Creating an int property

    public int IntField1

    {

        get { return intfield1; }

        set { intfield1 = value; }

    }

    //Creating a double property

    public double DoubleField1

    {

        get { return doublefield1; }

        set { doublefield1 = value; }

    }

}

{{< /highlight >}}
### **第 2 步：创建自定义集合**
现在，创建一个自定义集合来添加客户记录并从中访问它们。为简单起见，此示例使用包含只读索引器的 MyCollection 类。使用此索引器，我们可以获得存储在集合中的任何自定义记录。

**C#**

{{< highlight "csharp" >}}

 //Creating a custom collection

public class MyCollection : CollectionBase

{

    //Leaving the collection constructor empty

    public MyCollection()

    {

    }

    //Creating a readonly property for custom collection. This Item property is used by GridWeb control to

    //determine the collection's type

    public MyCustomRecord this[int index]

    {

        get { return (MyCustomRecord)this.List[index]; }

    }

}

{{< /highlight >}}
### **第 3 步：将工作表与自定义集合绑定**
创建自定义集合的过程已完成。现在使用自定义集合绑定到 Aspose.Cells.GridWeb 中的工作表。首先创建一个Web 窗体，向其中添加GridWeb 控件并添加一些代码。

要使用自定义集合进行绑定，首先创建 MyCollection 类的对象（在上述步骤中创建）。
然后创建 MyCustomRecord 对象并将其添加到 MyCollection 对象。

{{% alert color="primary" %}} 

您是否想知道为什么 MyCollection 类中没有用于将 MyCustomRecord 对象添加到集合中的方法。再看一下上面的代码，您会注意到 MyCollection 类是从 CollectionBase 类继承的（它实现了 IList 接口，该接口提供了用于将对象添加到集合中的 Add 方法）。通过将 MyCollection 对象向上转换为 IList 使用 IList 类的 Add 方法。

{{% /alert %}} 

最后，将 MyCollection 对象设置为工作表的数据源，并将工作表与集合绑定。此时，您还可以为工作表的绑定列创建验证规则。

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

    {

        //Creating an object of custom collection

        MyCollection list = new MyCollection();

        //Creating an instance of Random class

        System.Random rand = new System.Random();

        //Creating a loop that will run 5 times

        for (int i = 0; i < 5; i++)

        {

            //Creating an object of Custom Record

            MyCustomRecord rec = new MyCustomRecord();

            //Initializing all properties of Custom Record

            rec.DateField1 = DateTime.Now;

            rec.DoubleField1 = rand.NextDouble() * 10;

            rec.IntField1 = rand.Next(20);

            rec.StringField1 = "ABC_" + i;

            //Adding Custom Record to Collection

            ((IList)list).Add(rec);

        }

        //Accessing a desired worksheet

        GridWorksheet sheet = GridWeb1.WorkSheets[0];

        //Setting the Data Source of worksheet

        sheet.DataSource = list;

        //Creating columns automatically

        sheet.CreateAutoGenratedColumns();

        //Setting the validation type of value to DateTime

        sheet.BindColumns[2].Validation.ValidationType = ValidationType.DateTime;

        //Binding worksheet

        sheet.DataBind();

        //Assigning an event handler to InitializeNewBindRow event of the worksheet

        //sheet.InitializeNewBindRow += new InitializeNewBindRowHandler(GridWeb1_InitializeNewBindRow);

    }

}

{{< /highlight >}}
### **第 4 步：处理工作表的 InitializeNewBindRow 事件**
在上面的代码中，您可能已经注意到用于将 GridWeb1_InitializeNewBindRow 事件处理程序分配给工作表的 InitializeNewBindRow 的额外代码行。每当将新的绑定行添加到工作表时都会触发此事件。由于 MyCustomRecord 对象的 DateField1 属性，我们为此事件创建了一个事件处理程序。

 Aspose.Cells.GridWeb自动初始化**整数**和**双倍的**价值与**零 (0)**每当新的绑定行添加到 GridWeb 控件时。对于日期，我们希望 GridWeb 控件自动添加来自系统的当前日期。为此，我们为 InitializeNewBindRow 事件创建了 GridWeb1_InitializeNewBindRow 事件处理程序。

使用 bindObject 参数从 GridWeb 访问 MyCustomRecord 类的特定实例，然后将当前系统日期分配给它的 DateField1 属性。

**C#**

{{< highlight "csharp" >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **第 5 步：运行应用程序**
通过按**Ctrl+F5**或点击**开始**VS.NET 中的按钮。 Web 表单将在新的浏览器窗口中打开。

**与自定义集合绑定的工作表** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



右键单击 GridWeb 控件以添加或删除记录。例如，通过选择向工作表添加一条新记录**添加行**选项。

**从菜单中选择添加行选项** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



将新行添加到工作表时，单元格包含默认数据，包括当前系统日期。

**使用默认数据添加到工作表的新行** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



更改数据后，单击**救球**要么**提交**保存您的更改。

**通过单击保存按钮保存更改** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **结论**
{{% alert color="primary" %}} 

本文介绍了如何将工作表绑定到创建的自定义集合。使用 Aspose.Cells.GridWeb，开发人员可以通过工作表设计器以 GUI 模式或通过编码将工作表绑定到数据库或自定义集合。这为开发人员创建应用程序提供了广泛的选择。

{{% /alert %}}
