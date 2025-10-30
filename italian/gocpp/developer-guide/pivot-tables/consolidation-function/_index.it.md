---
title: Funzione di consolidamento con Golang tramite C++
linktitle: Funzione di consolidamento
type: docs
weight: 20
url: /it/go-cpp/consolidation-function/
description: Impara come applicare la funzione di consolidamento ai campi dati di una tabella pivot utilizzando Aspose.Cells con Golang tramite C++.
---

## **funzione di consolidamento**

Aspose.Cells può essere utilizzato per applicare ConsolidationFunction ai campi dati (o campi di valore) della tabella pivot. In Microsoft Excel, è possibile fare clic con il pulsante destro del mouse sul campo di valore e quindi selezionare l'opzione **Impostazioni campo valore...** e quindi selezionare la scheda **Sommario valori per**. Da lì, è possibile selezionare qualsiasi ConsolidationFunction a propria scelta come Somma, Conteggio, Media, Massimo, Minimo, Prodotto, Conteggio univoco, ecc.

Aspose.Cells fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/) per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction::Media
- ConsolidationFunction::Conta
- ConsolidationFunction::ContaNumeri
- ConsolidationFunction::ContaDistinti
- ConsolidationFunction::Massimo
- ConsolidationFunction::Minimo
- ConsolidationFunction::Prodotto
- ConsolidationFunction::DevStd
- ConsolidationFunction::DevStdp
- ConsolidationFunction::Somma
- ConsolidationFunction::Varianza
- ConsolidationFunction::VarianzaP

### **Applicazione della funzione di consolidamento ai campi dati della tabella pivot**

Il seguente codice applica la funzione di consolidamento **Media** al primo campo dati (o campo valore) e la funzione di consolidamento **ConteggioDistinto** al secondo campo dati (o campo valore).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
