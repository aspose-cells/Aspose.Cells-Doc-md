---
title: Utilisation de la fonctionnalité ICustomFunction
type: docs
weight: 890
url: /fr/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Cet article fournit une compréhension détaillée de la façon d’utiliser la fonctionnalité ICustomFunction pour implémenter des fonctions personnalisées avec les API Aspose.Cells.

L'interface ICustomFunction permet d'ajouter des fonctions de calcul de formule personnalisées pour étendre le moteur de calcul de base Aspose.Cells' afin de répondre à certaines exigences. Cette fonctionnalité est utile pour définir des fonctions personnalisées (définies par l'utilisateur) dans un fichier modèle ou dans du code où la fonction personnalisée peut être implémentée et évaluée à l'aide des API Aspose.Cells comme toute autre fonction Excel Microsoft par défaut.

 Attention, cette interface a été remplacée par[RésuméCalculMoteur](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) et sera supprimé à l'avenir. Quelques articles/exemples techniques sur le nouveau API :[ici](/cells/fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) et[ici](/cells/fr/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Si vous êtes nouveau sur les API Aspose.Cells for Java, veuillez vérifier[ce](https://docs.aspose.com/cells/java/installation/) article pour savoir comment acquérir et référencer le Aspose.Cells for Java dans votre projet.

{{% /alert %}} 
##  **Création et évaluation d'une fonction définie par l'utilisateur**
 Cet article montre l'implémentation de l'interface ICustomFunction pour écrire une fonction personnalisée et l'utiliser dans la feuille de calcul pour obtenir les résultats. Nous définirons une fonction personnalisée par son nom**MaFonction** qui acceptera 2 paramètres avec les détails suivants.

- Le 1er paramètre fait référence à une seule cellule
- Le 2ème paramètre fait référence à une plage de cellules

La fonction personnalisée ajoutera toutes les valeurs de la plage de cellules spécifiée comme 2ème paramètre et divisera le résultat avec la valeur du 1er paramètre.

Voici comment nous avons implémenté la méthode calculateCustomFunction.

**Java**

{{< highlight "csharp" >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

Voici comment utiliser la fonction nouvellement définie dans une feuille de calcul

**Java**

{{< highlight "csharp" >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
##  **Aperçu**
Les API Aspose.Cells placent simplement l'objet ReferredArea dans la "paramsList" lorsque le paramètre correspondant est une référence ou que son résultat calculé est une référence. Si vous avez besoin de la référence elle-même, vous pouvez utiliser directement ReferredArea. Si vous avez besoin d'obtenir la valeur d'une seule cellule à partir de la référence correspondant à la position de la formule, vous pouvez utiliser la méthode ReferredArea.getValue(rowOffset, int colOffset). Si vous avez besoin d'un tableau de valeurs de cellules pour toute la zone, vous pouvez utiliser la méthode ReferredArea.getValues.

Comme les API Aspose.Cells donnent la ReferredArea dans "paramsList", la ReferredAreaCollection dans "contextObjects" ne sera plus nécessaire (dans les anciennes versions, il n'était pas toujours possible de donner une carte un à un aux paramètres de la fonction personnalisée), donc il a été supprimé des "contextObjects".

{{< highlight "java" >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
