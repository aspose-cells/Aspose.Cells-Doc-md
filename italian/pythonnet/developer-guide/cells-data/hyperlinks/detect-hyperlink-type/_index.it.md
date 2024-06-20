---
title: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/python-net/detect-hyperlink-type/
description: Scopri come rilevare il tipo di collegamento ipertestuale tramite Aspose.Cells for Python via .NET API.
keywords: Libreria Excel di Python, Rileva il tipo di collegamento ipertestuale di Python, Rileva il tipo di collegamento ipertestuale di Python, Ottieni il tipo di collegamento di Python.
---

## **Rileva il tipo di collegamento ipertestuale**

Un file Excel può avere diversi tipi di collegamenti ipertestuali come esterni, riferimenti alle celle, percorsi dei file, ecc. Aspose.Cells for Python via .NET supporta la funzionalità di rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dall'enumerazione [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). L'enumerazione [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) ha i seguenti membri.

- ESTERNO: Collegamento esterno
- PERCORSO_FILE: Percorso locale e completo ai file\cartelle.
- EMAIL: Email
- RIFERIMENTO_CELLA: Collegamento a cella o intervallo nominato.

Per controllare il tipo di collegamento ipertestuale, la classe [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) fornisce una proprietà [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). Il seguente frammento di codice mostra l'uso della proprietà [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) utilizzando questo [file Excel di origine](94896195.xlsx).

### Codice Sorgente

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

Di seguito è riportato l'output generato dal frammento di codice indicato sopra.

### Output della console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
