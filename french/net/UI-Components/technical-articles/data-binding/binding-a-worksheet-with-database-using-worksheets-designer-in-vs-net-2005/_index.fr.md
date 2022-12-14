---
title: Liaison d'une feuille de calcul avec une base de données à l'aide du concepteur de feuilles de calcul dans VS.Net 2005
type: docs
weight: 40
url: /fr/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 Cet article décrit une approche plus simple pour lier des feuilles de calcul avec des tables de base de données dans**Visual Studio.Net 2005** en utilisant un outil spécial fourni avec Aspose.Cells.GridWeb nommé comme**Concepteur de feuilles de travail** . Cet article vous fera certainement sentir qu'il est plus facile d'utiliser la fonction de liaison de données dans Aspose.Cells.GridWeb avec l'aide de**Concepteur de feuilles de travail** .

{{% /alert %}}

## **Liaison d'une feuille de calcul avec une base de données à l'aide du concepteur de feuilles de calcul dans VS.Net 2005**

 Le but de cet article est de permettre à tous les développeurs d'apprendre comment vous pouvez créer une application de liaison de données dans**VS.Net 2005** et comprendre l'utilisation et le rôle de**Concepteur de feuilles de travail** éditeur. La meilleure façon d'apprendre et de comprendre quoi que ce soit est à travers des exemples. Ainsi, dans cet article, il serait également préférable pour nous de créer un exemple d'application pour démontrer l'utilisation de**Concepteur de feuilles de travail**dans des feuilles de travail contraignantes avec base de données. Créons une application étape par étape.

### **Étape 1 : Création d'un exemple de base de données**

 Tout d'abord, nous allons créer un exemple de base de données qui sera utilisé dans cet article. Nous avons utilisé MS Access pour créer un exemple de base de données contenant**Des produits** table dont le schéma est présenté ci-dessous :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**Chiffre:** Informations de conception de**Des produits** table

 Peu d'enregistrements factices sont ajoutés au**Des produits** tableau comme indiqué ci-dessous dans la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**Chiffre:** Enregistrements dans**Des produits** table

### **Étape 2 : Concevoir un exemple d'application**

 Un**Application Web ASP.NET** est créé et conçu dans Visual Studio.NET 2005, comme illustré dans les figures ci-dessous. Ces captures d'écran sont utiles pour les développeurs qui ne sont pas très familiers avec Aspose.Cells.GridWeb dans Visual Studio.Net 2005.

Premier démarrage de VS.Net 2005.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**Chiffre:** À partir de VS.Net 2005

Créez un nouveau site Web à partir du menu Fichier|Nouveau|Site Web....

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**Chiffre:** Création d'un nouveau site Web

 Après avoir cliqué sur l'option de menu Fichier|Nouveau|Site Web...,**Nouveau site Internet** boîte de dialogue s'affiche. Clique le**Parcourir** bouton dedans.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**Chiffre:**Boîte de dialogue Nouveau site Web

 Après avoir cliqué sur le**Parcourir** , choisissez le dossier d'emplacement dans le IIS local. Vous pouvez créer un nouveau dossier et en faire un dossier virtuel, comme indiqué sur la figure.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**Chiffre:** Création d'un nouveau dossier


 Après avoir cliqué sur le**Ouvert** bouton dans le**Choisissez l'emplacement** dialogue,**Nouveau site Internet** la boîte de dialogue ressemblera.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**Chiffre:** Définition de l'emplacement du projet

Le projet est maintenant créé

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**Chiffre:** Projet créé

### **Modes XHTML et HTML**

**Aspose.Cells.GridWeb** prend complètement en charge le mode XHTML qui est implémenté par défaut dans VS.Net 2005 depuis le**XhtmlMode** propriété de la**GrilleWeb** le contrôle est réglé sur**Vrai** par défaut lorsque vous placez le contrôle sur la page Web. Mais si vous souhaitez implémenter le mode HTML pour le contrôle dans VS.Net 2005, vous pouvez le faire assez facilement. Vous devez modifier le**<!DOCTYPE>** marquer un peu dans le code source de la page Web et définir le**XhtmlMode** propriété de la**GrilleWeb** contrôler pour**Faux** .

