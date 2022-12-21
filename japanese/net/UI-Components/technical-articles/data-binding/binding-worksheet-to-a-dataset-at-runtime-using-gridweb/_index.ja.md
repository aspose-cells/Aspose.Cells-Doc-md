---
title: GridWeb を使用して実行時にワークシートを DataSet にバインドする
type: docs
weight: 70
url: /ja/net/binding-worksheet-to-a-dataset-at-runtime-using-gridweb/
---
## **考えられる使用シナリオ**
Aspose.Cells.GridWeb は、DataSet をワークシートに動的にバインドするために使用できる簡単な API を提供します。
## **ワークシートを DataSet にバインドする**
次のサンプル コードは、実行時に Worksheet を DataSet にバインドする方法を説明しています。
## **サンプルコード**
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
## **出力スクリーンショット**
次のスクリーンショットは、上記のサンプル コードを実行した後の GridWeb を示しています。

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
