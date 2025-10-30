---
title: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento
type: docs
weight: 300
url: /es/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Agregar propiedades personalizadas visibles dentro del Panel de información del documento**

Aspose.Cells para Python via .NET se puede usar para agregar propiedades personalizadas dentro del objeto libro que son visibles en el Panel de Información del Documento. Puedes abrir el Panel de Información del Documento en Microsoft Excel usando los comandos de menú Archivo > Información > Propiedades > Mostrar Panel de Documento.

Por favor use el método [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) para agregar una propiedad personalizada que será visible en el Panel de Información del Documento

El siguiente código de ejemplo agrega dos propiedades personalizadas. La primera propiedad es sin ningún tipo y la segunda propiedad tiene un tipo como DateTime. Una vez que abra el archivo de Excel de salida generado por este código, verá estas dos propiedades dentro del Panel de Información del Documento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **Artículo Relacionado**

{{% alert color="primary" %}}

- [Usar Partes de XML Personalizadas en Aspose.Cells](/cells/es/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