#### **Dans cette rubrique, nous utiliserons le mode HTML pour le contrôle. Alors suivez les étapes ci-dessous**

##### **1. Basculez vers la vue Source de la page Web et recherchez la balise <!DOCTYPE> suivante dans le code source.**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

Une fois que vous avez trouvé cette balise, sélectionnez cette balise complète dans le code source, comme indiqué ci-dessous.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**Chiffre:** Sélection**Balise <!DOCTYPE>**

 Remplace le**<!DOCTYPE>** tag de votre code source par le suivant.

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**Chiffre:** Modification**Balise <!DOCTYPE>**

##### **2. Après avoir ajouté le contrôle GridWeb au formulaire Web. Vous devez sélectionner le contrôle et choisir la propriété XhtmlMode dans la fenêtre Propriétés pour la définir sur False.**

**Ajout de GridWeb au WebForm** 

 Clic droit sur**Boîte à outils** et sélectionnez**Choisissez les articles...** du menu.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**Chiffre:** Choisir des articles

 Sélectionnez maintenant**GrilleWeb** composant et cliquez sur**D'ACCORD**

{{% alert color="primary" %}}

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**Chiffre:** Sélection**GrilleWeb** composant dans la boîte de dialogue des composants

 Maintenant le**GrilleWeb** est ajouté comme indiqué dans la figure ci-dessous.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**Chiffre:** **GrilleWeb** est ajouté dans la boîte à outils

 Placer le**GrilleWeb** sur le formulaire Web comme indiqué ci-dessous.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**Chiffre:** Placement**GrilleWeb** sur la page internet

{{% /alert %}} {{% alert color="primary" %}}

**Procédure** : Sélectionnez le contrôle, Maintenant, choisissez le**XhtmlMode** propriété de la**Propriétés** fenêtre et réglez-le sur**Faux** évaluer.

{{% /alert %}}

##### **Étape 3 : Connexion à la base de données à l'aide de l'Explorateur de serveurs et définition de l'objet de connexion**

 Nous ajoutons d'abord la base de données MS Access au projet que nous avons précédemment créé dans**Étape 1** . Vous pouvez voir que**db.mdb** fichier est ajouté au projet.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**Chiffre:** Base de données ajoutée au dossier du projet

 Maintenant, nous allons à**Concepteur de composants** fenêtre du formulaire Web à l'aide de l'option de menu contextuel de la page Web.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**Chiffre:** Sélection**Afficher le concepteur de composants** option

La fenêtre du concepteur de composants est illustrée ci-dessous.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**Chiffre:** Fenêtre du concepteur de composants

 Double-cliquez sur le**OleDbConnectionOleDbConnection** composant du panneau Données pour placer l'objet oleDbConnection1 dans la fenêtre.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**Chiffre:** Objet oleDbConnection1

 Il est maintenant temps de se connecter à la base de données. Nous pouvons le faire facilement en utilisant**Explorateur de serveur** dans Visual Studio.NET 2005. Sélectionnez simplement**Connexion de données** dans**Explorateur de serveur** et clic droit. Vous verrez un menu contextuel apparaître devant vous. Sélectionner**Ajouter une connexion...**option dans le menu comme indiqué ci-dessous dans la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**Chiffre:** Sélection**Ajouter une connexion...** option du menu


 Après avoir sélectionné**Ajouter une connexion...** option du menu,**Ajouter une connexion** la boîte de dialogue s'ouvrira et**Parcourir** pour sélectionner le fichier de base de données comme indiqué ci-dessous.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**Chiffre:** Sélection du fichier de base de données

Vous pouvez tester la connexion.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**Chiffre:** Tester la connexion

