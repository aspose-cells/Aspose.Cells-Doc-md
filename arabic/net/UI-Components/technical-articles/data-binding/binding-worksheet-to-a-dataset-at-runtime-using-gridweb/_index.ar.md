---
title: ورقة عمل ملزمة لمجموعة DataSet في وقت التشغيل باستخدام GridWeb
type: docs
weight: 70
url: /ar/net/binding-worksheet-to-a-dataset-at-runtime-using-gridweb/
---
## **سيناريوهات الاستخدام الممكنة**
Aspose.Cells.GridWeb يوفر API سهلًا يمكن استخدامه لربط DataSet بورقة العمل ديناميكيًا.
## **ربط ورقة عمل إلى DataSet**
يشرح نموذج التعليمات البرمجية التالي كيفية ربط ورقة عمل إلى DataSet في وقت التشغيل.
## **عينة من الرموز**
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
## **لقطة شاشة الإخراج**
تُظهر لقطة الشاشة التالية GridWeb بعد تنفيذ نموذج التعليمات البرمجية أعلاه.

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-at-runtime-using-gridweb_1.png)
