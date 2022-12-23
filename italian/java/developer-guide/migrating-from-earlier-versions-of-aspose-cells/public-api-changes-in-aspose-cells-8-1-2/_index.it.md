---
title: Pubblico API Modifiche Aspose.Cells 8.1.2
type: docs
weight: 70
url: /it/java/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.1.1 alla 8.1.2, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto il supporto per l'avviso in caso di sostituzione dei caratteri**
Con Aspose.Cells for Java 8.1.2, sono state aggiunte le classi WarningInfo e WarningType, l'interfaccia IWarningCallback e le proprietà SaveOptions.WarningCallback e ImageOrPrintOptions.WarningCallback per consentire agli sviluppatori di ricevere avvisi quando si verifica la sostituzione dei caratteri durante la conversione di fogli di calcolo in immagini, formati XPS e PDF.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottenere avvisi per la sostituzione dei caratteri durante il rendering dei fogli di calcolo](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) per maggiori informazioni.

{{% /alert %}}
## **Proprietà PdfSaveOptions.ChartImageType obsoleta eliminata**
Aspose.Cells for Java 8.1.2 ha rimosso la proprietà obsoleta PdfSaveOptions.ChartImageType dal pubblico API.
