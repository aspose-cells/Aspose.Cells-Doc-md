---
title: Copiar y mover hojas de trabajo dentro y entre libros de trabajo con Golang mediante C++
linktitle: Copiar y mover hojas de trabajo
type: docs
weight: 80
url: /es/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aprenda cómo copiar y mover hojas de trabajo dentro y entre libros de trabajo de Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, necesita varias hojas de trabajo con formato y entrada de datos comunes. Por ejemplo, si trabaja con presupuestos trimestrales, puede querer crear un libro con hojas que contienen los mismos encabezados de columnas, filas y fórmulas. Hay una forma de hacer esto: creando una hoja y luego copiándola varias veces.

Aspose.Cells admite la copia o el movimiento de hojas de cálculo dentro o entre libros de Excel. Las hojas de cálculo, incluidos datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el más alto grado de precisión.

{{% /alert %}}

## **Copiar y mover hojas de cálculo**

### **Copiando una Hoja de Cálculo dentro de un Libro**

Los pasos iniciales son los mismos para todos los ejemplos:

1. Crear dos libros de trabajo con algunos datos en Microsoft Excel. Para este ejemplo, creamos dos nuevos libros en Microsoft Excel e ingresamos algunos datos en las hojas:
   - FirstWorkbook.xlsx (3 hojas de trabajo)
   - SecondWorkbook.xlsx (1 hoja de trabajo)

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Instalarlo en su ordenador de desarrollo

1. Cree un proyecto:
   1. Crear un nuevo proyecto en C++ en su IDE preferido

1. Agregue referencias:
   1. Agregar la biblioteca Aspose.Cells for C++ a su proyecto

1. Copia la hoja de cálculo dentro de un libro de trabajo.
   El primer ejemplo copia la primera hoja de cálculo (Copia) dentro de FirstWorkbook.xlsx.

Al ejecutar el código, se copia la hoja llamada Copia dentro de FirstWorkbook.xlsx con el nombre Última Hoja.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Moviendo una Hoja de Cálculo dentro de un Libro de Trabajo**

El siguiente código muestra cómo mover una hoja de cálculo desde una posición a otra en un libro de trabajo. Al ejecutar el código, se mueve la hoja llamada Mover del índice 1 al índice 2 en FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Copiando una hoja de cálculo entre libros**

Al ejecutar el código, copia la hoja llamada Copy a SecondWorkbook.xlsx con el nombre Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Moviendo una hoja de cálculo entre libros**

Al ejecutar el código se mueve la hoja llamada Mover de FirstWorkbook.xlsx a SecondWorkbook.xlsx con el nombre Hoja3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
