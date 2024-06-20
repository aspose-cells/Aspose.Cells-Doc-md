---
title: Aggiunta di Parametri di Report al Report
type: docs
weight: 60
url: /it/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Il modello di report di Aspose.Cells supporta i parametri di report dei Servizi di Report come origine dati per le celle che contengono un marcatore dei parametri di Reporting Services. Si prega di fare riferimento a [Modello di Aspose.Cells e Smart Marker](/cells/it/reportingservices/aspose-cells-template-and-smart-markers/) per apprendere i marcatori dei parametri di Reporting Services. I parametri di report vengono di solito collocati nell'area di testo dell'intestazione o del piè di pagina della tabella.

{{% /alert %}} 
### **Aggiunta di un Parametro di Report**
Per aggiungere parametri di report ai report:

1. Seleziona una cella. 

   **Selezione di una cella** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Fare clic su Inserisci formula sulla barra degli strumenti di Aspose.Cells.Report.Designer (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. Seleziona **Parametri** dal pannello dei Parametri a sinistra.
   Tutti i parametri sono elencati nel pannello di destra. 
1. Seleziona un parametro, nell'esempio abbiamo selezionato EmpID.
1. Fai doppio clic sul parametro per far apparire l'espressione nell'editor in cima al modulo.
   Un parametro ha due attributi dati: etichetta e valore (l'attributo predefinito è il valore). 

   **Selezione di un parametro** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. Nell'esempio, l'etichetta del parametro dovrebbe essere mostrata nel report, quindi modifica l'espressione in Parameters!EmpID.Label. 

   **Modifica del parametro** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. Fai clic su **OK**.
   La cella selezionata contiene un marcatore dei parametri di rapporto. 

   **Un parametro di report inserito nella cella** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
