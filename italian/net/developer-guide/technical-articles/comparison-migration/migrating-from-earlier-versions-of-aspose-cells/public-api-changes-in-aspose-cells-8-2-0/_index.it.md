---
title: Modifiche all'API pubblica in Aspose.Cells 8.2.0
type: docs
weight: 70
url: /it/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.1.2 alla 8.2.0, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta proprietà MultiThreadReading per la classe Cells**
Con Aspose.Cells for .NET 8.2.0, la proprietà MultiThreadReading è stata aggiunta alla classe Cells per fornire un meccanismo più robusto per leggere contemporaneamente i valori delle celle con più thread. L'impostazione della proprietà Boolean type su true nell'applicazione multithread assicura che ogni thread riceva il valore corretto delle celle.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Lettura simultanea dei valori Cells in un ambiente multithread](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) per maggiori informazioni.

{{% /alert %}}
## **Overload aggiunti per i metodi AutoFitRows e AutoFitColumns**
 Alla classe Worksheet sono stati aggiunti nuovi overload per AutoFitRows e AutoFitColumns, consentendo agli sviluppatori di adattare automaticamente le righe e le colonne in base ai rispettivi intervalli durante il passaggio di un'istanza della classe AutoFitterOptions.

Le firme dei suddetti metodi sono le seguenti:

1. AutoFitRows(int startRow, int endRow, opzioni AutoFitterOptions)
1. AutoFitColumns(int firstColumn, int lastColumn, Opzioni AutoFitterOptions)

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Adatta automaticamente righe e colonne](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
