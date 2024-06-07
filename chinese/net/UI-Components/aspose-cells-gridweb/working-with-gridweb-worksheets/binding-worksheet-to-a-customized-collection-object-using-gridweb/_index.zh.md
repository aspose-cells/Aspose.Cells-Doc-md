---
title: 使用GridWeb将工作表绑定到自定义集合对象
type: docs
weight: 130
url: /zh/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb，绑定
description: 本文介绍了如何在GridWeb中将工作表绑定到集合。 
---

{{% alert color="primary" %}} 

Microsoft .NET Framework提供了许多集合类，但有时它们无法满足开发需求，因此开发人员创建**自定义集合**，您可以将工作表与GridWeb中的此类自定义集合绑定。

{{% /alert %}} 
## **将工作表与自定义集合绑定**
为了说明此功能，本文逐步介绍了如何创建一个示例应用程序。首先，创建一个自定义集合，然后使用该集合来进行绑定。
### **步骤1：创建自定义记录**
在创建自定义集合之前，创建一个类来存储将存储在该集合中的自定义记录。本文的目的是介绍如何创建自定义集合并将其与GridWeb进行绑定，因此创建自定义记录的方式由您自行决定。

下面的示例使用了包含五个私有字段和五个公共属性的MyCustomRecord类来控制对私有字段的访问。以下是属性的结构：

- StringField1属性用于读写stringfield1（字符串）。
- ReadonlyField2属性只用于读取stringfield2（字符串）。
- DateField1属性用于读写datefield1（日期时间）。
- IntField1属性用于读写intfield1（整数）。
- DoubleField1属性用于读写doublefield1（浮点数）。

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
### **第2步：创建自定义集合**
现在，创建一个自定义集合用于添加和访问客户记录。为了简单起见，本例使用了包含只读索引器的MyCollection类。使用这个索引器，我们可以获取存储在集合中的任何自定义记录。

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
### **第3步：将工作表与自定义集合绑定**
创建自定义集合的过程已经完成。现在使用自定义集合将其与Aspose.Cells.GridWeb中的工作表绑定。首先创建一个web表单，将GridWeb控件添加到其中，并添加一些代码。

要使用自定义集合进行绑定，首先创建一个MyCollection类的对象（在上一步中创建）。
然后在MyCollection对象中创建并添加MyCustomRecord对象。

{{% alert color="primary" %}} 

你是否想知道为什么在MyCollection类中没有一个方法用于将MyCustomRecord对象添加到集合中。重新看一下上面的代码，你会注意到MyCollection类继承自CollectionBase类（该类实现了IList接口，提供了一个Add方法用于将对象添加到集合中）。通过将MyCollection对象向上转型为IList，使用IList类的Add方法。

{{% /alert %}} 

最后，将MyCollection对象设置为工作表的数据源，并将工作表与集合绑定。此时，还可以为工作表的绑定列创建验证规则。

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
### **第4步：处理工作表的InitializeNewBindRow事件**
在上面的代码中，你可能注意到多了一行代码，用于将GridWeb1_InitializeNewBindRow事件处理程序分配给工作表的InitializeNewBindRow事件。每当向工作表添加新的绑定行时，该事件将被触发。我们为该事件创建了一个事件处理程序，是因为MyCustomRecord对象的DateField1属性。

当向GridWeb控件添加新的绑定行时，Aspose.Cells.GridWeb会自动使用零（0）初始化int和double值。对于日期，我们希望GridWeb控件自动添加来自系统的当前日期。为此，我们为InitializeNewBindRow事件创建了GridWeb1_InitializeNewBindRow事件处理程序。

使用bindObject参数从GridWeb中访问MyCustomRecord类的特定实例，然后将当前系统日期分配给其DateField1属性。

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
### **第5步：运行应用程序**
通过按下Ctrl + F5或点击VS.NET中的开始按钮来运行应用程序。网页表单将在新的浏览器窗口中打开。 

**与自定义集合绑定的工作表** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



右键单击GridWeb控件以添加或删除记录。例如，通过选择**添加行**选项向工作表添加新记录。 

**从菜单中选择添加行选项** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



当向工作表添加新行时，单元格中包含默认数据，包括当前系统日期。 

**添加带有默认数据的新行到工作表** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



在对数据进行更改后，点击**保存**或**提交**来保存更改。 

**通过点击保存按钮保存更改** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **结论**
{{% alert color="primary" %}} 

本文介绍了如何将工作表与创建的自定义集合绑定。使用Aspose.Cells.GridWeb，开发人员可以通过GUI模式或编程方式将工作表绑定到数据库或自定义集合，为开发人员提供了广泛的选择。

{{% /alert %}}
