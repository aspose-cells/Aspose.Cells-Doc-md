---
title: Combinar varios libros de trabajo en un único libro
linktitle: Combinar libros de trabajo
type: docs
weight: 66
url: /es/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

A veces, necesita combinar libros de trabajo con contenido variado como imágenes, gráficos y datos en un solo libro. Aspose.Cells para Python via .NET soporta esta función. Este artículo muestra cómo crear una aplicación de consola en Visual Studio y combinar libros con unas pocas líneas de código usando Aspose.Cells para Python via .NET.

{{% /alert %}}

## **Combinar libros de trabajo con imágenes y gráficos**

El código de ejemplo combina dos libros en un solo libro usando Aspose.Cells para Python via .NET. El código carga los libros de origen, usa el método [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) para combinarlos y guarda el libro de salida.

### **Libros de trabajo de origen**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Libros de trabajo de salida**

- [combined.xlsx](5473095.xlsx)

### **Capturas de pantalla**

A continuación se muestran capturas de pantalla de los libros de trabajo de origen y de salida.

{{% alert color="primary" %}}

Puede utilizar cualquier libro de trabajo de origen. Estas imágenes son solo con fines ilustrativos.

{{% /alert %}}

**La primera hoja de cálculo del libro de trabajo de gráficos: apilada** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Segunda hoja de cálculo del libro de trabajo de gráficos: línea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primera hoja de cálculo del libro de trabajo de imagen: imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Las tres hojas de cálculo en el libro de trabajo combinado: apilada, línea, imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Temas avanzados**
- [Combinar múltiples hojas de cálculo en una sola hoja de cálculo](/cells/es/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionar archivos](/cells/es/python-net/merge-files/)

