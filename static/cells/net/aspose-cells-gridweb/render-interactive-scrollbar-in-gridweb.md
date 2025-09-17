##Render Interactive Scrollbar in GridWeb
This article introduces how to work with scrollbar in GridWeb.
## **Possible Usage Scenarios**
Aspose.Cells for GridWeb can render interactive scroll bar control inside the GridWeb worksheet. User can interact with the scroll bar like they do in Microsoft Excel. In order to create interactive scroll bar, you must add the links for **jQuery** and **jQuery UI** libraries as shown below.
## **Render Interactive Scrollbar in GridWeb**
The following sample code loads the [sample Excel file](61767764.xlsx) containing the scroll bar as shown in the following screenshot. The other screenshots show how the GridWeb renders interactive scroll bar and displays the value of scroll bar in cell B3. Whenever you scroll the scroll bar, the value of cell B3 shows the resulting value.
![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_1.png)
![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_2.png)
![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_3.png)
![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_4.png)
## **Sample Code**
\--------------------------------------------
\--------------------------------------------
\--------------------------------------------
using System;
using System.Collections;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Xml.Linq;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.GridWeb.Data;
using Aspose.Cells.GridWeb;
using System.Globalization;
using System.Threading;
using System.Collections.Generic;
public partial class TestGridWeb : System.Web.UI.Page
{
protected void Page_Load(object sender, EventArgs e)
{
if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)
{
lblVersion.Text = GridWeb.GetVersion();
string fileName = "sampleRenderScrollbarInGridWeb.xlsx";
string filePath = Server.MapPath("~/ExcelFile/" + fileName);
GridWeb1.ImportExcelFile(filePath);
}
}
}
