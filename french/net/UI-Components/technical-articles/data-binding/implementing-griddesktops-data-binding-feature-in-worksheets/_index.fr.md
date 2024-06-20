---
title: Implémentation de la fonctionnalité de liaison de données GridDesktop dans les feuilles de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop, liaison de données, données, lier
description: Cet article présente comment effectuer la liaison de données dans GridDesktop.
---

{{% alert color="primary" %}} 

La liaison de données est une fonctionnalité passionnante offerte par le framework Microsoft .NET. Nous savons que le contrôle DataGrid offert par Microsoft prend en charge la liaison de données, ce qui signifie qu'un DataGrid peut être lié à n'importe quelle source de données (en utilisant les objets DataSet, DataTable et DataView). Cette fonctionnalité a grandement facilité la vie des développeurs. Sur la base du même concept, Aspose.Cells.GridDesktop prend également en charge la liaison de données, ce qui permet aux développeurs de lier des feuilles de calcul à n'importe quelle source de données. Cet article explore cette fonctionnalité.

{{% /alert %}} 
## **Création d'une base de données d'exemple**
1. Créez une base de données d'exemple à utiliser avec l'exemple. Nous avons utilisé Microsoft Access pour créer une base de données d'exemple avec une table Produits (schéma ci-dessous). 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Trois enregistrements fictifs sont ajoutés à la table Produits.
   **Enregistrements dans la table Produits** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Créer une application d'exemple**
Maintenant, créez une application de bureau simple dans Visual Studio et faites ce qui suit.

1. Faites glisser le contrôle "GridControl" depuis la boîte à outils et déposez-le sur le formulaire.
1. Déposez quatre boutons depuis la boîte à outils en bas du formulaire et définissez leur propriété de texte respectivement comme **Lier à la feuille de calcul**, **Ajouter ligne**, **Supprimer ligne** et **Mettre à jour dans la base de données**.
## **Ajout de l'espace de noms et déclaration de variables globales**
Parce que cet exemple utilise une base de données Microsoft Access, ajoutez l'espace de noms System.Data.OleDb en haut du code.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Vous pouvez maintenant utiliser les classes regroupées sous cet espace de noms.

1. Déclarez des variables globales.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Remplissage du DataSet avec des données de la base de données**
Connectez-vous maintenant à la base de données d'exemple pour récupérer et remplir les données dans un objet DataSet.

1. Utilisez l'objet OleDbDataAdapter pour vous connecter à notre base de données d'exemple et remplir un DataSet avec les données récupérées de la table Produits dans la base de données, comme indiqué dans le code ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Lier la feuille de calcul avec le DataSet de données de la base de données Produits:**
Lié la feuille de calcul avec la table de produits du DataSet :

1. Accédez à la feuille de calcul souhaitée.
1. Liez la feuille de calcul à la table Produits du DataSet.

Ajoutez le code suivant à l'événement de clic du bouton **Lier la feuille de calcul**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Paramétrage des en-têtes de colonnes de la feuille de calcul**
La feuille de calcul liée charge désormais les données avec succès mais les en-têtes de colonne sont par défaut étiquetées A, B et C. Il serait préférable de définir les en-têtes de colonne sur les noms de colonne dans la table de la base de données.

Pour définir les en-têtes de colonne de la feuille de calcul :

1. Obtenez les légendes pour chaque colonne du DataTable (Produits) dans le DataSet.
1. Attribuez les légendes aux en-têtes des colonnes de la feuille de calcul.

Ajoutez le code écrit dans l'événement de clic du bouton **Lier la feuille de calcul** avec le extrait de code suivant. En faisant cela, les anciens en-têtes de colonne (A, B et C) seront remplacés par ProductID, ProductName et ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Personnalisation de la largeur et des styles des colonnes**
Pour améliorer l'apparence de la feuille de calcul, il est possible de définir la largeur et les styles des colonnes. Par exemple, parfois, l'en-tête de colonne ou la valeur à l'intérieur de la colonne est constitué d'un grand nombre de caractères qui ne rentrent pas dans la cellule. Pour résoudre de tels problèmes, Aspose.Cells.GridDesktop prend en charge la modification de la largeur des colonnes.

Ajoutez le code suivant au bouton **Lier la feuille de calcul**. Les largeurs des colonnes seront personnalisées selon les nouveaux paramètres.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop prend également en charge l'application de styles personnalisés aux colonnes. Le code suivant, ajouté au bouton **Lier la feuille de calcul**, personnalise les styles de colonne pour les rendre plus présentables.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Maintenant, exécutez l'application et cliquez sur le bouton **Lier la feuille de calcul**.
## **Ajout de lignes**
Pour ajouter de nouvelles lignes à une feuille de calcul, utilisez la méthode AddRow de la classe Worksheet. Cela ajoute une ligne vide en bas et une nouvelle DataRow est ajoutée à la source de données (ici, une nouvelle DataRow est ajoutée à la DataTable du DataSet). Les développeurs peuvent ajouter autant de lignes qu'ils le souhaitent en appelant la méthode AddRow à plusieurs reprises. Lorsqu'une ligne a été ajoutée, les utilisateurs peuvent y saisir des valeurs.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Suppression de lignes**
Aspose.Cells.GridDesktop prend également en charge la suppression de lignes en appelant la méthode RemoveRow de la classe Worksheet. Supprimer une ligne à l'aide d'Aspose.Cells.GridDesktop nécessite l'index de la ligne à supprimer.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Ajoutez le code ci-dessus au bouton **Supprimer la ligne** et exécutez l'application. Quelques enregistrements sont affichés avant que la ligne soit supprimée. En sélectionnant une ligne et en cliquant sur le bouton **Supprimer la ligne**, la ligne sélectionnée est supprimée.
## **Enregistrer les modifications dans la base de données**
Enfin, pour enregistrer les modifications apportées par les utilisateurs à la feuille de calcul dans la base de données, utilisez la méthode Update de l'objet OleDbDataAdapter. La méthode Update prend la source de données (DataSet, DataTable, etc.) de la feuille de calcul pour mettre à jour la base de données.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Ajoutez le code ci-dessus au bouton **Mettre à jour la base de données**.
1. Exécutez l'application.
1. Effectuez des opérations sur les données de la feuille de calcul, peut-être en ajoutant de nouvelles lignes et en modifiant ou en supprimant des données existantes.
1. Ensuite, cliquez sur **Mettre à jour la base de données** pour enregistrer les modifications dans la base de données.
1. Vérifiez la base de données pour voir si les enregistrements de la table ont été mis à jour en conséquence.
