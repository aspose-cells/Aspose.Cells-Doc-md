---
title: Installazione demo
type: docs
weight: 40
url: /it/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports include una serie di progetti demo per aiutarti a iniziare a esportare report in formati di documenti Excel Microsoft dalla tua applicazione.

Le demo fornite con Aspose.Cells for JasperReports sono demo standard di JasperReports modificate per dimostrare l'utilizzo dei nuovi esportatori.

{{% /alert %}}

Per eseguire le demo Aspose.Cells for JasperReports, procedere come segue:

1.  Scarica JasperReports (es<https://sourceforge.net/projects/jasperreports/files/archive/>). Assicurati di scaricare l'intero progetto archiviato con il codice sorgente e le demo, non solo un singolo JAR.
1. Scompattare il progetto archiviato in una posizione sul disco rigido, ad esempio C:\.
1.  Copia tutte le cartelle demo dalla cartella \demo di**Aspose.Cells.JasperReports.zip** a**\<DirInstall>\demo\samples**, dove "\<InstallDir>" è la posizione in cui hai decompresso JasperReports. Questo passaggio è necessario perché gli script di build demo si basano sulla struttura delle cartelle di JasperReports, altrimenti dovrai modificare gli script di build.
1.  copia**aspose.cells.jasperreports.jar** dalla cartella \lib di Aspose.Cells.JasperReports.zip a**\<DirInstall>\lib**.
1.  Prepara Ant Build Tool e Ivy Dependency Manager, vedi**\<DirInstall>\readme.txt**.
1.  Modifica il**build.xml** in**\<DirInstall>\demo\samples**, aggiungi aspose.cells.jasperreports.jar nel classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1.  Cambia la directory corrente in**\<DirInstall>\demo\hsqldb** ed eseguire la seguente riga di comando:
   **ant runServer**
1.  Cambia la directory corrente in una delle demo Aspose.Cells for JasperReports, ad esempio**\<DirInstall>\demo\samples\ac.charts** ed eseguire i seguenti comandi nella riga di comando:
   **prova della formica** - produrre file di report utilizzando l'esportatore Aspose XLS.
1.  Apri uno dei documenti risultanti da visualizzare, ad esempio**\<DirInstall>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel o un'altra applicazione.
