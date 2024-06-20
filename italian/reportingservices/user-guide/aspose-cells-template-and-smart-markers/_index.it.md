---
title: Modelli Aspose.Cells e Marker Smart
type: docs
weight: 30
url: /it/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Un modello Aspose.Cells è un foglio di calcolo di Microsoft Excel che contiene Smart Markers. I Marker Smart funzionano come segnaposti di dati per gli elementi del report e vengono sostituiti con i dati corrispondenti al momento del rendering. Esistono cinque tipi di marker smart, elencati di seguito. Tutti i marker possono essere inseriti in un modello tramite Aspose.Cells.Report.Designer. Possono anche essere modificati manualmente. 

{{% /alert %}} 
### **Marcatori intelligenti**
#### **Marker Dati**
Il formato dei **marker dati** è &=NomeDataSet.NomeCampo. Ad esempio: &=SalesDetail.vendite dove SalesDetail è il nome di un set di dati o una query e vendite è il nome di uno dei suoi campi. Al momento del rendering, i marker dati vengono sostituiti con i valori del dataset forniti da Reporting Services.
#### **Marker Formule Reporting Services**
Il formato dei **marker formule Reporting Services** è &=espressione. Ad esempio: &=somma(SalesDetail.vendite)/100. L'espressione è composta da funzioni, campi del dataset, operatori e così via. Al momento del rendering, i marker formule Reporting Services vengono sostituiti con valori calcolati.
#### **Marker Variabili Globali Reporting Services**
Il formato dei **segnalibri delle variabili globali** dei Reporting Services è &=Globals! NomeVariabile. Ad esempio: &=Globals!ExecutionTime dove ExecutionTime è il nome di una variabile globale. I segnalibri delle variabili globali vengono sostituiti con i valori delle variabili globali al momento del rendering.
#### **Marcatori dei Parametri dei Reporting Services**
Un parametro di report ha due attributi: valore ed etichetta. Di conseguenza, i **marcatori dei parametri** hanno due formati: &=Parameters!NomeParametro.Valore e &=Parameters!NomeParametro.Label. Indicano rispettivamente il nome e l'etichetta del parametro. Al momento del rendering, i marcatori dei parametri vengono sostituiti con i valori dei parametri inseriti dall'utente.
#### **Formule dinamiche**
Per effettuare calcoli sulle righe inserite, utilizzare formule dinamiche. Le **formule dinamiche** ti consentono di inserire le formule di Microsoft Excel nelle celle anche quando una formula fa riferimento a righe che verranno inserite durante il processo di esportazione. Possono essere ripetute per ogni riga inserita o utilizzate solo con le celle in cui sono posizionati i marcatori dei dati.

Il formato delle formule dinamiche è &=&=RepeatDynamicFormula.

Le Formule Dinamiche consentono le seguenti opzioni aggiuntive:

- {r} – Numero di riga corrente.
- {2}, {-1} – Offset al numero di riga corrente.

**Una formula dinamica ripetuta e il foglio di calcolo Excel risultante** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
