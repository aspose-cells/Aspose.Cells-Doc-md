---
title: Eliminar Estilos No Utilizados dentro del Libro de Trabajo
type: docs
weight: 470
url: /es/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Los estilos no utilizados en el archivo de Excel no solo ocupan espacio, sino que también causan problemas de rendimiento al convertir a diferentes formatos como PDF, HTML, etc. Aspose.Cells proporciona [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) para eliminar todos los estilos no utilizados dentro del libro de trabajo.

{{% /alert %}} 
## **Eliminar Estilos No Utilizados dentro del Libro de Trabajo**
El siguiente código explica el uso de [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--). El código carga el [archivo Excel de plantilla](5473451.xlsx) que puede descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado **AsposeStyle**, este estilo y todos los demás estilos no utilizados serán eliminados después de la ejecución del código. Consulte la siguiente captura de pantalla para mayor ilustración.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
