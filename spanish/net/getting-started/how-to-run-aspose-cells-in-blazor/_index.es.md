---
title: Cómo ejecutar Aspose.Cells en Blazor
type: docs
weight: 138
url: /es/net/how-to-run-aspose-cells-in-blazor/
description: Aprenda cómo ejecutar Aspose.Cells en Blazor.
keywords: C# Ejecutar Aspose.Cells en Blazor, Usar Aspose.Cells en Blazor, Aplicación de Servidor Blazor con Aspose.Cells
---

## Resumen

Para ejecutar Aspose.Cells en Blazor, necesita las plataformas .NET6 (o posteriores), en comparación con plataformas anteriores (.netcore31 o anteriores), una diferencia importante es acerca de la biblioteca de gráficos. En este [Documento oficial de Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), se explica que para las versiones de .NET6 o posteriores la biblioteca de gráficos "System.Drawing.Common" solo será compatible en Windows, y se dan recomendaciones para reemplazar la biblioteca de gráficos.

Para el producto Apose.Cells, hemos realizado la evaluación y completado la migración de la biblioteca de gráficos. Utilizamos SkiaSharp en lugar de System.Drawing.Common en sistemas no Windows, como se sugiere en la documentación oficial de Microsoft. Tenga en cuenta que este cambio crítico entrará en vigor en Aspose.Cells 22.10.1 o posterior para .Net6.

## Aplicación de Servidor Blazor con Aspose.Cells

En este ejemplo, creará una aplicación simple de servidor Blazor que agrega algunos datos y gráficos, y los renderiza en imágenes para mostrar en la página web. Durante el proceso de creación del proyecto, puede configurar opciones según sus propias necesidades. Por ejemplo, al marcar la opción "Habilitar Docker", la aplicación Blazor puede construirse y ejecutarse en Docker.

### Crear Aplicación de Servidor Blazor

Utilicemos la herramienta VS2022 como ejemplo para crear la primera aplicación Blazor con Aspose.Cells, siga los pasos a continuación:
1. Seleccione Archivo -> Nuevo -> Proyecto y filtre usando la palabra clave de blazor para seleccionar la plantilla de proyecto correspondiente.
<br>
<img src="1.png" width=70% />
1. Establezca el nombre del proyecto en "BlazorTest" y seleccione la ruta.
<br>
<img src="2.png" width=70% />
1. Configure las bibliotecas y otras opciones utilizadas en el proyecto. Finalmente, haga clic en el botón "Crear" para generar su primer proyecto blazer.
<br>
<img src="3.png" width=70% />
1. Después de ingresar al proyecto, haga clic en "Dependencias" en el proyecto y seleccione "Administrar Paquetes NuGet..." para agregar la biblioteca Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. Ingrese palabras clave para filtrar e instale la última biblioteca de Aspose.Cells. Al mismo tiempo se instalarán bibliotecas dependientes como SkiaSharp juntas.
<br>
<img src="5.png" width=70% />
1. Haga doble clic en el archivo "Index.razor" para editar e importar la biblioteca requerida. Agregue algunos datos y gráficos, y renderícelos en gráficos para mostrarlos.
<br>
<img src="5.png" width=70% />
1. Compile y ejecute el proyecto, y obtendrá los siguientes resultados.
<br>
<img src="7.png" width=70% />

### Código de Ejemplo en Aplicación de Servidor Blazor

El siguiente código de ejemplo está incluido en el archivo Index.razor:
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
