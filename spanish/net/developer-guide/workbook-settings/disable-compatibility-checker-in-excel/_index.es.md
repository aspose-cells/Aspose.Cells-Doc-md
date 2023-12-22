---
title: Deshabilitar el Comprobador de compatibilidad en Excel
type: docs
weight: 170
url: /es/net/disable-compatibility-checker-in-excel/
description: Este artículo muestra cómo deshabilitar el verificador de compatibilidad a través de Aspose.Cells for .NET API.
keywords: C# Disable Compatibility Checker, Excel Disable Compatibility Checker in C#, Disable Compatibility Checker in Workbook. 
---
##  Deshabilite el Comprobador de compatibilidad en hojas de cálculo de Excel en C#

{{% alert color="primary" %}}

Microsoft Los indicadores del Comprobador de compatibilidad de Excel al guardar un archivo en un formato de archivo anterior pueden causar problemas de funcionalidad o pérdida de fidelidad. El Comprobador de compatibilidad es una característica de Microsoft Office Excel 2007 y Microsoft Excel 2010.

Cuando guarda un libro en una versión anterior, de Excel 97 a Excel 2003, de Excel 2007 o Excel 2010, el Comprobador de compatibilidad escanea el libro para ver si contiene características que no son compatibles con la versión anterior. Para ayudarle a tomar decisiones sobre cómo manejar los problemas de compatibilidad, el Comprobador de compatibilidad muestra cuadros de diálogo con opciones. También se puede utilizar para crear un informe sobre cualquier problema en el libro o desactivar la función.

A veces, es necesario desactivar el Comprobador de compatibilidad para una hoja de cálculo en particular. Con las API de Aspose.Cells', puede hacer esto mediante programación para que los usuarios no se sientan frustrados o confundidos por el cuadro de diálogo Comprobador de compatibilidad que aparece cuando vuelven a guardar el archivo en Microsoft Excel manualmente.

{{% /alert %}}

##  **Cómo deshabilitar el Comprobador de compatibilidad usando Microsoft Excel**

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo Microsoft Excel 2007/2010):

-  (Excel 2007) En el botón Office, haga clic en**Prepare**, luego **Ejecute el Comprobador de compatibilidad** y luego borre **Verificar compatibilidad al guardar este libro.** opción.
-  (Excel 2010) En la pestaña Archivo, haga clic en**Información**, luego **Verificar problemas**, hacer clic en **Verificar compatibilidad** y, finalmente, borrar la casilla **Verificar compatibilidad al guardar este libro.** opción.

##  **Cómo deshabilitar el Comprobador de compatibilidad usando las API Aspose.Cells**

 Selecciona el[**Libro de trabajo.Configuración.ComprobarComptibilidad**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) propiedad a**FALSO** para desactivar Microsoft Comprobador de compatibilidad de Excel.

###  **Ejemplos de código**

Los ejemplos de código que siguen muestran cómo deshabilitar el Comprobador de compatibilidad con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
