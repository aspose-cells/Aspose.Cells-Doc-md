---
title: Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
type: docs
weight: 590
url: /it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells ha un potente motore di calcolo che può calcolare quasi tutte le formule di Microsoft Excel. Nonostante ciò, ti permette anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate nell'implementazione di questa funzionalità.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implementare un Motore di Calcolo Personalizzato**
Il codice seguente implementa il Custom Calculation Engine. Implementa l'interfaccia [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) che ha solo un metodo [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Questo metodo viene chiamato per tutte le formule. All'interno di questo metodo, catturiamo la funzione **TODAY** e aggiungiamo un giorno alla data di sistema. Quindi se la data corrente è 27/07/2023, allora il motore personalizzato calcolerà TODAY() come 28/07/2023.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Risultato**

Si prega di controllare l'output della console del codice di esempio sopra, il valore (data ora) di A1 con il motore personalizzato dovrebbe essere un giorno dopo rispetto al risultato senza il motore personalizzato.

### **Articolo correlato**
{{% alert color="primary" %}} 

- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
