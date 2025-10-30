---
title: Establecimiento de fórmulas  Aviso para usuarios no angloparlantes con Node.js mediante C++
linktitle: Configuración de fórmulas  Aviso para usuarios no ingleses
type: docs
weight: 10
url: /es/nodejs-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells soporta la mayoría de las fórmulas/funciones que forman parte de Microsoft Excel. Los desarrolladores pueden usar estas fórmulas con la API o [hojas de cálculo de diseño](/cells/es/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells soporta un enorme conjunto de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y referencia. Las fórmulas deben especificarse usando estilo inglés (EE. UU.).

{{% /alert %}} 

## **Aviso para usuarios no angloparlantes**
Hay dos consejos que deben seguir los usuarios no ingleses al crear fórmulas con Aspose.Cells:

1. Las fórmulas deben escribirse en inglés. Por ejemplo, utilizar el "=SUM()" en inglés, no el "=SUMME()" en alemán.
1. Siempre use una coma (,) para delimitar los parámetros de la función. Para algunas opciones o configuraciones de idioma, el delimitador de los parámetros de la función es un punto y coma, pero Aspose.Cells usa la coma en estilo inglés. Por ejemplo, use "=IF (C5=0,0,C3/C4)" en lugar de "=IF(C5=0;0;C3/C4)".  
{{< app/cells/assistant language="nodejs-cpp" >}}
