---
title: Pubblico API Modifiche Aspose.Cells 8.7.2
type: docs
weight: 250
url: /it/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.7.1 alla 8.7.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Esteso il motore di calcolo predefinito**
Aspose.Cells Le API hanno un potente motore di calcolo in grado di calcolare quasi tutte le Microsoft funzioni di Excel. Inoltre, le API Aspose.Cells ora consentono di estendere il motore di calcolo predefinito per soddisfare i requisiti di calcolo personalizzati di qualsiasi applicazione.

Le seguenti API sono state aggiunte con il rilascio di Aspose.Cells for .NET 8.7.2.

1. Classe AbstractCalculationEngine
1. Classe CalculationData
1. Proprietà CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Le API sopra menzionate consentono di implementare un motore di calcolo personalizzato per tutte le funzioni (incluse le funzioni native di Excel) con maggiore flessibilità.

{{% /alert %}} {{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Implementazione del motore di calcolo personalizzato](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

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


### **Aggiunto indicizzatore sovraccarico per TextBoxCollection**
Aspose.Cells for .NET 8.7.2 ha esposto l'indicizzazione in overload per la classe TextBoxCollection per poter accedere all'istanza di TextBox utilizzandone il nome come stringa.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Accesso al TextBox tramite il suo nome](/cells/it/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Lo scenario di utilizzo semplice è il seguente.

**C#**

{{< highlight "csharp" >}}

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


### **Aggiunto l'evento OnAfterColumnFilter per GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.2 ha esposto l'evento OnAfterColumnFilter che funge da callback al meccanismo di filtro eseguito tramite l'interfaccia utente Aspose.Cells.GridWeb. Come suggerisce il nome, l'evento viene attivato dopo l'applicazione del filtro della colonna e può essere utilizzato per ottenere informazioni sul filtro come l'indice della colonna su cui è stato applicato il filtro e il valore del filtro selezionato.

Lo scenario di utilizzo semplice è il seguente.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Non dimenticare di registrare l'evento nel controllo GridWeb<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
