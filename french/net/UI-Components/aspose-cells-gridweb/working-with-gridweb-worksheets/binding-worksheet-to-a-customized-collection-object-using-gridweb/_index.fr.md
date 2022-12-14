---
title: Liaison de feuille de calcul à un objet de collection personnalisé à l'aide de GridWeb
type: docs
weight: 130
url: /fr/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Le framework Microsoft .NET propose de nombreuses classes de collection, mais parfois elles ne répondent pas aux exigences de développement, de sorte que les développeurs créent**collections personnalisées**, et peut nécessiter de lier ces collections personnalisées avec Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Liaison d'une feuille de calcul avec une collection personnalisée**
Pour illustrer cette fonctionnalité, cet article explique comment créer un exemple d'application, étape par étape. Tout d'abord, créez une collection personnalisée, puis utilisez cette collection pour la liaison avec une feuille de calcul.
### **Étape 1 : Créer un enregistrement personnalisé**
Avant de créer une collection personnalisée, créez une classe pour contenir les enregistrements personnalisés qui seront stockés dans la collection. Le but de cet article est de donner une idée de la façon de créer vos propres collections personnalisées et de les lier avec Aspose.Cells.GridWeb, donc la façon dont vous créez l'enregistrement personnalisé dépend de vous.

L'exemple ci-dessous utilise la classe MyCustomRecord qui contient cinq champs privés et cinq propriétés publiques qui contrôlent l'accès aux champs privés. Voici la structure des propriétés :

-  La propriété StringField1 pour lire et écrire**champ de chaîne1** (chaîne de caractères).
-  La propriété ReadonlyField2 pour lire uniquement**champ de chaîne2** (chaîne de caractères).
-  La propriété DateField1 pour lire et écrire**datefield1** (DateHeure).
-  La propriété IntField1 pour lire et écrire**intfield1** (entier).
-  La propriété DoubleField1 pour lire et écrire**champ double1** (double).

**C#**

{{< highlight "csharp" >}}

 //Creating a class that will act as record for the custom collection

public class MyCustomRecord

{

    //Private data members

    private string stringfield1;

    private string stringfield2 = "ABC";

    private DateTime datefield1;

    private int intfield1;

    private double doublefield1;

    //Creating a string property

    public string StringField1

    {

        get { return stringfield1; }

        set { stringfield1 = value; }

    }

    //Creating a readonly string property

    public string ReadonlyField2

    {

        get { return stringfield2; }

    }

    //Creating a DateTime property

    public DateTime DateField1

    {

        get { return datefield1; }

        set { datefield1 = value; }

    }

    //Creating an int property

    public int IntField1

    {

        get { return intfield1; }

        set { intfield1 = value; }

    }

    //Creating a double property

    public double DoubleField1

    {

        get { return doublefield1; }

        set { doublefield1 = value; }

    }

}

{{< /highlight >}}
### **Étape 2 : Création d'une collection personnalisée**
Maintenant, créez une collection personnalisée pour y ajouter des enregistrements de clients et y accéder. Pour faire simple, cet exemple utilise la classe MyCollection qui contient un indexeur en lecture seule. En utilisant cet indexeur, nous pouvons obtenir n'importe quel enregistrement personnalisé stocké dans la collection.

**C#**

{{< highlight "csharp" >}}

 //Creating a custom collection

public class MyCollection : CollectionBase

{

    //Leaving the collection constructor empty

    public MyCollection()

    {

    }

    //Creating a readonly property for custom collection. This Item property is used by GridWeb control to

    //determine the collection's type

    public MyCustomRecord this[int index]

    {

        get { return (MyCustomRecord)this.List[index]; }

    }

}

{{< /highlight >}}
### **Étape 3 : Relier une feuille de calcul avec une collection personnalisée**
Le processus de création d'une collection personnalisée est terminé. Utilisez maintenant la collection personnalisée pour établir une liaison avec une feuille de calcul dans Aspose.Cells.GridWeb . Créez d'abord un formulaire Web, ajoutez-y le contrôle GridWeb et ajoutez du code.

Pour utiliser la collection personnalisée pour la liaison, créez d'abord un objet de la classe MyCollection (créé à l'étape ci-dessus).
Créez et ajoutez ensuite des objets MyCustomRecord à l'objet MyCollection.

{{% alert color="primary" %}} 

