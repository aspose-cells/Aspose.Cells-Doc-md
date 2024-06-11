---
title: 在客户端读取GridWeb单元格的值
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/
keywords: GridWeb，单元格，单元格值
description: 本文介绍了如何在GridWeb中获取单元格值。
---

## **可能的使用场景**
您可以使用gridwebinstance.getCellsArray()方法在客户端脚本中读取GridWeb单元格的值。一旦调用了该方法，它将返回活动工作表中所有单元格的数组。然后，您可以使用以下方法来检索单元格的值和其他信息。

- gridwebinstance.getCellName()
- gridwebinstance.getCellValueByCell()
- gridwebinstance.getCellRow()
- gridwebinstance.getCellColumn()
## **在客户端读取GridWeb单元格的值**
以下示例代码检索所有单元格，然后打印它们的名称、值、行和列。您可以在本文底部看到其控制台输出。以下截图显示了在Google Chrome上执行示例代码的控制台输出。
## **屏幕截图**
![todo:image_alt_text](read-the-values-of-the-gridweb-cells-on-client-side_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCellsClientSide.aspx" >}}

请按照上述示例代码中所示调用JavaScript函数ReadGridWebCells()。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCells.aspx" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight java >}}

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

{{< /highlight >}}
