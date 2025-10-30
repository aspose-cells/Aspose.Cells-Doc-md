---
title: Rileva il tipo di collegamento ipertestuale con Golang tramite C++
linktitle: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/go-cpp/detect-hyperlink-type/
description: Impara come rilevare il tipo di hyperlink tramite l API Aspose.Cells for C++.
keywords: Rileva il tipo di collegamento ipertestuale, Rileva il tipo di collegamento ipertestuale, Ottieni il tipo di collegamento ipertestuale
---

## **Rilevare il tipo di collegamento ipertestuale**

Un file di Excel può avere diversi tipi di collegamenti ipertestuali come esterno, riferimento alla cella, percorso del file, ecc. Aspose.Cells supporta la funzione per rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dall'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/). L'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) ha i seguenti membri.

- Esterno: collegamento esterno
- PercorsoFile: percorso locale e completo dei file\cartelle.
- Email: email
- RiferimentoCella: collegamento a cella o intervallo denominato.

Per controllare il tipo di collegamento ipertestuale, la classe [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) fornisce una proprietà [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). Il seguente frammento di codice mostra l'uso della proprietà [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) utilizzando questo [file Excel di origine](94896195.xlsx).

### Codice Sorgente

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
Di seguito è riportato l'output generato dal frammento di codice indicato sopra.

### Output della console
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
