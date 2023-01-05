---
title: Rapporto parametrizzato
type: docs
weight: 60
url: /it/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

 UN*rapporto parametrizzato* è un report che accetta i valori di input utilizzati durante l'elaborazione del report.

 Con un report parametrizzato è possibile variare l'output di un report in base ai valori impostati in fase di esecuzione. Reporting Services supporta due tipi di parametri: parametri di query e parametri di report.

- **Parametri di interrogazione** vengono utilizzati per selezionare o filtrare i dati durante l'elaborazione dei dati. Se viene specificato un parametro di query, è necessario fornire un valore dall'utente o dalle proprietà predefinite per completare l'istruzione SELECT o la stored procedure che recupera i dati per un report.
- **Parametri del rapporto**vengono utilizzati durante l'elaborazione del report per mostrare un aspetto diverso dei dati. Un parametro di report viene in genere utilizzato per filtrare un set di record di grandi dimensioni, ma può avere altri usi a seconda delle query e delle espressioni nel report.

 I parametri di report differiscono dai parametri di query in quanto vengono definiti in un report ed elaborati dal server di report, mentre i parametri di query vengono definiti come parte della query del set di dati ed elaborati nel server di database. In Aspose.Cells.Report.Designer, i parametri della query vengono specificati al momento della creazione della query in Microsoft Query.

È possibile creare parametri di report e mappare parametri di query al parametro di report corrispondente in Aspose.Cells.Report.Designer. In questo modo è possibile selezionare i valori per i parametri del report e farli passare nella query per limitare i dati recuperati dall'origine dati.

{{% /alert %}} 
###### **Questa sezione include i seguenti argomenti:**
- [Creazione dei parametri del rapporto](/cells/it/reportingservices/creating-report-parameters/)
- [Modifica dei parametri del rapporto](/cells/it/reportingservices/modifying-report-parameters/)
- [Mappatura dei parametri della query ai parametri del report](/cells/it/reportingservices/mapping-query-parameters-to-report-parameters/)
