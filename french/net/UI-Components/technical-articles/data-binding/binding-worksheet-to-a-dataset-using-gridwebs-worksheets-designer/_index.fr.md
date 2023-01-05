---
title: Liaison d'une feuille de calcul à un ensemble de données à l'aide du concepteur de feuilles de calcul GridWebs
type: docs
weight: 20
url: /fr/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 Cet article décrit une approche simple pour lier des feuilles de calcul à des tables de base de données en mode graphique à l'aide d'un outil spécial fourni avec Aspose.Cells.GridWeb, le concepteur de feuilles de calcul.

{{% /alert %}} 
## **Liaison d'une feuille de calcul avec une base de données à l'aide du concepteur de feuilles de calcul**
	**Étape 1 : Création d'un exemple de base de données**
1. Tout d'abord, nous créons l'exemple de base de données qui sera utilisé dans cet article. Nous utilisons Microsoft Access pour créer une base de données qui contient une table appelée Products. Son schéma est présenté ci-dessous.
   **Informations de conception de la table Produits** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Quelques enregistrements factices sont ajoutés à la table Produits.
   **Enregistrements dans la table Produits** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Étape 2 : Concevoir un exemple d'application**
 Une application Web ASP.NET est créée et conçue dans Visual Studio.NET, comme indiqué ci-dessous.
**Exemple d'application conçu** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Étape 3 : Connexion à la base de données à l'aide de l'explorateur de serveurs**
 Il est temps de se connecter à la base de données. Nous pouvons le faire facilement en utilisant l'Explorateur de serveurs dans Visual Studio.NET.

1.  Sélectionner**Connexion de données** dans**Explorateur de serveur** et faites un clic droit.
1.  Sélectionner**Ajouter une connexion** du menu.
   **Sélection de l'option Ajouter une connexion** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 La boîte de dialogue Propriétés des liaisons de données s'affiche.
**La boîte de dialogue Propriétés des liaisons de données** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 À l'aide de cette boîte de dialogue, vous pouvez vous connecter à n'importe quelle base de données. Par défaut, il vous permet de vous connecter à une base de données SQL Server. Pour cet exemple, nous devons nous connecter avec une base de données Access Microsoft.

1.  Clique le**Fournisseur** languette.
1.  Sélectionner**Microsoft Fournisseur OLE DB Jet 4.0** du**Fournisseur(s) OLE DB** liste.
1.  Cliquez sur**Suivant**.
   **Cliquer sur Suivant après avoir sélectionné un fournisseur OLE DB** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 Le**Lien** la page à onglet est ouverte.

1.  Sélectionnez le fichier de base de données Access Microsoft (dans notre cas, db.mdb) et cliquez sur**D'ACCORD**.
   **Cliquer sur le bouton OK après avoir sélectionné le fichier de base de données** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 Après avoir cliqué**D'ACCORD** , une connexion à la base de données Access Microsoft sera créée dans le**Explorateur de serveur**Double-cliquez sur la connexion pour voir toutes les tables, vues et procédures stockées dans la base de données.

{{% /alert %}} 
### **Étape 4 : Création graphique d'objets de connexion à la base de données**
1.  Parcourez les tables de la base de données à l'aide de la**Explorateur de serveur**.
 Il n'y a qu'une seule table, Produits.
1.  Faites glisser et déposez le tableau Produits du**Explorateur de serveur** au**Formulaire Web**.
   **Faire glisser la table Produits depuis l'Explorateur de serveurs et la déposer dans le formulaire Web** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Une boîte de dialogue peut apparaître.
**Boîte de dialogue pour confirmer l'inclusion du mot de passe de la base de données dans la chaîne de connexion** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Décidez si vous souhaitez inclure ou non un mot de passe de base de données dans la chaîne de connexion. Pour cet exemple, nous avons sélectionné**Ne pas inclure le mot de passe**. 
Deux objets de connexion à la base de données (oleDbConnection1 et oleDbDataAdapter1) ont été créés et ajoutés.
**Objets de connexion à la base de données (oleDbConnection1 & oleDbDataAdapter1) créés et affichés** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Étape 5 : Génération de l'ensemble de données**
Jusqu'à présent, nous avons créé des objets de connexion à la base de données, mais nous avons toujours besoin d'un endroit pour stocker les données après la connexion à la base de données. Un objet DataSet peut stocker des données avec précision et nous pouvons également les générer facilement à l'aide de l'IDE VS.NET.

