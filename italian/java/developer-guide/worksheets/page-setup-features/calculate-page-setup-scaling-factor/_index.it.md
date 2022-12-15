---
title: Calcola il fattore di scala dell'impostazione della pagina
type: docs
weight: 260
url: /it/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

Quando si imposta il ridimensionamento dell'impostazione di pagina utilizzando**Adatta a n pagine di larghezza per m di altezza** opzione, Microsoft Excel calcola il fattore di scala dell'impostazione di pagina. Puoi calcolare la stessa cosa usando[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) proprietà. Questa proprietà restituisce un valore double che può essere convertito in un valore percentuale. Ad esempio, se restituisce 0,5079621076, significa che il fattore di scala è del 51%.

{{% /alert %}} 
## **Calcola il fattore di scala dell'impostazione della pagina**
 Il seguente codice di esempio illustra come calcolare il fattore di ridimensionamento dell'impostazione della pagina utilizzando[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Uscita console**
Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
