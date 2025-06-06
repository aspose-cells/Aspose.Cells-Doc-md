---
title: Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo
linktitle: Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo
description: Aprende cómo obtener una lista de fuentes usadas en una hoja de cálculo o libro de trabajo usando Aspose.Cells for Node.js via C++. Este artículo te mostrará cómo recuperar información de fuentes de un documento.
keywords: Aspose.Cells, Node.js vía C++, Hoja de cálculo, Libro de trabajo, Fuente, Lista
type: docs
weight: 20
url: /es/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Escenarios de uso posibles**

A menudo es necesario conocer las fuentes que se están utilizando en tu libro de trabajo para fines de renderizado. Cuando conviertes tu libro de trabajo en PDF o imagen, Aspose.Cells requiere que todas las fuentes necesarias estén instaladas en tu sistema o presentes en tu **directorio de fuentes**. Si Aspose.Cells no puede encontrar la fuente necesaria, intenta reemplazarla con alguna otra fuente adecuada que esté presente en tu sistema o en tu directorio de fuentes y que pueda sustituir a tu fuente real. Esto no solo resulta en el renderizado no deseado de PDF o imágenes, sino que también requiere tiempo de procesamiento para encontrar fuentes adecuadas.

Para tratar estos casos, debes saber qué fuentes están siendo utilizadas por tu libro de trabajo, luego instalarlas en tu sistema en caso de Windows o colocarlas en tu directorio de fuentes en Windows o Linux.

Aspose.Cells for Node.js via C++ proporciona el método [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--) que devuelve la lista de todas las fuentes usadas en tu libro de trabajo o hoja de cálculo.

## **Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo**

El siguiente código de muestra carga el archivo Excel fuente y recupera la lista de fuentes utilizadas en él. Tiene una hoja de cálculo ficticia a la que se han añadido algunas fuentes ficticias con fines ilustrativos. Cuando el código imprime todas las fuentes dentro del libro de trabajo, también imprime esas fuentes ficticias. La siguiente captura de pantalla muestra el [archivo de Excel de muestra](25395211.xlsx) y cómo se enumeran las fuentes ficticias.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el [archivo Excel de muestra](25395211.xlsx).

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
