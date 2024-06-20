---
title: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 180
url: /it/java/detect-hyperlink-type/
---

## **Rileva il tipo di collegamento ipertestuale**

Un file Excel può avere diversi tipi di collegamenti ipertestuali come esterni, riferimenti a celle, percorsi dei file, ecc. Aspose.Cells supporta la funzionalità per rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dall'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). L'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) ha i seguenti membri.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Collegamento esterno
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Percorso locale e completo dei file\cartelle.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): Email
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Collegamento alla cella o al range denominato.

Per verificare il tipo di collegamento ipertestuale, la classe [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) fornisce una proprietà [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Il seguente snippet di codice dimostra l'uso della proprietà [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) utilizzando questo [file excel di origine](LinkTypes.xlsx).

## Codice Sorgente

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Di seguito è riportato l'output generato dal frammento di codice indicato sopra.

## Output della console
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
