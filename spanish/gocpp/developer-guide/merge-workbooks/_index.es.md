---
title: Combina Múltiples Libros en un Solo Libro con Golang vía C++
linktitle: Combinar libros de trabajo
type: docs
weight: 66
url: /es/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aprende cómo combinar múltiples libros en un solo libro usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

A veces, necesitas combinar libros de trabajo con diferentes contenidos, como imágenes, gráficos y datos, en un solo libro de trabajo. Aspose.Cells soporta esta función. Este artículo muestra cómo crear una aplicación de consola en Visual Studio y combinar libros de trabajo con unas pocas líneas de código usando Aspose.Cells.

{{% /alert %}}

## **Combinar libros de trabajo con imágenes y gráficos**

El código de ejemplo combina dos libros de trabajo en un único libro utilizando Aspose.Cells. El código carga los libros de trabajo de origen, utiliza el método [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) para combinarlos y guarda el libro de trabajo de salida.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Temas avanzados**
- [Combinar múltiples hojas de cálculo en una sola hoja de cálculo](/cells/es/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionar archivos](/cells/es/cpp/merge-files/)
