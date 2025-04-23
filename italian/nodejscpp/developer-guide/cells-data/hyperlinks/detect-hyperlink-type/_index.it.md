---
title: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/nodejs-cpp/detect-hyperlink-type/
description: Impara come rilevare il tipo di hyperlink attraverso l API Aspose.Cells for Node.js via C++.
keywords: Rileva il tipo di hyperlink Node.js tramite C++, Rileva il tipo di hyperlink Node.js tramite C++, Ottieni il tipo di hyperlink Node.js tramite C++
---

## **Rilevare il tipo di collegamento ipertestuale**

Un file Excel può avere diversi tipi di hyperlink come esterno, riferimento a cella, percorso file, ecc. Aspose.Cells for Node.js via C++ supporta la funzione per rilevare il tipo di hyperlink. I tipi di hyperlink sono rappresentati dall'enumerazione [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). L'enumerazione [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) ha i seguenti membri.

- Esterno: collegamento esterno
- FilePath: Percorso locale e completo ai file/cartelle.
- Email: Email
- RiferimentoCella: Link a cella o intervallo nominato.

Per verificare il tipo di hyperlink, la classe [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) fornisce un metodo [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). Il seguente esempio di codice dimostra l'uso del metodo [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) utilizzando questo [file Excel di origine](94896195.xlsx).

### Codice Sorgente

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


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
