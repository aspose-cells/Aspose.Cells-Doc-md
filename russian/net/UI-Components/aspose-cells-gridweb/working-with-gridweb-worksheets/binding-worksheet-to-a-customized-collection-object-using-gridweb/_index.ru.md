---
title: Привязка рабочего листа к настраиваемому объекту коллекции с использованием GridWeb
type: docs
weight: 130
url: /ru/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: В этой статье рассматривается способ привязки рабочего листа к коллекции в GridWeb. 
---

{{% alert color="primary" %}} 

Фреймворк Microsoft .NET предлагает множество классов коллекций, но иногда они не удовлетворяют требованиям разработки, поэтому разработчики создают **собственные коллекции**, и вы можете привязать рабочий лист к таким настраиваемым коллекциям в GridWeb.

{{% /alert %}} 
## **Привязка рабочего листа с настраиваемой коллекцией**
Чтобы проиллюстрировать эту особенность, в этой статье пошагово описывается, как создать образец приложения. Сначала создайте настраиваемую коллекцию, а затем используйте эту коллекцию для привязки с рабочим листом.
### **Шаг 1: Создание пользовательской записи**
Перед созданием пользовательской коллекции создайте класс для хранения пользовательских записей, которые будут храниться в коллекции. Цель этой статьи - дать представление о том, как создавать собственные коллекции и связывать их с GridWeb, поэтому способ создания пользовательской записи зависит от вас.

Приведенный ниже пример использует класс MyCustomRecord, который содержит пять частных полей и пять общедоступных свойств, контролирующих доступ к частным полям. Вот структура свойств:

- Свойство StringField1 для чтения и записи **stringfield1** (строка).
- Свойство ReadonlyField2 для чтения только **stringfield2** (строка).
- Свойство DateField1 для чтения и записи **datefield1** (DateTime).
- Свойство IntField1 для чтения и записи **intfield1** (целое число).
- Свойство DoubleField1 для чтения и записи **doublefield1** (вещественное число).

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
### **Шаг 2: Создание пользовательской коллекции**
Теперь создайте пользовательскую коллекцию для добавления записей клиентов и доступа к ним. Для простоты в этом примере используется класс MyCollection, который содержит только для чтения индексатор. Используя этот индексатор, мы можем получить любую пользовательскую запись, хранящуюся в коллекции.

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
### **Шаг 3: Привязка рабочего листа к пользовательской коллекции**
Процесс создания пользовательской коллекции завершен. Теперь используйте пользовательскую коллекцию для привязки к рабочему листу в Aspose.Cells.GridWeb. Сначала создайте веб-форму, добавьте к ней элемент управления GridWeb и добавьте немного кода.

Чтобы использовать пользовательскую коллекцию для привязки, сначала создайте объект класса MyCollection (созданный на предыдущем этапе).
Затем создайте и добавьте объекты MyCustomRecord в объект MyCollection.

{{% alert color="primary" %}} 

Возможно, вы удивлены тем, что в классе MyCollection не был создан метод для добавления объекта MyCustomRecord в коллекцию. Еще раз взгляните на приведенный выше код, и вы заметите, что класс MyCollection наследуется от класса CollectionBase (который реализует интерфейс IList, который предоставляет метод Add для добавления объекта в коллекцию). Используйте метод Add класса IList, приведя объект MyCollection к IList.

{{% /alert %}} 

Наконец, установите объект MyCollection в качестве источника данных рабочего листа и привяжите рабочий лист к коллекции. В этот момент вы также можете создать правила проверки для привязанных столбцов рабочего листа.

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
### **Шаг 4: Обработка события InitializeNewBindRow рабочего листа**
В приведенном выше коде вы, возможно, заметили дополнительную строку кода, используемую для присвоения обработчика событий GridWeb1_InitializeNewBindRow рабочему листу. Это событие срабатывает каждый раз, когда к рабочему листу добавляется новая привязанная строка. Мы создали обработчик этого события из-за свойства DateField1 объекта MyCustomRecord.

Aspose.Cells.GridWeb автоматически инициализирует значения **int** и **double** значением **ноль (0)** всякий раз, когда в элемент управления GridWeb добавляется новая привязанная строка. Для дат мы хотели бы, чтобы элемент управления GridWeb автоматически добавлял текущую дату из системы. Для этого мы создали обработчик события GridWeb1_InitializeNewBindRow для события InitializeNewBindRow.

Доступ к определенному экземпляру класса MyCustomRecord из GridWeb с использованием аргумента bindObject, а затем присвоение текущей системной даты его свойству DateField1.

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
### **Шаг 5: Запуск приложения**
Запустите приложение, нажав **Ctrl+F5** или нажав кнопку **Start** в VS.NET. Веб-форма откроется в новом окне браузера. 

**Рабочий лист привязан к пользовательской коллекции** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



Щелкните правой кнопкой мыши по элементу управления GridWeb, чтобы добавить или удалить запись. Например, добавьте новую запись на рабочий лист, выбрав **Добавить строку**. 

**Выбор опции Добавить строку из меню** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



Когда новая строка добавляется на рабочий лист, ячейки содержат данные по умолчанию, включая текущую системную дату. 

**Новая строка добавлена на рабочий лист со значениями по умолчанию** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



После внесения изменений в данные нажмите **Сохранить** или **Подтвердить**, чтобы сохранить ваши изменения. 

**Сохраните изменения, нажав кнопку Сохранить** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Заключение**
{{% alert color="primary" %}} 

Эта статья показывает, как привязать лист к пользовательской коллекции, созданной. Используя Aspose.Cells.GridWeb, разработчики могут привязать листы к базе данных или пользовательским коллекциям через конструктор листов в режиме GUI или через кодирование. Это предоставляет широкий спектр опций для создания приложений.

{{% /alert %}}
