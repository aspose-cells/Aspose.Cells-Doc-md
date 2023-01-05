---
title: Trabajar con fondo en archivos ODS
type: docs
weight: 170
url: /es/java/working-with-background-in-ods-files/
---
## **Antecedentes en ODS Archivos**

El fondo se puede agregar a las hojas en los archivos ODS. El fondo puede ser un fondo de color o un fondo gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el diálogo de vista previa de impresión.

Aspose.Cells brinda la capacidad de leer la información de fondo y agregar antecedentes en archivos ODS.

## **Leer información de fondo del archivo OSD**

Aspose.Cells proporciona el[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)clase para administrar el fondo en ODS Archivos. El siguiente ejemplo de código demuestra el uso de[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)clase cargando el[fuente ODS](GraphicBackground.ods)archivo y leer la información de fondo. Consulte la salida de la consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Salida de consola**

Tipo de fondo: GRÁFICO

Posición de fondo: CENTER_CENTER

## **Agregar fondo de color al archivo ODS**

Aspose.Cells proporciona el[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)clase para administrar el fondo en ODS Archivos. El siguiente ejemplo de código demuestra el uso de[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)propiedad para agregar un fondo de color al archivo ODS. Por favor vea el[salida ODS](ColoredBackground.ods)archivo generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Agregar fondo gráfico al archivo ODS**

Aspose.Cells proporciona el[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)clase para administrar el fondo en ODS Archivos. El siguiente ejemplo de código demuestra el uso de[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)propiedad para agregar un fondo gráfico al archivo ODS. Por favor vea el[salida ODS](GraphicBackground.ods)archivo generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
