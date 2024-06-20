---
title: Report parametrizzato
type: docs
weight: 60
url: /it/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

Un *report parametrizzato* è un report che accetta valori di input che vengono utilizzati durante l'elaborazione del report. 

Con un report parametrizzato, è possibile variare l'output di un report in base ai valori impostati durante l'esecuzione. I servizi di report supportano due tipi di parametri: parametri di query e parametri di report. 

- I **parametri di query** vengono utilizzati per selezionare o filtrare i dati durante l'elaborazione dei dati. Se è specificato un parametro di query, deve essere fornito un valore dall'utente o dalle proprietà predefinite per completare l'istruzione SELECT o la stored procedure che recupera i dati per un report.
- I **parametri di report** vengono utilizzati durante l'elaborazione del report per mostrare un aspetto diverso dei dati. Di solito un parametro di report viene utilizzato per filtrare un vasto insieme di record, ma può avere altri utilizzi a seconda delle query e delle espressioni nel report.

I parametri di report differiscono dai parametri di query in quanto sono definiti in un report e elaborati dal server di report, mentre i parametri di query sono definiti come parte della query del set di dati e elaborati sul server del database. In Aspose.Cells.Report.Designer, i parametri di query vengono specificati al momento della creazione della query in Microsoft Query. 

È possibile creare parametri di report e mappare i parametri di query al relativo parametro di report in Aspose.Cells.Report.Designer. In questo modo, è possibile selezionare i valori per i parametri di report e farli passare nella query per limitare i dati recuperati dalla sorgente di dati.

{{% /alert %}} 
###### **Questa sezione include i seguenti argomenti:** 
- [Creazione di parametri di report](/cells/it/reportingservices/creating-report-parameters/)
- [Modifica dei parametri di report](/cells/it/reportingservices/modifying-report-parameters/)
- [Mappatura dei parametri di query ai parametri di report](/cells/it/reportingservices/mapping-query-parameters-to-report-parameters/)
