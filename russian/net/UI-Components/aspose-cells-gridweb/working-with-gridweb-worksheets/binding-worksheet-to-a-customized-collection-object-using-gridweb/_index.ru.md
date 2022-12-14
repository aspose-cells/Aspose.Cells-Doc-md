---
title: Привязка рабочего листа к настраиваемому объекту коллекции с помощью GridWeb
type: docs
weight: 130
url: /ru/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Платформа Microsoft .NET Framework предлагает множество классов коллекций, но иногда они не соответствуют требованиям разработки, поэтому разработчики создают**пользовательские коллекции**, и может потребоваться привязка таких пользовательских коллекций к Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Связывание рабочего листа с пользовательской коллекцией**
Чтобы проиллюстрировать эту функцию, в этой статье шаг за шагом описывается создание примера приложения. Сначала создайте пользовательскую коллекцию, а затем используйте эту коллекцию для привязки к рабочему листу.
### **Шаг 1. Создание пользовательской записи**
Перед созданием пользовательской коллекции создайте класс для хранения пользовательских записей, которые будут храниться в коллекции. Цель этой статьи — дать представление о том, как создавать собственные настраиваемые коллекции и привязывать их к Aspose.Cells.GridWeb, поэтому то, как вы создаете настраиваемые записи, зависит от вас.

В приведенном ниже примере используется класс MyCustomRecord, который содержит пять частных полей и пять общедоступных свойств, управляющих доступом к закрытым полям. Вот структура свойств:

-  Свойство StringField1 для чтения и записи**строковое поле1** (нить).
-  Свойство ReadonlyField2 только для чтения**строковое поле2** (нить).
-  Свойство DateField1 для чтения и записи**поле даты1** (дата/время).
-  Свойство IntField1 для чтения и записи**intfield1** (целое число).
-  Свойство DoubleField1 для чтения и записи**даблфилд1** (двойной).

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
### **Шаг 2. Создание пользовательской коллекции**
Теперь создайте пользовательскую коллекцию, чтобы добавить записи о клиентах и получить к ним доступ. Для простоты в этом примере используется класс MyCollection, который содержит индексатор только для чтения. Используя этот индексатор, мы можем получить любую пользовательскую запись, хранящуюся в коллекции.

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
### **Шаг 3: привязка рабочего листа к пользовательской коллекции**
Процесс создания пользовательской коллекции завершен. Теперь используйте пользовательскую коллекцию для привязки к рабочему листу в Aspose.Cells.GridWeb . Сначала создайте веб-форму, добавьте в нее элемент управления GridWeb и добавьте некоторый код.

Чтобы использовать пользовательскую коллекцию для привязки, сначала создайте объект класса MyCollection (созданный на шаге выше).
Затем создайте и добавьте объекты MyCustomRecord в объект MyCollection.

{{% alert color="primary" %}} 

Вам интересно, почему в классе MyCollection не было метода для добавления объекта MyCustomRecord в коллекцию. Взгляните еще раз на приведенный выше код, и вы заметите, что класс MyCollection унаследован от класса CollectionBase (в котором реализован интерфейс IList, предоставляющий метод Add для добавления объекта в коллекцию). Используйте метод Add класса IList, преобразовав объект MyCollection в IList.

{{% /alert %}} 

Наконец, установите объект MyCollection в качестве источника данных рабочего листа и свяжите рабочий лист с коллекцией. На этом этапе вы также можете создать правила проверки для связанных столбцов рабочего листа.

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
### **Шаг 4. Обработка события InitializeNewBindRow рабочего листа**
В приведенном выше коде вы могли заметить дополнительную строку кода, используемую для назначения обработчика событий GridWeb1_InitializeNewBindRow свойству InitializeNewBindRow рабочего листа. Это событие запускается всякий раз, когда на лист добавляется новая связанная строка. Мы создали обработчик событий для этого события из-за свойства DateField1 объекта MyCustomRecord.

 Aspose.Cells.GridWeb автоматически инициализируется**инт** а также**двойной** значения с**ноль (0)**всякий раз, когда в элемент управления GridWeb добавляется новая связанная строка. Для дат мы хотели бы, чтобы элемент управления GridWeb автоматически добавлял текущую дату из системы. Для этого мы создали обработчик событий GridWeb1_InitializeNewBindRow для события InitializeNewBindRow.

Получите доступ к конкретному экземпляру класса MyCustomRecord из GridWeb с помощью аргумента bindObject, а затем назначьте текущую системную дату его свойству DateField1.

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
### **Шаг 5: Запуск приложения**
 Запустите приложение, нажав**Ctrl+F5** или нажав на**Начинать** кнопка в VS.NET. Веб-форма открывается в новом окне браузера.

**Рабочий лист, связанный с пользовательской коллекцией** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Щелкните правой кнопкой мыши элемент управления GridWeb, чтобы добавить или удалить запись. Например, добавьте новую запись на лист, выбрав**Добавить ряд** вариант.

**Выбор опции «Добавить строку» в меню** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 Когда на лист добавляется новая строка, ячейки содержат данные по умолчанию, включая текущую системную дату.

**На лист добавлена новая строка с данными по умолчанию** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



После внесения изменений в данные нажмите**Сохранять** или же**Представлять на рассмотрение** чтобы сохранить изменения.

**Сохранение изменений нажатием кнопки Сохранить** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Вывод**
{{% alert color="primary" %}} 

В этой статье показано, как привязать рабочий лист к созданной пользовательской коллекции. Используя Aspose.Cells.GridWeb, разработчики могут привязывать рабочие листы либо к базе данных, либо к пользовательским коллекциям с помощью конструктора рабочих листов в режиме графического интерфейса пользователя или с помощью кодирования. Это предоставляет разработчикам широкий спектр возможностей для создания приложений.

{{% /alert %}}
