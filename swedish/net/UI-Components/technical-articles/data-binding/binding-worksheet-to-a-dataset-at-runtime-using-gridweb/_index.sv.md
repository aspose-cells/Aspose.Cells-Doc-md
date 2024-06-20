---
title: Bindning av arbetsblad till en DataSet vid körning med hjälp av GridWeb
type: docs
weight: 70
url: /sv/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset/
keywords: GridWeb,bind,DataSet
description: Den här artikeln introducerar hur man binder arbetsblad till en DataSet i GridWeb.
---

## **Möjliga användningsscenario**
Aspose.Cells.GridWeb tillhandahåller en enkel API som kan användas för att dynamiskt binda en DataSet till arbetsblad.
## **Bind ett arbetsblad till DataSet**
Följande exemplarkod förklarar hur man binder ett arbetsblad till en DataSet vid körning.
## **Exempelkod**
{{< highlight java >}}

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
## **Utmatningsskärmbild**
Följande skärmbild visar GridWeb efter utförandet av ovanstående exemplarkod.

![todo:image_alt_text](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
