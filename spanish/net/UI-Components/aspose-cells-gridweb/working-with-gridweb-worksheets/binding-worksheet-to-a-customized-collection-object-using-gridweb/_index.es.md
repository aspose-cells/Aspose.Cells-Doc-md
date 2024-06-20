---
title: Vinculación de Hoja de Cálculo a un Objeto de Colección Personalizado utilizando GridWeb
type: docs
weight: 130
url: /es/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: Este artículo presenta cómo vincular hoja de cálculo a una colección en GridWeb. 
---

{{% alert color="primary" %}} 

El framework Microsoft .NET ofrece muchas clases de colección pero a veces no cumplen con los requisitos de desarrollo, por lo que los desarrolladores crean **colecciones personalizadas**, y puedes vincular una hoja de cálculo con esas colecciones personalizadas en GridWeb.

{{% /alert %}} 
## **Vinculación de una Hoja de Cálculo con una Colección Personalizada**
Para ilustrar esta característica, este artículo explica cómo crear una aplicación de ejemplo, paso a paso. Primero, crea una colección personalizada y luego utiliza esa colección para vincularla con una hoja de cálculo.
### **Paso 1: Crear un Registro Personalizado**
Antes de crear una colección personalizada, crea una clase para contener los registros personalizados que se almacenarán en la colección. El propósito de este artículo es dar una idea de cómo crear tus propias colecciones personalizadas y vincularlas con GridWeb, por lo que la forma de crear el registro personalizado depende de ti.

El ejemplo a continuación utiliza la clase MyCustomRecord que contiene cinco campos privados y cinco propiedades públicas que controlan el acceso a los campos privados. Aquí tienes la estructura de las propiedades:

- La propiedad StringField1 para leer y escribir **stringfield1** (cadena).
- La propiedad ReadonlyField2 para solo leer **stringfield2** (cadena).
- La propiedad DateField1 para leer y escribir **datefield1** (DateTime).
- La propiedad IntField1 para leer y escribir **intfield1** (entero).
- La propiedad DoubleField1 para leer y escribir **doublefield1** (doble).

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
### **Paso 2: Crear una colección personalizada**
Ahora, cree una colección personalizada para agregar registros de clientes y acceder a ellos. Para simplificar, este ejemplo utiliza la clase MyCollection que contiene un indexador de solo lectura. Usando este indexador, podemos obtener cualquier registro personalizado almacenado en la colección.

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
### **Paso 3: Vincular una hoja de cálculo con una colección personalizada**
El proceso de creación de una colección personalizada está completo. Ahora use la colección personalizada para enlazar a una hoja de cálculo en Aspose.Cells.GridWeb . Primero, cree un formulario web, agregue el control GridWeb a él y agregue algo de código.

Para usar la colección personalizada para el enlace, primero cree un objeto de la clase MyCollection (creada en el paso anterior).
Luego, cree y agregue objetos MyCustomRecord al objeto MyCollection.

{{% alert color="primary" %}} 

¿Te preguntas por qué no hubo un método en la clase MyCollection para agregar un objeto MyCustomRecord a la colección? Echa otro vistazo al código anterior y notarás que la clase MyCollection hereda de la clase CollectionBase (que ha implementado la interfaz IList que proporciona un método Add para agregar un objeto a la colección). Usa el método Add de la clase IList al hacer upcasting del objeto MyCollection a IList.

{{% /alert %}} 

Finalmente, establezca el objeto MyCollection como origen de datos de la hoja de cálculo y vincule la hoja de cálculo con la colección. En este punto, también puedes crear reglas de validación para las columnas vinculadas de la hoja de cálculo.

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
### **Paso 4: Manejar el evento InitializeNewBindRow de la hoja de cálculo**
En el código anterior, es posible que hayas notado una línea adicional de código utilizada para asignar el controlador de eventos GridWeb1_InitializeNewBindRow al evento InitializeNewBindRow de la hoja de cálculo. Este evento se activa cada vez que se agrega una nueva fila vinculada a la hoja de cálculo. Creamos un controlador de eventos para este evento debido a la propiedad DateField1 del objeto MyCustomRecord.

Aspose.Cells.GridWeb inicializa automáticamente los valores **int** y **double** con **cero (0)** cada vez que se agrega una nueva fila vinculada al control GridWeb. Para las fechas, nos gustaría que el control GridWeb agregue automáticamente la fecha actual del sistema. Para hacerlo, hemos creado el controlador de eventos GridWeb1_InitializeNewBindRow para el evento InitializeNewBindRow.

Acceda a una instancia particular de la clase MyCustomRecord desde el GridWeb usando el argumento bindObject y luego asigne la fecha actual del sistema a su propiedad DateField1.

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
### **Paso 5: Ejecutar la aplicación**
Ejecute la aplicación presionando **Ctrl+F5** o haciendo clic en el botón **Inicio** en VS.NET. El formulario web se abrirá en una nueva ventana del navegador. 

**Hoja de cálculo vinculada con una colección personalizada** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



Haga clic con el botón derecho en el control GridWeb para agregar o eliminar un registro. Por ejemplo, agregue un nuevo registro a la hoja de cálculo seleccionando la opción **Agregar fila**. 

**Seleccionar la opción Agregar fila desde el menú** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



Cuando se agrega una nueva fila a la hoja de cálculo, las celdas contienen datos predeterminados, incluida la fecha del sistema actual. 

**Nueva fila agregada a la hoja de cálculo con datos predeterminados** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Después de realizar cambios en los datos, haga clic en **Guardar** o **Enviar** para guardar sus cambios. 

**Guardar los cambios haciendo clic en el botón Guardar** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Conclusión**
{{% alert color="primary" %}} 

Este artículo mostró cómo vincular una hoja de cálculo a una colección personalizada creada. Usando Aspose.Cells.GridWeb, los desarrolladores pueden vincular hojas de cálculo a una base de datos o colecciones personalizadas a través del Diseñador de Hojas de Cálculo en modo GUI o a través de programación. Esto brinda una amplia gama de opciones a los desarrolladores para crear aplicaciones.

{{% /alert %}}
