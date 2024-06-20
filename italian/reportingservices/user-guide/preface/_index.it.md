---
title: Prefazione
type: docs
weight: 20
url: /it/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services contiene principalmente due componenti: Aspose.Cells.Report.Designer e Aspose.Cells.Renderer per Reporting Services. Il primo viene utilizzato per progettare report direttamente in Microsoft Excel e il secondo è responsabile del rendering di un report RDL in Microsoft Excel. 

{{% /alert %}} 
### **Progettazione di un report con il Report Designer**
I principali passaggi per progettare un report utilizzando Aspose.Cells.Report.Designer sono:

1. **Creare origini dati e query**.
   Microsoft Query è integrato con Aspose.Cells.Report.Designer e utilizzato come strumento grafico per creare origini dati e query. Gli utenti possono anche utilizzare un file RDL esistente in cui sono disponibili origini dati e query per le operazioni.
1. **Mappare i parametri**.
   Se le istruzioni SQL di una query includono parametri, gli utenti devono creare parametri di report e mappare i parametri SQL ai parametri di report. Puoi designare valori validi per un parametro di report in Aspose.Cells.Report.Designer.
1. **Progettare i contenuti, gli stili e i formati del modello di report di Microsoft Excel**.
   Un modello di report di Aspose.Cells può contenere un numero qualsiasi dei seguenti tipi di elementi di report: 
   1. Tabella
   1. Tabella pivot
   1. Grafico
   1. Casella di testo
   1. Matrice
      Normalmente una query (cioè, DataSet) viene utilizzata come origine dati per l'elemento di report. È inoltre possibile utilizzare parametri dei Reporting Services, formule e variabili globali come origine dati per alcuni tipi di elementi di report. Gli stili e i formati degli elementi di report sono specificati semplicemente impostando gli stili e i formati delle celle che compongono gli elementi di report.
1. **Pubblica il report**.
   Dopo i passaggi sopra descritti, il report è pronto per essere pubblicato. Gli utenti possono designare in quale cartella pubblicare il report. Se necessario, è possibile assegnare un'origine dati condivisa nel Server dei report come origine dati per il report.
1. **Anteprima del report**.
   Selezionando un report per l'anteprima nel Server dei report, ti viene chiesto di specificare in quale formato di file esportarlo (ad esempio formato binario XLS di Microsoft Excel 97-2003, SpreadsheetML o formato XLSX di Microsoft Excel 2007) e eventuali parametri di input del report creati durante la progettazione del report. Dopo questo, il report viene popolato con i dati forniti da Reporting Services.
