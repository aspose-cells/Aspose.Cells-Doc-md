---
title: Police par défaut et couleur de police de GridDesktop
type: docs
weight: 70
url: /fr/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop, police, couleur
description: Cet article présente la police par défaut et la couleur de la police dans GridDesktop.
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez modifier la police par défaut et la couleur de police de GridDesktop. Veuillez utiliser les deux propriétés suivantes à cette fin. Vous pouvez accéder à ces propriétés au moment de la conception ou à l'exécution en fonction de vos besoins.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Modifier la police et la couleur de la police par défaut au moment de la conception**
La capture d'écran suivante montre comment modifier la police par défaut et la couleur de la police de GridDesktop au moment de la conception.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Modifier la police et la couleur de la police par défaut à l'exécution**
Le code d'exemple suivant explique comment modifier la police par défaut et la couleur de la police de GridDesktop à l'exécution.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
