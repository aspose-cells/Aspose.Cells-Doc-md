---
title: Modifiche all API pubblica in Aspose.Cells 8.7.2
type: docs
weight: 260
url: /it/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.7.1 alla 8.7.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Esteso il Motore di Calcolo Predefinito**
Le API di Aspose.Cells hanno un potente motore di calcolo che può calcolare quasi tutte le funzioni di Microsoft Excel. Inoltre, le API di Aspose.Cells consentono ora di estendere il motore di calcolo predefinito per soddisfare i requisiti di calcolo personalizzati di qualsiasi applicazione.

Le seguenti API sono state aggiunte con il rilascio di Aspose.Cells for Java 8.7.2.

1. Classe AbstractCalculationEngine
1. Classe CalculationData
1. Proprietà CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Le API sopra menzionate consentono di implementare un motore di calcolo personalizzato per tutte le funzioni (incluso le funzioni native di Excel) con maggiore flessibilità.

{{% /alert %}} {{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Implementare un Motore di Calcolo Personalizzato](/cells/it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **Aggiunto Indicizzatore Sovraccaricato per TextBoxCollection**
Aspose.Cells for Java 8.7.2 ha esposto l'indicizzato sovraccaricato per la classe TextBoxCollection al fine di accedere all'istanza di TextBox utilizzando il suo nome come stringa.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Accedere alla TextBox tramite il suo Nome](/cells/it/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

Lo scenario di utilizzo semplice appare come segue. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