Vous vous demandez pourquoi il n'y avait pas de méthode dans la classe MyCollection pour ajouter un objet MyCustomRecord à la collection. Jetez un autre coup d'œil au code ci-dessus et vous remarquerez que la classe MyCollection est héritée de la classe CollectionBase (qui a implémenté l'interface IList qui fournit une méthode Add pour ajouter un objet à la collection). Utilisez la méthode Add de la classe IList en convertissant l'objet MyCollection en IList.

{{% /alert %}} 

Enfin, définissez l'objet MyCollection comme source de données de la feuille de calcul et liez la feuille de calcul à la collection. À ce stade, vous pouvez également créer des règles de validation pour les colonnes liées de la feuille de calcul.

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

    {

        //Creating an object of custom collection

        MyCollection list = new MyCollection();

        //Creating an instance of Random class

        System.Random rand = new System.Random();

        //Creating a loop that will run 5 times

        for (int i = 0; i < 5; i++)

        {

            //Creating an object of Custom Record

            MyCustomRecord rec = new MyCustomRecord();

            //Initializing all properties of Custom Record

            rec.DateField1 = DateTime.Now;

            rec.DoubleField1 = rand.NextDouble() * 10;

            rec.IntField1 = rand.Next(20);

            rec.StringField1 = "ABC_" + i;

            //Adding Custom Record to Collection

            ((IList)list).Add(rec);

        }

        //Accessing a desired worksheet

        GridWorksheet sheet = GridWeb1.WorkSheets[0];

        //Setting the Data Source of worksheet

        sheet.DataSource = list;

        //Creating columns automatically

        sheet.CreateAutoGenratedColumns();

        //Setting the validation type of value to DateTime

        sheet.BindColumns[2].Validation.ValidationType = ValidationType.DateTime;

        //Binding worksheet

        sheet.DataBind();

        //Assigning an event handler to InitializeNewBindRow event of the worksheet

        //sheet.InitializeNewBindRow += new InitializeNewBindRowHandler(GridWeb1_InitializeNewBindRow);

    }

}

{{< /highlight >}}
### **Étape 4 : Gestion de l'événement InitializeNewBindRow de la feuille de calcul**
Dans le code ci-dessus, vous avez peut-être remarqué une ligne de code supplémentaire utilisée pour affecter le gestionnaire d'événements GridWeb1_InitializeNewBindRow au InitializeNewBindRow de la feuille de calcul. Cet événement est déclenché chaque fois qu'une nouvelle ligne liée est ajoutée à la feuille de calcul. Nous avons créé un gestionnaire d'événements pour cet événement en raison de la propriété DateField1 de l'objet MyCustomRecord.

 Aspose.Cells.GridWeb s'initialise automatiquement**entier** et**double** valeurs avec**zéro (0)**chaque fois qu'une nouvelle ligne liée est ajoutée au contrôle GridWeb. Pour les dates, nous aimerions que le contrôle GridWeb ajoute automatiquement la date actuelle du système. Pour ce faire, nous avons créé le gestionnaire d'événements GridWeb1_InitializeNewBindRow pour l'événement InitializeNewBindRow.

Accédez à une instance particulière de la classe MyCustomRecord à partir de GridWeb à l'aide de l'argument bindObject, puis affectez la date système actuelle à sa propriété DateField1.

**C#**

{{< highlight "csharp" >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **Étape 5 : Exécution de l'application**
 Exécutez l'application en appuyant sur**Ctrl+F5** ou en cliquant sur le**Commencer** bouton dans VS.NET. Le formulaire Web s'ouvre dans une nouvelle fenêtre de navigateur.

**Feuille de calcul liée à une collection personnalisée** 

![tâche : image_autre_texte](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Cliquez avec le bouton droit sur le contrôle GridWeb pour ajouter ou supprimer un enregistrement. Par exemple, ajoutez un nouvel enregistrement à la feuille de calcul en sélectionnant**Ajouter une rangée** option.

**Sélection de l'option Ajouter une ligne dans le menu** 

![tâche : image_autre_texte](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 Lorsqu'une nouvelle ligne est ajoutée à la feuille de calcul, les cellules contiennent des données par défaut, y compris la date système actuelle.

**Nouvelle ligne ajoutée à la feuille de calcul avec les données par défaut** 

![tâche : image_autre_texte](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Après avoir modifié les données, cliquez sur**sauvegarder** ou**Soumettre** pour enregistrer vos modifications.

**Enregistrement des modifications en cliquant sur le bouton Enregistrer** 

![tâche : image_autre_texte](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Conclusion**
{{% alert color="primary" %}} 

Cet article a montré comment lier une feuille de calcul à une collection personnalisée créée. À l'aide de Aspose.Cells.GridWeb, les développeurs peuvent lier des feuilles de calcul à une base de données ou à des collections personnalisées via le concepteur de feuilles de calcul en mode graphique ou par codage. Cela offre un large éventail d'options aux développeurs pour créer des applications.

{{% /alert %}}
