---
title: Convertir-Excel-a-JSON
type: docs
weight: 300
url: /es/python-java/convert-excel-to-json/
description: Aprenda cómo convertir archivos de Excel a json con Aspose.Cells for Python via Java.
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells for Python via Java admite la conversión de un libro de trabajo a un archivo Json (notación de objetos JavaScript).

{{% /alert %}}

## **Convertir libro de Excel a JSON**

 No es necesario preguntarse cómo convertir Excel Workbook a JSON, porque la biblioteca Aspose.Cells for Python via Java tiene la mejor decisión. El Aspose.Cells for Python via Java API brinda soporte para convertir hojas de cálculo al formato JSON. Para exportar el libro de trabajo a JSON, pase[**GuardarFormato.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) como segundo parámetro de[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ) método. También puede usar[**JsonGuardarOpciones**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) class para especificar configuraciones adicionales para exportar la hoja de trabajo a JSON.

 El siguiente ejemplo de código muestra cómo exportar un libro de Excel a Json. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

 El siguiente ejemplo de código que usa la clase JsonSaveOptions para especificar configuraciones adicionales demuestra cómo exportar un libro de Excel a Json. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
