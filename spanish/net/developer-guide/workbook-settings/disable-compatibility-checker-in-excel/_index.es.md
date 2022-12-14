---
title: Deshabilitar el Comprobador de compatibilidad en Excel
type: docs
weight: 170
url: /es/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## Deshabilite el Comprobador de compatibilidad en hojas de cálculo de Excel en C#

{{% alert color="primary" %}}

Microsoft Las alertas del Comprobador de compatibilidad de Excel al guardar un archivo en un formato de archivo anterior pueden causar problemas de funcionalidad o pérdida de fidelidad. El Comprobador de compatibilidad es una función de Microsoft Office Excel 2007 y Microsoft Excel 2010.

Cuando guarda un libro de trabajo en una versión anterior, de Excel 97 a Excel 2003, de Excel 2007 o Excel 2010, el Comprobador de compatibilidad analiza el libro de trabajo para ver si contiene características que no son compatibles con la versión anterior. Para ayudarlo a tomar decisiones sobre cómo manejar los problemas de compatibilidad, el Comprobador de compatibilidad muestra cuadros de diálogo con opciones. También se puede usar para crear un informe sobre cualquier problema en el libro de trabajo o deshabilitar la función.

veces, debe deshabilitar el Comprobador de compatibilidad para una hoja de cálculo en particular. Con las API Aspose.Cells, puede hacer esto mediante programación para que los usuarios no se frustren o confundan con el cuadro de diálogo Comprobador de compatibilidad que aparece cuando vuelven a guardar el archivo en Microsoft Excel manualmente.

{{% /alert %}}

## **Usando Microsoft Excel**

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo, Microsoft Excel 2007/2010):

-  (Excel 2007) En el botón de Office, haga clic en**Preparar** , después**Ejecutar Comprobador de compatibilidad** y luego borre el**Verifique la compatibilidad cuando guarde este libro de trabajo** opción.
-  (Excel 2010) En la pestaña Archivo, haga clic en**Información** , después**Comprobar si hay problemas** , haga clic**Comprobar compatibilidad** y, finalmente, borre el**Verifique la compatibilidad cuando guarde este libro de trabajo** opción.

## **Uso de las API Aspose.Cells**

 Selecciona el[**Libro de trabajo.Configuración.Comprobar compatibilidad**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) propiedad a**Falso** para deshabilitar Microsoft Comprobador de compatibilidad de Excel.

### **Ejemplos de código**

Los ejemplos de código que siguen muestran cómo deshabilitar el Comprobador de compatibilidad con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
