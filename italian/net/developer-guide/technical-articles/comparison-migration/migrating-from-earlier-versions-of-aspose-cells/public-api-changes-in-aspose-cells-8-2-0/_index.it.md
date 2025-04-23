---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.2.0
type: docs
weight: 70
url: /it/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.1.2 alla 8.2.0, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta Proprietà MultiThreadReading per la Classe Cells**
Con Aspose.Cells for .NET 8.2.0, la proprietà MultiThreadReading è stata aggiunta alla classe Cells al fine di fornire un meccanismo più robusto per leggere i valori delle celle con più thread contemporaneamente. Impostare la proprietà di tipo Boolean su true nell'applicazione multithreading assicura che ciascun thread riceverà i valori corretti delle celle.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Leggere Contemporaneamente i Valori delle Celle in un Ambiente Multithread](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) per ulteriori informazioni.

{{% /alert %}}
## **Aggiunte Sovrapposizioni per i Metodi AutoFitRows e AutoFitColumns**
Nuove sovrapposizioni per AutoFitRows e AutoFitColumns sono state aggiunte alla classe Worksheet, consentendo agli sviluppatori di adattare automaticamente le righe e le colonne in base ai rispettivi intervalli passando un'istanza della classe AutoFitterOptions. 

Le firme dei suddetti metodi sono le seguenti:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Adatta Automaticamente Righe e Colonne](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
