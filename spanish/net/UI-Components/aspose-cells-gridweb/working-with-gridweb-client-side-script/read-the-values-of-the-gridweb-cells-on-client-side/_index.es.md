---
title: Leer los valores de las celdas de GridWeb en el lado del cliente
type: docs
weight: 30
url: /es/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/
keywords: GridWeb, celda, valor de celda
description: Este artículo presenta cómo obtener el valor de la celda en GridWeb.
---

## **Escenarios de uso posibles**
Puede leer los valores de las celdas de GridWeb en el script del lado del cliente utilizando el método gridwebinstance.getCellsArray(). Una vez que lo llame, devolverá la matriz de todas las celdas en la hoja de cálculo activa. Luego, puede usar los siguientes métodos para recuperar el valor y otra información de las celdas.

- gridwebinstance.getCellName()
- gridwebinstance.getCellValueByCell()
- gridwebinstance.getCellRow()
- gridwebinstance.getCellColumn()
## **Leer los valores de las celdas de GridWeb en el lado del cliente**
El siguiente código de ejemplo recupera todas las celdas y luego imprime su nombre, valor, fila y columna. Puedes ver su salida en la consola al final de este artículo. La siguiente captura de pantalla muestra la salida en la consola del código de ejemplo en Google Chrome.
## **Captura de pantalla**
![todo:image_alt_text](read-the-values-of-the-gridweb-cells-on-client-side_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCellsClientSide.aspx" >}}

Por favor llame a la función JavaScript ReadGridWebCells() como se muestra en el código de ejemplo anterior.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCells.aspx" >}}
## **Salida de la consola**
Este es el resultado de consola del código de ejemplo anterior.

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
