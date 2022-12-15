---
title: Aspose.Cells Template e Smart Marker
type: docs
weight: 30
url: /it/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

Un modello Aspose.Cells è una cartella di lavoro di Microsoft Excel che contiene marcatori intelligenti. Gli indicatori intelligenti fungono da segnaposto dei dati per gli elementi del report e vengono sostituiti con i dati corrispondenti al momento del rendering. Esistono cinque tipi di marcatori intelligenti, elencati di seguito. Tutti i marcatori possono essere inseriti in un modello da Aspose.Cells.Report.Designer. Il può anche essere modificato manualmente.

{{% /alert %}} 
### **Marcatori intelligenti**
#### **Indicatori di dati**
 Il formato di**indicatori di dati** è &=DataSetName.FieldName. Ad esempio: &=SalesDetail.sales dove SalesDetail è il nome di un set di dati o di una query e sales è il nome di uno dei relativi campi. Al momento del rendering, gli indicatori di dati vengono sostituiti con i valori del set di dati fornito da Reporting Services.
#### **Indicatori di formule di Reporting Services**
 Il formato di Reporting Services'**marcatori di formule**è &=espressione. Ad esempio: &=sum(SalesDetail.sales)/100. L'espressione è composta da funzione, campi del set di dati, operatore e così via. Al momento del rendering. Gli indicatori delle formule di Reporting Services vengono sostituiti con valori calcolati.
#### **Reporting Services Indicatori variabili globali**
 Il formato di Reporting Services'**marcatori variabili globali** è &=globali! Nome variabile. Ad esempio: &=Globals!ExecutionTime dove ExecutionTime è il nome di una variabile globale. I marcatori di variabili globali vengono sostituiti con valori di variabili globali al momento del rendering.
#### **Indicatori dei parametri di Reporting Services**
 Un parametro di report ha due attributi: valore ed etichetta. Di conseguenza,**marcatori di parametri** hanno due formati: &= Parametri! ParamName.Value e &=Parametri! ParamName.Label. Indicano rispettivamente il nome e l'etichetta del parametro. Al momento del rendering, i contrassegni dei parametri vengono sostituiti con i valori dei parametri immessi dall'utente.
#### **Formule dinamiche**
 Per eseguire calcoli su righe inserite, utilizzare formule dinamiche.**Formule dinamiche** consentono di inserire le formule di Microsoft Excel nelle celle anche quando una formula fa riferimento a righe che verranno inserite durante il processo di esportazione. Possono essere ripetuti per ogni riga inserita o utilizzati solo con le celle in cui sono posizionati i marcatori di dati per loro.

Il formato delle formule dinamiche è &=&=RepeatDynamicFormula.

Le formule dinamiche consentono le seguenti opzioni aggiuntive:

- {r} – Numero di riga corrente.
- {2}, {-1} – Scostamento rispetto al numero di riga corrente.

**Una formula dinamica ripetuta e il foglio di lavoro Excel risultante** 

![cose da fare:immagine_alt_testo](aspose-cells-template-and-smart-markers_1.png)
