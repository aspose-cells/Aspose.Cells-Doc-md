---
title: GridWeb de Çalışma Zamanında Bir DataSet e Çalışsheet Bağlama
type: docs
weight: 70
url: /tr/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset/
keywords: GridWeb,bind,DataSet
description: Bu makale, GridWeb de bir Veri Setini Çalışma Zamanında Çalış Sayfasına nasıl bağlayacağınızı tanıtır.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells.GridWeb, Veri Setini Dinamik olarak Çalış Sayfasına bağlamak için kullanılabilecek basit bir API sağlar.
## **Çalış Sayfasını Veri Setine Bağlama**
Aşağıdaki örnek kod, bir Çalış Sayfasını Çalışma Zamanında Veri Setine bağlamanın nasıl yapıldığını açıklar.
## **Örnek Kod**
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
## **Çıktı Ekran Görüntüsü**
Aşağıdaki ekran görüntüsü, yukarıdaki örnek kodun çalıştırılmasından sonra GridWeb'i göstermektedir.

![todo:image_alt_text](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
