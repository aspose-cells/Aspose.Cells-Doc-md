---
title: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 180
url: /it/java/detect-hyperlink-type/
---
## **Rileva il tipo di collegamento ipertestuale**

Un file Excel può avere diversi tipi di collegamenti ipertestuali come esterno, riferimento di cella, percorso file, ecc. Aspose.Cells supporta la funzione per rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dal[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Enumerazione. Il[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)L'enumerazione ha i seguenti membri.

- [**ESTERNO**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Link esterno
- [**PERCORSO DEL FILE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): percorso locale e completo di file\cartelle.
- [**E-MAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-mail
- [**RIFERIMENTO_CELLULA**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): collegamento alla cella o all'intervallo denominato.

Per verificare il tipo di collegamento ipertestuale, il file[**Collegamento ipertestuale**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) la classe fornisce a[**Tipo di collegamento**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) proprietà con un tipo restituito di[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Il seguente frammento di codice illustra l'uso di[**Tipo di collegamento**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)proprietà utilizzando this[file excel di origine](LinkTypes.xlsx).

## Codice sorgente

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Di seguito è riportato l'output generato dal frammento di codice sopra indicato.

## Uscita console
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
