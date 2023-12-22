---
title: Convertir Excel a JSON
type: docs
weight: 20
url: /es/java/convert-excel-to-json/
description: Aprenda a convertir archivos de Excel a json con las API Aspose.Cells for Java.
keywords: Java Export Workbook to json, Convert Excel to JSON using Java, Save Excel to JSON in Java, Convert Workbook to JSON using Java, Save Workbook to JSON in Java, Export Excel to JSON via Java.
---
{{% alert color="primary" %}}

Aspose.Cells admite la conversión de un libro de trabajo a un archivo Json (notación de objetos JavaScript).

{{% /alert %}}

##  **Cómo convertir un libro de Excel a JSON**

 No es necesario preguntarse cómo convertir un libro de Excel a JSON, porque la biblioteca Aspose.Cells Java tiene la mejor decisión. Aspose.Cells Java API proporciona soporte para convertir hojas de cálculo al formato JSON. Para exportar el libro a JSON, pase[**Guardar formato.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) como segundo parámetro de[**Libro de trabajo.guardar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) ) método. También puedes usar[**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) clase para especificar configuraciones adicionales para exportar la hoja de trabajo a JSON.

 El siguiente ejemplo de código demuestra la exportación de un libro de Excel a Json. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

 El siguiente ejemplo de código que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales demuestra la exportación de un libro de Excel a Json. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
