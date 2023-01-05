---
title: Aggiunta di parametri di report al report
type: docs
weight: 60
url: /it/reportingservices/adding-report-parameters-to-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells' supporta i parametri del report di Reporting Services come origine dati per le celle che contengono un indicatore di parametro di Reporting Services. Per favore riferisci a[Aspose.Cells Template e Smart Marker](/cells/it/reportingservices/aspose-cells-template-and-smart-markers/) per informazioni sugli indicatori di parametro di Reporting Services. I parametri del report vengono normalmente posizionati nell'area di testo dell'intestazione o del piè di pagina della tabella.

{{% /alert %}} 
### **Aggiunta di un parametro di report**
Per aggiungere parametri di report ai report:

1.  Seleziona una cella.

   **Selezione di una cella** 

![cose da fare:immagine_alt_testo](adding-report-parameters-to-report_1.png)




1. Fare clic su Inserisci formula nella barra degli strumenti Aspose.Cells.Report.Designer (

![cose da fare:immagine_alt_testo](adding-report-parameters-to-report_2.png)

).

1.  Selezionare**Parametri** dal pannello Parametri a sinistra.
 Tutti i parametri sono elencati nel pannello di destra.
1. Seleziona un parametro, nell'esempio abbiamo selezionato EmpID.
1. Fare doppio clic sul parametro per visualizzare l'espressione nell'editor nella parte superiore del modulo.
 Un parametro ha due attributi di dati: etichetta e valore (l'attributo predefinito è valore).

   **Selezione di un parametro** 

![cose da fare:immagine_alt_testo](adding-report-parameters-to-report_3.png)




1.  Nell'esempio, l'etichetta del parametro dovrebbe essere mostrata nel report, quindi modificare l'espressione in Parameters!EmpID.Label.

   **Modifica del parametro** 

![cose da fare:immagine_alt_testo](adding-report-parameters-to-report_4.png)




1.  Clic**OK**.
 La cella selezionata contiene un indicatore dei parametri del report.

   **Un parametro del report inserito nella cella** 

![cose da fare:immagine_alt_testo](adding-report-parameters-to-report_5.png)
