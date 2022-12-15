---
title: Deshabilitar el Comprobador de compatibilidad en Excel
type: docs
weight: 270
url: /es/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft El Comprobador de compatibilidad de Excel indica al guardar un archivo en un formato de archivo anterior que guardar el archivo puede causar problemas de funcionalidad o pérdida de fidelidad. El Comprobador de compatibilidad es una función de Microsoft Office Excel 2007, 2010 y 2013.

Cuando guarda un libro de trabajo en una versión anterior, de Excel 97 a Excel 2003, de Excel 2007 o Excel 2010, el Comprobador de compatibilidad analiza el libro de trabajo para ver si contiene características que no son compatibles con la versión anterior. Para ayudarlo a tomar decisiones sobre cómo manejar los problemas de compatibilidad, el Comprobador de compatibilidad muestra cuadros de diálogo con opciones. También se puede usar para crear un informe sobre cualquier problema en el libro de trabajo o deshabilitar la función.

A veces, debe deshabilitar el Comprobador de compatibilidad para una hoja de cálculo en particular. Con las API Aspose.Cells, puede hacer esto dinámicamente para que los usuarios no se sientan frustrados o confundidos por el cuadro de diálogo Comprobador de compatibilidad que aparece cuando vuelven a guardar el archivo en Microsoft Excel manualmente.

{{% /alert %}}

## **Usando Microsoft Excel**

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo, Microsoft Excel 2007/2010):

-  (Excel 2007) En el botón de Office, haga clic en**Preparar** , después**Ejecutar Comprobador de compatibilidad** y luego borre el**Verifique la compatibilidad cuando guarde este libro de trabajo** opción.
-  (Excel 2010 y 2013) En la pestaña Archivo, haga clic en**Información** , después**Comprobar si hay problemas** , haga clic**Comprobar compatibilidad** y, finalmente, borre la**Verifique la compatibilidad cuando guarde este libro de trabajo** opción.

## **Uso de las API Aspose.Cells**

 Selecciona el[**WorkbookSettings.Comprobar la compatibilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) propiedad a**Falso** para deshabilitar Microsoft Comprobador de compatibilidad de Excel.

Supongamos que tenemos un archivo XLS de plantilla. Cuando un usuario lo guarda o vuelve a guardar en MS Excel 2007/2010/2013, se muestra el cuadro de diálogo Comprobador de compatibilidad, como se muestra en la siguiente captura de pantalla.

![todo:imagen_alternativa_texto](disable-compatibility-checker-in-excel_1.png)

El siguiente código muestra cómo deshabilitar el Comprobador de compatibilidad con Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
