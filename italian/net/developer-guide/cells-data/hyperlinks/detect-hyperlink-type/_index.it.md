---
title: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/net/detect-hyperlink-type/
description: Impara come rilevare il tipo di collegamento ipertestuale tramite l API Aspose.Cells for .NET
keywords: Rileva il tipo di collegamento ipertestuale, Rileva il tipo di collegamento ipertestuale, Ottieni il tipo di collegamento ipertestuale
---

## **Rileva il tipo di collegamento ipertestuale**

Un file di Excel può avere diversi tipi di collegamenti ipertestuali come esterno, riferimento alla cella, percorso del file, ecc. Aspose.Cells supporta la funzione per rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dall'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). L'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) ha i seguenti membri.

- Esterno: collegamento esterno
- PercorsoFile: percorso locale e completo dei file\cartelle.
- Email: email
- RiferimentoCella: collegamento a cella o intervallo denominato.

Per controllare il tipo di collegamento ipertestuale, la classe [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) fornisce una proprietà [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Il seguente frammento di codice mostra l'uso della proprietà [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) utilizzando questo [file Excel di origine](94896195.xlsx).

### Codice Sorgente

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

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
