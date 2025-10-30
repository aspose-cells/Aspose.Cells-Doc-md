---
title: Eliminar Estilos No Utilizados dentro del Libro de Trabajo
type: docs
weight: 340
url: /es/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Los estilos no utilizados en el archivo de Excel no solo ocupan espacio sino que también causan problemas de rendimiento al convertir a otros formatos como PDF, HTML, etc. Aspose.Cells para Python via .NET proporciona el método [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) para eliminar todos los estilos no utilizados dentro del libro.

{{% /alert %}}

El siguiente código explica el uso de [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). El código carga el [archivo de Excel de plantilla](5115520.xlsx) que puedes descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado **AsposeStyle**, este estilo y todos los demás estilos no utilizados se eliminarán después de la ejecución del código.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
