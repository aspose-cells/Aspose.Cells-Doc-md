---
title: Utilizzo della funzione AbstractCalculationEngine
type: docs
weight: 20
url: /it/cpp/using-abstractcalculationengine-feature/
---

## Le funzioni sono ancora in fase di sviluppo, quindi rimanete sintonizzati.


## **Introduzione**
Questo articolo fornisce una comprensione di come utilizzare la funzione [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) per implementare funzioni personalizzate con le API Aspose.Cells.

<!--

L'interfaccia AbstractCalculationEngine ti consente di aggiungere funzioni di calcolo personalizzate per estendere il motore di calcolo di base di Aspose.Cells al fine di soddisfare determinati requisiti. Questa funzione è utile per definire funzioni personalizzate (definite dall'utente) in un file di modello o in un codice dove la funzione personalizzata può essere implementata e valutata utilizzando le API Aspose.Cells come qualsiasi altra funzione predefinita di Microsoft Excel.
## **Utilizzo della funzione AbstractCalculationEngine**
Il seguente codice di esempio implementa l'interfaccia AbstractCalculationEngine che valuta e restituisce i valori delle due funzioni personalizzate, ossia MySampleFunc() e YourSampleFunc(). Queste funzioni personalizzate sono all'interno delle celle A1 e A2 rispettivamente. Successivamente, chiama il metodo Workbook.CalculateFormula(const CalculationOptions& options) per invocare l'implementazione del metodo AbstractCalculationEngine .Calculate(CalculationData& data). Successivamente, stampa i valori di A1 e A2 sulla console. Si prega di vedere l'Output Console del codice di esempio qui sotto per ulteriori dettagli.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **Output della console**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->
