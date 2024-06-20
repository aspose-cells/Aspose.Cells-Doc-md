---
title: Calcola le funzioni personalizzate in GridWeb
type: docs
weight: 90
url: /it/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: Questo articolo introduce le caratteristiche delle funzioni personalizzate in GridWeb.
---


## **Possibili Scenari di Utilizzo**
Aspose.Cells.GridWeb supporta il calcolo delle funzioni personalizzate con la proprietà GridWeb.CustomCalculationEngine. Questa proprietà richiede l'istanza dell'interfaccia GridAbstractCalculationEngine. Si prega di implementare l'interfaccia GridAbstractCalculationEngine e calcolare le funzioni personalizzate con la propria logica.
## **Calcola le funzioni personalizzate in GridWeb**
Il seguente codice di esempio aggiunge una funzione personalizzata chiamata MYTESTFUNC() nella cella B3. Quindi calcoliamo il valore di questa funzione implementando l'interfaccia GridAbstractCalculationEngine. Calcoliamo MYTESTFUNC() in modo che moltiplichi il suo parametro per 2 e restituisca il risultato. Quindi se il suo parametro è 9, restituirà 2*9 = 18.
### **Codice di Esempio**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
