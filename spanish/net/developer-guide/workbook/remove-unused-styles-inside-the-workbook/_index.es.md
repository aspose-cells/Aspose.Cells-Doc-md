---
title: Eliminar estilos no utilizados dentro del libro de trabajo
type: docs
weight: 340
url: /es/net/remove-unused-styles-inside-the-workbook/
---
{{% alert color="primary" %}}

Los estilos no utilizados en el archivo de Excel no solo ocupan espacio sino que también causan problemas de rendimiento al convertir a diferentes formatos como PDF, HTML, etc. Aspose.Cells proporciona la[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) para eliminar todos los estilos no utilizados dentro del libro de trabajo.

{{% /alert %}}

 El siguiente código explica el uso de[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) . El código carga el[plantilla de archivo de Excel](5115520.xlsx) que puede descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado**AsposeEstilo**, este estilo y todos los demás estilos no utilizados se eliminarán después de la ejecución del código.

![todo:imagen_alternativa_texto](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
