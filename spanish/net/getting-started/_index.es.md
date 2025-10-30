---
title: Empezando
type: docs
weight: 10
url: /es/net/getting-started/
---

{{% alert color="primary" %}} 

Esta página le mostrará cómo instalar Aspose Cells y crear una aplicación Hola Mundo.

{{% /alert %}}

## **Instalación**

### **Instalar Aspose.Cells a través de NuGet**

NuGet es la forma más sencilla de descargar e instalar Aspose.Cells for .NET. 

1. Abra Microsoft Visual Studio y el administrador de paquetes NuGet. 
1. Busque "aspose.cells" para encontrar el Aspose.Cells for .NET deseado. 
1. Haga clic en "Instalar", Aspose.Cells for .NET se descargará y se referenciará en su proyecto.
**![Instalar Aspose.Cells a través de NuGet](install-through-nuget.png)**

También puedes descargarlo desde la página web de nuget para aspose.cells: 
[Paquete NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

[Más pasos para detalles](/cells/es/net/installation/)

### **Instalar Aspose.Cells en Windows**

1. Descarga Aspose.Cells.msi desde la siguiente página:
[Descargar Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Haz doble clic en Aspose Cells msi y sigue las instrucciones para instalarlo:

**![Instalar Aspose Cells en Windows](install-on-windows.png)**

[Más pasos para detalles](/cells/es/net/installing-aspose-cells-on-windows/)

### **Instalar Aspose.Cells en Linux**

En este ejemplo, uso Ubuntu para mostrar cómo empezar a usar Aspose.Cells en Linux.

1. Crea una aplicación .netcore, llamada "AsposeCellsTest".
2. Abre el archivo "AsposeCellsTest.csproj", y agrega las siguientes líneas para las referencias del paquete Aspose.Cells:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. Abre el proyecto con VSCode en Ubuntu:
**![Instalar Aspose Cells en Linux](install-on-linux.png)**
4. ejecuta la prueba con el siguiente código:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Nota: Aspose.Cells For .NetStandard puede cubrir tus necesidades en Linux.

Aplica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 y versiones avanzadas.

### **Instalar Aspose.Cells en MAC OS**

En este ejemplo, utilizo macOS High Sierra para mostrar cómo empezar a usar Aspose.Cells en MAC OS.

1. Crea una aplicación .netcore, llamada "AsposeCellsTest".
2. Abre la aplicación con Visual Studio para Mac, luego instala Aspose Cells a través de NuGet:
**![Instalar Aspose Cells en macOS](install-on-mac-os.png)**
3. Ejecuta la prueba con el siguiente código:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Si necesitas usar funciones relacionadas con el dibujo, por favor instala libgdiplus en macOS, consulta:
[Cómo instalar libgdiplus en macOS](/cells/es/net/how-to-install-libgdiplus-in-macos/)

Nota: Aspose.Cells For .NetStandard puede satisfacer tu requerimiento en MAC OS.

Aplica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 y versiones avanzadas.

### [**Run Aspose Cells in Docker**](/cells/es/net/how-to-run-aspose-cells-in-docker/)

### **Cómo usar la biblioteca de gráficos en plataformas no-Windows con Net6**

Aspose.Cells for Net6 ahora usa SkiaSharp como la biblioteca de gráficos, según lo recomendado en la [declaración oficial de Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md). Para más detalles sobre cómo usar Aspose.Cells con NET6, por favor consulta [Cómo ejecutar Aspose.Cells for .Net6](/cells/es/net/how-to-run-aspose-cells-for-net6/).

## **Creación de la aplicación Hola Mundo**

Los siguientes pasos crean la aplicación Hola Mundo utilizando la API de Aspose.Cells:

1. Si tienes una licencia, entonces [aplícala](/cells/es/net/licensing/).
   Si estás usando la versión de evaluación, omite las líneas de código relacionadas con la licencia.
1. Crea una instancia de la clase [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) para crear un archivo de Excel nuevo, o abrir un archivo de Excel existente.
1. Accede a cualquier celda deseada de una hoja de cálculo en el archivo de Excel.
1. Inserte las palabras **¡Hola, mundo!** en una celda accesada.
1. Genere el archivo modificado de Microsoft Excel.

La implementación de los pasos anteriores se muestra en los ejemplos a continuación.

### **Ejemplo de código: Crear un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, inserta "¡Hola Mundo!" en la celda A1 de la primera hoja de trabajo y lo guarda como archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Ejemplo de código: Abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Microsoft Excel existente "Sample.xlsx", inserta "¡Hola Mundo!" en la celda A1 de la primera hoja de trabajo y lo guarda como archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
