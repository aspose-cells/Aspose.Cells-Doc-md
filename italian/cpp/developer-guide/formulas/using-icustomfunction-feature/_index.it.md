---
title: Utilizzo della funzione ICustomFunction
type: docs
weight: 20
url: /it/cpp/using-icustomfunction-feature/
---
## **introduzione**
Questo articolo fornisce informazioni su come usare la funzionalità ICustomFunction per implementare funzioni personalizzate con le API Aspose.Cells.

L'interfaccia ICustomFunction consente di aggiungere funzioni di calcolo delle formule personalizzate per estendere il motore di calcolo principale Aspose.Cells al fine di soddisfare determinati requisiti. Questa funzionalità è utile per definire funzioni personalizzate (definite dall'utente) in un file modello o in un codice in cui la funzione personalizzata può essere implementata e valutata utilizzando le API Aspose.Cells come qualsiasi altra funzione Excel predefinita Microsoft.
## **Utilizzo della funzione ICustomFunction**
Il seguente codice di esempio implementa l'interfaccia ICustomFunction che valuta e restituisce i valori delle due funzioni personalizzate, ad esempio MySampleFunc() e YourSampleFunc(). Queste funzioni personalizzate si trovano rispettivamente all'interno delle celle A1 e A2. Quindi chiama il metodo IWorkbook.CalculateFormula(false, ICustomFunction) per richiamare l'implementazione del metodo ICustomFunction.CalculateCustomFunction(). Quindi, stampa i valori di A1 e A2 sulla console che sono effettivamente i valori restituiti da ICustomFunction.CalculateCustomFunction(). Consulta l'output della console del codice di esempio riportato di seguito per ulteriore assistenza.
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Uscita console**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
