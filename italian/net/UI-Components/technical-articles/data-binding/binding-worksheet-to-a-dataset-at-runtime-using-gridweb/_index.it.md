---
title: Associazione del foglio di lavoro a un set di dati in fase di esecuzione tramite GridWeb
type: docs
weight: 70
url: /it/net/binding-worksheet-to-a-dataset-at-runtime-using-gridweb/
---
## **Possibili scenari di utilizzo**
Aspose.Cells.GridWeb fornisce una semplice API che può essere utilizzata per associare dinamicamente un DataSet a un foglio di lavoro.
## **Associazione di un foglio di lavoro a DataSet**
Il codice di esempio seguente illustra come associare un foglio di lavoro a un DataSet in fase di esecuzione.
## **Codice di esempio**
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
## **Schermata di uscita**
Lo screenshot seguente mostra GridWeb dopo l'esecuzione del codice di esempio precedente.

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
