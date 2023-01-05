---
title: Combine varios libros de trabajo en un solo libro de trabajo
linktitle: Fusión de libros
type: docs
weight: 66
url: /es/net/combine-multiple-workbooks-into-a-single-workbook/
---
{{% alert color="primary" %}}

veces, necesita combinar libros de trabajo con varios contenidos como imágenes, gráficos y datos en un solo libro de trabajo. Aspose.Cells admite esta función. Este artículo muestra cómo crear una aplicación de consola en Visual Studio y combinar libros de trabajo con unas pocas líneas de código simples usando Aspose.Cells.

{{% /alert %}}

## **Combinar libros de trabajo con imágenes y gráficos**

El código de ejemplo combina dos libros de trabajo en un solo libro de trabajo usando Aspose.Cells. El código carga los libros de trabajo de origen, usa el[**Libro de trabajo.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)método para combinarlos y guarda el libro de trabajo de salida.

### **Libros de origen**

- [gráficos.xlsx](5473097.xlsx)
- [imagen.xlsx](5473096.xlsx)

### **Libros de trabajo de salida**

- [combinado.xlsx](5473095.xlsx)

### **capturas de pantalla**

A continuación se muestran capturas de pantalla de los libros de trabajo de origen y de salida.

{{% alert color="primary" %}}

Puede utilizar cualquier libro de trabajo de origen. Estas imágenes son solo para fines ilustrativos.

{{% /alert %}}

**La primera hoja de cálculo del libro de gráficos - apilada** 

![todo:imagen_alternativa_texto](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Segunda hoja de trabajo del libro de gráficos - línea** 

![todo:imagen_alternativa_texto](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primera hoja de trabajo del libro de trabajo de imágenes - imagen** 

![todo:imagen_alternativa_texto](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Las tres hojas de trabajo en el libro de trabajo combinado: apiladas, línea, imagen** 

![todo:imagen_alternativa_texto](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Temas avanzados**
- [Combine varias hojas de trabajo en una sola hoja de trabajo](/cells/es/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Combinar archivos](/cells/es/net/merge-files/)
