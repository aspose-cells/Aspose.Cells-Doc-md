---
title: Trabajar con fondo en archivos ODS
type: docs
weight: 150
url: /es/python-net/working-with-background-in-ods-files/
description: Cómo trabajar con fondo en archivos ODS con Aspose.Cells for Python via .NET API.
keywords: Python work with Background in ODS Files, Read Background Information from ODS file Pyton via NET, Add Colored Background to ODS file using Python via NET, Python via NET Add Graphic Background to ODS file.
---
##  **Antecedentes en archivos ODS**

Se puede agregar fondo a las hojas en archivos ODS. El fondo puede ser de color o gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el diálogo de vista previa de impresión.

Aspose.Cells for Python via .NET proporciona la capacidad de leer la información de fondo y agregar el fondo en archivos ODS.

##  **Lea la información general del archivo ODS**

Aspose.Cells for Python via .NET proporciona la[**OdsPáginaFondo**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) clase para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de[**OdsPáginaFondo**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) clase cargando el[fuente ODS](90112030.ods) archivo y leer la información de fondo. Consulte la salida de la consola generada por el código como referencia.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

###  **Salida de consola**

Tipo de fondo: Gráfico

Posición de fondo: CentroCentro

##  **Agregar fondo de color al archivo ODS**

Aspose.Cells for Python via .NET proporciona la[**OdsPáginaFondo**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)clase para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de[**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) propiedad para agregar un color de fondo al archivo ODS. Por favor vea el[salida ODS](90112031.ods) Archivo generado por el código como referencia.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

##  **Agregar fondo gráfico al archivo ODS**

Aspose.Cells for Python via .NET proporciona la[**OdsPáginaFondo**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)clase para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de[**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/)Propiedad para agregar fondo gráfico al archivo ODS. Por favor vea el[salida ODS](90112030.ods)Archivo generado por el código como referencia.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
