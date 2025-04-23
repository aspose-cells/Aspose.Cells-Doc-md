---
title: Guardar archivo ODS en las Especificaciones ODF 1.1, 1.2 y 1.3
type: docs
weight: 170
url: /es/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells admite guardar archivos (**OpenDocument Spreadsheet**) ODS en el (**Formato OpenDocument**) ODF 1.1, 1.2 y 1.3. Aspose.Cells ha añadido la propiedad [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) para usar la versión ODF al guardar archivos ODS. El valor predeterminado de esta propiedad es [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12), por lo que los archivos ODS guardados sin esta configuración especial usarán la especificación 1.2.

{{% /alert %}}

El código de muestra a continuación crea el objeto del libro, agrega algún valor en la celda A1 de la primera hoja de trabajo y luego guarda el archivo ODS en las especificaciones ODF 1.1 y 1.2. Por defecto, el archivo ODS se guarda en la especificación ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
