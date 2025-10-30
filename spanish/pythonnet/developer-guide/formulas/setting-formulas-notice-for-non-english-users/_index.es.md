---
title: Configuración de fórmulas  Aviso para usuarios no ingleses
type: docs
weight: 10
url: /es/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells para Python via .NET admite la mayoría de las fórmulas y funciones que forman parte de Microsoft Excel. Los desarrolladores pueden usar estas fórmulas con la API o [planillas de diseño](/cells/es/net/what-is-a-designer-spreadsheet/). Aspose.Cells para Python via .NET soporta un enorme conjunto de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, bases de datos, búsqueda y referencia. Las fórmulas deben especificarse en estilo inglés (EE.UU).

{{% /alert %}} 

## **Aviso para usuarios no angloparlantes**
Hay dos consejos que los usuarios que no hablan inglés deben seguir al crear fórmulas con Aspose.Cells para Python via .NET:

1. Las fórmulas deben escribirse en inglés. Por ejemplo, utilizar el "=SUM()" en inglés, no el "=SUMME()" en alemán.
1. Usa siempre una coma (,) para delimitar los parámetros de la función. Para algunas opciones o configuraciones de idioma, el delimitador de los parámetros de función es un punto y coma, pero Aspose.Cells para Python via .NET usa la coma en estilo inglés. Por ejemplo, usa "=SI (C5=0,0,C3/C4)" en lugar de "=SI(C5=0;0;C3/C4)"

{{< app/cells/assistant language="python-net" >}}
