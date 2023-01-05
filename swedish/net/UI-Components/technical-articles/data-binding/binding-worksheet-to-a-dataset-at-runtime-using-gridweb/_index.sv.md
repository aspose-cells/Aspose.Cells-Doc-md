---
title: Bindande arbetsblad till en datauppsättning vid körning med GridWeb
type: docs
weight: 70
url: /sv/net/binding-worksheet-to-a-dataset-at-runtime-using-gridweb/
---
## **Möjliga användningsscenarier**
Aspose.Cells.GridWeb tillhandahåller ett enkelt API som kan användas för att dynamiskt binda en datamängd till arbetsblad.
## **Bindning av ett kalkylblad till datauppsättning**
Följande exempelkod förklarar hur man binder ett kalkylblad till en datauppsättning vid körning.
## **Exempelkod**
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
## **Utdata skärmdump**
Följande skärmdump visar GridWeb efter exekveringen av ovanstående exempelkod.

![todo:image_alt_text](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
