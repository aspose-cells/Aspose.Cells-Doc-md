---
title: Läs värdena för GridWeb-cellerna på klientsidan
type: docs
weight: 30
url: /sv/net/read-the-values-of-the-gridweb-cells-on-client-side/
---
## **Möjliga användningsscenarier**
Du kan läsa värdena för GridWeb-celler på klientsidans skript med metoden gridwebinstance.getCellsArray() . En gång, du kommer att kalla det, kommer det att returnera arrayen av alla celler i det aktiva kalkylbladet. Du kan sedan använda följande metoder för att hämta värdet och annan information för cellerna.

- gridwebinstance.getCellName()
- gridwebinstance.getCellValueByCell()
- gridwebinstance.getCellRow()
- gridwebinstance.getCellColumn()
## **Läs värdena för GridWeb-cellerna på klientsidan**
Följande exempelkod hämtar alla celler och skriver sedan ut deras namn, värde, rad och kolumn. Du kan se dess konsolutgång längst ner i den här artikeln. Följande skärmdump visar konsolutgången för exempelkoden på Google Chrome.
## **Skärmdump**
![todo:image_alt_text](read-the-values-of-the-gridweb-cells-on-client-side_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCellsClientSide.aspx" >}}

Anropa JavaScript-funktionen ReadGridWebCells() som visas i exempelkoden ovan så här.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCells.aspx" >}}
## **Konsolutgång**
Detta är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

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
