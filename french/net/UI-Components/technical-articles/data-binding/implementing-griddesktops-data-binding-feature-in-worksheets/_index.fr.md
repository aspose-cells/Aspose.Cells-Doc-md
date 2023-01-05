---
title: Implémentation de la fonctionnalité de liaison de données GridDesktop dans les feuilles de calcul
type: docs
weight: 10
url: /fr/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

La liaison de données est une fonctionnalité intéressante offerte par le framework Microsoft .NET. Nous savons que le contrôle DataGrid proposé par Microsoft prend en charge la liaison de données, ce qui signifie qu'un DataGrid peut être lié à n'importe quelle source de données (à l'aide d'objets DataSet, DataTable et DataView). Cette fonctionnalité a rendu la vie des développeurs beaucoup plus facile. Basé sur le même concept, Aspose.Cells. GridDesktop prend également en charge la liaison de données, ce qui permet aux développeurs de lier des feuilles de calcul à n'importe quelle source de données. Cet article explore la fonctionnalité.

{{% /alert %}} 
## **Création d'un exemple de base de données**
1.  Créez un exemple de base de données à utiliser avec l'exemple. Nous avons utilisé Microsoft Access pour créer un exemple de base de données avec une table Products (schéma ci-dessous).

![tâche : image_autre_texte](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Trois enregistrements factices sont ajoutés à la table Produits.
   **Enregistrements dans la table Produits** 

![tâche : image_autre_texte](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Créer un exemple d'application**
Créez maintenant une application de bureau simple dans Visual Studio et procédez comme suit.

1. Faites glisser le contrôle "GridControl" de la boîte à outils et déposez-le sur le formulaire.
1. Déposez quatre boutons de la boîte à outils en bas du formulaire et définissez leur propriété de texte sur**Relier la feuille de travail**, **Ajouter une rangée**, **Supprimer la ligne** et**Mettre à jour la base de données** respectivement.
## **Ajouter un espace de noms et déclarer des variables globales**
Étant donné que cet exemple utilise une base de données Access Microsoft, ajoutez l'espace de noms System.Data.OleDb en haut du code.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Vous pouvez maintenant utiliser les classes empaquetées sous cet espace de noms.

1. Déclarez des variables globales.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Remplir DataSet avec des données de la base de données**
Connectez-vous maintenant à l'exemple de base de données pour récupérer et remplir des données dans un objet DataSet.

1. Utilisez l'objet OleDbDataAdapter pour vous connecter à notre exemple de base de données et remplir un DataSet avec les données extraites de la table Products de la base de données, comme indiqué dans le code ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Feuille de calcul de liaison avec DataSet**
Liez la feuille de calcul à la table Products du DataSet :

1. Accédez à une feuille de calcul souhaitée.
1. Liez la feuille de calcul à la table Products du DataSet.

 Ajoutez le code suivant au**Relier la feuille de travail** l'événement de clic du bouton.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Définition des en-têtes de colonne de la feuille de calcul**
La feuille de calcul liée charge maintenant les données avec succès, mais les en-têtes de colonne sont étiquetés A, B et C par défaut. Il serait préférable de définir les en-têtes de colonne sur les noms de colonne dans la table de base de données.

Pour définir les en-têtes de colonne de la feuille de calcul :

1. Obtenez les légendes pour chaque colonne du DataTable (Produits) dans le DataSet.
1. Attribuez les légendes aux en-têtes des colonnes de la feuille de calcul.

 Joindre le code écrit dans le**Relier la feuille de travail** l'événement de clic du bouton avec l'extrait de code suivant. En faisant cela, les anciens en-têtes de colonne (A, B et C) seront remplacés par ProductID, ProductName et ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Personnalisation de la largeur et des styles de colonnes**
Pour améliorer encore l'apparence de la feuille de calcul, il est possible de définir la largeur et les styles des colonnes. Par exemple, parfois, l'en-tête de colonne ou la valeur à l'intérieur de la colonne se compose d'un long nombre de caractères qui ne rentrent pas dans la cellule. Pour résoudre ces problèmes, Aspose.Cells.GridDesktop prend en charge la modification de la largeur des colonnes.

 Ajoutez le code suivant au**Relier la feuille de travail** bouton. Les largeurs de colonne seront personnalisées en fonction des nouveaux paramètres.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop prend également en charge l'application de styles personnalisés aux colonnes. Le code suivant, annexé au**Relier la feuille de travail** , personnalise les styles de colonnes pour les rendre plus présentables.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Exécutez maintenant l'application et cliquez sur le**Relier la feuille de travail** Bouton.
## **Ajout de lignes**
Pour ajouter de nouvelles lignes à une feuille de calcul, utilisez la méthode AddRow de la classe Worksheet. Cela ajoute une ligne vide en bas et un nouveau DataRow est ajouté à la source de données (ici, un nouveau DataRow est ajouté au DataTable du DataSet). Les développeurs peuvent ajouter autant de lignes qu'ils le souhaitent en appelant encore et encore la méthode AddRow. Lorsqu'une ligne a été ajoutée, les utilisateurs peuvent y saisir des valeurs.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Suppression de lignes**
Aspose.Cells.GridDesktop prend également en charge la suppression de lignes en appelant la méthode RemoveRow de la classe Worksheet. La suppression d'une ligne à l'aide de Aspose.Cells.GridDesktop nécessite la suppression de l'index de la ligne.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Ajout du code ci-dessus au**Supprimer la ligne** bouton et exécutez l'application. Quelques enregistrements sont affichés avant la suppression de la ligne. Sélectionnez une ligne et cliquez sur le**Supprimer la ligne** Le bouton supprime la ligne sélectionnée.
## **Enregistrement des modifications dans la base de données**
Enfin, pour enregistrer les modifications apportées par les utilisateurs à la feuille de calcul dans la base de données, utilisez la méthode Update de l'objet OleDbDataAdapter. La méthode Update prend la source de données (DataSet, DataTable, etc.) de la feuille de calcul pour mettre à jour la base de données.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  Ajoutez le code ci-dessus au**Mettre à jour la base de données** bouton.
1. Exécutez l'application.
1. Effectuez certaines opérations sur les données de la feuille de calcul, par exemple en ajoutant de nouvelles lignes et en modifiant ou en supprimant des données existantes.
1.  Puis clique**Mettre à jour la base de données** pour enregistrer les modifications dans la base de données.
1. Vérifiez la base de données pour voir que les enregistrements de la table ont été mis à jour en conséquence.
