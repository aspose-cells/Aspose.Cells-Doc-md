---
title: Obtener encabezados o pies de página
type: docs
weight: 30
url: /es/net/get-headers-or-footers/
description: Este artículo explica cómo obtener mediante programación encabezados y pies de página de archivos de Excel u OpenOffice utilizando la biblioteca C# API o .NET.
---
{{% alert color="primary" %}}

 Los encabezados y pies de página solo se muestran en la vista Diseño de página, Vista previa de impresión y en páginas impresas.

 También puede utilizar el cuadro de diálogo Configurar página si desea ver encabezados o pies de página de más de una hoja de trabajo a la vez.

Para otros tipos de hojas, como hojas de gráficos o gráficos, puede insertar encabezados y pies de página únicamente mediante el cuadro de diálogo Configurar página.

{{% /alert %}}

##  **Obtener encabezados y pies de página en MS Excel**
1. Haga clic en la hoja de trabajo donde desea ver o cambiar los encabezados o pies de página.
2. En la pestaña Vista, en el grupo Vistas del libro, haga clic en Diseño de página.
Excel muestra la hoja de trabajo en la vista Diseño de página.
3. Para ver o editar un encabezado o pie de página, haga clic en el cuadro de texto del encabezado o pie de página izquierdo, central o derecho en la parte superior o inferior de la página de la hoja de trabajo (debajo de Encabezado o encima de Pie de página).


##  **Obtener encabezados y pies de página usando Aspose.Cells para .Net**
 Con[**Hoja de trabajo.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) y[**Hoja de trabajo.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) métodos, el desarrollador .Net puede simplemente obtener encabezados o pies de página del archivo.

1. Construya el libro de trabajo para abrir el archivo.
2. Obtiene la hoja de trabajo donde desea colocar los encabezados o pies de página.
3. Obtiene el encabezado o pie de página con una identificación de sección específica.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **Analizar encabezados y pies de página en la lista de comandos**
El texto del encabezado o pie de página puede contener comandos especiales, por ejemplo, un marcador de posición para el número de página, la fecha actual o atributos de formato de texto.

Los comandos especiales están representados por una sola letra con un signo inicial ("&").

Las cadenas de encabezado y pie de página se construyen utilizando gramática ABNF. No es fácil de entender sin espectador.

 Aspose.Cells para .Net proporciona[**Hoja de trabajo.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)Método para analizar encabezados y pies de página como lista de comandos.

Los siguientes códigos explican cómo analizar el encabezado o pie de página como lista de comandos y procesar comandos:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
