---
title: Vinculación de una hoja de trabajo a un objeto de colección personalizado mediante GridWeb
type: docs
weight: 130
url: /es/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 El marco Microsoft .NET ofrece muchas clases de colección, pero a veces no cumplen con los requisitos de desarrollo, por lo que los desarrolladores crean**colecciones personalizadas**, y puede requerir vincular dichas colecciones personalizadas con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Encuadernación de una hoja de trabajo con una colección personalizada**
Para ilustrar esta característica, este artículo explica cómo crear una aplicación de muestra, paso a paso. Primero, cree una colección personalizada y luego use esa colección para enlazar con una hoja de trabajo.
### **Paso 1: crear un registro personalizado**
Antes de crear una colección personalizada, cree una clase para contener los registros personalizados que se almacenarán en la colección. El propósito de este artículo es dar una idea de cómo crear sus propias colecciones personalizadas y vincularlas con Aspose.Cells.GridWeb, de modo que la forma de crear el registro personalizado depende de usted.

El siguiente ejemplo usa la clase MyCustomRecord que contiene cinco campos privados y cinco propiedades públicas que controlan el acceso a los campos privados. Aquí está la estructura de las propiedades:

-  La propiedad StringField1 para leer y escribir**campo de cadena1** (cuerda).
-  La propiedad ReadonlyField2 para solo leer**campo de cuerdas2** (cuerda).
-  La propiedad DateField1 para leer y escribir**campo de fecha1** (Fecha y hora).
-  La propiedad IntField1 para leer y escribir**intfield1** (entero).
-  La propiedad DoubleField1 para leer y escribir**campo doble1** (doble).

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
### **Paso 2: crear una colección personalizada**
Ahora, cree una colección personalizada para agregar registros de clientes y acceder a ellos. Para hacerlo simple, este ejemplo usa la clase MyCollection que contiene un indexador de solo lectura. Usando este indexador, podemos obtener cualquier registro personalizado almacenado en la colección.

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
### **Paso 3: Encuadernación de una hoja de trabajo con una colección personalizada**
El proceso de creación de una colección personalizada está completo. Ahora use la colección personalizada para enlazar a una hoja de trabajo en Aspose.Cells.GridWeb. Primero cree un formulario web, agréguele el control GridWeb y agregue algo de código.

Para usar la colección personalizada para el enlace, primero cree un objeto de la clase MyCollection (creado en el paso anterior).
Luego cree y agregue objetos MyCustomRecord al objeto MyCollection.

{{% alert color="primary" %}} 

¿Se pregunta por qué no había un método en la clase MyCollection para agregar un objeto MyCustomRecord a la colección? Eche otro vistazo al código anterior y notará que la clase MyCollection se hereda de la clase CollectionBase (que ha implementado la interfaz IList que proporciona un método Add para agregar un objeto a la colección). Utilice el método Add de la clase IList al convertir el objeto MyCollection en IList.

{{% /alert %}} 

Finalmente, configure el objeto MyCollection como fuente de datos de la hoja de trabajo y vincule la hoja de trabajo con la colección. En este punto, también puede crear reglas de validación para las columnas enlazadas de la hoja de trabajo.

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
### **Paso 4: Manejo del evento InitializeNewBindRow de la hoja de trabajo**
En el código anterior, es posible que haya notado una línea adicional de código que se usa para asignar el controlador de eventos GridWeb1_InitializeNewBindRow a InitializeNewBindRow de la hoja de trabajo. Este evento se activa cada vez que se agrega una nueva fila enlazada a la hoja de trabajo. Creamos un controlador de eventos para este evento debido a la propiedad DateField1 del objeto MyCustomRecord.

 Aspose.Cells.GridWeb se inicializa automáticamente**En t** y**doble** valores con**cero (0)**cada vez que se agrega una nueva fila enlazada al control GridWeb. Para las fechas, nos gustaría que el control GridWeb agregue automáticamente la fecha actual del sistema. Para ello, hemos creado el controlador de eventos GridWeb1_InitializeNewBindRow para el evento InitializeNewBindRow.

Acceda a una instancia particular de la clase MyCustomRecord desde GridWeb usando el argumento bindObject y luego asigne la fecha actual del sistema a su propiedad DateField1.

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
### **Paso 5: ejecutar la aplicación**
 Ejecute la aplicación presionando**Ctrl+F5** o haciendo clic en el**comienzo** botón en VS.NET. El formulario web se abre en una nueva ventana del navegador.

**Hoja de trabajo encuadernada con una colección personalizada** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Haga clic con el botón derecho en el control GridWeb para agregar o eliminar un registro. Por ejemplo, agregue un nuevo registro a la hoja de cálculo seleccionando**Añadir fila** opción.

**Seleccionar la opción Agregar fila del menú** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 Cuando se agrega una nueva fila a la hoja de cálculo, las celdas contienen datos predeterminados, incluida la fecha actual del sistema.

**Nueva fila agregada a la hoja de trabajo con datos predeterminados** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Después de realizar cambios en los datos, haga clic en**Ahorrar** o**Enviar** para guardar sus cambios.

**Guardar cambios haciendo clic en el botón Guardar** 

![todo:imagen_alternativa_texto](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Conclusión**
{{% alert color="primary" %}} 

Este artículo mostró cómo vincular una hoja de trabajo a una colección personalizada creada. Usando Aspose.Cells.GridWeb, los desarrolladores pueden vincular hojas de trabajo a una base de datos o colecciones personalizadas a través del Diseñador de hojas de trabajo en un modo GUI o mediante codificación. Esto proporciona una amplia gama de opciones a los desarrolladores para crear aplicaciones.

{{% /alert %}}
