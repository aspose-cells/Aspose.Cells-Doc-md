---
title: Appliquer un style sur une ligne ou une colonne
type: docs
weight: 50
url: /fr/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, style, ligne, colonne
description: Cet article présente comment appliquer un style sur une ligne ou une colonne dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans ce sujet, nous discuterons du changement de la police et de la couleur de la police des lignes et des colonnes d'une feuille de calcul. Il s'agit d'un niveau de formatage de base offert par Aspose.Cells.GridDesktop qui permet aux développeurs de personnaliser la vue de leurs feuilles de calcul pour les rendre plus présentables.

{{% /alert %}} 
## **Appliquer un style sur une colonne**
Pour appliquer un style personnalisé sur une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Accédez à n'importe quelle **Worksheet** souhaitée
- Accéder à une **Colonne** sur laquelle nous voulons appliquer un **Style**
- Obtenir le **Style** de la **Colonne**
- Définir les propriétés du **Style** selon vos besoins personnalisés
- Enfin, définir le **Style** de la **Colonne** avec celui mis à jour

Il existe de nombreuses propriétés et méthodes utiles offertes par l'objet **Style** qui peuvent être utilisées par les développeurs pour personnaliser le style selon leurs besoins.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Application de style sur une ligne**
Pour appliquer un style personnalisé sur une ligne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Accédez à n'importe quelle **Worksheet** souhaitée
- Accéder à une **Ligne** sur laquelle nous voulons appliquer un **Style**
- Obtenir le **Style** de la **Ligne**
- Définir les propriétés du **Style** selon vos besoins personnalisés
- Enfin, définir le **Style** de la **Ligne** avec celui mis à jour

Il existe de nombreuses propriétés et méthodes utiles offertes par l'objet **Style** qui peuvent être utilisées par les développeurs pour personnaliser le style selon leurs besoins.



{{< highlight csharp >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
