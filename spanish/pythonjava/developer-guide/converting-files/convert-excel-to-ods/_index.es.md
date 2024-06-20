---
title: Convertir Excel a ODS
type: docs
weight: 40
url: /es/python-java/convert-excel-to-ods/
---

## **Convertir Excel a ODS**
Los archivos ODS son creados por el programa Calc que es parte de Apache OpenOffice Suite. Los archivos ODS almacenan datos organizados en filas y columnas y están formateados utilizando el estándar basado en XML de OpenDocument de OASIS.

Aspose.Cells para Python via Java soporta trabajar con archivos ODS. Los siguientes ejemplos demuestran la conversión de Excel a un archivo ODS.
### **Conversión Directa**
La forma más simple de convertir un archivo Excel a ODS es cargar el libro de trabajo y guardarlo pasando [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) como el segundo parámetro del método [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)).

El siguiente fragmento de código demuestra la conversión directa de Excel a ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Guardar el documento ODS en las Especificaciones ODF 1.1 o 1.2**
Aspose.Cells para Python via Java soporta guardar archivos ODS en las especificaciones ODF 1.1 y ODF 1.2. Para esto, la API proporciona la propiedad [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11). Establecer esta propiedad como **true** guardará el archivo con la especificación ODF 1.1. El valor predeterminado de [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) es **false**, por lo que el archivo ODS guardado sin configuraciones especiales se guarda con la especificación ODF 1.2.

El siguiente fragmento de código demuestra cómo guardar archivos ODS con las especificaciones ODF 1.1 y 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
