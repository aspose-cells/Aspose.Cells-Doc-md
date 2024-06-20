---
title: Configuración de fórmulas  Aviso para usuarios no ingleses
type: docs
weight: 20
url: /es/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells admite la mayoría de las fórmulas/funciones que forman parte de Microsoft Excel. Los desarrolladores pueden usar estas fórmulas con la API o con [hojas de cálculo de diseñador](/cells/es/java/what-is-a-designer-spreadsheet/). Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y referencia. Las fórmulas deben especificarse usando el estilo inglés (EE. UU.)

Hay dos consejos que deben seguir los usuarios no ingleses al crear fórmulas con Aspose.Cells:

1. Las fórmulas deben ingresarse en inglés.
   Por ejemplo, use el inglés "=SUM()" no el alemán "=SUMME()".
1. Siempre use una coma (,) para delimitar los parámetros de la función.
   Para algunas opciones o configuraciones de idioma, el delimitador para los parámetros de función es un punto y coma, pero Aspose.Cells usa la coma inglesa. Por ejemplo, use "=IF (C5=0,0,C3/C4)" no "=IF(C5=0;0;C3/C4)" 

{{% /alert %}}
