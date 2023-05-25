---
title: Configuración de las opciones de impresión
type: docs
weight: 40
url: /es/net/setting-print-options/
description: Este artículo muestra cómo configurar mediante programación las opciones de impresión de la función de configuración de página de la hoja de cálculo de Excel utilizando la biblioteca C# API y .NET. Puede configurar el área de impresión, los títulos de impresión y el orden de las páginas.
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---
{{% alert color="primary" %}}

Microsoft Los ajustes de configuración de página de Excel proporcionan varias opciones de impresión (también denominadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo.

{{% /alert %}}

##  **Configuración de las opciones de impresión**

Estas opciones de impresión permiten a los usuarios:

- Seleccione un área de impresión específica en una hoja de cálculo.
- Imprimir títulos.
- Imprimir líneas de cuadrícula.
- Imprimir encabezados de fila/columna.
- Consiga calidad de borrador.
- Imprimir comentarios.
- Imprimir errores de celda.
- Definir el orden de las páginas.

 Aspose.Cells admite todas las opciones de impresión que ofrece Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de trabajo utilizando las propiedades que ofrece el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)clase. Cómo se utilizan estas propiedades se analiza a continuación con más detalle.

###  **Establecer área de impresión**

De forma predeterminada, el área de impresión incorpora todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de trabajo.

 Para seleccionar un área de impresión específica, use el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**Área de impresión**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)propiedad. Asigne un rango de celdas que defina el área de impresión a esta propiedad.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

###  **Establecer títulos de impresión**

 Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de trabajo impresa. Para hacerlo, utilice el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**ImprimirTítuloColumnas**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) y[**ImprimirTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)propiedades.

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

###  **Establecer otras opciones de impresión**

 El[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class también proporciona varias otras propiedades para configurar las opciones generales de impresión de la siguiente manera:

- [**ImprimirGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): una propiedad booleana que define si se imprimen líneas de cuadrícula o no.
- [**ImprimirEncabezados**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): una propiedad booleana que define si se imprimen o no los encabezados de fila y columna.
- [**blanco y negro**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): una propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**ImprimirComentarios**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): define si mostrar los comentarios de impresión en la hoja de trabajo o al final de la hoja de trabajo.
- [**ImprimirBorrador**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): una propiedad booleana que define si imprimir la hoja sin gráficos.
- [**Errores de impresión**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): define si se imprimen los errores de celda como mostrados, en blanco, guiones o N/A.

 Para configurar el[**ImprimirComentarios**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) y[**Errores de impresión**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)properties, Aspose.Cells también proporciona dos enumeraciones,[**ImprimirComentariosTipo**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , y[**Tipo de error de impresión**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) que contienen valores predefinidos para ser asignados a la[**ImprimirComentarios**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) y[**Errores de impresión**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)propiedades respectivamente.

 Los valores predefinidos en el[**ImprimirComentariosTipo**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)enumeración se enumeran a continuación con sus descripciones.

|**Imprimir tipos de comentarios**|**Descripción**|
| :- | :- |
|Imprimir en el lugar|Especifica que se impriman los comentarios tal como se muestran en la hoja de trabajo.|
|ImprimirNoComentarios|Especifica que no se impriman comentarios.|
|ImprimirFinHoja|Especifica que se impriman comentarios al final de la hoja de trabajo.|

 Los valores predefinidos de[**Tipo de error de impresión**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)enumeración se enumeran a continuación con sus descripciones.



|**Tipos de errores de impresión**|**Descripción**|
| :- | :- |
|Errores de impresiónEn blanco|Especifica que no se impriman errores.|
|PrintErrorsGuión|Especifica que se impriman errores como "--".|
|Errores de impresión mostrados|Especifica que se impriman los errores como se muestran.|
|PrintErrorsNA|Especifica que se impriman errores como "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

###  **Establecer orden de página**

 El[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) la clase proporciona la[**Orden**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)propiedad que se utiliza para ordenar que se impriman varias páginas de la hoja de trabajo. Hay dos posibilidades para ordenar las páginas de la siguiente manera.

- **Abajo y luego encima:** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **Arriba y luego abajo:** imprime páginas de izquierda a derecha antes de imprimir las siguientes páginas.

 Aspose.Cells proporciona una enumeración,[**Tipo de pedido de impresión**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)que contiene todos los tipos de órdenes predefinidos.

 Los valores predefinidos de la[**Tipo de pedido de impresión**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)enumeración se enumeran a continuación.

|**Tipos de órdenes de impresión**|**Descripción**|
| :- | :- |
|AbajoLuegoOver|Representa el orden de impresión como abajo y luego encima.|
|sobreentoncesabajo|Representa el orden de impresión como terminado y luego abajo.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
