---
title: Trabajar con fondo en archivos ODS
type: docs
weight: 170
url: /es/java/working-with-background-in-ods-files/
---

## **Fondo en archivos ODS**

Se pueden agregar fondos a las hojas en los archivos ODS. El fondo puede ser un fondo de color o un fondo gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el diálogo de vista previa de impresión.

Aspose.Cells proporciona la capacidad de leer la información de fondo y agregar fondo en archivos ODS.

## **Leer Información de Fondo de archivos OSD**

Aspose.Cells proporciona la clase [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de la clase [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) cargando el [ODS de origen](GraphicBackground.ods) y leyendo la información de fondo. Consulte la Salida de la Consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Salida de la consola**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Agregar fondo de color al archivo ODS**

Aspose.Cells proporciona la clase [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) para agregar un fondo de color al archivo ODS. Consulte el archivo [ODS de salida](ColoredBackground.ods) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Agregar fondo gráfico al archivo ODS**

Aspose.Cells proporciona la clase [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) para gestionar el fondo en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) para agregar fondo gráfico al archivo ODS. Consulte el archivo [ODS de salida](GraphicBackground.ods) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
{{< app/cells/assistant language="java" >}}
