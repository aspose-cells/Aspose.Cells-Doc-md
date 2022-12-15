---
title: Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo
type: docs
weight: 20
url: /es/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Posibles escenarios de uso**

 menudo es necesario conocer las fuentes que se utilizan en su libro de trabajo para fines de representación. Cuando convierte su libro de trabajo en PDF o imagen, entonces Aspose.Cells requiere que todas las fuentes necesarias estén instaladas en su sistema o presentes en su**directorio de fuentes**Si Aspose.Cells no puede encontrar la fuente necesaria, intenta reemplazarla con alguna otra fuente adecuada que esté presente en su sistema o en su directorio de fuentes y puede sustituir su fuente real. Esto no solo da como resultado la representación no deseada de PDF o imágenes, sino que también requiere tiempo de procesamiento para encontrar las fuentes adecuadas.

Para lidiar con tales casos, debe saber qué fuentes está utilizando su libro de trabajo, luego instale esas fuentes en su sistema en el caso del entorno Windows o colóquelas en su directorio de fuentes en el caso de Windows o entorno Linux.

 Aspose.Cells proporciona el**[Libro de trabajo.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**método que devuelve la lista de todas las fuentes utilizadas en su libro de trabajo u hoja de cálculo.

## **Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo**

 El siguiente código de muestra carga el archivo fuente de Excel y recupera la lista de fuentes utilizadas en su interior. Tiene una hoja de trabajo ficticia que tiene algunas fuentes ficticias agregadas con fines ilustrativos. Cuando el código imprime todas las fuentes dentro del libro de trabajo, también imprime esas fuentes ficticias. La siguiente captura de pantalla muestra la[ejemplo de archivo de Excel](25395211.xlsx) cómo se enumeran las fuentes ficticias.

![todo:imagen_alternativa_texto](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **Salida de consola**

 Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el dado[ejemplo de archivo de Excel](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0]]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

{{< /highlight >}}
