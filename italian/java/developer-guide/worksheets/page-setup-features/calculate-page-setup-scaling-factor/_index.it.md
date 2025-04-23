---
title: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 260
url: /it/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

Quando imposti il ridimensionamento della configurazione di pagina utilizzando l'opzione **Regola su n pagine di larghezza per m di altezza**, Microsoft Excel calcola il fattore di ridimensionamento della configurazione di pagina. Puoi calcolare la stessa cosa utilizzando la proprietà [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale). Questa proprietà restituisce un valore double che può essere convertito in un valore percentuale. Ad esempio, se restituisce 0.5079621076 significa che il fattore di ridimensionamento è 51%.

{{% /alert %}} 
## **Calcolare il fattore di scala del layout pagina**
Il seguente codice di esempio illustra come calcolare il fattore di ridimensionamento della configurazione di pagina utilizzando la proprietà [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
