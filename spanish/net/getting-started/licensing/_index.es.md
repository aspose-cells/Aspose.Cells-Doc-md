---
title: Licencia
type: docs
weight: 120
url: /es/net/licensing/
---
{{% alert color="primary" %}}

 Puede descargar fácilmente una versión de evaluación de Aspose.Cells desde su[página de descarga](https://www.nuget.org/packages/Aspose.Cells) @ NuGet repos. La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del componente. Además, la versión de evaluación simplemente obtiene la licencia cuando compra una licencia y agrega un par de líneas de código para aplicar la licencia.

{{% /alert %}}

## **Limitaciones de la versión de evaluación**

La versión de evaluación del producto Aspose.Cells (sin una licencia especificada) proporciona la funcionalidad completa del producto, pero está limitada a abrir 100 archivos en un programa y una hoja de trabajo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

- **Número de archivos abiertos** (Aspose.Cells)
Al ejecutar su programa, solo puede abrir 100 archivos de Excel usando la biblioteca Aspose.Cells. Si su aplicación excede este número, se lanzará una excepción.
- **Configuración del archivo de configuración** (Aspose.Cells.GridWeb)
 No puede volver a especificar la ruta del script agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config). El acw_client es una carpeta que contiene archivos y Aspose.Cells. GridWeb usa esta carpeta para administrar su configuración interna, tiene archivos de script, archivos de imagen y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. El archivo de configuración se usa para evitar que el control use los recursos del cliente incorporado (imágenes, scripts, etc.), lo cual es útil en algunos casos/escenarios. Además, estos ajustes de configuración en el archivo web.config solo tendrán efecto con la versión CON LICENCIA del control.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Esta configuración puede ser obligatoria en algunos casos/escenarios si está utilizando el control Aspose.Cells.GridWeb en sitios web del sistema de archivos o extensiones de MS Ajax, etc.

{{% /alert %}}

Además, una hoja de trabajo con marca de agua de evaluación siempre se mostrará como la hoja de trabajo activa en el archivo de Excel generado usando la biblioteca Aspose.Cells. Solo en la versión con licencia, puede configurar la hoja de trabajo activa en otras hojas de trabajo. En el archivo de imagen o PDF de salida por Aspose.Cells, se pegaría una marca de agua de evaluación en la parte superior del documento/imagen. No puede ocultar la Advertencia de derechos de autor de evaluación (la hoja de trabajo adicional) en el control GridWeb también, siempre se agregará (al final en las pestañas de la hoja de trabajo) en el control.

