---
title: Calcola funzioni personalizzate in GridWeb
type: docs
weight: 90
url: /it/net/calculate-custom-functions-in-gridweb/
---
## **Possibili scenari di utilizzo**
Aspose.Cells.GridWeb supporta il calcolo delle funzioni personalizzate con la proprietà GridWeb.CustomCalculationEngine. Questa proprietà accetta l'istanza dell'interfaccia GridAbstractCalculationEngine. Implementa l'interfaccia GridAbstractCalculationEngine e calcola le tue funzioni personalizzate con la tua logica.
## **Calcola funzioni personalizzate in GridWeb**
Il seguente codice di esempio aggiunge una funzione personalizzata denominata MYTESTFUNC() nella cella B3. Quindi calcoliamo il valore di questa funzione implementando l'interfaccia GridAbstractCalculationEngine. Calcoliamo MYTESTFUNC() in modo tale che moltiplichi il suo parametro per 2 e restituisca il risultato. Quindi, se il suo parametro è 9, restituirà 2*9 = 18.
### **Codice d'esempio**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
