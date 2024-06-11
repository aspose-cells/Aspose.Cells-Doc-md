---
title: 在运行时将工作表绑定到 DataSet 使用 GridWeb
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset/
keywords: GridWeb,bind,DataSet
description: 本文介绍如何在 GridWeb 中将工作表绑定到 DataSet。
---

## **可能的使用场景**
Aspose.Cells.GridWeb 提供了一个易于使用的 API，可用于动态地将 DataSet 绑定到工作表。
## **将工作表绑定到 DataSet**
以下示例代码解释了如何在运行时将工作表绑定到 DataSet。
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
## **输出截图**
下面的截图显示了在执行上述示例代码后的 GridWeb。

![todo:image_alt_text](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
