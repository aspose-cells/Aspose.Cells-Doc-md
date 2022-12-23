---
title: Appliquer un style sur une ligne ou une colonne
type: docs
weight: 50
url: /fr/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

Dans cette rubrique, nous discuterons de la modification de la police et de la couleur de police des lignes et des colonnes d'une feuille de calcul. Il s'agit d'une fonction de formatage de base offerte par Aspose.Cells.GridDesktop qui permet aux développeurs de personnaliser l'affichage de leurs feuilles de calcul pour les rendre plus présentables.

{{% /alert %}} 
## **Appliquer un style sur une colonne**
Pour appliquer un style personnalisé sur une colonne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Accédez à tout**Feuille de travail**
-  Accéder à un**Colonne** sur lequel on veut appliquer une**Style**
-  Obtenir**Style** du**Colonne**
-  Ensemble**Style** propriétés selon vos besoins personnalisés
-  Enfin, réglez**Style** du**Colonne** avec la mise à jour

 Il existe de nombreuses propriétés et méthodes utiles offertes par**Style** objet qui peut être utilisé par les développeurs pour personnaliser le style en fonction de leurs besoins.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Appliquer un style sur une ligne**
Pour appliquer un style personnalisé sur une ligne à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Accédez à tout**Feuille de travail**
-  Accéder à un**Ligne** sur lequel on veut appliquer une**Style**
-  Obtenir**Style** du**Ligne**
-  Ensemble**Style** propriétés selon vos besoins personnalisés
-  Enfin, réglez**Style** du**Ligne** avec la mise à jour

 Il existe de nombreuses propriétés et méthodes utiles offertes par**Style** objet qui peut être utilisé par les développeurs pour personnaliser le style en fonction de leurs besoins.



{{< highlight "csharp" >}}

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
