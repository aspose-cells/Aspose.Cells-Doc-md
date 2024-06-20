---
title: Liaison de la feuille de calcul à un DataSet à l aide du concepteur de feuilles de calcul GridWebs
type: docs
weight: 20
url: /fr/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: Cet article présente comment utiliser le concepteur de feuilles de calcul pour lier une feuille de calcul à un DataSet dans GridWeb.
---

{{% alert color="primary" %}} 

Cet article discute d'une approche facile pour lier des feuilles de calcul à des tables de base de données en mode GUI en utilisant un outil spécial fourni avec Aspose.Cells.GridWeb, le concepteur de feuilles de calcul. 

{{% /alert %}} 
## **Lier une feuille de calcul avec une base de données en utilisant le concepteur de feuilles de calcul**
	**Étape 1 : Création d'une base de données d'exemple**
1. Tout d'abord, nous créons la base de données d'exemple qui sera utilisée dans cet article. Nous utilisons Microsoft Access pour créer une base de données contenant une table appelée Products. Son schéma est indiqué ci-dessous.
   **Informations de conception de la table Products** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Quelques enregistrements fictifs sont ajoutés à la table Products.
   **Enregistrements dans la table des produits** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Étape 2 : Conception de l'application d'exemple**
Une application web ASP.NET est créée et conçue dans Visual Studio.NET comme indiqué ci-dessous. 
**Application d'exemple conçue** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Étape 3 : Connexion à la base de données en utilisant l'Explorateur de serveur**
Il est temps de se connecter à la base de données. Nous pouvons le faire facilement en utilisant l'Explorateur de serveur dans Visual Studio.NET. 

1. Sélectionnez **Connexion de données** dans **Explorateur de serveur** et cliquez avec le bouton droit.
1. Sélectionnez **Ajouter une connexion** dans le menu.
   **Sélection de l'option Ajouter une connexion** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



La boîte de dialogue Propriétés du lien de données s'affiche. 
**La boîte de dialogue Propriétés du lien de données** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



En utilisant cette boîte de dialogue, vous pouvez vous connecter à n'importe quelle base de données. Par défaut, il vous permet de vous connecter à une base de données SQL Server. Pour cet exemple, nous devons nous connecter à une base de données Microsoft Access. 

1. Cliquez sur l'onglet **Fournisseur**.
1. Sélectionnez **Microsoft Jet 4.0 OLE DB Provider** dans la liste des **Fournisseurs OLE DB**.
1. Cliquez sur **Suivant**.
   **Cliquez sur Suivant après avoir sélectionné un fournisseur OLE DB** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


La page de l'onglet **Connexion** est ouverte. 

1. Sélectionnez le fichier de base de données Microsoft Access (dans notre cas, db.mdb) et cliquez sur **OK**.
   **Cliquez sur le bouton OK après avoir sélectionné le fichier de la base de données** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

Après avoir cliqué sur **OK**, une connexion à la base de données Microsoft Access sera créée dans l'**Explorateur de serveurs**. Double-cliquez sur la connexion pour voir toutes les tables, vues et procédures stockées dans la base de données.

{{% /alert %}} 
### **Étape 4 : Créer des objets de connexion à la base de données graphiquement**
1. Parcourez les tables de la base de données en utilisant l'**Explorateur de serveurs**.
   Il n'y a qu'une seule table, Produits. 
1. Faites glisser et déposez la table Produits depuis l'**Explorateur de serveurs** dans le **Formulaire Web**.
   **Faites glisser la table Produits depuis l'Explorateur de serveurs et déposez-la dans le formulaire web** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Une boîte de dialogue peut apparaître.
**Boîte de dialogue pour confirmer l'inclusion du mot de passe de la base de données dans la chaîne de connexion** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Décidez si vous souhaitez inclure un mot de passe de base de données dans la chaîne de connexion ou non. Pour cet exemple, nous avons sélectionné **Ne pas inclure de mot de passe**. 
Deux objets de connexion à la base de données (oleDbConnection1 et oleDbDataAdapter1) ont été créés et ajoutés.
**Objets de connexion à la base de données (oleDbConnection1 & oleDbDataAdapter1) créés et affichés** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Étape 5 : Générer le DataSet**
Jusqu'à présent, nous avons créé des objets de connexion à la base de données mais nous avons encore besoin d'un endroit pour stocker les données après s'être connecté à la base de données. Un objet DataSet peut stocker précisément des données et nous pouvons également le générer facilement à l'aide de l'IDE VS. NET. 

