---
title: Utiliser les options de vérification des erreurs
type: docs
weight: 60
url: /fr/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des options et des règles de vérification des erreurs. Les utilisateurs voient souvent des contrôles d'erreur lors de la création de formules, un petit triangle dans le coin supérieur droit d'une cellule met en évidence lorsqu'il y a un problème avec une cellule. Excel fournit des informations qui aident les utilisateurs à corriger les problèmes courants.

{{% /alert %}} 
## **Types d'erreurs**
Les erreurs qui signifient que la formule ne peut pas renvoyer de résultat, comme la division d'un nombre par zéro, nécessitent une attention immédiate et une valeur d'erreur s'affiche dans la cellule. Cliquer sur le triangle vert affiche un point d'exclamation, cliquer dessus ouvre la liste des options.

L'erreur peut être résolue à l'aide des options ou être ignorée. Ignorer une erreur signifie que cette erreur n'apparaîtra pas dans les contrôles d'erreur ultérieurs.

Aspose.Cells fournit des fonctionnalités d'option de vérification des erreurs. La classe ErrorCheckOptions gère différents types de contrôles d'erreurs, par exemple les nombres stockés sous forme de texte, les erreurs de calcul de formule et les erreurs de validation. Utilisez l'énumération ErrorCheckType pour définir la vérification d'erreur souhaitée.
## **Numbers stocké sous forme de texte**
Parfois, les nombres peuvent être formatés et stockés dans des cellules sous forme de texte. Cela peut entraîner des problèmes de calcul ou produire des ordres de tri déroutants. Numbers formatés en tant que texte sont alignés à gauche au lieu d'être alignés à droite dans la cellule. Si une formule qui doit effectuer une opération mathématique sur des cellules ne renvoie pas de valeur, vérifiez l'alignement dans les cellules auxquelles la formule fait référence - certaines ou toutes ces cellules peuvent être des nombres au format texte.

Vous pouvez utiliser les options de vérification des erreurs pour convertir rapidement les nombres stockés sous forme de texte en nombres réels. Dans Excel Microsoft 2003 :

1.  Sur le**Outils** menu, cliquez sur**Choix**.
1. Sélectionnez l'onglet Vérification des erreurs.
   **Numéro stocké sous forme de texte** option est cochée par défaut.
1. Désactivez-le.
 Voir l'image ci-dessous sur la façon dont le triangle vert est affiché pour les données dans MS Excel.

![tâche : image_autre_texte](use-error-checking-options_1.png)

 L'exemple de code suivant montre comment désactiver les nombres stockés en tant qu'option de vérification des erreurs de texte pour une feuille de calcul dans le fichier de modèle XLS à l'aide des API Aspose.Cells.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
