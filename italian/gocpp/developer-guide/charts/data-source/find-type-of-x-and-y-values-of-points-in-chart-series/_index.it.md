---
title: Trova il tipo di valori X e Y dei punti nella serie del grafico con Golang via C++
linktitle: Trova il tipo di valori X e Y dei punti nella serie del grafico
description: Scopri come determinare il tipo di valori X e Y nei punti della serie del grafico usando Aspose.Cells for C++. La nostra guida spiegherà i vari tipi di valori dei dati e mostrerà come accedervi e lavorarci all interno dei tuoi grafici.
keywords: Aspose.Cells for C++, grafici, valori X, valori Y, tipi di dati, accesso, lavoro con, serie del grafico.
type: docs
weight: 150
url: /it/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possibili Scenari di Utilizzo**
A volte, vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce i metodi `ChartPoint::get_XValueType` e `ChartPoint::get_YValueType` che possono essere usati a questo scopo. Nota che dovrai chiamare il metodo `Chart::Calculate()` prima di poter utilizzare efficacemente queste proprietà.

## **Trova il tipo di valori X e Y dei punti nella serie del grafico**
Il seguente esempio di codice carica il file Excel di esempio ([sample Excel file](64716905.xlsx)) e accede al primo grafico all’interno del primo foglio di lavoro. Successivamente chiama il metodo `Chart::Calculate()` e determina il tipo di valori X e Y del primo punto del grafico, stampandoli sulla console. Consulta l’output della console riportato di seguito come riferimento.

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **Output della console**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
