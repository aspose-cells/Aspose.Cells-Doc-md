---
title: Public API Changements dans Aspose.Cells 8.7.2
type: docs
weight: 250
url: /fr/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.7.1 à 8.7.2 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Extension du moteur de calcul par défaut**
Les API Aspose.Cells disposent d'un puissant moteur de calcul capable de calculer presque toutes les fonctions Excel Microsoft. De plus, les API Aspose.Cells permettent désormais d'étendre le moteur de calcul par défaut pour répondre aux exigences de calcul personnalisées de n'importe quelle application.

Les API suivantes ont été ajoutées avec la version Aspose.Cells for .NET 8.7.2.

1. Classe AbstractCalculationEngine
1. Classe CalculationData
1. Propriété CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Les API mentionnées ci-dessus permettent d'implémenter un moteur de calcul personnalisé pour toutes les fonctions (y compris les fonctions natives d'Excel) avec plus de flexibilité.

{{% /alert %}} {{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Implémentation d'un moteur de calcul personnalisé](/cells/fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

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


### **Indexeur surchargé ajouté pour TextBoxCollection**
Aspose.Cells for .NET 8.7.2 a exposé l'indexation surchargée pour la classe TextBoxCollection afin d'accéder à l'instance de TextBox en utilisant son nom comme chaîne.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Accéder à la TextBox via son nom](/cells/fr/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Le scénario d'utilisation simple se présente comme suit.

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


### **Ajout de l'événement OnAfterColumnFilter pour GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.2 a exposé l'événement OnAfterColumnFilter qui sert de rappel au mécanisme de filtrage effectué via l'interface utilisateur Aspose.Cells.GridWeb. Comme son nom l'indique, l'événement est déclenché après l'application du filtrage de colonne et peut être utilisé pour obtenir les informations de filtrage telles que l'index de colonne sur lequel le filtre a été appliqué et la valeur de filtre sélectionnée.

Le scénario d'utilisation simple se présente comme suit.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

N'oubliez pas d'enregistrer l'événement au contrôle GridWeb<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
