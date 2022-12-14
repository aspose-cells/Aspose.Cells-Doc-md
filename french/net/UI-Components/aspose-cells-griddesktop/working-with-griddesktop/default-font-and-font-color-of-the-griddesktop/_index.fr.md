---
title: Police par défaut et couleur de police du GridDesktop
type: docs
weight: 70
url: /fr/net/default-font-and-font-color-of-the-griddesktop/
---
## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez modifier la police et la couleur de police par défaut du GridDesktop. Veuillez utiliser les deux propriétés suivantes à cette fin. Vous pouvez accéder à ces propriétés au moment de la conception ou au moment de l'exécution en fonction de vos besoins.

- GridDesktop.DefaultCellFontGridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Modifier la police et la couleur de police par défaut au moment de la conception**
La capture d'écran suivante montre comment modifier la police et la couleur de police par défaut de GridDesktop au moment de la conception.

![tâche : image_autre_texte](default-font-and-font-color-of-the-griddesktop_1.png)
## **Modifier la police par défaut et la couleur de police au moment de l'exécution**
L'exemple de code suivant explique comment modifier la police et la couleur de police par défaut de GridDesktop au moment de l'exécution.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
