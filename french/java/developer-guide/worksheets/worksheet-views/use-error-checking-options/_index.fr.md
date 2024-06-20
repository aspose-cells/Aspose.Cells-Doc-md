---
title: Utiliser les options de vérification des erreurs
type: docs
weight: 60
url: /fr/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des options et des règles de vérification des erreurs. Les utilisateurs voient souvent des contrôles d'erreurs lors de la création de formules, un petit triangle en haut à droite d'une cellule met en évidence un problème avec une cellule. Excel fournit des informations qui aident les utilisateurs à corriger les problèmes courants.

{{% /alert %}} 
## **Types d'erreurs**
Les erreurs signifient que la formule ne peut pas renvoyer de résultat - comme diviser un nombre par zéro - nécessitent une attention immédiate et une valeur d'erreur est affichée dans la cellule. En cliquant sur le triangle vert, un point d'exclamation s'affiche, en cliquant dessus ouvre une liste d'options. 

L'erreur peut être résolue à l'aide des options ou être ignorée. Ignorer une erreur signifie que cette erreur n'apparaîtra pas dans d'autres vérifications d'erreur.

Aspose.Cells fournit des fonctionnalités d'options de vérification des erreurs. La classe ErrorCheckOptions gère différents types de vérifications d'erreurs, par exemple les nombres stockés en tant que texte, les erreurs de calcul de formule et les erreurs de validation. Utilisez l'énumération ErrorCheckType pour définir la vérification d'erreur souhaitée.
## **Nombres stockés sous forme de texte**
Parfois, les nombres peuvent être formatés et stockés dans des cellules sous forme de texte. Cela peut causer des problèmes avec les calculs ou produire des ordres de tri confus. Les nombres formatés comme du texte sont alignés à gauche au lieu de droite dans la cellule. Si une formule qui devrait effectuer une opération mathématique sur des cellules ne renvoie pas de valeur, vérifiez l'alignement dans les cellules auxquelles la formule se réfère, certaines ou toutes ces cellules pourraient être des nombres formatés comme du texte.

Vous pouvez utiliser les options de vérification des erreurs pour convertir rapidement les nombres stockés sous forme de texte en nombres réels. Dans Microsoft Excel 2003 :

1. Dans le menu **Outils**, cliquez sur **Options**.
1. Sélectionnez l'onglet Vérification des erreurs.
   L'option **Nombre stocké comme texte** est activée par défaut. 
1. Désactivez-la.
   Consultez l'image ci-dessous sur la façon dont le triangle vert est affiché pour les données dans MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

Le code d'exemple suivant montre comment désactiver l'option de vérification des erreurs pour les nombres stockés sous forme de texte pour une feuille de calcul dans le fichier XLS modèle à l'aide des API Aspose.Cells. 

**Java**

{{< highlight csharp >}}

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