1.  Sélectionner**oleDbDataAdaper1** et faites un clic droit.
1.  Sélectionner**Générer un ensemble de données** option du menu.
   **Sélection de l'option Générer un ensemble de données** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 La boîte de dialogue Générer un ensemble de données s'affiche.
 Ici, il est possible de sélectionner un nom pour le nouvel objet DataSet à créer, et quelles tables doivent lui être ajoutées.

1.  Sélectionnez le**Ajouter cet ensemble de données au concepteur** option.
1.  Cliquez sur**D'ACCORD**.
   **Cliquer sur le bouton OK pour générer DataSet** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Un objet dataSet11 est ajouté au concepteur.
**DataSet généré et ajouté au concepteur** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Étape 6 : Utilisation du concepteur de feuilles de calcul**
 Maintenant, il est temps d'ouvrir le secret.

1. Sélectionnez le contrôle GridWeb et cliquez avec le bouton droit.
1.  Sélectionner**Concepteur de feuilles de travail** option du menu.

   **Sélection de l'option Concepteur de feuilles de calcul** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 L'éditeur de collection de feuilles de calcul (également appelé concepteur de feuilles de calcul) s'affiche.
**Boîte de dialogue Éditeur de collection de feuilles de calcul** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



La boîte de dialogue contient plusieurs propriétés qui peuvent être configurées pour lier Sheet1 à n'importe quelle table de la base de données.

1.  Sélectionnez le**La source de données** la propriété.
 L'objet dataSet11 généré à l'étape précédente est répertorié dans le menu.
1. Sélectionnez dataSet11.
1.  Clique le**Membre de données** la propriété.
 Le concepteur de feuilles de calcul affiche automatiquement une liste de tables dans dataSet11. Il n'y a qu'une seule table, Produits.
1. Sélectionnez la table Produits.
   **Définition des propriétés DataSource et DataMember** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  Vérifier la**LierColonnes** la propriété.
   **Cliquer sur la propriété BindColumns** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 En cliquant sur le**LierColonnes** La propriété ouvre l'éditeur de collection BindColumn.
**L'éditeur de collections BindColumn** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 Dans l'éditeur de collection BindColumn, toutes les colonnes de la**Des produits** table sont automatiquement ajoutés à la collection BindColumns.

1. Sélectionnez n'importe quelle colonne et personnalisez ses propriétés.
 Par exemple, vous pouvez modifier chaque légende de colonne.
   **Modification de la colonne Caption of ProductID** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  Après avoir apporté des modifications, cliquez sur**D'ACCORD**.
1.  Fermez toutes les boîtes de dialogue en cliquant sur**D'ACCORD**.
 Enfin, vous revenez à la page WebForm1.aspx.
   **Retour à la page WebForm1.aspx après avoir utilisé le concepteur de feuilles de calcul** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 Ci-dessus, le nom de la colonne de la table Produits est affiché. La largeur des colonnes est petite, de sorte que les noms complets de certaines colonnes ne sont pas entièrement visibles.
### **Étape 7 : Ajout de code au gestionnaire d'événements Page_Load**
 Nous avons utilisé le concepteur de feuilles de calcul et il nous suffit maintenant d'ajouter du code au gestionnaire d'événements Page_Load pour remplir l'objet dataSet11 avec les données de la base de données (à l'aide de oleDbDataAdapter1) et lier le contrôle GridWeb à dataSet11 en appelant sa méthode DataBind.

1.  Ajoutez le code :

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

1. Vérifiez le code ajouté au gestionnaire d'événements Page_Load.
   **Code ajouté au gestionnaire d'événements Page_Load** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Étape 8 : Exécution de l'application**
 Compilez et lancez l'application : soit appuyez sur**Ctrl+F5** ou cliquez**Démarrer**. 
**Lancer l'application** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Après compilation, la page WebForm1.aspx s'ouvre dans une fenêtre de navigateur avec toutes les données chargées depuis la base de données.
**Données chargées dans le champ GridWeb depuis la base de données** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Utilisation du contrôle GridWeb**
 Lorsque les données sont chargées dans le contrôle GridWeb, elles permettent aux utilisateurs de contrôler les données. Un certain nombre de différents types de fonctionnalités de manipulation de données sont offerts par le GridWeb.