Vous pouvez parcourir la connexion pour vérifier la table et ses champs.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**Chiffre:** Vérification de la table et de ses champs de la connexion

 Maintenant, si vous sélectionnez**oleDbConnection1** objet dans le**Concepteur de composants** fenêtre, vous pouvez sélectionner la chaîne de connexion liée à la connexion existante qui vient d'être créée, elle se trouve dans la propriété "ConnectionString" de la**oleDbConnection1** objet dans la fenêtre Propriétés.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**Chiffre:** Sélection de la chaîne de connexion pour l'objet

 Enfin, le modificateur de l'objet est changé en**Protégé** pour une meilleure accessibilité.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**Chiffre:** Définition du modificateur de l'objet

##### **Étape 4 : configuration de l'objet adaptateur de données**

 Maintenant, ajoutez un**OleDbDataAdapter** composant dans le panneau Données de la boîte à outils pour le configurer. Double-cliquez sur le**OleDbDataAdapter** dans le panneau Données de la boîte à outils, il lancera son assistant de configuration et sélectionnera la connexion existante comme indiqué sur la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**Chiffre:** Assistant de configuration de l'adaptateur de données

 Après avoir cliqué**Prochain** bouton, cliquez sur le**Générateur de requêtes** pour ajouter le**Des produits** tableau, sélectionnez Toutes les colonnes et cliquez sur**D'ACCORD** bouton.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**Chiffre:** Ajout de la table des produits

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**Chiffre:** Générateur de requêtes

 Cliquez maintenant**Finir** bouton pour terminer l'assistant.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**Chiffre:** Terminer l'assistant

 Après avoir configuré l'assistant, oleDbDataAdapter1 est automatiquement ajouté à la fenêtre, comme indiqué ci-dessous. De plus, vous pouvez définir son modificateur sur**Protégé**.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**Chiffre:** Récupération de l'objet OleDbDataAdapter sur la fenêtre du concepteur

##### **Étape 5 : Génération de l'ensemble de données**

 Comme nous avons créé des objets de connexion à la base de données et d'adaptateur de données, nous avons toujours besoin de quelque chose où nous pouvons stocker des données après la connexion à la base de données. UN**Base de données**object peut stocker des données avec précision et nous pouvons également les générer facilement à l'aide de VS.NET 2005 IDE. Pour ce faire, sélectionnez**oleDbDataAdaper1** et clic droit. Un menu contextuel apparaîtra avec certaines options. Sélectionner**Générer** **Base de données...** option dans le menu comme indiqué ci-dessous dans la figure.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**Chiffre:** Sélection**Générer** **Base de données...** option du menu

 Après avoir sélectionné**Générer** **Base de données...** option du menu, un**Générer un ensemble de données** la boîte de dialogue s'ouvrirait. En utilisant cette boîte de dialogue, nous pouvons sélectionner ce que serait le nom du nouveau**Base de données** l'objet à créer et les tables à ajouter**Base de données** . Vérifier**Ajouter cet ensemble de données au concepteur** option et cliquez**D'ACCORD** bouton comme indiqué ci-dessous dans la figure.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**Chiffre:** En cliquant**D'ACCORD** bouton pour générer**Base de données**

 Maintenant, vous pouvez voir un**dataSet11** objet ajouté au concepteur comme indiqué ci-dessous dans la figure. Définissez le modificateur d'objet sur**Protégé**.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**Chiffre:** **Base de données** généré et ajouté à la fenêtre du concepteur

Certains codes sont automatiquement générés dans la connexion liée au fichier .cs, l'adaptateur de données, l'objet de jeu de données.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**Chiffre:** Code généré