{{% alert color="primary" %}}

 Si desea probar Aspose.Cells sin limitaciones de la versión de evaluación, también puede solicitar una[Licencia temporal de 30 días](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Aplicación de una licencia en el componente Aspose.Cells**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores para los que tiene licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique. Incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará. Debe configurar una licencia antes de utilizar Aspose.Cells si desea evitar su limitación de evaluación. Solo se requiere establecer una licencia una vez por aplicación (o proceso). La licencia se puede cargar desde un archivo, transmisión o un recurso incrustado.

Aspose.Cells intenta encontrar la licencia en las siguientes ubicaciones:

- Ruta explícita
- La carpeta que contiene Aspose.Cells.dll
- La carpeta que contiene el ensamblado llamado Aspose.Cells.dll
- La carpeta que contiene el ensamblado de entrada (su .exe)
- Un recurso incrustado en el ensamblado que llamó a Aspose.Cells.dll

Existen dos métodos comunes para aplicar una licencia, desde un archivo o transmisión, o como un recurso incrustado.

### **Aplicación de una licencia desde disco o transmisión**

La forma más fácil de configurar una licencia es colocar el archivo de licencia en la misma carpeta que el de Aspose.Cells.dll y especificar solo el nombre del archivo sin su ruta.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

 Cuando llama al método SetLicense, el nombre de la licencia debe ser el mismo que el nombre de su archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia a**Aspose.Cells.lic.xml**. Luego, en su código, debe usar el nombre de licencia modificado (**Aspose.Cells.lic.xml**) para el método SetLicense.

{{% /alert %}}

También es posible cargar una licencia desde un stream.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Aplicación de licencia medida**

Aspose.Cells permite a los desarrolladores aplicar la clave medida. Es un nuevo mecanismo de licencia. El nuevo mecanismo de concesión de licencias se utilizará junto con el método de concesión de licencias existente. Aquellos clientes que deseen que se les facture en función del uso de las funciones API pueden utilizar la licencia medida. Para obtener más detalles, consulte[Preguntas frecuentes sobre licencias medidas](https://purchase.aspose.com/faqs/licensing/metered)sección.

una nueva clase[medido](https://reference.aspose.com/cells/net/aspose.cells/metered)se ha introducido para aplicar la clave medida. El siguiente es el código de muestra que demuestra cómo establecer una clave pública y privada medida.

{{< highlight "csharp" >}}

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

### **Uso de un recurso integrado**

Otra forma ordenada de empaquetar la licencia con su aplicación y asegurarse de que no se pierda es incluirla como un recurso incrustado en uno de los ensamblados que llama al Aspose.Cells. Para incluir el archivo de licencia como un recurso incrustado, realice los siguientes pasos :

1.  En Visual Studio .NET, incluya el archivo de licencia (.lic) en el proyecto mediante la selección**Agregar elemento existente** desde el**Expediente** menú.
1. Seleccione el archivo en el Explorador de soluciones y establezca**Acción de compilación** a**Recurso integrado** en la ventana Propiedades

 Para acceder a la licencia integrada en el ensamblado (como recurso integrado), no es necesario llamar a los métodos GetExecutingAssembly y GetManifestResourceStream de la clase System.Reflection.Assembly de Microsoft .NET Framework. Todo lo que se necesita hacer es simplemente agregar el archivo de licencia como un recurso incrustado a su proyecto y pasar el nombre del archivo de licencia al método SetLicense. los**Aspose.Cells.License** class encontrará automáticamente el archivo de licencia en los recursos incrustados. Revise el ejemplo que se proporciona a continuación para comprender este método de configuración de la licencia (incrustada) en sus aplicaciones.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Configuración de licencia en Aspose.Cells Grid Controls**

En Aspose.Cells Grid Suite, la licencia se puede cargar desde un archivo, flujo o recurso incrustado. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb intenta encontrar la licencia en las siguientes ubicaciones:

1. Ruta explícita
1. La carpeta que contiene la dll del componente (incluida en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La carpeta que contiene el ensamblado que llamó a la dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La carpeta que contiene el ensamblado de entrada (su .exe)
1. Un recurso incrustado en el ensamblaje que llamó a la dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Si utiliza el control Aspose.Cells.GridDesktop, la clase de licencia se utilizará como Aspose.Cells.GridDesktop.License, pero si utiliza el control Aspose.Cells.GridWeb, se utilizará la clase Aspose.Cells.GridWeb.License para establecer la licencia.

{{% /alert %}}

### **Aplicación de una licencia desde disco o transmisión**

La forma más fácil de configurar una licencia es colocar el archivo de licencia en la misma carpeta que la dll del componente (incluido en Aspose.Cells.GridWeb) y especificar solo el nombre del archivo sin su ruta.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llama al método SetLicense, el nombre de la licencia debe ser el mismo que el nombre de su archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia a "MyLicense.lic.xml". Luego, en su código, debe usar el nombre de licencia modificado (es decir, MyLicense.lic.xml) para el método SetLicense.

{{% /alert %}}

También es posible cargar una licencia desde un stream.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Aplicación de una licencia como recurso integrado**

Otra buena forma de empaquetar la licencia con su aplicación y asegurarse de que no se pierda es incluirla como un recurso incrustado en uno de los ensamblados que llama al dll del componente (incluido en Aspose.Cells.GridDesktop). Para incluir el archivo de licencia como un recurso incrustado, realice los siguientes pasos:

1.  En Visual Studio .NET, incluya el archivo de licencia (.lic) en el proyecto usando el**Agregar elemento existente** opción en el**Expediente** menú.
1. Seleccione el archivo en el Explorador de soluciones y establezca Acción de compilación en Recurso incrustado en la ventana Propiedades.
1. Para acceder a la licencia incrustada en el ensamblado (como recurso incrustado), no es necesario llamar a los métodos GetExecutingAssembly y GetManifestResourceStream de la clase System.Reflection.Assembly de Microsoft .NET Framework. En su lugar, agregue el archivo de licencia como un recurso incrustado en su proyecto y pase el nombre del archivo de licencia al método SetLicense. La clase de licencia encuentra automáticamente el archivo de licencia en los recursos integrados.

Revise el ejemplo que se proporciona a continuación para comprender este método de aplicar una licencia como un recurso incorporado a sus aplicaciones.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Aplicación de una licencia en Aspose.Cells.GridDesktop para una aplicación WinForm**

Se recomienda que coloque su código de licencia antes de que comience su aplicación y lo aplique solo una vez. Por ejemplo, para una aplicación de Windows C#, coloque el código de licencia en el método Principal.

{{< highlight "csharp" >}}

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

Se recomienda colocar el código de licencia en Global.asax.cs de su aplicación web (se supone que este archivo de licencia se coloca en la unidad "d:\"):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Cargar una licencia desde un flujo

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
