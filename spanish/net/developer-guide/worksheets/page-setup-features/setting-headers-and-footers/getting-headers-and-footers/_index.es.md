---
title: Obteniendo Encabezados o Pies de Página
type: docs
weight: 30
url: /es/net/get-headers-or-footers/
description: Este artículo explica cómo obtener programáticamente los encabezados y pies de página de archivos de Excel o OpenOffice utilizando la API de C# o la biblioteca .NET.
---

{{% alert color="primary" %}}

Los encabezados y pies de página se muestran solo en la vista Diseño de página, en la vista previa de impresión y en las páginas impresas. 

También puedes usar el cuadro de diálogo Configurar página si deseas ver encabezados o pies de página para más de una hoja de cálculo a la vez. 

Para otros tipos de hojas, como hojas de gráficos o gráficos, solo puedes insertar encabezados y pies de página mediante el cuadro de diálogo Configurar página.

{{% /alert %}}

## **Obteniendo Encabezados y Pies de Página en MS Excel**
1. Haz clic en la hoja de cálculo donde deseas ver o cambiar los encabezados o pies de página.
2. En la pestaña Ver, en el grupo Vistas de libro, haz clic en Diseño de página.
  Excel muestra la hoja de cálculo en la vista Diseño de página.
3. Para ver o editar un encabezado o pie de página, haz clic en el cuadro de texto de encabezado o pie de página izquierdo, central o derecho en la parte superior o inferior de la página de la hoja de cálculo (debajo de Encabezado, o encima de Pie de página).


## **Obteniendo Encabezados y Pies de Página usando Aspose.Cells para .Net**
Con los métodos [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getheader/) y [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getfooter/), el desarrollador .Net puede obtener fácilmente encabezados o pies de página del archivo.

1. Construir un libro de trabajo para abrir el archivo.
2. Obtiene la hoja de cálculo donde deseas obtener encabezados o pie de página.
3. Obtiene el encabezado o pie de página con un identificador de sección específico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **Analizar Encabezados y Pies de Página para Lista de Comandos**
El texto del encabezado o pie de página puede contener  comandos especiales, por ejemplo, un marcador de posición para el número de página, la fecha actual o atributos de formato de texto.

Los comandos especiales están representados por una sola letra con un ampersand inicial ("&").

Las cadenas de encabezado y pie de página se construyen utilizando la gramática ABNF. No es fácil de entender sin visor.

Aspose.Cells para .Net proporciona el método [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getcommands/) para analizar encabezados y pies de página como lista de comandos.

Los siguientes códigos muestran cómo analizar un encabezado o pie de página como lista de comandos y procesar comandos:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
