---
title: Licencias
type: docs
weight: 120
url: /es/net/licensing/
description: Aspose.Cells for .NET ofrece diferentes planes para comprar u ofrece un Prueba Gratuita y una Licencia Temporal de 30 días para evaluación utilizando políticas de Licenciamiento y Suscripción en C#.
keywords: C# Aplicar Licencia desde Disco o Stream. C# Establecer Licencia desde Disco o Stream. Aplicar Licencia en Aspose.Cells for NET.
---

## **Cómo Aplicar una Licencia en el Componente Aspose.Cells**

La licencia es un archivo XML de texto plano que contiene detalles como el nombre del producto, número de desarrolladores con licencia, fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifiques. Incluso la adición inadvertida de un salto de línea extra en el archivo lo invalidará. Necesitas establecer una licencia antes de utilizar Aspose.Cells si deseas evitar su limitación de evaluación. Solo es necesario establecer una licencia una vez por aplicación (o proceso). La licencia se puede cargar desde un archivo, stream o un recurso incrustado.

Aspose.Cells intenta encontrar la licencia en las siguientes ubicaciones:

- Ruta explícita
- La carpeta que contiene Aspose.Cells.dll
- La carpeta que contiene el ensamblado que llamó a Aspose.Cells.dll
- La carpeta que contiene el ensamblado de entrada (tu .exe)
- Un recurso incrustado en el ensamblado que llamó a Aspose.Cells.dll

Existen dos métodos comunes para aplicar una licencia, desde un archivo o stream, o como un recurso incrustado.

### **Cómo aplicar una licencia desde un disco o un flujo**

La forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que la de Aspose.Cells.dll y especificar solo el nombre de archivo sin su ruta.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llamas al método SetLicense, el nombre de la licencia debe ser igual al de tu archivo de licencia. Por ejemplo, puedes cambiar el nombre del archivo de licencia a ** Aspose.Cells.lic.xml **. Luego en tu código, debes usar el nombre de licencia modificado (** Aspose.Cells.lic.xml **) para el método SetLicense.

{{% /alert %}}

También es posible cargar una licencia desde un flujo.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Cómo aplicar una licencia medida**

Aspose.Cells permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de licencias. Este nuevo mecanismo de licencias se utilizará junto con el método de licenciamiento existente. Aquellos clientes que deseen ser facturados en función del uso de las funciones de la API pueden utilizar el licenciamiento medido. Para más detalles, consulte sección de [Preguntas frecuentes sobre Licenciamiento Medido](https://purchase.aspose.com/faqs/licensing/metered).  

Se ha introducido una nueva clase [Medido](https://reference.aspose.com/cells/net/aspose.cells/metered) para aplicar una clave medida. A continuación se muestra el código de muestra que demuestra cómo configurar la clave pública y privada medida.

{{< highlight csharp >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

### **Cómo usar un recurso incrustado**

Otra forma adecuada de empaquetar la licencia con su aplicación y asegurarse de que no se pierda, es incluirla como un recurso incrustado en uno de los ensamblados que llama a Aspose.Cells. Para incluir el archivo de licencia como un recurso incrustado, realice los siguientes pasos:

1. En Visual Studio .NET, incluya el archivo de licencia (.lic) en el proyecto seleccionando **Agregar elemento existente** en el menú **Archivo**.
1. Seleccione el archivo en el Explorador de soluciones y establezca la **Acción de compilación** en **Recurso incrustado** en la ventana de Propiedades

Para acceder a la licencia incrustada en el ensamblado (como recurso incrustado), no es necesario llamar a los métodos GetExecutingAssembly y GetManifestResourceStream de la clase System.Reflection.Assembly del Framework de Microsoft .NET. Todo lo que se necesita hacer es agregar el archivo de licencia como un recurso incrustado a su proyecto y pasar el nombre del archivo de licencia al método SetLicense. La clase **Aspose.Cells.License** encontrará automáticamente el archivo de licencia en los recursos incrustados. Por favor, revise el ejemplo dado a continuación para entender este método de configurar la licencia (incrustada) en sus aplicaciones.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Cómo establecer una licencia en los controles de cuadrícula de Aspose.Cells**

En el conjunto de cuadrícula de Aspose.Cells, la licencia se puede cargar desde un archivo, un flujo o un recurso incrustado. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb intenta encontrar la licencia en las siguientes ubicaciones:

1. Ruta explícita
1. La carpeta que contiene el dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La carpeta que contiene el ensamblado que llamó al dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La carpeta que contiene el ensamblado de entrada (su .exe)
1. Un recurso incrustado en el ensamblado que llamó al dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Si está utilizando el control Aspose.Cells.GridDesktop, entonces se usará la clase de licencia como Aspose.Cells.GridDesktop.License pero si está utilizando el control Aspose.Cells.GridWeb, entonces se usará la clase Aspose.Cells.GridWeb.License para establecer la licencia.

{{% /alert %}}

### **Cómo aplicar una licencia desde un disco o un flujo**

La forma más sencilla de establecer una licencia es poner el archivo de licencia en la misma carpeta que la del dll del componente (incluido en Aspose.Cells.GridWeb) y especificar solo el nombre de archivo sin su ruta.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llame al método SetLicense, el nombre de la licencia debe ser el mismo que el de su archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia por "MyLicense.lic.xml". Luego, en su código, debe usar el nombre de licencia modificado (es decir, MyLicense.lic.xml) para el método SetLicense.

{{% /alert %}}

También es posible cargar una licencia desde un flujo.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Cómo aplicar una licencia como un recurso incrustado**

Otra forma adecuada de empaquetar la licencia con su aplicación y asegurarse de que no se pierda, es incluirla como un recurso incrustado en uno de los ensamblajes que llama al archivo dll del componente (incluido en Aspose.Cells.GridDesktop). Para incluir el archivo de licencia como un recurso incrustado, realice los siguientes pasos:

1. En Visual Studio .NET, incluya el archivo de licencia (.lic) en el proyecto utilizando la opción **Agregar elemento existente** en el menú **Archivo**.
1. Seleccione el archivo en el Explorador de soluciones y establezca la acción de compilación en Recurso incrustado en la ventana de propiedades.
1. Para acceder a la licencia incrustada en el ensamblado (como recurso incrustado), no es necesario llamar a los métodos GetExecutingAssembly y GetManifestResourceStream de la clase System.Reflection.Assembly de Microsoft .NET Framework. En su lugar, agregue el archivo de licencia como un recurso incrustado en su proyecto y pase el nombre del archivo de licencia al método SetLicense. La clase License encuentra automáticamente el archivo de licencia en los recursos incrustados.

Por favor, revise el ejemplo dado a continuación para entender este método de aplicar una licencia como un recurso incrustado a sus aplicaciones.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Cómo aplicar una licencia en Aspose.Cells.GridDesktop para una aplicación WinForm**

Se recomienda que coloque su código de licencia antes de que su aplicación se inicie y aplíquelo solo una vez. Por ejemplo, para una aplicación C# de Windows, coloque el código de licencia en el método Main.

{{< highlight csharp >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

## **Notas sobre la aplicación de una licencia en Aspose.Cells.GridWeb**

Se recomienda colocar el código de licencia en Global.asax.cs de su aplicación web (se supone que este archivo de licencia se encuentra en la unidad "d:\").

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Cargando una licencia desde un flujo

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
