---
title: Changement de la police et de la couleur d une ligne ou colonne
type: docs
weight: 110
url: /fr/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop, police, couleur
description: Cet article explique comment changer la police et la couleur dans une ligne ou une colonne dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans ce sujet, nous discuterons du changement de la police et de la couleur de la police des lignes et des colonnes d'une feuille de calcul. Il s'agit d'un niveau de formatage de base offert par Aspose.Cells.GridDesktop qui permet aux développeurs de personnaliser la vue de leurs feuilles de calcul pour les rendre plus présentables.

{{% /alert %}} 
## **Changement de la police et de la couleur d'une colonne**
Pour changer la police et la couleur d'une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Accédez à n'importe quelle **Worksheet** souhaitée
- Accéder à une **Colonne** dont la police et la couleur doivent être changées
- Créer une **police personnalisée**
- Définir la **Police** de la **Colonne** sur celle personnalisée
- Enfin, définir la **Couleur de la police** de la **Colonne** sur n'importe quelle **Couleur** souhaitée



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **Changement de la police et de la couleur d'une ligne**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Accéder à une **ligne** dont la police et la couleur doivent être modifiées
- Créer une **police personnalisée**
- Définir la **police** de la **ligne** sur celle personnalisée
- Enfin, définir la **couleur de la police** de la **ligne** sur n'importe quelle **couleur** souhaitée



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
