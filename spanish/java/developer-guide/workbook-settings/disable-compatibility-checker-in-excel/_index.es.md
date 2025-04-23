---
title: Deshabilitar el Comprobador de Compatibilidad en Excel
type: docs
weight: 270
url: /es/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

El Comprobador de Compatibilidad de Microsoft Excel alerta al guardar un archivo en un formato de archivo anterior que hacerlo podría causar problemas de funcionalidad o pérdida de fidelidad. El Comprobador de Compatibilidad es una función de Microsoft Office Excel 2007, 2010 y 2013.

Al guardar un libro de trabajo en una versión anterior, Excel 97 a través de Excel 2003, desde Excel 2007 o Excel 2010, el Comprobador de Compatibilidad escanea el libro de trabajo para ver si contiene funciones que no son compatibles con la versión anterior. Para ayudarlo a tomar decisiones sobre cómo manejar problemas de compatibilidad, el Comprobador de Compatibilidad muestra cuadros de diálogo con opciones. También se puede utilizar para crear un informe sobre cualquier problema en el libro de trabajo o deshabilitar la función.

A veces, necesita deshabilitar el Comprobador de Compatibilidad para una hoja de cálculo en particular. Con las API de Aspose.Cells, puede hacerlo dinámicamente para que los usuarios no se sientan frustrados o confundidos por la aparición del cuadro de diálogo del Comprobador de Compatibilidad al guardar manualmente el archivo en Microsoft Excel.

{{% /alert %}}

## **Usar Microsoft Excel**

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo, Microsoft Excel 2007/2010):

- (Excel 2007) En el botón de Office, haz clic en **Preparar**, luego en **Ejecutar Comprobador de compatibilidad**, y luego desmarca la opción **Comprobar compatibilidad al guardar este libro**.
- (Excel 2010 y 2013) En la pestaña Archivo, haz clic en **Información**, luego en **Buscar problemas**, haz clic en **Comprobar compatibilidad**, y, finalmente, desmarca la opción **Comprobar compatibilidad al guardar este libro**.

## **Usando las APIs de Aspose.Cells**

Establece la propiedad [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) en **Falso** para deshabilitar el Comprobador de compatibilidad de Microsoft Excel.

Supongamos que tenemos un archivo XLS plantilla. Cuando un usuario lo guarda o vuelve a guardarlo en MS Excel 2007/2010/2013, se muestra el cuadro de diálogo del Comprobador de compatibilidad, como se muestra en la captura de pantalla a continuación.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

El siguiente código muestra cómo deshabilitar el Comprobador de compatibilidad con Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
{{< app/cells/assistant language="java" >}}
