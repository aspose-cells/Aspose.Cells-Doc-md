---
title: Чтение значений ячеек GridWeb на стороне клиента
type: docs
weight: 30
url: /ru/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/
keywords: GridWeb, ячейка, значение ячейки
description: В этой статье рассматривается, как получить значение ячейки в GridWeb.
---

## **Возможные сценарии использования**
Вы можете считывать значения ячеек GridWeb на стороне клиента с использованием метода gridwebinstance.getCellsArray(). После вызова этого метода он вернет массив всех ячеек в активном листе. Затем вы можете использовать следующие методы для извлечения значения и другой информации о ячейках.

- gridwebinstance.getCellName()
- gridwebinstance.getCellValueByCell()
- gridwebinstance.getCellRow()
- gridwebinstance.getCellColumn()
## **Чтение значений ячеек GridWeb на стороне клиента**
В следующем образце кода извлекаются все ячейки, а затем печатаются их имя, значение, строка и столбец. Вы можете увидеть вывод в консоли внизу этой статьи. На следующем скриншоте показан вывод в консоли образца кода в Google Chrome.
## **Снимок экрана**
![todo:image_alt_text](read-the-values-of-the-gridweb-cells-on-client-side_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCellsClientSide.aspx" >}}

Пожалуйста, вызовите функцию JavaScript ReadGridWebCells() как показано в приведенном выше образце кода.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCells.aspx" >}}
## **Вывод в консоль**
Это вывод консоли вышеуказанного образца кода.

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
