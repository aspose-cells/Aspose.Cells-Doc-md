---
title: Convertir Excel a ODS
type: docs
weight: 40
url: /es/python-java/convert-excel-to-ods/
---
## **Convertir Excel a ODS**
Los archivos ODS son creados por el programa Calc, que forma parte de Apache OpenOffice Suite. Los archivos ODS almacenan datos organizados en filas y columnas y están formateados utilizando el estándar basado en XML OASIS OpenDocument.

Aspose.Cells for Python via Java admite archivos de trabajo ODS. Los siguientes ejemplos muestran cómo convertir Excel a un archivo ODS.
### **Conversión Directa**
La forma más sencilla de convertir un archivo de Excel a ODS es cargar el libro de trabajo y guardarlo pasando[GuardarFormato.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) como segundo parámetro de la[Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) método.

El siguiente fragmento de código demostró convertir Excel directamente a ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Guarde el documento ODS en ODF 1.1 o 1.2 Especificaciones**
Aspose.Cells for Python via Java admite guardar archivos ODS en las especificaciones ODF 1.1 y ODF 1.2. Para esto, el API proporciona[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) propiedad. Estableciendo esta propiedad en**verdadero** guardará el archivo con la especificación ODF 1.1. El valor predeterminado de[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) es**falso**, por lo que el archivo ODS guardado sin configuraciones especiales se guarda con la especificación ODF 1.2.

El siguiente fragmento de código demostró guardar archivos ODS con especificaciones ODF 1.1 y 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
