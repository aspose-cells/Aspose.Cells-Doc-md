---
title: Configurando fórmulas  Aviso para usuarios que no hablan inglés con JavaScript a través de C++
linktitle: Configuración de fórmulas  Aviso para usuarios no ingleses
type: docs
weight: 10
url: /es/javascript-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells soporta la mayoría de las fórmulas/funciones que forman parte de Microsoft Excel. Los desarrolladores pueden usar estas fórmulas con la API o [diseñadores de hojas de cálculo](/cells/es/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells soporta un conjunto enorme de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, bases de datos, búsqueda y referencia. Las fórmulas deben ser especificadas usando estilo en inglés (EE. UU.).

{{% /alert %}} 

## **Aviso para usuarios no angloparlantes**
Hay dos consejos que deben seguir los usuarios no ingleses al crear fórmulas con Aspose.Cells:

1. Las fórmulas deben escribirse en inglés. Por ejemplo, utilizar el "=SUM()" en inglés, no el "=SUMME()" en alemán.
1. Siempre use una coma (,) para delimitar los parámetros de la función. Para algunas opciones o configuraciones de idioma, el delimitador de los parámetros de la función es un punto y coma, pero Aspose.Cells usa la coma en estilo inglés. Por ejemplo, use "=IF (C5=0,0,C3/C4)" en lugar de "=IF(C5=0;0;C3/C4)".
