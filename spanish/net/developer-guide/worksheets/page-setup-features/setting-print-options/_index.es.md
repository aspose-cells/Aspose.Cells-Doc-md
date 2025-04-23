---
title: Configuración de Opciones de Impresión
type: docs
weight: 40
url: /es/net/setting-print-options/
description: Este artículo demuestra cómo establecer programáticamente las Opciones de Impresión de la función Configuración de Página de la Hoja de Cálculo de Excel utilizando la API de C# y la Biblioteca .NET. Puede establecer el Área de Impresión, los Títulos de Impresión y el Orden de Páginas.
keywords: establecer área de impresión de excel c#, establecer títulos de impresión de excel c#, establecer orden de páginas de excel c#
---

{{% alert color="primary" %}}

La configuración de página de Microsoft Excel proporciona varias opciones de impresión (también conocidas como opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo.

{{% /alert %}}

## **Configuración de Opciones de Impresión**

Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica en una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

Aspose.Cells admite todas las opciones de impresión ofrecidas por Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de cálculo utilizando las propiedades ofrecidas por la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Cómo se utilizan estas propiedades se discute a continuación con más detalle.

### **Establecer Área de Impresión**

De forma predeterminada, el área de impresión abarca todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de cálculo.

Para seleccionar un área de impresión específica, utilice la propiedad [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Asigne un rango de celdas que define el área de impresión a esta propiedad.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Establecer Títulos de Impresión**

Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de cálculo impresa. Para hacerlo, utilice las propiedades [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) y [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Establecer Otras Opciones de Impresión**

La clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) también proporciona varias otras propiedades para establecer opciones de impresión generales de la siguiente manera:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): propiedad booleana que define si imprimir o no las líneas de la cuadrícula.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): propiedad booleana que define si imprimir o no los encabezados de fila y columna.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja de cálculo.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): propiedad booleana que define si imprimir la hoja sin gráficos.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): define si se deben imprimir los errores de celda como se muestra, en blanco, como guion o N/A.

Para establecer las propiedades [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) y [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors), Aspose.Cells también proporciona dos enumeraciones, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) y [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) que contienen valores predefinidos para asignar a las propiedades [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) y [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) respectivamente.

Los valores predefinidos en la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) se enumeran a continuación con sus descripciones.

|**Tipos de Imprimir Comentarios**|**Descripción**|
| :- | :- |
|PrintInPlace| Especifica imprimir comentarios como se muestra en la hoja de cálculo.
|PrintNoComments| Especifica no imprimir comentarios.
|PrintSheetEnd| Especifica imprimir comentarios al final de la hoja de cálculo.

Los valores predefinidos de la enumeración [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) se enumeran a continuación con sus descripciones.



|**Tipos de Imprimir Errores**|**Descripción**|
| :- | :- |
|PrintErrorsBlank| Especifica no imprimir errores.
|PrintErrorsDash| Especifica imprimir errores como "--".
|PrintErrorsDisplayed| Especifica imprimir errores como se muestra.
|PrintErrorsNA| Especifica imprimir errores como "#N/A".

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Establecer Orden de Páginas**

La clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) proporciona la propiedad [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) que se utiliza para ordenar varias páginas de la hoja de cálculo a imprimir. Hay dos posibilidades para ordenar las páginas de la siguiente manera.

- **Hacia abajo y luego hacia la derecha:** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **Hacia la derecha y luego hacia abajo:** imprime las páginas de izquierda a derecha antes de imprimir las páginas por debajo.

Aspose.Cells proporciona una enumeración, [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) que contiene todos los tipos de orden predefinidos.

Los valores predefinidos de la enumeración [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) se enumeran a continuación.

|**Tipos de Orden de Impresión**|**Descripción**|
| :- | :- |
|DownThenOver|Representa el orden de impresión como primero hacia abajo y luego hacia adelante.|
|OverThenDown|Representa el orden de impresión como primero hacia adelante y luego hacia abajo.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
