##Read the values of the GridWeb cells on Client Side
## **Possible Usage Scenarios**
You can read the values of GridWeb cells on client side script using the gridwebinstance.getCellsArray() method. Once, you will call it, it will return the array of all the cells in active worksheet. You can then use the following methods to retrieve the value and other information of the cells.
- gridwebinstance.getCellName()
- gridwebinstance.getCellValueByCell()
- gridwebinstance.getCellRow()
- gridwebinstance.getCellColumn()
## **Read the values of the GridWeb cells on Client Side**
The following sample code retrieves all the cells and then prints their name, value, row and column. You can see its console output at the bottom of this article. The following screenshot shows the console output of the sample code on Google Chrome.
## **Screenshot**
![todo:image_alt_text](read-the-values-of-the-gridweb-cells-on-client-side_1.png)
## **Sample Code**
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
//Print GridWeb version on Console
System.out.println("Aspose.Cells.GridWeb for Java Version: " + GridWebBean.getVersion());
System.out.println(path);
System.out.println(basePath);
ExtPage BeanManager=ExtPage.getInstance();
GridWebBean gridweb=BeanManager.getBean(request);
out.println(gridweb.getHTMLHead());
%>
function ReadGridWebCells() {
// Access GridWeb instance and cells array
var gridwebins = gridwebinstance.get("<%=gridweb.get_ClientID()%>");
var cells = gridwebins.getCellsArray();
// Log cell name, values, row & column indexes in console
for (var j = 0; j < cells.length; j++)
{
var cellInfo = j + ":" + gridwebins.getCellName(cells[j]) + ",";
cellInfo += "value is:" + gridwebins.getCellValueByCell(cells[j]) + " ,";
cellInfo += "row:" + gridwebins.getCellRow(cells[j]) + ",";
cellInfo += "col:" + gridwebins.getCellColumn(cells[j]);
console.log(cellInfo);
}
}
gridweb.setReqRes(request, response);
gridweb.setEnableAJAX(true);
gridweb.setWidth(Unit.Pixel(600));
gridweb.setHeight(Unit.Pixel(400));
gridweb.prepareRender();
out.print(gridweb.getHTMLBody());
%>
## **Console Output**
This is the console output of the above sample code.
0:A1,value is:This ,row:0,col:0
1:B1,value is:is ,row:0,col:1
2:C1,value is:sample ,row:0,col:2
3:D1,value is:data ,row:0,col:3
4:E1,value is: ,row:0,col:4
5:F1,value is: ,row:0,col:5
6:G1,value is: ,row:0,col:6
7:H1,value is: ,row:0,col:7
8:A2,value is:This ,row:1,col:0
9:B2,value is:is ,row:1,col:1
10:C2,value is:sample ,row:1,col:2
11:D2,value is:data ,row:1,col:3
12:E2,value is: ,row:1,col:4
13:F2,value is: ,row:1,col:5
14:G2,value is: ,row:1,col:6
15:H2,value is: ,row:1,col:7
16:A3,value is:This ,row:2,col:0
17:B3,value is:is ,row:2,col:1
18:C3,value is:sample ,row:2,col:2
19:D3,value is:data ,row:2,col:3
20:E3,value is: ,row:2,col:4
21:F3,value is: ,row:2,col:5
22:G3,value is: ,row:2,col:6
23:H3,value is: ,row:2,col:7
24:A4,value is:This ,row:3,col:0
25:B4,value is:is ,row:3,col:1
26:C4,value is:sample ,row:3,col:2
27:D4,value is:data ,row:3,col:3
28:E4,value is: ,row:3,col:4
29:F4,value is: ,row:3,col:5
30:G4,value is: ,row:3,col:6
31:H4,value is: ,row:3,col:7
32:A5,value is:This ,row:4,col:0
33:B5,value is:is ,row:4,col:1
34:C5,value is:sample ,row:4,col:2
35:D5,value is:data ,row:4,col:3
36:E5,value is: ,row:4,col:4
37:F5,value is: ,row:4,col:5
38:G5,value is: ,row:4,col:6
39:H5,value is: ,row:4,col:7
40:A6,value is: ,row:5,col:0