1. Sélectionnez **oleDbDataAdaper1** et cliquez avec le bouton droit.
1. Sélectionnez l'option **Générer DataSet** dans le menu.
   **Sélection de l'option Générer DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



La boîte de dialogue Générer DataSet s'affiche. 
Il est possible de sélectionner un nom pour le nouvel objet DataSet à créer, et quelles tables doivent y être ajoutées. 

1. Sélectionnez l'option **Ajouter ce jeu de données au concepteur**.
1. Cliquez sur **OK**.
   **Cliquez sur le bouton OK pour générer le DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Un objet dataSet11 est ajouté au concepteur.
**DataSet généré et ajouté au concepteur** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Étape 6: Utilisation du concepteur de feuilles de calcul**
Maintenant, il est temps d'ouvrir le secret. 

1. Sélectionnez le contrôle GridWeb et cliquez avec le bouton droit.
1. Sélectionnez l'option **Concepteur de feuilles de calcul** dans le menu. 

   **Sélection de l'option Concepteur de feuilles de calcul** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



L'éditeur de collection de feuilles de calcul (également appelé le Concepteur de feuilles de calcul) s'affiche. 
**Boîte de dialogue de l'éditeur de collection de feuilles de calcul** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



La boîte de dialogue contient plusieurs propriétés qui peuvent être configurées pour lier la Feuille1 à n'importe quelle table dans la base de données.

1. Sélectionnez la propriété **DataSource**.
   L'objet dataSet11 généré à l'étape précédente est répertorié dans le menu. 
1. Sélectionnez dataSet11.
1. Cliquez sur la propriété **DataMember**.
   Le concepteur de feuilles de calcul affiche automatiquement une liste de tables dans dataSet11. Il n'y a qu'une seule table, Produits.
1. Sélectionnez la table Produits.
   **Définition des propriétés DataSource et DataMember** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. Vérifiez la propriété **BindColumns**.
   **Cliquez sur la propriété BindColumns** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



Cliquer sur la propriété **BindColumns** ouvre l'Éditeur de collection BindColumn.
**L'Éditeur de collection BindColumn** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



Dans l'Éditeur de collection BindColumn, toutes les colonnes de la table **Produits** sont automatiquement ajoutées à la collection BindColumns. 

1. Sélectionnez une colonne et personnalisez ses propriétés.
   Par exemple, vous pouvez modifier le libellé de chaque colonne.
   **Modification du libellé de la colonne ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. Après avoir apporté des modifications, cliquez sur **OK**.
1. Fermez toutes les boîtes de dialogue en cliquant sur **OK**.
   Enfin, vous revenez à la page WebForm1.aspx. 
   **Retour à la page WebForm1.aspx après avoir utilisé le concepteur de feuilles de calcul** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Ci-dessus, le nom de la colonne de la table Produits est affiché. La largeur des colonnes est petite, donc les noms complets de certaines colonnes ne sont pas entièrement visibles. 
### **Étape 7 : Ajout de code à l'événement Page_Load**
Nous avons utilisé le concepteur de feuilles de calcul et nous devons maintenant ajouter du code au gestionnaire d'événements Page_Load pour remplir l'objet dataSet11 avec des données de la base de données (en utilisant oleDbDataAdapter1) et lier le contrôle GridWeb à dataSet11 en appelant sa méthode DataBind. 

1. Ajouter le code : 

**C#**

