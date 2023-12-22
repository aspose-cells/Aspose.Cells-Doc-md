---
title: Cómo ejecutar Aspose.Cells en Blazor
type: docs
weight: 138
url: /es/net/how-to-run-aspose-cells-in-blazor/
description: Aprenda cómo ejecutar Aspose.Cells en Blazor.
keywords: C# Run Aspose.Cells in Blazor, Use Aspose.Cells in Blazor
---
##  Descripción general

 Para ejecutar Aspose.Cells en Blazor, necesita las plataformas .NET6 (o posteriores); en comparación con las plataformas anteriores (.netcore31 o anteriores), una diferencia importante es la biblioteca de gráficos. en este funcionario[Microsoft Documento](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), explica que para .NET6 o versiones posteriores la biblioteca de gráficos "System.Drawing.Common" solo será compatible con Windows y ofrece recomendaciones para reemplazar la biblioteca de gráficos.

Para el producto Apose.Cells, realizamos la evaluación y completamos la migración de la biblioteca de gráficos. Usamos SkiaSharp en lugar de System.Drawing.Common en sistemas que no son Windows, como se sugiere en la documentación oficial de Microsoft. Tenga en cuenta que este cambio crítico entrará en vigor en Aspose.Cells 22.10.1 o posterior para .Net6.

##  Primera aplicación de Blazor con Aspose.Cells

En este ejemplo, creará una aplicación de servidor Blazor simple que agrega algunos datos y gráficos y los convierte en imágenes para mostrarlas en la página web. Durante el proceso de creación del proyecto, puede configurar opciones según sus propias necesidades. Por ejemplo, cuando marca la opción "Habilitar Docker", la aplicación Blazor se puede compilar y ejecutar en Docker.

###  Cree la primera aplicación Blazor

Usemos la herramienta VS2022 como ejemplo para crear la primera aplicación Blazor con Aspose.Cells, siga los pasos a continuación:
1. Seleccione Archivo ->Nuevo ->Proyecto y filtre usando la palabra clave blazer para seleccionar la plantilla de proyecto correspondiente.
<br>
<img src="1.png" width=70% />
1. Establezca el nombre del proyecto en "BlazorTest" y seleccione la ruta.
<br>
<img src="2.png" width=70% />
1. Configure las bibliotecas y otras opciones utilizadas en el proyecto. Finalmente, haz clic en el botón "Crear" para generar tu primer proyecto blazer.
<br>
<img src="3.png" width=70% />
1. Después de ingresar al proyecto, haga clic en "Dependencias" debajo del proyecto y seleccione "Administrar paquetes NuGet ..." para agregar la biblioteca Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. Ingrese palabras clave para filtrar e instalar la última biblioteca Aspose.Cells. Al mismo tiempo, también se instalarán bibliotecas dependientes, como SkiaSharp.
<br>
<img src="5.png" width=70% />
1. Haga doble clic en el archivo "Index.razor" para editar e importar la biblioteca requerida. Agregue algunos datos y gráficos y conviértalos en gráficos para su visualización.
<br>
<img src="5.png" width=70% />
1. Compile y ejecute el proyecto y obtendrá los siguientes resultados.
<br>
<img src="7.png" width=70% />

###  Código de muestra en la primera aplicación Blazor

El siguiente código de muestra se incluye en el archivo Index.razor:
```
@page "/"
@using SkiaSharp;
@using Aspose.Cells;
@using Aspose.Cells.Drawing;
@using Aspose.Cells.Rendering;


<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />

<img src="@imageSrc" />

@code
{
    private string imageSrc;

    public Index()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "test data for blazor";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}

```