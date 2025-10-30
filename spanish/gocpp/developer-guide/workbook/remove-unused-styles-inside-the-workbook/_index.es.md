---  
title: Eliminar estilos no utilizados dentro del Libro de trabajo con Golang a través de C++  
linktitle: Eliminar Estilos No Utilizados dentro del Libro de Trabajo  
type: docs  
weight: 340  
url: /es/go-cpp/remove-unused-styles-inside-the-workbook/  
description: Eliminar estilos no utilizados en el libro de Excel usando Aspose.Cells con Golang a través de C++  
---  

{{% alert color="primary" %}}  

Los estilos no utilizados en archivos de Excel no solo ocupan espacio, sino que también causan problemas de rendimiento al convertir a diferentes formatos como PDF, HTML, etc. Aspose.Cells proporciona el método [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) para eliminar todos los estilos no utilizados dentro del libro.  

{{% /alert %}}  

El siguiente código explica el uso de [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/). El código carga el [archivo de plantilla de Excel](5115520.xlsx) que puedes descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado **AsposeStyle**; este estilo y todos los demás estilos no utilizados serán eliminados después de la ejecución del código.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveUnusedStylesInsideTheWorkbook.go" >}}