{{< highlight csharp >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Implementing Page_Load event handler

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub



{{< /highlight >}}

1. Vérifier le code ajouté à l'événement Page_Load.
   **Code ajouté à l'événement Page_Load** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Étape 8 : Exécution de l'application**
Compiler et exécuter l'application : appuyez sur **Ctrl+F5** ou cliquez sur **Démarrer**. 
**Exécution de l'application** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Après la compilation, la page WebForm1.aspx s'ouvre dans une fenêtre de navigateur avec toutes les données chargées depuis la base de données.
**Données chargées dans le contrôle GridWeb depuis la base de données** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Travailler avec le contrôle GridWeb**
Lorsque des données sont chargées dans le contrôle GridWeb, cela offre aux utilisateurs un contrôle sur les données. Un certain nombre de fonctionnalités de manipulation de données différentes sont proposées par le GridWeb. 
### **Validation des données**
Aspose.Cells.GridWeb crée automatiquement des règles de validation appropriées pour toutes les colonnes liées selon les types de données définis dans la base de données. Voir le type de validation d'une cellule en survolant le curseur dessus.
**Vérifier le type de validation d'une cellule** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Suppression de lignes**
Pour supprimer une ligne, sélectionnez une ligne (ou n'importe quelle cellule de la ligne), faites un clic droit et sélectionnez **Supprimer la ligne**.
**Sélection de l'option Supprimer la ligne dans le menu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


La ligne sera supprimée instantanément.
**Données du tableau (après qu'une ligne soit supprimée)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Modification de lignes**
Modifiez les données dans les cellules ou les lignes, puis cliquez sur **Enregistrer** ou **Soumettre** pour enregistrer les modifications. 
### **Ajout de lignes**
1. Pour ajouter une ligne, cliquez avec le bouton droit sur une cellule et sélectionnez **Ajouter une ligne**.
   **Sélection de l'option Ajouter une ligne dans le menu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Une nouvelle ligne est ajoutée à la feuille à la fin des autres lignes.
**Nouvelle ligne ajoutée à la grille** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Ajoutez des valeurs à la nouvelle ligne.
1. Cliquez sur **Enregistrer** ou **Soumettre** pour confirmer le changement.
   **Enregistrer les modifications des données en cliquant sur le bouton **Enregistrer** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Paramétrage du format numérique**
Actuellement, les prix dans la colonne **Prix du produit** sont affichés sous forme de valeurs numériques. Il est possible de les faire ressembler à de la monnaie.

1. Retournez à Visual Studio.NET.
1. Ouvrez l'Éditeur de collection BindColumn.
   La propriété **TypeNombre** de la colonne **Prix du produit** est définie sur **Général**.
   **La propriété TypeNombre définie sur Général** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. Cliquez sur **Liste déroulante** et sélectionnez **Devise4** dans la liste.
   **La propriété TypeNombre a été modifiée en Devise4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Exécutez à nouveau l'application.
   Les valeurs dans la colonne **Prix du produit** sont maintenant en monnaie.
   **Prix des produits au format numérique de la devise** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Modification des données**
L'application permet jusqu'à présent seulement à ses utilisateurs de visualiser les données de table. Les utilisateurs peuvent modifier les données dans le contrôle GridWeb, mais une fois le navigateur fermé et la base de données ouverte, rien n'a changé. Les modifications apportées ne sont pas enregistrées dans la base de données. 

L'exemple suivant ajoute du code à l'application afin que le GridWeb puisse enregistrer les modifications dans la base de données. 

1. Ouvrez le volet **Propriétés** et sélectionnez l'événement SaveCommand du contrôle GridWeb dans la liste.
   **Sélectionner l'événement SaveCommand de GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. Double-cliquez sur l'événement **SaveCommand** et VS.NET créera le gestionnaire d'événements GridWeb1_SaveCommand.
1. Ajoutez du code à ce gestionnaire d'événements qui mettra à jour la base de données avec toute donnée modifiée dans le DataSet lié à la feuille de calcul à l'aide de oleDbDataAdapter1. 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

Vous pouvez également vérifier le code ajouté au gestionnaire d'événements GridWeb1_SaveCommand
**Code ajouté au gestionnaire d'événements GridWeb1_SaveCommand** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Les modifications apportées à la base de données à l'aide du bouton **Enregistrer** sont maintenant définitivement enregistrées.
## **Conclusion**
{{% alert color="primary" %}} 

La liaison de données est une fonctionnalité importante de Aspose.Cells.GridWeb. Il est facile de lier des feuilles de calcul à une base de données en utilisant l'utilitaire Worksheets Designer proposé par Aspose.Cells.GridWeb. Aspose.Cells.GridWeb permet de gagner du temps et des efforts lors de la création de puissantes solutions de grille. 

{{% /alert %}}
