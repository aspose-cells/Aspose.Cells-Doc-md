---
title: Trabajar con fondo en archivos ODS
type: docs
weight: 150
url: /es/net/working-with-background-in-ods-files/
---

## **Fondo en archivos ODS**

Se puede agregar fondo a las hojas en archivos ODS. El fondo puede ser de color o gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el cuadro de diálogo de vista previa de impresión.

Aspose.Cells proporciona la capacidad de leer la información de fondo y agregar el fondo en archivos ODS.

## **Leer información de fondo de archivo ODS**

Aspose.Cells proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de la clase [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) cargando el [archivo ODS de origen](90112030.ods) y leyendo la información de fondo. Consulte la salida de consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Salida de la consola**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Agregar fondo de color al archivo ODS**

Aspose.Cells proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) para agregar un fondo de color al archivo ODS. Consulte el [archivo ODS de salida](90112031.ods) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Agregar fondo gráfico al archivo ODS**

Aspose.Cells proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata) para agregar un fondo gráfico al archivo ODS. Consulte el [archivo ODS de salida](90112030.ods) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
