---
title: Trova celle con uno stile specifico
type: docs
weight: 80
url: /it/java/find-cells-with-specific-style/
description: Questo articolo dimostra come trovare celle con uno stile specifico utilizzando MS Excel e l API Aspose.Cells for Java.
keywords: trova celle con uno stile specifico, trova celle con uno stile specifico excel, trova celle con uno stile specifico excel java, cerca celle con uno stile specifico, cerca celle con uno stile specifico excel, cerca celle con uno stile specifico excel java, come trovare celle con uno stile specifico, come trovare celle con uno stile specifico excel, come trovare celle con uno stile specifico excel java
---

{{% alert color="primary" %}}

A volte è necessario trovare le celle con uno stile particolare. Questo articolo dimostra come farlo utilizzando Microsoft Excel e l'API Aspose.Cells for Java.

{{% /alert %}}

Utilizzo di Microsoft Excel

Questi sono i passaggi necessari per cercare celle con stili specifici in MS Excel.

1. Seleziona **Trova e seleziona** nella **scheda Home**.
1. Seleziona **Trova**.
1. Fai clic su **Opzioni** se le opzioni avanzate non sono visibili.
1. Seleziona **Scegli formato dalla cella...** dal menu a discesa **Formato**.
1. Seleziona la cella con lo stile che desideri cercare.
1. Fare clic su **Trova tutto** per trovare tutte le celle con uno stile simile a quella selezionata.

## Utilizzo di Aspose.Cells for Java

Aspose.Cells for Java fornisce la funzionalità di trovare le celle nel foglio di lavoro con uno stile specifico. A tale scopo, l'API fornisce la proprietà [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style).

### Codice di esempio

Il seguente frammento di codice trova tutte le celle che hanno lo stesso stile di quella della cella **A1** e cambia il testo all'interno di quelle celle. Si prega di vedere lo screenshot dei file di origine e di output per analizzare l'output del codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Dopo l'esecuzione del codice, tutte le celle che hanno lo stesso stile della cella A1 avranno un testo "Trovato".

### Screenshot

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Figura:** File di origine con celle che hanno stili

Ecco il file di output generato dal codice seguente. È possibile vedere tutte le celle che hanno lo stesso stile della cella **A1** hanno un testo "Trovato".

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Figura:** File di output con celle trovate dopo la ricerca dello stile **A1**
