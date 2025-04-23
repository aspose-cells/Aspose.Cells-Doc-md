---
title: Rilascia le risorse non gestite del Workbook con Python via .NET
linktitle: Rilascia le risorse non gestite
type: docs
weight: 310
url: /it/python-net/release-unmanaged-resources-of-the-workbook/
description: Impara come rilasciare correttamente le risorse non gestite lavorando con i workbook Excel usando Aspose.Cells per Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) per rilasciare le risorse non gestite dell’oggetto [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Questo pattern è fondamentale per gestire risorse non gestite come handle di file, stream o allocazioni di memoria che non sono gestite automaticamente dal garbage collector di Python.

{{% /alert %}}

La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) implementa il protocollo del gestore di contesto di Python per la gestione delle risorse. Puoi chiamare esplicitamente il metodo [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) o usare l'istruzione `with` di Python per garantire una corretta pulizia.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
