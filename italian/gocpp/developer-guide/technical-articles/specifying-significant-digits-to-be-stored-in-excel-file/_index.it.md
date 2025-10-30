---
title: Specificare le Cifre Significative da memorizzare nel file Excel con Golang tramite C++
linktitle: Specificare le cifre significative
type: docs
weight: 30
url: /it/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Impara come specificare le cifre significative da memorizzare nei file Excel usando Aspose.Cells con Golang tramite C++.
---

## **Possibili Scenari di Utilizzo**

Di default, Aspose.Cells memorizza 17 cifre significative di valori double all’interno del file Excel, a differenza di MS-Excel che ne memorizza solo 15. Puoi modificare il comportamento predefinito di Aspose.Cells da 17 a 15 cifre significative usando la proprietà [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/).

## **Specifica delle cifre significative da memorizzare nel file Excel**

Il seguente esempio di codice impone ad Aspose.Cells di usare 15 cifre significative durante la memorizzazione di valori double nel file Excel. Controlla il file Excel di output [22774105.xlsx](https://example.com). Cambia l’estensione in .zip, estrailo, e vedrai che sono memorizzate solo 15 cifre significative. Lo screenshot seguente spiega l’effetto della proprietà [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) sul file Excel di output.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
