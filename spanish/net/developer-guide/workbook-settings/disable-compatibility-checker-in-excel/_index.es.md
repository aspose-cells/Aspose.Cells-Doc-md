---
title: Deshabilitar el Comprobador de Compatibilidad en Excel
type: docs
weight: 170
url: /es/net/disable-compatibility-checker-in-excel/
description: Este artículo muestra cómo deshabilitar el comprobador de compatibilidad a través de la API Aspose.Cells for .NET.
keywords: C# Deshabilitar el comprobador de compatibilidad, Excel Deshabilitar el comprobador de compatibilidad en C#, Deshabilitar el comprobador de compatibilidad en el libro de trabajo. 
---

## Deshabilitar el comprobador de compatibilidad en las hojas de cálculo de Excel en C# 

{{% alert color="primary" %}}

El Comprobador de compatibilidad de Microsoft Excel señala cuando guardar un archivo en un formato anterior podría causar problemas de funcionamiento o pérdida de fidelidad. El Comprobador de compatibilidad es una característica de Microsoft Office Excel 2007 y Microsoft Excel 2010.

Al guardar un libro de trabajo en una versión anterior, Excel 97 a través de Excel 2003, desde Excel 2007 o Excel 2010, el Comprobador de Compatibilidad escanea el libro de trabajo para ver si contiene funciones que no son compatibles con la versión anterior. Para ayudarlo a tomar decisiones sobre cómo manejar problemas de compatibilidad, el Comprobador de Compatibilidad muestra cuadros de diálogo con opciones. También se puede utilizar para crear un informe sobre cualquier problema en el libro de trabajo o deshabilitar la función.

A veces, necesitas deshabilitar el Comprobador de compatibilidad para una hoja de cálculo en particular. Con las API de Aspose.Cells puedes hacerlo programáticamente para que los usuarios no se frustren o se confundan con el cuadro de diálogo del Comprobador de compatibilidad que aparece al re-guardar manualmente el archivo en Microsoft Excel.

{{% /alert %}}

## **Cómo Deshabilitar el Comprobador de compatibilidad usando Microsoft Excel**

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo, Microsoft Excel 2007/2010):

- (Excel 2007) En el botón de Office, haz clic en **Preparar**, luego en **Ejecutar Comprobador de compatibilidad**, y luego desmarca la opción **Comprobar compatibilidad al guardar este libro**.
- (Excel 2010) En la pestaña **Archivo**, haz clic en **Información**, luego en **Buscar problemas**, haz clic en **Comprobar compatibilidad** y, finalmente, desmarca la opción **Comprobar compatibilidad al guardar este libro**.

## **Cómo Deshabilitar el Comprobador de compatibilidad usando las API de Aspose.Cells**

Establece la propiedad [**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) en **Falso** para deshabilitar el Comprobador de compatibilidad de Microsoft Excel.

### **Ejemplos de código**

Los ejemplos de código que se muestran a continuación muestran cómo deshabilitar el Comprobador de compatibilidad con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