##### **Étape 6 : Utilisation du concepteur de feuilles de calcul**

 Maintenant, il est temps d'ouvrir le secret. Sélectionnez le contrôle et faites un clic droit. Un menu contextuel s'ouvrira. Sélectionnez l'option Worksheets Designer... dans le menu, comme indiqué ci-dessous dans la figure.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**Chiffre:** Sélection**Concepteur de feuilles de travail...** option du menu

 Après ça**Éditeur de collection de feuilles de calcul** boîte de dialogue (également appelée**Concepteur de feuilles de travail** ) sera ouvert, vous pouvez voir plusieurs propriétés qui peuvent être configurées pour lier le**Feuille1** avec n'importe quelle table de la base de données. sélectionnons**La source de données** propriété. Écrire**dataSet11** dedans (que nous avons généré et ajouté à la fenêtre du concepteur à l'étape précédente). Cliquez ensuite sur**Membre de données** propriété. Écrire**Des produits** comme nom de table ici, comme indiqué ci-dessous dans la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**Chiffre:** Paramètre**La source de données** et**Membre de données** Propriétés

 Maintenant, vous pouvez configurer**LierColonnes** propriété. Après avoir cliqué dessus, vous pouvez maintenant ajouter les colonnes de liaison et définir le**Légende** , **Champ de données** (Cela devrait être le même que**Des produits** champs de table) et d'autres propriétés. Vous pouvez régler le**EstCrééAuto** à**vrai** et appliquer**Validation** et réglez le**NuméroType**de différents domaines pour vos besoins.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**Chiffre:** En cliquant**LierColonnes** propriété

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**Chiffre:** **Éditeur de collections BindColumn** dialogue

##### **Étape 7 : Ajout de quelques lignes de code pour la page Web**

 Nous avons utilisé**Concepteur de feuilles de travail** facilement et maintenant nous n'avons plus qu'à ajouter quelques lignes de code

 Nous ajouterons d'abord**OnInit** code lié à l'événement à initialiser**InitializeComponent** méthode pour initialiser et créer des objets de connexion, de commande, d'adaptateur de données et d'ensemble de données. Ces lignes de code ne sont pas ajoutées avec le code généré automatiquement, nous devons donc les ajouter manuellement.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**Chiffre:** Ajouter du code1

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**Chiffre:** Ajouter du code2

 Maintenant, nous ajoutons du code dans le**Page_Load** gestionnaire d'événements pour le remplissage**dataSet11** objet avec des données de la base de données (en utilisant**oleDbDataAdapter1** ) et reliure**GrilleWeb** contrôler avec**dataSet11** en appelant son**DataBind** méthode.

{{% alert color="primary" %}}   {{% /alert %}}

##### **Exemple:**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

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

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

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

 Vous pouvez également vérifier le code ajouté à**Page_Load** gestionnaire d'événements comme indiqué ci-dessous dans la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**Chiffre:** Code ajouté à**Page_Load** gestionnaire d'événements

De loin, nous avons construit une application de base de données très utile. Mais, cette application vous permet uniquement de visualiser les données de la table. Bien que vous puissiez modifier les données dans**GrilleWeb** contrôle mais quand vous fermerez la fenêtre de votre navigateur et ouvrirez votre base de données. Vous constaterez que rien n'a changé. Cela signifie que les modifications que vous avez apportées ne sont pas enregistrées dans la base de données. Donc, il y a quelque chose que vous devez faire.

 Nous allons maintenant ajouter du code à notre application afin que**GrilleWeb** peut enregistrer ses modifications dans la base de données réelle. Ouvrons**Propriétés** volet et sélectionnez**Enregistrer la commande** événement de la**GrilleWeb** contrôle à partir de la liste de ses événements. Si vous double-cliquez sur**Enregistrer la commande** événement alors VS.NET 2005 IDE créera**GridWeb1_SaveCommand** gestionnaire d'événements pour vous. Ajoutez du code à ce gestionnaire d'événements pour mettre à jour la base de données avec les données modifiées contenues dans**Base de données** (lié à la feuille de travail) en utilisant**oleDbDataAdapter1**.

##### **Exemple:**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

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

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

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

 Vous pouvez également vérifier le code ajouté à**GridWeb1_SaveCommand** gestionnaire d'événements comme indiqué ci-dessous dans la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**Chiffre:** Code ajouté à**GridWeb1_SaveCommand** gestionnaire d'événements

 Maintenant, si vous enregistrez vos modifications dans la base de données en utilisant**sauvegarder** bouton de la**GrilleWeb** , ils seraient définitivement sauvés.

