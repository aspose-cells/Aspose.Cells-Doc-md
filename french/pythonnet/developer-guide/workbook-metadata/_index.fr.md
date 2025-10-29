---
title: Utilisation de WorkbookMetadata avec Python.NET
linktitle: Métadonnées du classeur
type: docs
weight: 320
url: /fr/python-net/using-workbookmetadata/
description: Apprenez comment gérer efficacement les métadonnées du classeur en utilisant l’API Aspose.Cells pour Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de charger une version légère du classeur en mémoire pour éditer ses informations de métadonnées. Veuillez utiliser la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) pour charger le classeur.

{{% /alert %}}

Le code d'exemple suivant utilise la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) pour modifier les propriétés personnalisées du document d'un classeur. Une fois que vous avez ouvert le classeur à l'aide de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), vous pourrez lire les propriétés du document. Voici un exemple de code utilisant la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata).

```python
import os
from aspose.cells import Workbook
from aspose.cells.metadata import MetadataOptions, MetadataType, WorkbookMetadata

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Open Workbook metadata
options = MetadataOptions(MetadataType.DOCUMENT_PROPERTIES)
meta = WorkbookMetadata(os.path.join(data_dir, "Sample1.xlsx"), options)

# Set some properties
meta.custom_document_properties.add("test", "test")

# Save the metadata info
meta.save(os.path.join(data_dir, "Sample2.out.xlsx"))

# Open the workbook
w = Workbook(os.path.join(data_dir, "Sample2.out.xlsx"))

# Read document property
print(w.custom_document_properties.get("test"))

print("Press any key to continue...")
```

{{< app/cells/assistant language="python-net" >}}
