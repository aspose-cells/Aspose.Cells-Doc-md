---
title: Configuración de fórmulas - Aviso para usuarios que no hablan inglés
type: docs
weight: 20
url: /es/java/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

 Aspose.Cells admite la mayoría de las fórmulas/funciones que forman parte de Microsoft Excel. Los desarrolladores pueden usar estas fórmulas con el API o[hojas de calculo de diseñador](/cells/es/java/what-is-a-designer-spreadsheet/). Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y de referencia. Las fórmulas deben especificarse utilizando el estilo inglés (EE. UU.).

Hay dos consejos que los usuarios que no hablan inglés deben seguir al crear fórmulas con Aspose.Cells:

1. Las fórmulas deben ingresarse en inglés.
 Por ejemplo, utilice el inglés "=SUM()" y no el alemán "=SUMME()".
1. Utilice siempre una coma (,) para delimitar los parámetros de la función.
Para algunas opciones o configuraciones de idioma, el delimitador de los parámetros de función es un punto y coma, pero Aspose.Cells usa la coma de estilo inglés. Por ejemplo, use "=SI (C5=0,0,C3/C4)" no "=SI(C5=0;0;C3/C4)"

{{% /alert %}}
