---
title: Liaison de feuille de calcul à un ensemble de données lors de l'exécution à l'aide de GridWeb
type: docs
weight: 70
url: /fr/net/binding-worksheet-to-a-dataset-at-runtime-using-gridweb/
---
## **Scénarios d'utilisation possibles**
Aspose.Cells.GridWeb fournit un API simple qui peut être utilisé pour lier dynamiquement un DataSet à une feuille de travail.
## **Liaison d'une feuille de calcul à DataSet**
L'exemple de code suivant explique comment lier une feuille de calcul à un DataSet au moment de l'exécution.
## **Exemple de code**
{{< highlight "java" >}}

 // Implementing Page_Load event handler

public partial class GridBind : System.Web.UI.Page

{

    protected void Page_Load(object sender, EventArgs e)

    {

        if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

        {

            // Create Product Data Table

            DataTable prodTbl = new DataTable("Products");

            prodTbl.Columns.Add("ProductID");

            prodTbl.Columns.Add("ProductName");

            prodTbl.Columns.Add("ProductPrice");

            // Add products inside the data table

            prodTbl.Rows.Add(1, "Grape Juice", "$30.00");

            prodTbl.Rows.Add(3, "Mineral Water", "$25.00");

            prodTbl.Rows.Add(6, "Olive Oil", "$50.00");

            prodTbl.Rows.Add(4, "Chocolate", "$10.00");

            prodTbl.Rows.Add(7, "Oranges", "$28.00");

            // Create a DataSet and put both table in it.

            DataSet set = new DataSet();

            set.Tables.Add(prodTbl);

            // Accessing a desired worksheet

            GridWorksheet sheet = GridWeb1.WorkSheets[0];

            // Specifying Data Source for the worksheet

            sheet.DataSource = set;

            // Specifying Products tables as the DataMember

            sheet.DataMember = "Products";

            // Creating data bound columns automatically

            sheet.CreateAutoGenratedColumns();

            // Binding worksheet with DataSet

            sheet.DataBind();

        }

    }

}

{{< /highlight >}}
## **Capture d'écran de sortie**
La capture d'écran suivante montre le GridWeb après l'exécution de l'exemple de code ci-dessus.

![tâche : image_autre_texte](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
