---
title: Eliminar Estilos No Utilizados dentro del Libro de Trabajo
type: docs
weight: 340
url: /es/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Los estilos no utilizados en un archivo de Excel no solo ocupan espacio, sino que también causan problemas de rendimiento al convertir a diferentes formatos como PDF, HTML, etc. Aspose.Cells proporciona el [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) para eliminar todos los estilos no utilizados dentro del libro de trabajo.

{{% /alert %}}

El siguiente código explica el uso de [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles). El código carga el [archivo de Excel de plantilla](5115520.xlsx) que puedes descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado **AsposeStyle**, este estilo y todos los demás estilos no utilizados se eliminarán después de la ejecución del código.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