### **La validation des données**
Aspose.Cells.GridWeb crée automatiquement des règles de validation appropriées pour toutes les colonnes liées en fonction des types de données définis dans la base de données. Voir le type de validation d'une cellule en passant le curseur dessus.
**Vérification du type de validation d'une cellule** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Ici, la cellule sélectionnée contient le**<INT>** validation, ce qui signifie que les utilisateurs ne peuvent y saisir que des valeurs entières. S'ils saisissent une autre valeur, une erreur de validation se produit. En outre,**<OBLIGATOIRE>** indique que la valeur Product ID doit être soumise.
### **Suppression de lignes**
 Pour supprimer une ligne, sélectionnez une ligne (ou n'importe quelle cellule de la ligne), faites un clic droit et sélectionnez**Supprimer la ligne**.
**Sélection de l'option Supprimer la ligne dans le menu** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


La ligne serait supprimée instantanément.
**Données de grille (après la suppression d'une ligne)** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Modification des lignes**
Modifiez les données dans les cellules ou les lignes, puis cliquez sur**Sauver** ou alors**Nous faire parvenir** pour enregistrer les modifications.
### **Ajout de lignes**
1.  Pour ajouter une ligne, cliquez avec le bouton droit sur une cellule et sélectionnez**Ajouter une rangée**.
   **Sélection de l'option Ajouter une ligne dans le menu** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Une nouvelle ligne est ajoutée à la feuille à la fin des autres lignes.
**Nouvelle ligne ajoutée à la grille** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 À gauche de la nouvelle ligne se trouve un astérisque{{< emoticons/cross >}} , indiquant que la ligne est nouvelle.

1. Ajoutez des valeurs à la nouvelle ligne.
1.  Cliquez sur**Sauver** ou alors**Nous faire parvenir** pour confirmer le changement.
   **Enregistrement des modifications apportées aux données en cliquant sur * Enregistrer** bouton*

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Définition du format de nombre**
 Pour le moment, les prix dans le**Prix du produit** colonne sont affichées sous forme de valeurs numériques. Il est possible de les faire ressembler à de la monnaie.

1. Revenez à Visual Studio.NET.
1. Ouvrez l'éditeur de collections BindColumn.
 Le**NuméroType** propriété de la**Prix du produit** la colonne est définie sur**Général**.
   **La propriété NumberType définie sur General** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Cliquez sur**La liste déroulante** et sélectionnez**Devise4** de la liste.
   **La propriété NumberType a été remplacée par Currency4** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Exécutez à nouveau l'application.
 Les valeurs dans le**Prix du produit** la colonne est maintenant la devise.
   **Prix des produits en devise Format numérique** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Modification des données**
 Jusqu'à présent, l'application ne permet à ses utilisateurs que de visualiser les données du tableau. Les utilisateurs peuvent modifier les données dans le contrôle GridWeb mais, lors de la fermeture du navigateur et de l'ouverture de la base de données, rien n'a changé. Les modifications apportées ne sont pas enregistrées dans la base de données.

 L'exemple suivant ajoute du code à l'application afin que GridWeb puisse enregistrer les modifications apportées à la base de données.

1. Ouvrez le**Propriétés** volet et sélectionnez l'événement SaveCommand du contrôle GridWeb dans la liste.
   **Sélection de l'événement SaveCommand de GridWeb** 

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  Double-cliquez sur le**Enregistrer la commande** et VS.NET crée le gestionnaire d'événements GridWeb1_SaveCommand.
1.  Ajoutez du code à ce gestionnaire d'événements qui mettra à jour la base de données avec toutes les données modifiées dans le DataSet lié à la feuille de calcul à l'aide de oleDbDataAdapter1.

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

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

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

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

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 Enregistrez les modifications dans la base de données à l'aide de la**Sauver** maintenant les enregistre définitivement.
## **Conclusion**
{{% alert color="primary" %}} 

La liaison de données est une fonctionnalité importante de Aspose.Cells.GridWeb. Il est facile de lier des feuilles de calcul à une base de données à l'aide de l'utilitaire Worksheets Designer proposé par Aspose.Cells.GridWeb. Aspose.Cells.GridWeb permet d'économiser du temps et des efforts lors de la création de puissantes solutions de grille.

{{% /alert %}}
