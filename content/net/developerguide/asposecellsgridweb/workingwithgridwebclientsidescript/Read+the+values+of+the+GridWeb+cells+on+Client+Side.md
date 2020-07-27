+++
title = "Read the values of the GridWeb cells on Client Side" 
description = "" 
weight = 16680 
+++

Aspose.Cells for .NET : Read the values of the GridWeb cells on Client Side  

# Aspose.Cells for .NET : Read the values of the GridWeb cells on Client Side


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#ReadthevaluesoftheGridWebcellsonClientSide-PossibleUsageScenarios)
*   2 [Read the values of the GridWeb cells on Client Side](#ReadthevaluesoftheGridWebcellsonClientSide-ReadthevaluesoftheGridWebcellsonClientSide)
*   3 [Screenshot](#ReadthevaluesoftheGridWebcellsonClientSide-Screenshot)
*   4 [Sample Code](#ReadthevaluesoftheGridWebcellsonClientSide-SampleCode)
*   5 [Console Output](#ReadthevaluesoftheGridWebcellsonClientSide-ConsoleOutput)
{{< /panel >}}
 

 

## Possible Usage Scenarios

You can read the values of GridWeb cells on client side script using the `gridwebinstance.getCellsArray()` method. Once, you will call it, it will return the array of all the cells in active worksheet. You can then use the following methods to retrieve the value and other information of the cells.

*   `gridwebinstance.getCellName()`
*   `gridwebinstance.getCellValueByCell()`
*   `gridwebinstance.getCellRow()`
*   `gridwebinstance.getCellColumn()`

## Read the values of the GridWeb cells on Client Side

The following sample code retrieves all the cells and then prints their name, value, row and column. You can see its console output at the bottom of this article. The following screenshot shows the console output of the sample code on Google Chrome.

## Screenshot

![](https://docs2.aspose.com/cells/net/attachments/5013765/5115360.png)

## Sample Code

  

Please call the JavaScript function `ReadGridWebCells()` as shown in the above sample code like this.

  

## Console Output

This is the console output of the above sample code.

{{< code lang="cs" >}}
0:A1,value is:0 ,row:0,col:0
1:B1,value is:4 ,row:0,col:1
2:C1,value is:1 ,row:0,col:2
3:D1,value is:1 ,row:0,col:3
4:E1,value is:2 ,row:0,col:4
5:F1,value is:6 ,row:0,col:5
6:G1,value is:9 ,row:0,col:6
7:H1,value is: ,row:0,col:7
8:A2,value is:5 ,row:1,col:0
9:B2,value is:9 ,row:1,col:1
10:C2,value is:1 ,row:1,col:2
11:D2,value is:5 ,row:1,col:3
12:E2,value is:10 ,row:1,col:4
13:F2,value is:9 ,row:1,col:5
14:G2,value is:5 ,row:1,col:6
15:H2,value is: ,row:1,col:7
16:A3,value is:4 ,row:2,col:0
17:B3,value is:9 ,row:2,col:1
18:C3,value is:2 ,row:2,col:2
19:D3,value is:9 ,row:2,col:3
20:E3,value is:4 ,row:2,col:4
21:F3,value is:5 ,row:2,col:5
22:G3,value is:6 ,row:2,col:6
23:H3,value is: ,row:2,col:7
24:A4,value is:3 ,row:3,col:0
25:B4,value is:9 ,row:3,col:1
26:C4,value is:6 ,row:3,col:2
27:D4,value is:4 ,row:3,col:3
28:E4,value is:9 ,row:3,col:4
29:F4,value is:5 ,row:3,col:5
30:G4,value is:2 ,row:3,col:6
31:H4,value is: ,row:3,col:7
32:A5,value is: ,row:4,col:0
33:B5,value is: ,row:4,col:1
34:C5,value is: ,row:4,col:2
35:D5,value is: ,row:4,col:3
36:E5,value is: ,row:4,col:4
37:F5,value is: ,row:4,col:5
38:G5,value is: ,row:4,col:6
39:H5,value is: ,row:4,col:7
40:A6,value is: ,row:5,col:0 
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [chrome-console-log.png](https://docs2.aspose.com/cells/net/attachments/5013765/5115360.png) (image/png)  

