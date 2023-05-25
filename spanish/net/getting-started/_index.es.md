---
title: Empezando
type: docs
weight: 10
url: /es/net/getting-started/
---
{{% alert color="primary" %}} 

Esta página le mostrará cómo instalar Aspose Cells y crear una aplicación Hello World.

{{% /alert %}}

##  **Instalación**

###  **Instalar Aspose.Cells a NuGet**

 NuGet es la forma más fácil de descargar e instalar Aspose.Cells for .NET.

1.  Abra Microsoft Visual Studio y NuGet administrador de paquetes.
1.  Busque "aspose.cells" para encontrar el Aspose.Cells for .NET deseado.
1. Haga clic en "Instalar", Aspose.Cells for .NET se descargará y referenciará en su proyecto.
**![Instalar Aspose Cells hasta NuGet](instalar hasta nuget.png)**

 También puede descargarlo desde la página web nuget para aspose.cells:
[Aspose.Cells for .NET NuGet Paquete](https://www.nuget.org/packages/Aspose.Cells/)

[Más pasos para detalles](/cells/es/net/installation/)

###  **Instalar Aspose.Cells en windows**

1. Descargue Aspose.Cells.msi desde la siguiente página:
[Descargar Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Haga doble clic en Aspose Cells msi y siga las instrucciones para instalarlo:

**![Instalar Aspose Cells en windows](instalar-en-windows.png)**

[Más pasos para detalles](/cells/es/net/installing-aspose-cells-on-windows/)

###  **Instalar Aspose.Cells en linux**

En este ejemplo, uso Ubuntu para mostrar cómo comenzar a usar Aspose.Cells en Linux.

1. Cree una aplicación .netcore, denominada "AsposeCellsTest".
2. Abra el archivo "AsposeCellsTest.csproj", agregue las siguientes líneas para las referencias del paquete Aspose.Cells:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.5" />
  </ItemGroup>
{{< /highlight >}}
3. Abra el proyecto con VSCode en Ubuntu:
**![Instalar Aspose Cells en linux](instalar-en-linux.png)**
4. Ejecute la prueba con el siguiente código:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Nota: Aspose.Cells para .NetStandard puede admitir sus requisitos en Linux.

Se aplica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 y versión avanzada.

###  **Instalar Aspose.Cells en MAC OS**

En este ejemplo, uso macOS High Sierra para mostrar cómo comenzar a usar Aspose.Cells en MAC OS.

1. Cree una aplicación .netcore, denominada "AsposeCellsTest".
2. Abra la aplicación con Visual Studio para Mac, luego instale Aspose Cells a NuGet:
**![Instalar Aspose Cells en macOS](instalar-en-mac-os.png)**
3. Ejecute la prueba con el siguiente código:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Si necesita usar funciones relacionadas con el dibujo, instale libgdiplus en macOS, consulte:
[Cómo instalar libgdiplus en macOS](/cells/es/net/how-to-install-libgdiplus-in-macos/)

Nota: Aspose.Cells para .NetStandard puede admitir sus requisitos en MAC OS.

Se aplica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 y versión avanzada.

###  **[Ejecute Aspose Cells en Docker](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **Cómo usar la biblioteca de gráficos en plataformas que no son de Windows con Net6**

 Aspose.Cells para Net6 ahora usa SkiaSharp como biblioteca de gráficos, como se recomienda en[comunicado oficial del Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Para obtener más detalles sobre el uso de Aspose.Cells con NET6, consulte[Cómo ejecutar Aspose.Cells para .Net6](/cells/es/net/how-to-run-aspose-cells-for-net6/).

##  **Creación de la aplicación Hello World**

Los pasos a continuación crean la aplicación Hello World usando el Aspose.Cells API:

1.  Si tiene una licencia, entonces[apliquelo](/cells/es/net/licensing/).
Si está utilizando la versión de evaluación, omita las líneas de código relacionadas con la licencia.
1.  Crear una instancia de la[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook) class para crear un nuevo archivo de Excel o abrir un archivo de Excel existente.
1. Acceda a cualquier celda deseada de una hoja de trabajo en el archivo de Excel.
1.  Inserta las palabras**Hello World!** en una celda accedida.
1. Genere el archivo de Excel Microsoft modificado.

La implementación de los pasos anteriores se demuestra en los siguientes ejemplos.

###  **Ejemplo de código: creación de un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, inserta "Hello World!" en la celda A1 de la primera hoja de cálculo y se guarda como archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Ejemplo de código: abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Excel Microsoft existente "Sample.xlsx", inserta "Hello World!" en la celda A1 de la primera hoja de cálculo y se guarda como archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
