---
title: Pubblico API Modifiche Aspose.Cells 8.2.1
type: docs
weight: 80
url: /it/net/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche al Aspose.Cells API dalla versione 8.2.0 alla 8.2.1, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto il metodo GetValidation() per la classe Cell**
La convalida dei dati è una delle funzionalità utilizzate dai progettisti di fogli di calcolo per impedire agli utenti di inserire valori non validi in una determinata cella. Con Aspose.Cells for .NET 8.2.1, API ha esposto un semplice meccanismo che identifica se la convalida dei dati è stata applicata su una cella. Utilizzare il metodo GetValidation della classe Cell per acquisire qualsiasi convalida applicata. Se non c'è convalida, il metodo restituisce null. Allo stesso modo, è possibile utilizzare il metodo GetValidationInCell della classe ValidationCollection per acquisire la convalida applicata a qualsiasi cella fornendo i relativi indici di riga e colonna.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottieni la convalida applicata su uno Cell](/cells/it/net/get-validation-applied-on-a-cell/) per maggiori informazioni.

{{% /alert %}}
## **Aggiunto il metodo GetValidationValue() per la classe Cell**
Oltre a determinare se la convalida è stata applicata, è anche possibile verificare se un determinato valore soddisfa le regole di convalida dei dati per una determinata cella. Questa funzionalità è utile negli scenari in cui si desidera verificare al volo se il valore immesso nella cella soddisfa le regole di convalida dei dati. Il Aspose.Cells API ha esposto il metodo GetValidationValue per la classe Cell. Se il valore immesso in una cella non soddisfa le regole di convalida dei dati, il metodo GetValidationValue per la classe Cell restituisce false.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Verificare che il valore Cell soddisfi le regole di convalida dei dati](/cells/it/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Aggiunto il metodo ToPrinter(PrinterSettings printerSettings) di overload per la classe WorkbookRender**
È possibile utilizzare il metodo di overload per eseguire il rendering della cartella di lavoro su Printer tramite PrinterSettings.
