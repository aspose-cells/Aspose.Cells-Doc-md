---
title: Lire les valeurs des cellules GridWeb côté client
type: docs
weight: 30
url: /fr/net/read-the-values-of-the-gridweb-cells-on-client-side/
---
## **Scénarios d'utilisation possibles**
Vous pouvez lire les valeurs des cellules GridWeb sur le script côté client à l'aide de la méthode gridwebinstance.getCellsArray(). Une fois que vous l'appelez, il renverra le tableau de toutes les cellules de la feuille de calcul active. Vous pouvez ensuite utiliser les méthodes suivantes pour récupérer la valeur et d'autres informations des cellules.

- gridwebinstance.getCellName()
- gridwebinstance.getCellValueByCell()
- gridwebinstance.getCellRow()
- gridwebinstance.getCellColumn()
## **Lire les valeurs des cellules GridWeb côté client**
L'exemple de code suivant récupère toutes les cellules, puis imprime leur nom, leur valeur, leur ligne et leur colonne. Vous pouvez voir sa sortie console au bas de cet article. La capture d'écran suivante montre la sortie de la console de l'exemple de code sur Google Chrome.
## **Capture d'écran**
![tâche : image_autre_texte](read-the-values-of-the-gridweb-cells-on-client-side_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCellsClientSide.aspx" >}}

Veuillez appeler la fonction JavaScript ReadGridWebCells() comme indiqué dans l'exemple de code ci-dessus comme celui-ci.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-ReadCellsClientSide-ReadGridWebCells.aspx" >}}
## **Sortie console**
Il s'agit de la sortie console de l'exemple de code ci-dessus.

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
