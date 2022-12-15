---
title: Modifiche all'API pubblica in Aspose.Cells 8.1.2
type: docs
weight: 60
url: /it/net/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.1.1 alla 8.1.2, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto il supporto per l'avviso in caso di sostituzione dei caratteri**
Con Aspose.Cells for .NET 8.1.2, sono state aggiunte le classi WarningInfo, WarningType, l'interfaccia IWarningCallback e le proprietà SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback per consentire all'utente di ricevere un avviso in caso di sostituzione dei caratteri durante la conversione dei fogli di calcolo in immagini o in formato PDF.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottenere avvisi per la sostituzione dei caratteri durante il rendering dei fogli di calcolo](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Proprietà PdfSaveOptions.ChartImageType obsoleta eliminata**
Aspose.Cells for .NET 8.1.2 ha rimosso la proprietà obsoleta PdfSaveOptions.ChartImageType dall'API pubblica.
