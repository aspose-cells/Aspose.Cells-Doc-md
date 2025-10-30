---
title: Trabajar con fondo en archivos ODS
type: docs
weight: 150
url: /es/python-net/working-with-background-in-ods-files/
description: Cómo trabajar con el Fondo en archivos ODS con Aspose.Cells para la API de Python via .NET.
keywords: Python trabaja con el Fondo en archivos ODS, Leer Información de Fondo de archivo ODS con Python via NET, Agregar Fondo de Color a archivo ODS usando Python via NET, Python via NET Añadir Fondo Gráfico a archivo ODS.
---

## **Fondo en archivos ODS**

Se puede agregar fondo a las hojas en archivos ODS. El fondo puede ser de color o gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el cuadro de diálogo de vista previa de impresión.

Aspose.Cells para Python via .NET proporciona la capacidad de leer la información de fondo y agregar el fondo en archivos ODS.

## **Leer información de fondo de archivo ODS**

Aspose.Cells para Python via .NET proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código muestra el uso de la clase [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) al cargar el archivo ODS fuente y leer la información de fondo. Consulte la Salida de Consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **Salida de la consola**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Agregar fondo de color al archivo ODS**

Aspose.Cells para Python via .NET proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código muestra el uso de la propiedad [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) para agregar un fondo de color al archivo ODS. Consulte el archivo ODS de salida generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **Agregar fondo gráfico al archivo ODS**

Aspose.Cells para Python via .NET proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código muestra el uso de la propiedad [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) para agregar un fondo gráfico al archivo ODS. Consulte el archivo ODS de salida generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
