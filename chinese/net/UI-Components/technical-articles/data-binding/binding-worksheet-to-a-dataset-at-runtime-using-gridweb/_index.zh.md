---
title: 在运行时使用GridWeb将工作表与DataSet绑定
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset/
keywords: GridWeb，bind，DataSet
description: 本文介绍了如何在GridWeb中将工作表绑定到DataSet。
---

## **可能的使用场景**
Aspose.Cells.GridWeb提供了一个简单的API，可用于动态地将DataSet绑定到工作表。
## **将工作表绑定到DataSet**
下面的示例代码解释了如何在运行时将工作表绑定到DataSet。
## **示例代码**
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
## **输出屏幕截图**
下面的屏幕截图显示了在执行上述示例代码后的GridWeb。

![todo:image_alt_text](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
