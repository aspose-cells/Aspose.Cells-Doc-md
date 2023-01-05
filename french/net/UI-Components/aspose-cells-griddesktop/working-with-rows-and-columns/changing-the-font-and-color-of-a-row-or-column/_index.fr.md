---
title: Modification de la police et de la couleur d'une ligne ou d'une colonne
type: docs
weight: 110
url: /fr/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

Dans cette rubrique, nous discuterons de la modification de la police et de la couleur de police des lignes et des colonnes d'une feuille de calcul. Il s'agit d'une fonction de formatage de base offerte par Aspose.Cells.GridDesktop qui permet aux développeurs de personnaliser l'affichage de leurs feuilles de calcul pour les rendre plus présentables.

{{% /alert %}} 
## **Changer la police et la couleur d'une colonne**
Pour modifier la police et la couleur d'une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Accédez à tout**Feuille de travail**
-  Accéder à un**Colonne** dont la police et la couleur doivent être modifiées
-  Créer un personnalisé**Police de caractère**
-  Met le**Police de caractère** du**Colonne** au personnalisé
-  Enfin, réglez**Couleur de la police** du**Colonne** à tout désiré**Couleur**



{{< highlight "csharp" >}}

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
## **Changer la police et la couleur d'une ligne**
-  Accédez à tout**Feuille de travail**
-  Accéder à un**Ligne** dont la police et la couleur doivent être modifiées
-  Créer un personnalisé**Police de caractère**
-  Met le**Police de caractère** du**Ligne** au personnalisé
-  Enfin, réglez**Couleur de la police** du**Ligne** à tout désiré**Couleur**



{{< highlight "csharp" >}}

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
