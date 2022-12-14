---
title: Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
type: docs
weight: 590
url: /it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells ha un potente motore di calcolo in grado di calcolare quasi tutte le formule Excel Microsoft. Nonostante ciò, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate per implementare questa funzione.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [Motore di calcolo astratto](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Dati di calcolo](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implementa il motore di calcolo personalizzato**
Il codice seguente implementa il motore di calcolo personalizzato. Implementa l'interfaccia[Motore di calcolo astratto](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) che ha un solo metodo[calcola(Dati CalcoloDati)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Questo metodo viene chiamato contro tutte le tue formule. All'interno di questo metodo, acquisiamo il file**SOMMA** formula e ne aumenta il valore di 30. Quindi, se il valore calcolato Aspose.Cells è 20, il nostro motore personalizzato lo renderà 50 aggiungendo 30.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Uscita console**
Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **Articolo correlato**
{{% alert color="primary" %}} 

- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
