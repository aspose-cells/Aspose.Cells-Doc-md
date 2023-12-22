---
title: Licensing
type: docs
weight: 120
url: /es/net/licensing/
description: Aspose.Cells for .NET proporciona diferentes planes de compra u ofrece una prueba gratuita y una licencia temporal de 30 días para evaluación utilizando Licensing y políticas de suscripción en C#.
keywords: Apply License from Disk or Stream. Set License from Disk or Stream. Apply License in Aspose.Cells.
---
{{% alert color="primary" %}}

 Puede descargar fácilmente una versión de evaluación de Aspose.Cells desde su[pagina de descarga](https://www.nuget.org/packages/Aspose.Cells) @ NuGet repositorios. La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del componente. Además, la versión de evaluación simplemente adquiere la licencia cuando usted compra una licencia y agrega un par de líneas de código para aplicar la licencia.

{{% /alert %}}

##  **Limitaciones de la versión de evaluación**

La versión de evaluación del producto Aspose.Cells (sin una licencia especificada) proporciona funcionalidad completa del producto, pero está limitada a abrir 100 archivos en un programa y una hoja de trabajo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

- **Número de archivos abiertos** (Aspose.Cells)
 Al ejecutar su programa, solo puede abrir 100 archivos de Excel usando la biblioteca Aspose.Cells. Si su aplicación excede este número, se generará una excepción.
- **Configuración del archivo de configuración**(Aspose.Cells.GridWeb)
 No puede volver a especificar la ruta del script agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config). acw_client es una carpeta que contiene archivos y Aspose.Cells.GridWeb usa esta carpeta para administrar su configuración interna, tiene archivos de script, archivos de imágenes y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. El archivo de configuración se utiliza para evitar que el control utilice los recursos del cliente integrados (imágenes, scripts, etc.), lo cual es útil en algunos casos/escenarios. Además, estos ajustes de configuración en el archivo web.config solo tendrán efecto con la versión CON LICENCIA del control.

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

Además, una hoja de trabajo con marca de agua de evaluación siempre se mostrará como la hoja de trabajo activa en el archivo Excel generado utilizando la biblioteca Aspose.Cells. Sólo en la versión con licencia, puede configurar la hoja de trabajo activa para otras hojas de trabajo. En la salida PDF o el archivo de imagen de Aspose.Cells, se pegará una marca de agua de evaluación en la parte superior del documento/imagen. No puede ocultar la Advertencia de derechos de autor de evaluación (la hoja de trabajo adicional) en el control GridWeb, siempre se agregará (al final en las pestañas de la hoja de trabajo) en el control.

