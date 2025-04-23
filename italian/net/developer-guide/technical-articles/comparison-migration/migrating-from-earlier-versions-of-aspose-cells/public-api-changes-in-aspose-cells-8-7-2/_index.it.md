---
title: Modifiche all API pubblica in Aspose.Cells 8.7.2
type: docs
weight: 250
url: /it/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.7.1 alla 8.7.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Esteso il Motore di Calcolo Predefinito**
Le API di Aspose.Cells hanno un potente motore di calcolo che può calcolare quasi tutte le funzioni di Microsoft Excel. Inoltre, le API di Aspose.Cells consentono ora di estendere il motore di calcolo predefinito per soddisfare i requisiti di calcolo personalizzati di qualsiasi applicazione.

Le API seguenti sono state aggiunte con il rilascio di Aspose.Cells for .NET 8.7.2.

1. Classe AbstractCalculationEngine
1. Classe CalculationData
1. Proprietà CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Le API sopra menzionate consentono di implementare un motore di calcolo personalizzato per tutte le funzioni (incluso le funzioni native di Excel) con maggiore flessibilità.

{{% /alert %}} {{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzione, consulta l'articolo dettagliato su [Implementazione di un Motore di Calcolo Personalizzato](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **Aggiunto Indicizzatore Sovraccaricato per TextBoxCollection**
Aspose.Cells for .NET 8.7.2 ha esposto l'indicizzatore sovraccaricato per la classe TextBoxCollection al fine di accedere all'istanza di TextBox utilizzando il suo nome come stringa.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzione, consulta l'articolo dettagliato su [Accesso al TextBox tramite il suo Nome](/cells/it/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Lo scenario di utilizzo semplice appare come segue.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **Aggiunto evento OnAfterColumnFilter per GridWeb**
Aspose.Cells.GridWeb per .NET 8.7.2 ha esposto l'evento OnAfterColumnFilter che funge da callback per il meccanismo di filtro effettuato tramite l'interfaccia utente di Aspose.Cells.GridWeb. Come suggerisce il nome, l'evento viene attivato dopo che il filtro delle colonne è stato applicato e può essere utilizzato per ottenere informazioni sul filtro come l'indice della colonna su cui è stato applicato il filtro e il valore del filtro selezionato.

Lo scenario di utilizzo semplice appare come segue.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
