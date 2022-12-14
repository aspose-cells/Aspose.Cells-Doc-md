---
title: Pubblico API Modifiche Aspose.Cells 8.2.0
type: docs
weight: 80
url: /it/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche al Aspose.Cells API dalla versione 8.1.2 alla 8.2.0, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta proprietà MultiThreadReading per la classe Cells**
Con Aspose.Cells for Java 8.2.0, la proprietà MultiThreadReading è stata aggiunta alla classe Cells per fornire un meccanismo più robusto per leggere contemporaneamente i valori delle celle con più thread. L'impostazione della proprietà Boolean type su true nell'applicazione multithread assicura che ogni thread riceva il valore corretto delle celle.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Lettura simultanea dei valori Cells in un ambiente multithread](/cells/it/java/reading-cell-values-in-multiple-threads-simultaneously/) per maggiori informazioni.

{{% /alert %}}
## **Aggiunti Overload per i metodi autoFitRows e autoFitColumns**
 Nuovi overload per autoFitRows e autoFitColumns sono stati aggiunti alla classe Worksheet, consentendo agli sviluppatori di adattare automaticamente le righe e le colonne in base ai rispettivi intervalli durante il passaggio di un'istanza della classe AutoFitterOptions.

Le firme dei suddetti metodi sono le seguenti:

1. autoFitRows(int startRow, int endRow, opzioni AutoFitterOptions)
1. autoFitColumns(int firstColumn, int lastColumn, Opzioni AutoFitterOptions)

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Adatta automaticamente righe e colonne](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
