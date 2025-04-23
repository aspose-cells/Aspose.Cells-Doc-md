---
title: Funzione di consolidamento
type: docs
weight: 20
url: /it/nodejs-cpp/consolidation-function/
description: Come applicare la funzione di consolidamento ai campi dati della tabella pivot con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, libreria Excel Node.js, funzione di consolidamento ai campi dati della tabella pivot usando la libreria Excel Aspose.Cells for Node.js via C++.
---

## **funzione di consolidamento**

Aspose.Cells for Node.js via C++ può essere usato per applicare la funzione di consolidamento ai campi dati (o campi valore) della tabella pivot. In Microsoft Excel, puoi cliccare con il tasto destro sul campo valore e selezionare l'opzione **Impostazioni campo valore...** e poi andare nella scheda **Riepiloga valori per**. Da lì, puoi scegliere qualsiasi funzione di consolidamento come Somma, Conta, Media, Max, Min, Prodotto, Conta distinta, ecc.

Aspose.Cells for Node.js via C++ fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Come applicare la funzione di consolidamento ai campi dati della tabella pivot usando Aspose.Cells for Node.js via C++**

Il seguente codice applica la funzione di consolidamento **Media** al primo campo dati (o campo valore) e la funzione di consolidamento **ConteggioDistinto** al secondo campo dati (o campo valore).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

La funzione di consolidamento **CONTEGGIODISTINTO** è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
