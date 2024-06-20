---
title: Guardar archivo ODS en las especificaciones ODF 1.1 y 1.2
linktitle: Guardar como ODF 1.1 y 1.2 
description: Convertir Excel a las especificaciones ODF 1.1 y 1.2 con Aspose.Cells.
type: docs
weight: 230
url: /es/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells admite guardar un archivo ODS (**OpenDocument Spreadsheet**) en las especificaciones ODF (**OpenDocument Format**) 1.1 y 1.2. Aspose.Cells tiene una propiedad [**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11) que especifica el uso de la especificación ODF 1.1 para guardar archivos ODS. El valor predeterminado de esta propiedad es **falso**, por lo que el archivo ODS guardado sin esta configuración usa las especificaciones 1.2.

{{% /alert %}}

El código de muestra a continuación crea un objeto de libro, agrega algún valor a la celda A1 en la primera hoja de cálculo y luego guarda el archivo ODS en las especificaciones ODF 1.1 y 1.2. Por defecto, el archivo ODS se guarda en la especificación ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
