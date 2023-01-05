---
title: Prefazione
type: docs
weight: 20
url: /it/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services contiene principalmente due componenti: Aspose.Cells.Report.Designer e Aspose.Cells.Renderer for Reporting Services. Il primo è utilizzato per progettare report direttamente in Microsoft Excel e il secondo è responsabile del rendering di un report RDL in Microsoft Excel.

{{% /alert %}} 
### **Progettazione di un report con Report Designer**
I passaggi principali per progettare un report utilizzando Aspose.Cells.Report.Designer sono:

1. **Creare origini dati e query**.
 Microsoft Query è integrato con Aspose.Cells.Report.Designer e utilizzato come strumento grafico per la creazione di sorgenti dati e query. Gli utenti possono anche utilizzare un file RDL esistente in cui sono disponibili origini dati e query per le operazioni.
1. **Parametri della mappa**.
 Se le istruzioni SQL di una query includono parametri, gli utenti devono creare i parametri del report e mappare i parametri SQL ai parametri del report. È possibile designare valori validi per un parametro di report in Aspose.Cells.Report.Designer.
1. **Design Microsoft Contenuto, stili e formati del modello di report Excel**.
Un modello di report Aspose.Cells può contenere un numero qualsiasi dei seguenti tipi di elementi di report:
 1. Tavolo
 1. Tavolo girevole
 1. Grafico
 1. Casella di testo
 1. Matrice
 Normalmente una query (ovvero DataSet) viene utilizzata come origine dati per l'elemento del report. È inoltre possibile utilizzare parametri, formule e variabili globali di Reporting Services come origine dati per alcuni tipi di elementi del report. Gli stili ei formati degli elementi del report vengono specificati semplicemente impostando gli stili ei formati delle celle che compongono gli elementi del report.
1. **Pubblica rapporto**.
 Dopo i passaggi precedenti, il report è pronto per la pubblicazione. Gli utenti possono designare la cartella in cui pubblicare il report. Se necessario, è possibile assegnare un'origine dati condivisa nel server di report come origine dati per il report.
1. **Rapporto di anteprima**.
Quando si seleziona un report per l'anteprima sul server di report, viene richiesto di specificare il formato di file in cui esportarlo (ad esempio formato Microsoft Excel 97-2003 binario XLS, SpreadsheetML o Microsoft formato Excel 2007 XLSX) e gli eventuali parametri del report di input creati durante la progettazione del rapporto. Successivamente, il report viene popolato con i dati forniti da Reporting Services.
