---
title: Establecer el Comentario de la Tabla u Objeto de Lista
type: docs
weight: 60
url: /es/python-java/set-the-comment-of-table-or-list-object/
---

## **Establecer el Comentario de la Tabla o Objeto de Lista dentro de la Hoja de Cálculo**
Aspose.Cells for Python via Java admite agregar el comentario de un objeto de lista. Para esto, la API proporciona la propiedad [ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment). El comentario agregado por la propiedad [ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment) será visible dentro del archivo *xl/tables/tableName.xml*.

La siguiente captura de pantalla muestra el comentario creado por el código de muestra en el rectángulo rojo.

![todo:image_alt_text](setting-list-object-comment.png)

El siguiente código de muestra carga el [archivo de excel de origen](source.xlsx), establece el comentario del primer objeto de tabla o lista dentro de la hoja de cálculo 

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-SetTheCommentOfTableOrListObject.py" >}}
