---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.2.0
type: docs
weight: 80
url: /it/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.1.2 alla 8.2.0, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta Proprietà MultiThreadReading per la Classe Cells**
Con Aspose.Cells for Java 8.2.0, la proprietà MultiThreadReading è stata aggiunta alla classe Cells per fornire un meccanismo più robusto per leggere i valori delle celle con più thread contemporaneamente. Impostando la proprietà di tipo Boolean su true nell'applicazione multi-threading si assicura che ogni thread riceva il valore corretto delle celle.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Lettura simultanea dei valori delle celle in un ambiente multi-threaded](/cells/it/java/reading-cell-values-in-multiple-threads-simultaneously/) per ulteriori informazioni.

{{% /alert %}}
## **Aggiunte sovraccariche per i metodi autoFitRows & autoFitColumns**
Nuove sovraccariche per i metodi autoFitRows & autoFitColumns sono state aggiunte alla classe Worksheet, consentendo agli sviluppatori di adattare automaticamente le righe & colonne in base ai rispettivi intervalli passando un'istanza della classe AutoFitterOptions. 

Le firme dei suddetti metodi sono le seguenti:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Adatta automaticamente righe e colonne](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
