---
title: Configuración de Opciones de Impresión
type: docs
weight: 40
url: /es/python-net/setting-print-options/
description: Este artículo demuestra cómo configurar programáticamente las opciones de impresión de la función de configuración de página de la hoja de cálculo de Excel usando la API Aspose.Cells para Python via .NET. Puedes establecer el área de impresión, los títulos de impresión y el orden de las páginas.
keywords: Biblioteca de Python para Excel, establecer área de impresión en Python, establecer títulos de impresión en Python, cómo configurar el orden de página en Python, cómo establecer opciones de impresión en Python, cómo establecer el área de impresión en Python, cómo establecer títulos de impresión en Python. 
---

{{% alert color="primary" %}}

La configuración de página de Microsoft Excel proporciona varias opciones de impresión (también conocidas como opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo.

{{% /alert %}}

## **Cómo establecer opciones de impresión**

Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica en una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

Aspose.Cells para Python via .NET soporta todas las opciones de impresión ofrecidas por Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de cálculo usando las propiedades ofrecidas por la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Cómo se usan estas propiedades se discute más abajo en más detalle.

## **Cómo establecer el área de impresión**

De forma predeterminada, el área de impresión abarca todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de cálculo.

Para seleccionar un área de impresión específica, utilice la propiedad [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Asigne un rango de celdas que define el área de impresión a esta propiedad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Cómo establecer los títulos de impresión**

Aspose.Cells para Python via .NET permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de cálculo impresa. Para hacerlo, usa las propiedades [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) y [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Cómo establecer otras opciones de impresión**

La clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) también proporciona varias otras propiedades para establecer opciones de impresión generales de la siguiente manera:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): propiedad booleana que define si imprimir o no las líneas de la cuadrícula.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): propiedad booleana que define si imprimir o no los encabezados de fila y columna.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja de cálculo.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): propiedad booleana que define si imprimir la hoja sin gráficos.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): define si se deben imprimir los errores de celda como se muestra, en blanco, como guion o N/A.

Para establecer las propiedades [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) y [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors), Aspose.Cells también proporciona dos enumeraciones, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) y [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) que contienen valores predefinidos para asignar a las propiedades [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) y [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) respectivamente.

Los valores predefinidos en la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) se enumeran a continuación con sus descripciones.

|**Tipos de Imprimir Comentarios**|**Descripción**|
| :- | :- |
|PRINT_IN_PLACE|Especifica imprimir comentarios tal como se muestran en la hoja de cálculo.|
|PRINT_NO_COMMENTS|Especifica no imprimir comentarios.|
|PRINT_SHEET_END|Especifica imprimir comentarios al final de la hoja de cálculo.|

Los valores predefinidos de la enumeración [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) se enumeran a continuación con sus descripciones.



|**Tipos de Imprimir Errores**|**Descripción**|
| :- | :- |
|PRINT_ERRORS_BLANK|Especifica no imprimir errores.|
|PRINT_ERRORS_DASH|Especifica imprimir errores como "--".|
|PRINT_ERRORS_DISPLAYED|Especifica imprimir errores como se muestran.|
|PRINT_ERRORS_NA|Especifica imprimir errores como "#N/A".|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Cómo establecer el orden de las páginas**

La clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) proporciona la propiedad [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) que se utiliza para ordenar varias páginas de la hoja de cálculo a imprimir. Hay dos posibilidades para ordenar las páginas de la siguiente manera.

- **Hacia abajo y luego hacia la derecha:** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **Hacia la derecha y luego hacia abajo:** imprime las páginas de izquierda a derecha antes de imprimir las páginas por debajo.

Aspose.Cells proporciona una enumeración, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) que contiene todos los tipos de orden predefinidos.

Los valores predefinidos de la enumeración [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) se enumeran a continuación.

|**Tipos de Orden de Impresión**|**Descripción**|
| :- | :- |
|DOWN_THEN_OVER|Representa el orden de impresión como abajo y luego a la derecha.|
|OVER_THEN_DOWN|Representa el orden de impresión como a la derecha y luego abajo.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
