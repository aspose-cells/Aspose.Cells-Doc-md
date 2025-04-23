---
title: Cómo imprimir Excel como páginas ajustadas en ancho y alto
type: docs
weight: 200
url: /es/net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Este artículo te muestra un código que explica cómo establecer FitToPagesWide y FitToPagesTall usando la biblioteca Aspose.Cells.
keywords: C# Cómo establecer FitToPagesWide y FitToPagesTall, Cómo agregar FitToPagesWide y FitToPagesTall en C#, Cómo establecer FitToPagesWide y FitToPagesTall en Excel, Cómo borrar FitToPagesWide y FitToPagesTall en Excel, Cómo imprimir Excel como páginas ajustadas anchas y altas, Cómo imprimir hoja de trabajo como una página, Cómo imprimir todas las columnas de la hoja en una página.
---

## **Introducción**

Las configuraciones FitToPagesWide y FitToPagesTall se usan en aplicaciones de hojas de cálculo (como Microsoft Excel) para controlar cómo se escala una hoja de cálculo al imprimir. Estas configuraciones ayudan a garantizar que tu salida impresa quepa dentro de un número específico de páginas, tanto en horizontal como en vertical. Aquí hay una descripción de cada configuración:

1. FitToPagesWide: Esta configuración especifica el número de páginas de ancho en las que la salida impresa debe ajustarse. Por ejemplo, establecer FitToPagesWide en 1 significa que el contenido se escalará para ajustarse dentro de una sola anchura de página, sin importar cuán ancha sea la hoja de cálculo.
1. FitToPagesTall: Esta configuración especifica el número de páginas de alto en las que la salida impresa debe ajustarse. Por ejemplo, establecer FitToPagesTall en 1 significa que el contenido se escalará para ajustarse dentro de una sola altura de página, independientemente del número de filas.

## **Por qué usar FitToPagesWide y FitToPagesTall**
Aquí hay algunas razones para configurar FitToPagesWide y FitToPagesTall:
1. Control sobre el diseño impreso: Al especificar el número de páginas de ancho y alto, puedes asegurarte de que tu documento impreso sea fácil de leer y esté bien organizado, sin que columnas o filas se dividan de manera incómoda en las páginas.
1. Consistencia: Si estás imprimiendo varias hojas o informes, usar estas configuraciones ayuda a mantener un formato consistente, lo que facilita comparar y analizar los documentos impresos.
1. Presentación profesional: Escalar y ajustar correctamente el contenido a un número especificado de páginas puede resultar en una presentación más profesional y pulida de tus datos.

## **Cómo imprimir un archivo como páginas ajustadas en ancho y alto en Excel**

Para configurar FitToPagesWide y FitToPagesTall en Microsoft Excel, sigue estos pasos:

1. Abre tu libro de Excel y ve a la hoja que deseas imprimir.
1. Ve a la pestaña Diseño de página en la cinta de opciones.
1. En el grupo Configuración de página, haz clic en la pequeña flecha en la esquina inferior derecha para abrir el cuadro de diálogo Configuración de página.
1. En el cuadro de diálogo Configuración de página, ve a la pestaña Página.
1. Bajo Escalado, selecciona la opción "Ajustar a" y luego especifica el número de páginas de ancho y alto que deseas: Ingresa el número de páginas de ancho en el primer cuadro (Ajustar a x páginas de ancho). Ingresa el número de páginas de alto en el segundo cuadro (Ajustar a y páginas de alto).
<br>
<img src="2.png" width=60% />

1. Haz clic en Aceptar para aplicar las configuraciones.


## **Cómo Imprimir Excel como Páginas Ajustadas en Ancho y Alto usando Aspose.Cells**

Para establecer FitToPagesWide y FitToPagesTall en una hoja de trabajo especificada: Primero, carga el [archivo de ejemplo](input.xlsx), y luego debes modificar las propiedades [**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/) y [**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/) del objeto [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) para la hoja de trabajo deseada. Aquí un ejemplo en C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

El resultado de la salida:
<br>
<img src="1.png" width=60% />


## **Cómo imprimir la hoja de trabajo como una sola página usando Aspose.Cells**

Para imprimir la hoja de trabajo como una sola página: Primero, carga el [archivo de muestra](sample.xlsx), y luego debes establecer la propiedad [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/) del objeto [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/). Aquí hay un ejemplo en C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

El resultado de la salida:
<br>
<img src="3.png" width=60% />


## **Cómo imprimir todas las columnas de la hoja en una sola página usando Aspose.Cells**

Para imprimir todas las columnas de la hoja de trabajo en una sola página: primero, carga el [archivo de muestra](sample.xlsx), y luego debes establecer la propiedad [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/) del objeto [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/). Aquí hay un ejemplo en C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

El resultado de la salida:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
