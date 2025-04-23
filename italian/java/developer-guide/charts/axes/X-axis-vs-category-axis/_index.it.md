---
title: Asse X vs. Asse delle categorie
description: Scopri come differenziare tra l asse X e l asse delle categorie in Aspose.Cells for Java. La nostra guida ti aiuterà a capire le differenze nel loro utilizzo e proprietà, e come configurarli in base alle tue esigenze.
keywords: Aspose.Cells for Java, asse X, asse delle categorie, differenza, utilizzo, proprietà, configurazione.
type: docs
weight: 180
url: /it/java/x-axis-vs-category-axis/
---

## **Possibili Scenari di Utilizzo**
Ci sono diversi tipi di assi X. Mentre l'asse Y è un asse di tipo Valore, l'asse X può essere un asse di tipo Categoria o un asse di tipo Valore. Utilizzando un asse di tipo Valore, i dati sono trattati come dati numerici continuamente variabili, e il marcatore è posizionato in un punto lungo l'asse che varia in base al suo valore numerico. Utilizzando un asse di tipo Categoria, i dati sono trattati come una sequenza di etichette di testo non numeriche, e il marcatore è posizionato in un punto lungo l'asse in base alla sua posizione nella sequenza. Il codice di esempio qui sotto illustra la differenza tra Assi di Valore e di Categoria.
I nostri dati di esempio sono mostrati nella [tabella di esempio](sample.png) di seguito. La prima colonna contiene i nostri dati asse X, che possono essere trattati come Categorie o come Valori. Nota che i numeri non sono equispaziati, né appaiono in ordine numerico.

![todo:image_alt_text](sample.png)
## **Gestire l'asse X e il'asse delle categorie come Microsoft Excel**
Mostreremo questi dati su due tipi di grafico, il primo grafico è un grafico XY (disperso) con l'asse X come asse dei valori, il secondo grafico è un grafico a linee con l'asse X come asse delle categorie.

![todo:image_alt_text](compare.png)

Il seguente codice di esempio genera il [file Excel di output](XAxis.xlsx).

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
{{< app/cells/assistant language="java" >}}
