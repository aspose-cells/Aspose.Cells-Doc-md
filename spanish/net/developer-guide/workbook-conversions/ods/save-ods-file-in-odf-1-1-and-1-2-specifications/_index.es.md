---
title: Guardar archivos ODS en especificaciones ODF 1.1, 1.2 y 1.3
linktitle: Guardar como ODF 1.1, 1.2 y 1.3
description: Convertir Excel a especificaciones ODF 1.1, 1.2 y 1.3 con Aspose.Cells.
type: docs
weight: 230
url: /es/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells soporta guardar un archivo ODS (**Hoja de cálculo del Documento Abierto**) en las especificaciones ODF (**Formato del Documento Abierto**) 1.1, 1.2 y 1.3. Aspose.Cells tiene una propiedad [**OdsSaveOptions.OdfStrictVersion**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/odfstrictversion/) que especifica la versión ODF para guardar archivos ODS. El valor predeterminado de esta propiedad es [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/net/aspose.cells.ods/opendocumentformatversiontype/), por lo que el archivo ODS guardado sin esta configuración utiliza las especificaciones 1.2.

{{% /alert %}}

El código de ejemplo a continuación crea un objeto de libro de trabajo, añade algunos valores a la celda A1 en la primera hoja y luego guarda el archivo ODS en las especificaciones ODF 1.1, 1.2 y 1.3. Por defecto, el archivo ODS se guarda en la especificación ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
{{< app/cells/assistant language="csharp" >}}
