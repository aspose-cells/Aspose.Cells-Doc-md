---
title: Rileva tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/net/detect-hyperlink-type/
description: Scopri come rilevare il tipo di collegamento ipertestuale tramite Aspose.Cells for .NET API.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **Rileva tipo di collegamento ipertestuale**

 Un file Excel può avere diversi tipi di collegamenti ipertestuali come esterno, riferimento di cella, percorso file, ecc. Aspose.Cells supporta la funzionalità per rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati da[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Enumerazione. IL[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)L'enumerazione ha i seguenti membri.

- Esterno: collegamento esterno
- FilePath: percorso locale e completo di file\cartelle.
- E-mail: e-mail
- CellReference: collegamento alla cella o all'intervallo denominato.

 Per verificare il tipo di collegamento ipertestuale, il file[**Collegamento ipertestuale**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) la classe fornisce a[**Tipo di collegamento**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) proprietà con un tipo restituito di[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Il seguente frammento di codice illustra l'uso di[**Tipo di collegamento**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)proprietà utilizzando questo[file Excel di origine](94896195.xlsx).

###  Codice sorgente

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Quello che segue è l'output generato dallo snippet di codice indicato sopra.

###  Uscita della console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
