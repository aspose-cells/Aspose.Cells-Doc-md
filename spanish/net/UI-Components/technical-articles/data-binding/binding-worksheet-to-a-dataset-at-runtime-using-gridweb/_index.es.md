---
title: Enlace de la hoja de trabajo a un conjunto de datos en tiempo de ejecución usando GridWeb
type: docs
weight: 70
url: /es/net/binding-worksheet-to-a-dataset-at-runtime-using-gridweb/
---
## **Posibles escenarios de uso**
Aspose.Cells.GridWeb proporciona un API sencillo que se puede usar para vincular dinámicamente un conjunto de datos a una hoja de trabajo.
## **Vincular una hoja de trabajo a un conjunto de datos**
El siguiente código de ejemplo explica cómo vincular una hoja de trabajo a un conjunto de datos en tiempo de ejecución.
## **Código de muestra**
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
## **Captura de pantalla de salida**
La siguiente captura de pantalla muestra GridWeb después de la ejecución del código de ejemplo anterior.

![todo:imagen_alternativa_texto](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
