---
title: Accedi alla casella del testo per nome con Golang tramite C++
linktitle: Accedere alla casella di testo per nome
type: docs
weight: 230
url: /it/go-cpp/access-the-text-box-by-the-name/
description: Impara come accedere a una text box tramite il suo nome usando Aspose.Cells for C++.
---

## Accedere alla casella di testo per nome

In passato, le caselle di testo erano accessibili tramite indice dalla collezione [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/), ma ora puoi anche accedere alla casella di testo per nome da questa collezione. Questo metodo è comodo e rapido se conosci già il suo nome.

Il seguente esempio di codice crea prima una text box e le assegna del testo e un nome. Successivamente, nelle righe successive, accediamo alla stessa text box tramite il suo nome e stampiamo il suo testo.

### Codice C++ per accedere alla text box tramite nome

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### Uscita della console generata dal codice di esempio

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
