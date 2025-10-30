---
title: Guardar archivo ODS en las especificaciones ODF 1.1 y 1.2
linktitle: Guardar como ODF 1.1 y 1.2 
description: Convertir Excel a las especificaciones ODF 1.1 y 1.2 con Aspose.Cells.
type: docs
weight: 230
url: /es/python-net/save-ods-file-in-odf-1-1-and-1-2-specifications/
description: Cómo guardar un archivo ODS en las especificaciones ODF 1.1 y 1.2 con la API de Aspose.Cells for Python via .NET.
keywords: Python Guardar archivo ODS en las especificaciones ODF 1.1 y 1.2, Guardar archivo ODS en las especificaciones ODF 1.1 y 1.2 con Python via NET.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET admite guardar un archivo ODS (Hoja de cálculo de Documento Abierto) en las especificaciones ODF (Formato de Documento Abierto) 1.1 y 1.2. Aspose.Cells for Python via .NET tiene una propiedad [**OdsSaveOptions.is_strict_schema11**](https://reference.aspose.com/cells/python-net/aspose.cells/odssaveoptions/is_strict_schema11/) que especifica el uso de la especificación ODF 1.1 para guardar archivos ODS. El valor predeterminado de esta propiedad es **falso**, por lo que el archivo ODS guardado sin este ajuste utiliza las especificaciones 1.2.

{{% /alert %}}

El código de muestra a continuación crea un objeto de libro, agrega algún valor a la celda A1 en la primera hoja de cálculo y luego guarda el archivo ODS en las especificaciones ODF 1.1 y 1.2. Por defecto, el archivo ODS se guarda en la especificación ODF 1.2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.py" >}}
{{< app/cells/assistant language="python-net" >}}
