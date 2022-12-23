---
title: Trabajar con fondo en archivos ODS
type: docs
weight: 150
url: /es/net/working-with-background-in-ods-files/
---
## **Antecedentes en ODS Archivos**

El fondo se puede agregar a las hojas en los archivos ODS. El fondo puede ser un fondo de color o un fondo gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el diálogo de vista previa de impresión.

Aspose.Cells brinda la capacidad de leer la información de fondo y agregar el fondo en archivos ODS.

## **Lea la información de antecedentes del archivo ODS**

Aspose.Cells proporciona el[**OdsPageFondo**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) clase para administrar el fondo en ODS Archivos. El siguiente ejemplo de código demuestra el uso de[**OdsPageFondo**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) clase cargando el[fuente ODS](90112030.ods) archivo y leer la información de fondo. Consulte la salida de la consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Salida de consola**

Tipo de fondo: Gráfico

Posición de fondo: CentroCentro

## **Agregar fondo de color al archivo ODS**

Aspose.Cells proporciona el[**OdsPageFondo**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)clase para administrar el fondo en ODS Archivos. El siguiente ejemplo de código demuestra el uso de[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) propiedad para agregar un fondo de color al archivo ODS. Por favor vea el[salida ODS](90112031.ods) archivo generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Agregar fondo gráfico al archivo ODS**

Aspose.Cells proporciona el[**OdsPageFondo**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)clase para administrar el fondo en ODS Archivos. El siguiente ejemplo de código demuestra el uso de[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)propiedad para agregar un fondo gráfico al archivo ODS. Por favor vea el[salida ODS](90112030.ods)archivo generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
