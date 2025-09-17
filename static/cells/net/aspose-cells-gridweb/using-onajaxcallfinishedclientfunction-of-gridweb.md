##Using OnAjaxCallFinishedClientFunction of GridWeb
This article introduces how to work with OnAjaxCallFinishedClientFunction  in GridWeb.
## **Possible Usage Scenarios**
OnAjaxCallFinishedClientFunction is a client side function which is called when user copies some data to GridWeb worksheet. This function is helpful when bulk of cells are updated and you want to keep the track of those updated cells at client side (i.e. in web browsers like FireFox, Google Chrome etc.).
## **Using OnAjaxCallFinishedClientFunction of GridWeb**
The following sample code explains how to make use of OnAjaxCallFinishedClientFunction client function. The screenshots show the console output in Google Chrome and FireFox when the code is executed. Once, you execute the code, please copy/paste some data spanning multiple cells inside the GridWeb worksheet and then check the Web Browser Console as shown in screenshots.
## **Google Chrome Console Output**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox Console Output**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Sample Code**
//-------------------------------------------------------
//------TestGridWeb.aspx---------------------------------
//-------------------------------------------------------
//
var updateCells = new Array();
function TestAjaxCallFinish()
{
for (var i = 0; i < updateCells.length; i++) {
console.log("updated:" + toString(this,updateCells[i]));
}
updateCells = [];
}
function CellUpdate(cell) {
var id = updateCells.length;
updateCells[id++] = cell;
}
function toString(gridweb,cell) {
return gridweb.getCellName(cell) +
",value is:" +
gridweb.getCellValueByCell(cell) +
" ,row:" +
gridweb.getCellRow(cell) +
",col:" +
gridweb.getCellColumn(cell);
}
//-------------------------------------------------------
//------TestGridWeb.aspx.cs------------------------------
//-------------------------------------------------------
//
using System;
using System.Web.UI;
using Aspose.Cells.GridWeb;
public partial class TestGridWeb : System.Web.UI.Page
{
protected void Page_Load(object sender, EventArgs e)
{
if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)
{
lblVersion.Text = GridWeb.GetVersion();
}
}
}
