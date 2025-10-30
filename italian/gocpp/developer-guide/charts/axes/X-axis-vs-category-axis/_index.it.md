---
title: Asse X vs. Asse categoria con Golang tramite C++
linktitle: Asse X vs. Asse delle categorie
description: Impara come differenziare tra l asse X e l asse Categoria in Aspose.Cells for C++. La nostra guida ti aiuterà a comprendere le differenze nel loro utilizzo e proprietà, e come configurarli secondo le tue esigenze.
keywords: Aspose.Cells for C++, asse X, asse Categoria, differenza, utilizzo, proprietà, configurazione.
type: docs
weight: 180
url: /it/go-cpp/X-axis-vs-category-axis/
---

## **Possibili Scenari di Utilizzo**
Ci sono diversi tipi di assi X. Mentre l'asse Y è un asse di tipo Valore, l'asse X può essere un asse di tipo Categoria o un asse di tipo Valore. Utilizzando un asse di tipo Valore, i dati sono trattati come dati numerici continuamente variabili, e il marcatore è posizionato in un punto lungo l'asse che varia in base al suo valore numerico. Utilizzando un asse di tipo Categoria, i dati sono trattati come una sequenza di etichette di testo non numeriche, e il marcatore è posizionato in un punto lungo l'asse in base alla sua posizione nella sequenza. Il codice di esempio qui sotto illustra la differenza tra Assi di Valore e di Categoria.
I nostri dati di esempio sono mostrati nella [tabella di esempio](sample.png) di seguito. La prima colonna contiene i nostri dati asse X, che possono essere trattati come Categorie o come Valori. Nota che i numeri non sono equispaziati, né appaiono in ordine numerico.

![todo:image_alt_text](sample.png)

## **Gestire l'asse X e il'asse delle categorie come Microsoft Excel**
Mostreremo questi dati su due tipi di grafico, il primo grafico è XY (Scatter) con asse X come asse dei valori, il secondo grafico è a linee con asse X come asse Categoria.

![todo:image_alt_text](compare.png)

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-XAxisVsCategoryAxis.go" >}}
