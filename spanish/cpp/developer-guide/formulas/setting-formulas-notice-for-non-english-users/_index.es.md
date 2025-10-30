---
title: Configuración de fórmulas  Aviso para usuarios que no hablan inglés con C++
linktitle: Configuración de fórmulas  Aviso para usuarios no ingleses
type: docs
weight: 10
url: /es/cpp/setting-formulas-notice-for-non-english-users/
description: Aprenda cómo establecer fórmulas en Aspose.Cells for C++ con estilo en inglés (EE. UU.) para usuarios que no hablan inglés.
---

{{% alert color="primary" %}} 

Aspose.Cells admite la mayoría de las fórmulas/funciones que forman parte de Microsoft Excel. Los desarrolladores pueden usar estas fórmulas con la API o [herramientas de hojas de cálculo del diseñador](/cells/es/cpp/what-is-a-designer-spreadsheet/). Aspose.Cells soporta un conjunto enorme de fórmulas matemáticas, de texto, booleanas, de fecha/hora, estadísticas, bases de datos, búsqueda y referencia. Las fórmulas deben especificarse usando estilo en inglés (EE. UU.).

{{% /alert %}} 

## **Aviso para usuarios no angloparlantes**
Hay dos consejos que deben seguir los usuarios no ingleses al crear fórmulas con Aspose.Cells:

1. Las fórmulas deben escribirse en inglés. Por ejemplo, utilizar el "=SUM()" en inglés, no el "=SUMME()" en alemán.
1. Siempre use una coma (,) para delimitar los parámetros de la función. Para algunas opciones o configuraciones de idioma, el delimitador de los parámetros de la función es un punto y coma, pero Aspose.Cells usa la coma en estilo inglés. Por ejemplo, use "=IF (C5=0,0,C3/C4)" en lugar de "=IF(C5=0;0;C3/C4)".
{{< app/cells/assistant language="cpp" >}}