{{% alert color="primary" %}}

 Si desea probar Aspose.Cells sin limitaciones de versión de evaluación, también puede solicitar una[Licencia Temporal de 30 Días](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

##  **Cómo aplicar una licencia en el componente Aspose.Cells**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores para los que tiene licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique. Incluso la adición inadvertida de un salto de línea adicional al archivo lo invalidará. Debe configurar una licencia antes de utilizar Aspose.Cells si desea evitar su limitación de evaluación. Sólo es necesario establecer una licencia una vez por solicitud (o proceso). La licencia se puede cargar desde un archivo, una secuencia o un recurso integrado.

Aspose.Cells intenta encontrar la licencia en las siguientes ubicaciones:

- Camino explícito
- La carpeta que contiene Aspose.Cells.dll
- La carpeta que contiene el ensamblado que llamó Aspose.Cells.dll
- La carpeta que contiene el ensamblado de entrada (su .exe)
- Un recurso incrustado en el ensamblado que llamó Aspose.Cells.dll

Existen dos métodos comunes para aplicar una licencia, desde un archivo o secuencia, o como un recurso integrado.

###  **Cómo aplicar una licencia desde Disk o Stream**

La forma más sencilla de configurar una licencia es colocar el archivo de licencia en la misma carpeta que el de Aspose.Cells.dll y especificar solo el nombre del archivo sin su ruta.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llama al método SetLicense, el nombre de la licencia debe ser el mismo que el nombre del archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia a *Aspose.Cells.lic.xml**. Luego, en su código, debe usar el nombre de licencia modificado (**Aspose.Cells.lic.xml**) para el método SetLicense.

{{% /alert %}}

También es posible cargar una licencia desde una secuencia.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Cómo solicitar una licencia medida**

Aspose.Cells permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de concesión de licencias. El nuevo mecanismo de concesión de licencias se utilizará junto con el método de concesión de licencias existente. Aquellos clientes que quieran que se les facture según el uso de las funciones API pueden utilizar la licencia medida. Para obtener más detalles, consulte[Preguntas frecuentes sobre el medidor Licensing](https://purchase.aspose.com/faqs/licensing/metered)sección.

una nueva clase[medido](https://reference.aspose.com/cells/net/aspose.cells/metered)Se ha introducido para aplicar la clave medida. A continuación se muestra el código de muestra que demuestra cómo configurar la clave pública y privada medida.

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

###  **Cómo utilizar un recurso integrado**

Otra forma elegante de empaquetar la licencia con su aplicación y asegurarse de que no se pierda es incluirla como un recurso integrado en uno de los ensamblados que llama a Aspose.Cells. Para incluir el archivo de licencia como un recurso integrado, realice los siguientes pasos :

1.  En Visual Studio .NET, incluya el archivo de licencia (.lic) en el proyecto mediante selección**Agregar artículo existente** desde el**Archivo** menú.
1.  Seleccione el archivo en el Explorador de soluciones y configure**Construir acción** a**Recurso integrado** en la ventana Propiedades

Para acceder a la licencia integrada en el ensamblado (como recurso integrado), no es necesario llamar a los métodos GetExecutingAssembly y GetManifestResourceStream de la clase System.Reflection.Assembly del Framework Microsoft .NET. Todo lo que necesita hacer es simplemente agregar el archivo de licencia como un recurso integrado a su proyecto y pasar el nombre del archivo de licencia al método SetLicense. El**Aspose.Cells.License** class encontrará automáticamente el archivo de licencia en los recursos integrados. Revise el ejemplo que se proporciona a continuación para comprender este método de configurar la licencia (integrada) en sus aplicaciones.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Cómo configurar la licencia en Aspose.Cells Grid Controls**

En Aspose.Cells Grid Suite, la licencia se puede cargar desde un archivo, secuencia o recurso integrado. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb intenta encontrar la licencia en las siguientes ubicaciones:

1. Camino explícito
1. La carpeta que contiene la dll del componente (incluida en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La carpeta que contiene el ensamblado que llamó a la dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La carpeta que contiene el ensamblado de entrada (su .exe)
1. Un recurso incrustado en el ensamblado que llamó a la dll del componente (incluido en Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Si está utilizando el control Aspose.Cells.GridDesktop, la clase de licencia se utilizará como Aspose.Cells.GridDesktop.License, pero si está utilizando el control Aspose.Cells.GridWeb, entonces se utilizará la clase Aspose.Cells.GridWeb.License para configurar la licencia.

{{% /alert %}}

###  **Cómo aplicar una licencia desde Disk o Stream**

La forma más sencilla de configurar una licencia es colocar el archivo de licencia en la misma carpeta que la dll del componente (incluido en Aspose.Cells.GridWeb) y especificar solo el nombre del archivo sin su ruta.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llama al método SetLicense, el nombre de la licencia debe ser el mismo que el nombre del archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia a "MyLicense.lic.xml". Luego, en su código, debe usar el nombre de licencia modificado (es decir, MyLicense.lic.xml) para el método SetLicense.

{{% /alert %}}

También es posible cargar una licencia desde una secuencia.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Cómo aplicar una licencia como recurso integrado**

Otra buena forma de empaquetar la licencia con su aplicación y asegurarse de que no se pierda es incluirla como un recurso integrado en uno de los ensamblados que llama al dll del componente (incluido en Aspose.Cells.GridDesktop). Para incluir el archivo de licencia como recurso integrado, realice los siguientes pasos:

1.  En Visual Studio .NET, incluya el archivo de licencia (.lic) en el proyecto usando el**Agregar artículo existente** opción en el**Archivo** menú.
1. Seleccione el archivo en el Explorador de soluciones y configure Acción de compilación en Recurso integrado en la ventana Propiedades.
1. Para acceder a la licencia integrada en el ensamblado (como recurso integrado), no es necesario llamar a los métodos GetExecutingAssembly y GetManifestResourceStream de la clase System.Reflection.Assembly del Framework Microsoft .NET. En su lugar, agregue el archivo de licencia como un recurso integrado en su proyecto y pase el nombre del archivo de licencia al método SetLicense. La clase Licencia encuentra automáticamente el archivo de licencia en los recursos integrados.

Revise el ejemplo que se proporciona a continuación para comprender este método de aplicar una licencia como un recurso integrado en sus aplicaciones.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **Cómo aplicar una licencia en Aspose.Cells.GridDesktop para una aplicación WinForm**

Se recomienda que coloque su código de licencia antes de que se inicie la aplicación y lo aplique solo una vez. Por ejemplo, para una aplicación de Windows C#, coloque el código de licencia en el método Principal.

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

##  **Notas sobre la aplicación de una licencia en Aspose.Cells.GridWeb**

Se recomienda colocar el código de licencia en Global.asax.cs de su aplicación web (se supone que este archivo de licencia está en la unidad " d:\ "):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Cargando una licencia desde una secuencia

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
