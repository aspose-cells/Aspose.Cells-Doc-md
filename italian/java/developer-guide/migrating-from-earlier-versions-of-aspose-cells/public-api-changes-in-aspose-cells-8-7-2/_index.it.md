---
title: Modifiche all'API pubblica in Aspose.Cells 8.7.2
type: docs
weight: 260
url: /it/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.7.1 alla 8.7.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Esteso il motore di calcolo predefinito**
Aspose.Cells Le API hanno un potente motore di calcolo in grado di calcolare quasi tutte le funzioni di Microsoft Excel. Inoltre, le API Aspose.Cells ora consentono di estendere il motore di calcolo predefinito per soddisfare i requisiti di calcolo personalizzati di qualsiasi applicazione.

Le seguenti API sono state aggiunte con il rilascio di Aspose.Cells for Java 8.7.2.

1. Classe AbstractCalculationEngine
1. Classe CalculationData
1. Proprietà CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Le API sopra menzionate consentono di implementare un motore di calcolo personalizzato per tutte le funzioni (incluse le funzioni native di Excel) con maggiore flessibilità.

{{% /alert %}} {{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Implementazione del motore di calcolo personalizzato](/cells/it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Aggiunto indicizzatore sovraccarico per TextBoxCollection**
Aspose.Cells for Java 8.7.2 ha esposto l'indicizzatore di overload per la classe TextBoxCollection per accedere all'istanza di TextBox utilizzando il suo nome come String.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Accesso al TextBox tramite il suo nome](/cells/it/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 Lo scenario di utilizzo semplice è il seguente.

**Giava**

{{< highlight "csharp" >}}

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
