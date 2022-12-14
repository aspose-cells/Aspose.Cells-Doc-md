---
title: Création d'une feuille de vue hiérarchique
type: docs
weight: 30
url: /fr/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 La liaison de données est une fonctionnalité GridWeb puissante et conviviale. Les données stockées dans les tables de base de données sont récupérées dans un DataSet et remplies de données

 représentant les tables de données. À l'aide de la fonction de liaison de données, vous pouvez créer une vue hiérarchique (une vue maître-enfant) des données interconnectées et

 l'afficher dans le champ pour le rendre plus élégant.

 Cette rubrique traite de la création d'une feuille de vue hiérarchique. Certaines lignes de la feuille ont des vues enfant. Lorsqu'un utilisateur clique sur la ligne**Développer**

 bouton{{< emoticons/cross >}} , la table de vue enfant de cette ligne est développée vers le bas. Cette fonctionnalité est très utile pour créer un rapport de vue hiérarchique.

**Un tableau avec une vue hiérarchique** 

![tâche : image_autre_texte](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Créer des relations pour les tables de données**
Par exemple, vous utilisez ADO.Net API et extrayez des données des tables de la base de données. Pour créer une feuille de vue hiérarchique, vous devez concevoir un DataSet

 objet basé sur certaines tables et créez d'abord une relation entre elles. Utilisez les VS.NET**Concepteur d'ensembles de données** pour créer la relation. Dans

 cet exemple, il y a trois DataTables : Customers, Orders, Order Details. La feuille affiche toutes les informations du client par défaut. Lorsque

 l'utilisateur développe un client, la grille affiche toutes les commandes passées par ce client. Lorsque l'utilisateur développe une commande, la grille affiche les détails

de cet ordre. Les données sont hiérarchiques : les détails des commandes sont répertoriés sous les commandes et les commandes sont répertoriées sous les clients.

Pour que cela fonctionne, les relations suivantes doivent être établies entre les tables de données :

1.  Créez une clé étrangère sur DataTable Orders, le champ clé est CustomerID

![tâche : image_autre_texte](creating-hierarchical-view-sheet_2.png)




1. Créez une clé étrangère sur DataTable Order Details, le champ clé est OrderID.

![tâche : image_autre_texte](creating-hierarchical-view-sheet_3.png)



 Le DataSet Designer ressemble maintenant à ceci :

![tâche : image_autre_texte](creating-hierarchical-view-sheet_4.png)
### **Relier la feuille de travail**
 Utilisez maintenant le**Concepteur de feuilles de travail** pour définir DataSource et DataMember pour la feuille de calcul et configurer les colonnes de liaison de champ de données.

 Le contrôle ajoute automatiquement une icône + pour chaque ligne correspondant à un enregistrement dont l'objet de liaison (généralement un objet DataRowView) a

 vues d'enfants. Lorsque vous cliquez sur l'icône +, l'enregistrement se développe pour afficher la vue enfant. L'exemple ci-dessous utilise le**Concepteur de feuilles de travail** lier le

 feuille de calcul au parent racine DataTable Customers.

![tâche : image_autre_texte](creating-hierarchical-view-sheet_5.png)
### **Personnaliser les colonnes de liaison des tables enfants**
 Le contrôle fournit un événement nommé GridWeb.BindingChildView que les développeurs utilisent pour personnaliser les colonnes de liaison des tables enfants. Cet exemple

 doit afficher les détails de la commande'**Prix unitaire** champ dans un format monétaire. Ajoutez un gestionnaire d'événements pour modifier le format numérique de la colonne de liaison.

**C#**

{{< highlight "csharp" >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Charger des données à partir de la base de données et de la liaison**
Comme décrit dans[Liaison d'une feuille de calcul à un ensemble de données à l'aide du concepteur de feuilles de calcul de GridWeb](/cells/fr/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 vous devez ajouter du code au bloc Page_Load pour charger des données dans le DataSet à partir d'une base de données et lier le DataSet à la feuille dans le

 L'étape suivante.

La classe Asppose.Grid.Web.Data.WebWorksheet possède des propriétés utiles.

- Par exemple, la propriété EnableCreateBindColumnHeader est utilisée pour créer les en-têtes de la colonne liée dans la feuille, ou la colonne

 headers affiche les noms des colonnes liées. Il prend les valeurs**vrai** ou**faux**. 

- Les propriétés BindStartRow et BindStartColumn spécifient la position dans la feuille du contrôle GridWeb auquel la source doit être liée.
- La propriété EnableExpandChildView est utilisée pour désactiver la vue enfant développée pour la feuille de calcul. Par défaut, il est défini sur vrai.

 La classe a aussi quelques méthodes utiles.

- La méthode DataBind() lie une feuille à la source.
- Le CreateNewBindRow() ajoute une nouvelle ligne et la lie à la source de données.
- Le DeleteBindRow() supprime une ligne liée.
- La méthode SetRowExpand() définit la ligne développée et affiche le contenu de la vue enfant en mode de liaison de données.
- La méthode GetRowExpand() obtient une valeur booléenne qui indique si la ligne est développée ou non.

 Dans le code ci-dessous, l'objet DataSet "dataSet21" est rempli de données basées sur trois tables. La table Clients est filtrée pour en faire la

 premier tableau de l'affichage hiérarchique. Un objet WebWorksheet nommé "feuille" est créé, qui efface d'abord la feuille, puis la définit

 lié à la source de données.

**C#**

{{< highlight "csharp" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Gère MyBase.Load

 'Mettre le code utilisateur pour initialiser la page ici

 Sinon IsPostBack Then

 BindWithoutInSheetHeaders()

 Fin si

Sous-titre de fin

Privé Sub BindWithoutInSheetHeaders()

 Dim db As DemoDatabase2 = New DemoDatabase2()

Dim path As String = MapPath(".")

 chemin = chemin.Substring(0, chemin.LastIndexOf("\"))

 chemin = chemin.Substring(0, chemin.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

 Essayer

 ' Se connecte à la base de données et récupère les données.

 ' Tableau des clients.

 db.OleDbDataAdapter1.Fill(DataSet21)

 ' Tableau des commandes.

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' Tableau des détails de la commande.

 db.OleDbDataAdapter3.Fill(DataSet21)

 ' Filtrer les données

 DataSet21.Customers.DefaultView.RowFilter = "ID client<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
