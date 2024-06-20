---
title: Créer une vue hiérarchique de la feuille
type: docs
weight: 30
url: /fr/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb, hiérarchique
description: Cet article présente comment créer une vue hiérarchique dans GridWeb.
---

{{% alert color="primary" %}} 

La liaison de données est une fonctionnalité puissante et conviviale de GridWeb. Les données stockées dans les tables de base de données sont récupérées dans un DataSet et remplies de données représentant les tables de données. En utilisant la fonctionnalité de liaison de données, vous pouvez créer une vue hiérarchique (une vue maître-enfant) de données interconnectées et l'afficher dans le contrôle pour la rendre plus élégante. 

représentant les tables de données. En utilisant la fonctionnalité de liaison des données, vous pouvez créer une vue hiérarchique (une vue maître-enfant) de données interconnectées et 

Cet article discute de la création d'une vue hiérarchique de la feuille. Certaines lignes de la feuille possèdent des vues enfants. Lorsqu'un utilisateur clique sur **Étendre** la ligne 

Ce sujet traite de la création d'une vue hiérarchique de feuille. Certaines des lignes de la feuille possèdent des vues enfant. Lorsqu'un utilisateur clique sur l'**Étendre** de la ligne

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**Une table avec une vue hiérarchique** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Créer des relations pour les DataTables**
Par exemple, vous utilisez l'API ADO.Net et extrayez des données des tables de la base de données. Pour créer une feuille de vue hiérarchique, vous devez concevoir un DataSet

objet basé sur certaines tables et créer une relation entre elles en premier lieu. Utilisez le **Concepteur de DataSet** de VS.NET pour créer la relation. Dans 

cet exemple, il y a trois DataTables : Clients, Commandes, Détails de commande. La feuille affiche toutes les informations client par défaut. Lorsque 

l'utilisateur développe un client, la grille montre toutes les commandes que ce client a passées. Lorsque l'utilisateur développe une commande, la grille montre les détails 

de cette commande. Les données sont hiérarchiques : les détails de commande sont répertoriés sous les commandes, et les commandes sont répertoriées sous les clients.

Pour que cela fonctionne, les relations suivantes doivent être établies entre les tables de données:

1. Créer une clé étrangère sur DataTable Orders, le champ clé est CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Créer une clé étrangère sur DataTable Order Details, le champ clé est OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



Le Concepteur de DataSet ressemble maintenant à ceci: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Lier la feuille de travail**
Utilisez maintenant le **Concepteur de feuilles de travail** pour définir la source de données et le membre de données pour la feuille, et configurer les colonnes de liaison de champ de donnée. 

Le contrôle ajoute automatiquement une icône + pour chaque ligne correspondant à un enregistrement dont l'objet de liaison (généralement un objet DataRowView) a 

des vues filles. Lorsque l'icône + est cliquée, l'enregistrement s'étend pour afficher la vue enfant. L'exemple ci-dessous utilise le **Concepteur de feuilles de travail** pour lier la 

feuille de travail à la table de données parent Customers. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Personnaliser les Colonnnes de Liaison des Tables Enfants**
Le contrôle fournit un événement appelé GridWeb.BindingChildView que les développeurs utilisent pour personnaliser les colonnes de liaison des tables enfants. Cet exemple 

doit afficher le champ **PrixUnitaire** des détails de commande au format de devise. Ajoutez un gestionnaire d'événement pour changer le format de nombre de la colonne de liaison. 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Charger des données à partir de la base de données et liaison**
Comme décrit dans [Liaison de la feuille de calcul à un jeu de données à l'aide du concepteur de feuilles de calcul de GridWeb](/cells/fr/net/liaison-feuille-de-calcul-jeu-de-donnees-concepteur-gridwebs-feuilles-de-calcul/),
vous devez ajouter du code au bloc Page_Load pour charger des données dans le jeu de données à partir d'une base de données, et lier le jeu de données à la feuille dans la 

prochaine étape. 

La classe Asppose.Grid.Web.Data.WebWorksheet a certaines propriétés utiles.

- Par exemple, la propriété EnableCreateBindColumnHeader est utilisée pour créer les en-têtes de la colonne liée dans la feuille, ou la colonne

headers affiche les noms des colonnes liées. Elle prend les valeurs **true** ou **false**. 

- Les propriétés BindStartRow et BindStartColumn spécifient la position dans la feuille du contrôle GridWeb auquel la source doit être liée.
- La propriété EnableExpandChildView est utilisée pour désactiver la vue enfant étendue pour la feuille. Par défaut, elle est définie sur true.

La classe a aussi quelques méthodes utiles. 

- La méthode DataBind() lie une feuille à la source.
- La méthode CreateNewBindRow() ajoute une nouvelle ligne et la lie à la source de données.
- La méthode DeleteBindRow() supprime une ligne liée.
- La méthode SetRowExpand() définit la ligne étendue et affiche le contenu de la vue enfant en mode de liaison de données.
- La méthode GetRowExpand() obtient une valeur booléenne qui indique si la ligne est étendue ou non.

Dans le code ci-dessous, l'objet DataSet "dataSet21" est rempli de données basées sur trois tables. La table Customers est filtrée pour en faire la 

première table dans l'affichage hiérarchique. Un objet WebWorksheet nommé "feuille" est créé, qui efface d'abord la feuille puis la lie 

au source de données. 

**C#**

{{< highlight csharp >}}

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

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

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

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

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
