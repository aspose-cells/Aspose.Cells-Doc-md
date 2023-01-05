---
title: Public API Changements dans Aspose.Cells 8.7.2
type: docs
weight: 260
url: /fr/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.7.1 à 8.7.2 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Extension du moteur de calcul par défaut**
Les API Aspose.Cells disposent d'un puissant moteur de calcul capable de calculer presque toutes les fonctions Excel Microsoft. De plus, les API Aspose.Cells permettent désormais d'étendre le moteur de calcul par défaut pour répondre aux exigences de calcul personnalisées de n'importe quelle application.

Les API suivantes ont été ajoutées avec la version Aspose.Cells for Java 8.7.2.

1. Classe AbstractCalculationEngine
1. Classe CalculationData
1. Propriété CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Les API mentionnées ci-dessus permettent d'implémenter un moteur de calcul personnalisé pour toutes les fonctions (y compris les fonctions natives d'Excel) avec plus de flexibilité.

{{% /alert %}} {{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Implémentation d'un moteur de calcul personnalisé](/cells/fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

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
### **Indexeur surchargé ajouté pour TextBoxCollection**
Aspose.Cells for Java 8.7.2 a exposé l'indexeur surchargé pour la classe TextBoxCollection afin d'accéder à l'instance de TextBox en utilisant son nom comme String.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Accéder à la TextBox via son nom](/cells/fr/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 Le scénario d'utilisation simple se présente comme suit.

**Java**

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
