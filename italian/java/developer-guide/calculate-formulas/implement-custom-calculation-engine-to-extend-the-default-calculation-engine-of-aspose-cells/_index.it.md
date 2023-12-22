---
title: Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
type: docs
weight: 590
url: /it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells dispone di un potente motore di calcolo in grado di calcolare quasi tutte le formule Excel di Microsoft. Nonostante ciò, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Per implementare questa funzionalità vengono utilizzate le proprietà e le classi seguenti.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [Motore di calcolo astratto](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Dati di calcolo](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Implementare il motore di calcolo personalizzato**
Il codice seguente implementa il motore di calcolo personalizzato. Implementa l'interfaccia[Motore di calcolo astratto](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) che ha un solo metodo[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Questo metodo viene chiamato contro tutte le tue formule. All'interno di questo metodo, catturiamo il file**TODAY** funzione e aggiungere un giorno alla data del sistema. Pertanto, se la data corrente è 27/07/2023, il motore personalizzato calcolerà TODAY() come 28/07/2023.

###  **Esempio di programmazione**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Risultato**

Controlla l'output della console del codice di esempio riportato sopra, il valore (data e ora) di A1 con il motore personalizzato dovrebbe essere un giorno successivo rispetto al risultato senza motore personalizzato.

###  **Articolo correlato**
{{% alert color="primary" %}} 

- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