##### **Étape 8 : Lancer votre application**

 Enfin, nous pouvons compiler et exécuter notre application en appuyant sur**Ctrl+F5** ou en cliquant**Commencer** bouton. Dans la boîte de dialogue de débogage, vous pouvez spécifier l'option de débogage appropriée et cliquer sur**D'ACCORD** bouton comme indiqué ci-dessous dans la figure.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**Chiffre:** Application en cours d'exécution

 Après compilation,**Par défaut.aspx** La page de notre application Web s'ouvrira dans une nouvelle fenêtre de navigateur où nous pourrons voir toutes les données chargées à partir de la base de données, comme indiqué ci-dessous :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**Chiffre:** Données chargées dans**GrilleWeb** contrôle depuis la base de données

 Lorsque les données sont chargées dans**GrilleWeb** contrôle alors vous auriez l'impression que Aspose.Cells.GridWeb fournit un contrôle implicite des données à ses utilisateurs. Vérifions que le type de fonctionnalités de manipulation de données est proposé par**GrilleWeb** à ses utilisateurs.

##### **La validation des données**

Aspose.Cells.GridWeb crée automatiquement des règles de validation appropriées pour toutes les colonnes liées en fonction de leurs types de données définis dans la base de données. Vous pouvez voir le type de validation d'une cellule en passant le pointeur de la souris dessus, comme indiqué ci-dessous dans la figure :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**Chiffre:**Vérification du type de validation d'une cellule

 Dans la figure ci-dessus, nous pouvons voir que la cellule sélectionnée contient**\<INT>** type de validation, ce qui signifie que les utilisateurs ne peuvent saisir qu'une valeur entière, sinon une erreur de validation se produira. En outre,**\<OBLIGATOIRE>** montre que la valeur de**Identifiant du produit** doit être soumis par l'utilisateur.

##### **Suppression de lignes**

 Pour supprimer une ligne, vous devez d'abord sélectionner une ligne (ou n'importe quelle cellule de la ligne) et sélectionner**Supprimer la ligne** option dans le menu contextuel comme indiqué ci-dessous :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**Chiffre:** Sélection**Supprimer la ligne** option du menu

 Après avoir sélectionné**Supprimer la ligne** du menu, la ligne est supprimée du**GrilleWeb** . Cliquez maintenant**enregistrer** bouton de la**GrilleWeb** pour supprimer cet enregistrement dans la table de base de données d'origine.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**Chiffre:** Données de grille (après la suppression d'une ligne)

##### **Modification des lignes**

 Vous pouvez également modifier les données dans les cellules ou les lignes, puis cliquer sur**sauvegarder** bouton pour enregistrer vos modifications.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**Chiffre:** Données de grille (Modification de l'enregistrement 1)

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**Chiffre:** Données de la grille (Editing Record2)

##### **Ajout de lignes**

 Pour ajouter une ligne, sélectionnez**Ajouter une rangée** option dans le menu contextuel comme indiqué ci-dessous :

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**Chiffre:** Sélection**Ajouter une rangée** option du menu

Une nouvelle ligne sera ajoutée à la feuille à la fin des lignes après avoir sélectionné**Ajouter une rangée** option du menu. À gauche de la ligne nouvellement ajoutée, vous remarquerez un**astérisque** marque, indiquant que la ligne vient d'être ajoutée.

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**Chiffre:** Nouvelle ligne ajoutée à la grille

 Après avoir entré les valeurs dans la nouvelle ligne, cliquez sur**sauvegarder** bouton pour confirmer les modifications dans la table de base de données d'origine, comme indiqué ci-dessous

![tâche : image_autre_texte](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**Chiffre:** Enregistrement des modifications dans la table de base de données en cliquant sur**sauvegarder** bouton

{{% alert color="primary" %}}   {{% /alert %}}

##### **Conclusion**

{{% alert color="primary" %}}

**Liaison de données** est une fonctionnalité importante de Aspose.Cells.GridWeb . Il est vraiment facile pour les développeurs de lier leurs feuilles de calcul à la base de données en utilisant**Concepteur de feuilles de travail** utilitaire offert par Aspose.Cells.GridWeb . Aspose.Cells.GridWeb est très utile pour les développeurs pour économiser leur temps et leurs efforts dans la création de puissantes solutions de grille.

{{% /alert %}}
