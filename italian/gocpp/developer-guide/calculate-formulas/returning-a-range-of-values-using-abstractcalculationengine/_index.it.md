---
title: Restituire un intervallo di valori usando AbstractCalculationEngine con Golang tramite C++
linktitle: Restituzione di un Intervallo di Valori utilizzando l AbstractCalculationEngine
description: Questo articolo introduce un motore di calcolo astratto che restituisce un intervallo di valori in Microsoft Excel utilizzando la libreria Aspose.Cells con Golang tramite C++. Caricando un file Excel esistente o creando uno nuovo, possiamo usare i metodi forniti da Aspose.Cells per ottenere un intervallo di valori e restituire il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, un motore di calcolo astratto che restituisce una serie di valori
type: docs
weight: 55
url: /it/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) che viene utilizzata per implementare funzioni utente o personalizzate non supportate da Microsoft Excel come funzioni integrate.

Questo articolo spiegherà come restituire l'intervallo di valori da [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{% /alert %}}

Il seguente esempio mostra l'uso della classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) e restituisce l'intervallo di valori tramite il suo metodo.

Crea una classe con una funzione `CalculateCustomFunction`. Questa classe implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
Ora usa la funzione sopra nel tuo programma.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
