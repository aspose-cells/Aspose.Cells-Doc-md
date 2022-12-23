---
title: Convertir-Excel-a-JSON
type: docs
weight: 20
url: /es/java/convert-excel-to-json/
description: Aprenda cómo convertir un archivo de Excel a json con Aspose.Cells.
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells admite la conversión de un libro de trabajo a un archivo Json (notación de objetos de JavaScript).

{{% /alert %}}

## **Convertir libro de Excel a JSON**

 No hay necesidad de preguntarse cómo convertir Excel Workbook a JSON, porque la biblioteca Aspose.Cells Java tiene la mejor decisión. El Aspose.Cells Java API brinda soporte para convertir hojas de cálculo al formato JSON. Para exportar el libro de trabajo a JSON, pase[**GuardarFormato.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) como segundo parámetro de[**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) ) método. También puede usar[**JsonGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) class para especificar configuraciones adicionales para exportar la hoja de trabajo a JSON.

 El siguiente ejemplo de código muestra cómo exportar un libro de Excel a Json. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

 El siguiente ejemplo de código que usa la clase JsonSaveOptions para especificar configuraciones adicionales demuestra cómo exportar un libro de Excel a Json. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
