---
title: 将工作表绑定到使用 GridWeb 的自定义集合对象
type: docs
weight: 130
url: /zh/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: 本文介绍了如何在 GridWeb 中将工作表绑定到集合。 
---

{{% alert color="primary" %}} 

Microsoft .NET Framework 提供了许多集合类，但有时它们无法满足开发需求，因此开发人员会创建自定义集合，并可以将工作表与 GridWeb 中的这些自定义集合绑定。

{{% /alert %}} 
## **将工作表与自定义集合绑定**
为了说明这一特性，本文逐步演示了如何创建一个示例应用程序。首先创建一个自定义集合，然后使用该集合与工作表进行绑定。
### **第一步：创建自定义记录**
在创建自定义集合之前，创建一个类来保存将存储在集合中的自定义记录。本文旨在介绍如何创建自己的自定义集合并将其与 GridWeb 进行绑定，因此如何创建自定义记录由您决定。

下面的示例使用了 MyCustomRecord 类，其中包含了五个私有字段和五个控制对私有字段访问的公共属性。以下是属性的结构：

- StringField1 属性用于读取和写入 stringfield1（字符串）。
- ReadonlyField2 属性仅用于读取 stringfield2（字符串）。
- DateField1 属性用于读取和写入 datefield1（DateTime）。
- IntField1 属性用于读取和写入 intfield1（整数）。
- DoubleField1 属性用于读取和写入 doublefield1（双精度）。

**C#**

{{< highlight csharp >}}

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
### **第二步：创建自定义集合**
现在，创建一个自定义集合，以添加客户记录并从中访问。为了简单起见，本示例使用了包含只读索引器的 MyCollection 类。通过使用此索引器，我们可以获取存储在集合中的任何自定义记录。

**C#**

{{< highlight csharp >}}

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
### **第三步：将工作表与自定义集合绑定**
创建自定义集合的过程已经完成。现在在 Aspose.Cells.GridWeb 中使用自定义集合绑定到一个工作表。首先创建一个 Web 表单，向其添加 GridWeb 控件并添加一些代码。

要使用自定义集合进行绑定，首先创建 MyCollection 类的对象（在上述步骤中创建）。
然后创建并将MyCustomRecord对象添加到MyCollection对象中。

{{% alert color="primary" %}} 

您是否在想为什么MyCollection类中没有添加MyCustomRecord对象的方法到集合中。再看一下上面的代码，你会注意到MyCollection类是从CollectionBase类继承而来的（它实现了IList接口，提供了用于向集合添加对象的Add方法）。通过向上转型将MyCollection对象转换为IList，使用IList类的Add方法。

{{% /alert %}} 

最后，将MyCollection对象设置为工作表的数据源，并将工作表与该集合绑定。此时，还可以为工作表的绑定列创建验证规则。

**C#**

{{< highlight csharp >}}

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
### **步骤4: 处理工作表的InitializeNewBindRow事件**
在上面的代码中，您可能已经注意到使用了一行额外的代码，将GridWeb1_InitializeNewBindRow事件处理程序分配给工作表的InitializeNewBindRow。当向工作表添加新的绑定行时，将触发此事件。我们为此事件创建了一个事件处理程序，是因为MyCustomRecord对象的DateField1属性。

Aspose.Cells.GridWeb 在向 GridWeb 控件添加新的绑定行时，会自动用零（0）初始化 **int** 和 **double** 值。对于日期，我们希望 GridWeb 控件自动从系统中添加当前日期。为此，我们已经为 InitializeNewBindRow 事件创建了 GridWeb1_InitializeNewBindRow 事件处理程序。

使用 bindObject 参数从 GridWeb 中访问 MyCustomRecord 类的特定实例，然后将当前系统日期分配给其 DateField1 属性。

**C#**

{{< highlight csharp >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **步骤 5: 运行应用程序**
通过按 **Ctrl+F5** 或在 VS.NET 中单击 **开始** 按钮来运行应用程序。Web 表单将在新的浏览器窗口中打开。 

**使用自定义集合绑定工作表** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



右键单击 GridWeb 控件以添加或删除记录。例如，通过选择 **添加行** 选项向工作表添加新记录。 

**从菜单中选择添加行选项** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



向工作表添加新行时，单元格包含默认数据，包括当前系统日期。 

**向工作表添加含默认数据的新行** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



对数据进行更改后，单击 **保存** 或 **提交** 以保存更改。 

**通过单击保存按钮保存更改** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **结论**
{{% alert color="primary" %}} 

本文介绍了如何将工作表绑定到创建的自定义集合。使用 Aspose.Cells.GridWeb，开发人员可以通过工作表设计器在 GUI 模式或通过编码将工作表绑定到数据库或自定义集合。这为开发人员提供了广泛的选项来创建应用程序。

{{% /alert %}}
